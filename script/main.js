  // Optimized particle creation
  function createParticles() {
    const emojis = ['❤️', '🌎', '🌠', '💝', '🌟', '💞'];
    const container = document.body;
    let lastTime = 0;

    function animate(timestamp) {
        if (!lastTime || timestamp - lastTime >= 500) { // Reduced frequency
            const particle = document.createElement('div');
            particle.className = 'love-particle';
            particle.textContent = emojis[Math.floor(Math.random() * emojis.length)];
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDuration = Math.random() * 3 + 3 + 's';
            container.appendChild(particle);
            setTimeout(() => particle.remove(), 6000);
            lastTime = timestamp;
        }
        requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
}

// Optimized message animation
let currentMessage = 0;
const messages = document.querySelectorAll('.message');
const finalQuestion = document.querySelector('.final-question');

function showNextMessage() {
    requestAnimationFrame(() => {
        if (currentMessage > 0) {
            messages[currentMessage - 1].classList.add('exit');
        }
        
        if (currentMessage < messages.length) {
            messages[currentMessage].classList.add('active');
            currentMessage++;
            setTimeout(showNextMessage, 3000);
        } else {
            finalQuestion.style.display = 'block';
            finalQuestion.style.opacity = '1';
        }
    });
}

// Button interactions
document.querySelector('.yes-btn').addEventListener('click', function() {
    const celebration = document.querySelector('.celebration');
    celebration.style.display = 'block';

    // Optimized heart burst
    requestAnimationFrame(() => {
        for (let i = 0; i < 50; i++) {
            const heart = document.createElement('div');
            heart.className = 'heart-burst';
            heart.textContent = '❤️';
            heart.style.left = Math.random() * 100 + '%';
            heart.style.top = Math.random() * 100 + '%';
            heart.style.animationDelay = Math.random() * 0.5 + 's';
            celebration.appendChild(heart);
        }
    });

   finalQuestion.innerHTML = 
"<h2>🌌 Then let the universe witness this moment...</h2>" +
"<p>From this timeline onward... you are mine and I am yours.</p>" +
"<div style='margin-top: 2rem; font-size: 3rem'>❤️✨🌠</div>" +

"<div class='btn-group' style='margin-top:2rem'>" +
"   <button class='valentine-btn redirect-btn'>Click Me Please 💌</button>" +
"</div>";

});

// Redirect after clicking "Click Me Please"
document.addEventListener('click', function(e) {

    // Check if redirect button was clicked
    if (e.target && e.target.classList.contains('redirect-btn')) {

        // Small dramatic delay before redirect (optional)
        document.body.style.transition = "opacity 0.5s";
        document.body.style.opacity = "0";

        setTimeout(() => {
            window.location.href = "next.html";
        }, 500);

    }

});




document.querySelector('.no-btn').addEventListener('mouseover', function() {
    requestAnimationFrame(() => {
        this.style.transform = 
            `translate(${Math.random() * 200 - 100}px, 
            ${Math.random() * 200 - 100}px)
            rotate(${Math.random() * 360}deg)`;
        this.style.transition = 'all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1)';
    });
});

// Initialize
createParticles();
setTimeout(showNextMessage, 1000);