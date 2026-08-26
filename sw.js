/**
 * SalaryPlan Service Worker
 * MindTech Financial Intelligence Platform
 * CHSH S=2.76 · SA 2026/05142
 */

const CACHE_VERSION = 'v2.0.0';
const CACHE_NAME = `salaryplan-${CACHE_VERSION}`;
const QUANTUM_CACHE = `quantum-state-${CACHE_VERSION}`;

const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/css/style.css',
  '/css/quantum-theme.css',
  '/js/app.js',
  '/js/quantum-badge.js',
  '/js/offline-manager.js',
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png',
  '/manifest.json'
];

const OFFLINE_API_ENDPOINTS = [
  '/api/v1/health',
  '/api/v1/quantum/badge',
  '/api/v1/quantum/chsh'
];

// Install event
self.addEventListener('install', event => {
  console.log(`[SalaryPlan] Installing service worker ${CACHE_VERSION}`);
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[SalaryPlan] Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => caches.open(QUANTUM_CACHE))
      .then(() => self.skipWaiting())
      .catch(error => console.error('[SalaryPlan] Installation failed:', error))
  );
});

// Activate event
self.addEventListener('activate', event => {
  console.log(`[SalaryPlan] Activating service worker ${CACHE_VERSION}`);
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== CACHE_NAME && cacheName !== QUANTUM_CACHE) {
              console.log(`[SalaryPlan] Deleting old cache: ${cacheName}`);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch event
self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);
  
  if (request.method !== 'GET') {
    return event.respondWith(fetch(request));
  }
  
  // API requests
  if (url.pathname.startsWith('/api/')) {
    return event.respondWith(handleApiRequest(request));
  }
  
  // Static assets
  if (url.pathname.match(/\.(css|js|png|jpg|jpeg|gif|svg|ico|webp)$/)) {
    return event.respondWith(handleStaticAsset(request));
  }
  
  // Navigation
  if (request.mode === 'navigate') {
    return event.respondWith(handleNavigation(request));
  }
  
  // Default: cache-first
  return event.respondWith(
    caches.match(request)
      .then(response => {
        if (response) {
          updateCache(request);
          return response;
        }
        return fetch(request)
          .then(response => {
            if (response && response.status === 200) {
              const responseClone = response.clone();
              caches.open(CACHE_NAME).then(cache => cache.put(request, responseClone));
            }
            return response;
          })
          .catch(() => getOfflineFallback(request));
      })
  );
});

async function handleApiRequest(request) {
  const url = new URL(request.url);
  
  if (OFFLINE_API_ENDPOINTS.some(endpoint => url.pathname.includes(endpoint))) {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) return cachedResponse;
  }
  
  try {
    const response = await fetch(request);
    if (response && response.status === 200) {
      const responseClone = response.clone();
      const cache = await caches.open(QUANTUM_CACHE);
      await cache.put(request, responseClone);
      return response;
    }
    throw new Error('API response not OK');
  } catch (error) {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) return cachedResponse;
    
    return new Response(
      JSON.stringify({
        status: 'offline',
        message: 'You are offline. Data will sync when connection is restored.',
        quantum_state: { chsh: 'S=2.76', entanglement: 'maximal', timestamp: new Date().toISOString() }
      }),
      { status: 503, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-cache' } }
    );
  }
}

async function handleStaticAsset(request) {
  try {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) return cachedResponse;
    
    const response = await fetch(request);
    if (response && response.status === 200) {
      const responseClone = response.clone();
      const cache = await caches.open(CACHE_NAME);
      await cache.put(request, responseClone);
      return response;
    }
    throw new Error('Static asset not available');
  } catch (error) {
    return new Response('Asset not available offline', { status: 404, headers: { 'Content-Type': 'text/plain' } });
  }
}

