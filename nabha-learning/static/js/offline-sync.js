/*
 * offline-sync.js
 * Handles the "offline-first" behaviour of the platform:
 *  1. Registers the service worker so pages/lessons already visited are cached.
 *  2. Lets other scripts queue quiz attempts / lesson completions made while offline.
 *  3. Automatically pushes the queue to /api/sync as soon as the browser regains connectivity.
 */

const OFFLINE_QUEUE_KEY = 'nabha_offline_queue';

function getQueue() {
    const raw = localStorage.getItem(OFFLINE_QUEUE_KEY);
    return raw ? JSON.parse(raw) : { attempts: [], completed_lessons: [] };
}

function saveQueue(queue) {
    localStorage.setItem(OFFLINE_QUEUE_KEY, JSON.stringify(queue));
}

function queueOfflineQuizAttempt(quizId, answers) {
    const queue = getQueue();
    queue.attempts.push({ quiz_id: parseInt(quizId, 10), answers });
    saveQueue(queue);
}

function queueOfflineLessonCompletion(lessonId) {
    const queue = getQueue();
    const id = parseInt(lessonId, 10);
    if (!queue.completed_lessons.includes(id)) {
        queue.completed_lessons.push(id);
        saveQueue(queue);
    }
}

async function syncOfflineQueue() {
    const queue = getQueue();
    if (queue.attempts.length === 0 && queue.completed_lessons.length === 0) return;

    try {
        const res = await fetch('/api/sync', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(queue),
        });
        if (res.ok) {
            // Only clear the queue once the server has confirmed it saved everything.
            saveQueue({ attempts: [], completed_lessons: [] });
            console.log('Offline data synced successfully.');
        }
    } catch (err) {
        // Still offline or the sync failed — leave the queue in place, try again later.
        console.log('Sync attempt failed, will retry later.', err);
    }
}

function updateOfflineBanner() {
    const banner = document.getElementById('offline-banner');
    if (!banner) return;
    banner.classList.toggle('hidden', navigator.onLine);
}

window.addEventListener('online', () => {
    updateOfflineBanner();
    syncOfflineQueue();
});
window.addEventListener('offline', updateOfflineBanner);

document.addEventListener('DOMContentLoaded', () => {
    updateOfflineBanner();
    if (navigator.onLine) syncOfflineQueue();   // catch up on anything queued from a previous offline session

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/service-worker.js').catch(err => {
            console.log('Service worker registration failed:', err);
        });
    }
});
