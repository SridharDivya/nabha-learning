/*
 * service-worker.js
 * Caches the app shell (CSS/JS) on install, and caches every page/lesson the
 * student actually visits (cache-as-you-go). If a later request fails because
 * the device is offline, it is served from this cache instead.
 */

const CACHE_NAME = 'nabha-learning-v1';
const APP_SHELL = [
    '/',
    '/static/css/style.css',
    '/static/js/offline-sync.js',
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL))
    );
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) =>
            Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
        )
    );
    self.clients.claim();
});

self.addEventListener('fetch', (event) => {
    // Only handle simple GET page/asset requests; let POST/API calls go straight to the network.
    if (event.request.method !== 'GET') return;

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                const copy = response.clone();
                caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
                return response;
            })
            .catch(() => caches.match(event.request))
    );
});