async function handleNavigation(request) {
  try {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) return cachedResponse;
    
    const response = await fetch(request);
    if (response && response.status === 200) {
      const responseClone = response.clone();
      const cache = await caches.open(CACHE_NAME);
      await cache.put(request, responseClone);
      return response;
    }
    throw new Error('Page not available');
  } catch (error) {
    return new Response(`
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SalaryPlan - Offline</title>
        <style>
          body { background: #0a0e17; color: #00d4ff; font-family: -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; text-align: center; }
          .offline-container { max-width: 400px; }
          h1 { font-size: 2rem; margin-bottom: 0.5rem; background: linear-gradient(135deg, #00d4ff, #7b2ffc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
          .quantum-badge { margin: 20px 0; padding: 10px 20px; background: rgba(0,212,255,0.1); border: 1px solid rgba(0,212,255,0.3); border-radius: 8px; font-size: 0.9rem; }
          p { color: #8892b0; line-height: 1.6; }
          .retry-btn { background: linear-gradient(135deg, #00d4ff, #7b2ffc); color: white; border: none; padding: 12px 30px; border-radius: 8px; font-size: 1rem; cursor: pointer; margin-top: 20px; transition: transform 0.2s; }
          .retry-btn:hover { transform: scale(1.05); }
        </style>
      </head>
      <body>
        <div class="offline-container">
          <h1>⚛️ SalaryPlan</h1>
          <p>You're currently offline</p>
          <div class="quantum-badge">⚛️ CHSH S=2.76 · SA 2026/05142</div>
          <p>Don't worry! Your data is safe on your device.<br>Connect to the internet to sync.</p>
          <button class="retry-btn" onclick="location.reload()">🔄 Try Again</button>
        </div>
      </body>
      </html>
    `, { status: 200, headers: { 'Content-Type': 'text/html', 'Cache-Control': 'no-cache' } });
  }
}

function updateCache(request) {
  if ('caches' in self) {
    caches.open(CACHE_NAME).then(cache => {
      fetch(request).then(response => {
        if (response && response.status === 200) cache.put(request, response);
      }).catch(() => {});
    }).catch(() => {});
  }
}

function getOfflineFallback(request) {
  const url = new URL(request.url);
  if (url.pathname.endsWith('.css')) return new Response('/* Offline fallback */', { headers: { 'Content-Type': 'text/css' } });
  if (url.pathname.endsWith('.js')) return new Response('// Offline fallback', { headers: { 'Content-Type': 'application/javascript' } });
  return new Response('Resource not available offline', { status: 404, headers: { 'Content-Type': 'text/plain' } });
}

// Push notifications
self.addEventListener('push', event => {
  const data = event.data ? event.data.json() : {};
  const options = {
    body: data.body || 'Financial update from SalaryPlan',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/icon-96x96.png',
    vibrate: [200, 100, 200],
    data: { url: data.url || '/' },
    actions: [{ action: 'view', title: 'View Details' }, { action: 'dismiss', title: 'Dismiss' }],
    tag: data.tag || 'salaryplan-notification',
    renotify: true,
    requireInteraction: true
  };
  event.waitUntil(self.registration.showNotification(data.title || '⚛️ SalaryPlan Update', options));
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  if (event.action === 'dismiss') return;
  const urlToOpen = event.notification.data?.url || '/';
  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true })
      .then(clientList => {
        for (const client of clientList) {
          if (client.url === urlToOpen && 'focus' in client) return client.focus();
        }
        if (self.clients.openWindow) return self.clients.openWindow(urlToOpen);
      })
  );
});

// Background sync
self.addEventListener('sync', event => {
  if (event.tag === 'sync-financial-data') {
    event.waitUntil(syncFinancialData());
  }
});

async function syncFinancialData() {
  try {
    const cache = await caches.open(QUANTUM_CACHE);
    const requests = await cache.keys();
    for (const request of requests) {
      if (request.url.includes('/api/') && request.url.includes('sync')) {
        const response = await fetch(request);
        if (response && response.status === 200) await cache.put(request, response.clone());
      }
    }
    console.log('[SalaryPlan] Financial data synced successfully');
    return true;
  } catch (error) {
    console.error('[SalaryPlan] Sync failed:', error);
    return false;
  }
}

console.log(`[SalaryPlan] Service worker ${CACHE_VERSION} initialized`);
console.log('⚛️ CHSH S=2.76 · SA 2026/05142');
