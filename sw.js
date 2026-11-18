const CACHE = "fluentkey-shell-v02";
const CORE = ["./", "./index.html", "./manifest.webmanifest", "./icon-192.svg", "./icon-512.svg"];
self.addEventListener("install", event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(CORE)));
  self.skipWaiting();
});
self.addEventListener("activate", event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin || url.pathname.includes("/api/")) return;
  event.respondWith(caches.match(event.request).then(cached => cached || fetch(event.request)));
});