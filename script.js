
        // Generar corazones para formar la copa del árbol
        function createTreeHearts() {
            const crown = document.getElementById('heartCrown');
            const colors = ['pink1', 'pink2', 'pink3', 'pink4', 'pink5'];
            
            // Crear corazones en forma circular/orgánica
            for (let i = 0; i < 80; i++) {
                const heart = document.createElement('div');
                heart.className = `heart ${colors[Math.floor(Math.random() * colors.length)]}`;
                
                // Posicionar corazones en forma de corona circular con variaciones
                const angle = (i / 80) * 2 * Math.PI;
                const radius = 80 + Math.random() * 60; // Radio variable para forma orgánica
                const x = Math.cos(angle) * radius + 140; // Centrado
                const y = Math.sin(angle) * radius + 140;
                
                heart.style.left = x + 'px';
                heart.style.top = y + 'px';
                heart.style.animationDelay = (Math.random() * 2) + 's';
                
                // Añadir clase de flotación aleatoria
                if (Math.random() > 0.7) {
                    heart.classList.add('floating-heart');
                }
                
                crown.appendChild(heart);
            }
        }

        // Crear corazones que caen
        function createFallingHeart() {
            const heart = document.createElement('div');
            const colors = ['pink1', 'pink2', 'pink3', 'pink4', 'pink5'];
            heart.className = `heart falling-heart ${colors[Math.floor(Math.random() * colors.length)]}`;
            
            heart.style.left = Math.random() * window.innerWidth + 'px';
            heart.style.top = '-50px';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            
            document.body.appendChild(heart);
            
            // Remover el corazón después de la animación
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 7000);
        }

        // Crear chispas/brillos
        function createSparkle() {
            const sparkle = document.createElement('div');
            sparkle.className = 'sparkle';
            
            sparkle.style.left = Math.random() * window.innerWidth + 'px';
            sparkle.style.top = Math.random() * window.innerHeight + 'px';
            sparkle.style.animationDelay = Math.random() * 2 + 's';
            
            document.body.appendChild(sparkle);
            
            setTimeout(() => {
                if (sparkle.parentNode) {
                    sparkle.parentNode.removeChild(sparkle);
                }
            }, 2000);
        }

        // Inicializar la animación
        function init() {
            createTreeHearts();
            
            // Crear corazones que caen periódicamente
            setInterval(createFallingHeart, 1500);
            
            // Crear chispas periódicamente
            setInterval(createSparkle, 800);
        }

        // Evento de clic para crear más corazones
        document.addEventListener('click', function(e) {
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    const heart = document.createElement('div');
                    const colors = ['pink1', 'pink2', 'pink3', 'pink4', 'pink5'];
                    heart.className = `heart ${colors[Math.floor(Math.random() * colors.length)]}`;
                    heart.style.position = 'absolute';
                    heart.style.left = e.clientX + (Math.random() - 0.5) * 100 + 'px';
                    heart.style.top = e.clientY + (Math.random() - 0.5) * 100 + 'px';
                    heart.style.animation = 'float 2s ease-out forwards';
                    heart.style.zIndex = '1000';
                    
                    document.body.appendChild(heart);
                    
                    setTimeout(() => {
                        if (heart.parentNode) {
                            heart.parentNode.removeChild(heart);
                        }
                    }, 2000);
                }, i * 100);
            }
        });

        // Iniciar cuando la página cargue
        window.addEventListener('load', init);
  