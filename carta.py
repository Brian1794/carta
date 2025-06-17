import pygame
import random
import math
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💖 Carta Romántica Animada 💖")

# Colores
PINK = (255, 182, 193)
HOT_PINK = (255, 105, 180)
DEEP_PINK = (255, 20, 147)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GOLD = (255, 215, 0)
DARK_PINK = (199, 21, 133)
LIGHT_PINK = (255, 228, 225)
PURPLE = (138, 43, 226)

# Fuentes
try:
    font_large = pygame.font.Font(None, 48)
    font_medium = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)
except:
    font_large = pygame.font.SysFont('arial', 48)
    font_medium = pygame.font.SysFont('arial', 36)
    font_small = pygame.font.SysFont('arial', 24)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-3, -1)
        self.life = 255
        self.color = random.choice([PINK, HOT_PINK, DEEP_PINK, RED, GOLD])
        self.size = random.randint(3, 8)
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 3
        self.size = max(1, self.size - 0.1)
        
    def draw(self, screen):
        if self.life > 0:
            color = (*self.color[:3], max(0, self.life))
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class HeartParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-2, -0.5)
        self.life = 180
        self.size = random.randint(8, 15)
        self.color = random.choice([RED, HOT_PINK, DEEP_PINK])
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 2
        
    def draw(self, screen):
        if self.life > 0:
            self.draw_heart(screen, int(self.x), int(self.y), self.size)
            
    def draw_heart(self, screen, x, y, size):
        # Dibujar corazón simple
        points = []
        for i in range(20):
            angle = i * math.pi / 10
            heart_x = size * (16 * math.sin(angle)**3)
            heart_y = size * (13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle))
            points.append((x + heart_x/16, y - heart_y/16))
        
        if len(points) > 2:
            pygame.draw.polygon(screen, self.color, points)

def draw_heart(screen, x, y, size, color):
    """Dibuja un corazón matemático perfecto"""
    points = []
    for i in range(100):
        t = i * 2 * math.pi / 100
        heart_x = size * (16 * math.sin(t)**3)
        heart_y = size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        points.append((x + heart_x/8, y - heart_y/8))
    
    if len(points) > 2:
        pygame.draw.polygon(screen, color, points)

def draw_gradient_background(screen):
    """Dibuja un fondo con degradado"""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(255 * (1 - ratio) + 255 * ratio)
        g = int(182 * (1 - ratio) + 228 * ratio)
        b = int(193 * (1 - ratio) + 225 * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def create_floating_hearts():
    """Crea corazones flotantes en el fondo"""
    hearts = []
    for _ in range(15):
        x = random.randint(0, WIDTH)
        y = random.randint(HEIGHT, HEIGHT + 200)
        size = random.randint(10, 25)
        speed = random.uniform(0.5, 2)
        hearts.append({'x': x, 'y': y, 'size': size, 'speed': speed, 'color': random.choice([PINK, HOT_PINK, RED])})
    return hearts

def main():
    clock = pygame.time.Clock()
    particles = []
    heart_particles = []
    floating_hearts = create_floating_hearts()
    
    # Variables de animación
    time = 0
    pulse_scale = 1.0
    text_alpha = 0
    fade_in = True
    
    # Mensaje de la carta
    messages = [
        "Para la persona más especial",
        "de mi vida...",
        "",
        "Eres la razón por la que",
        "mi corazón late más fuerte",
        "cada día.",
        "",
        "Tu sonrisa ilumina",
        "mis días más oscuros",
        "y tu amor me hace",
        "la persona más feliz",
        "del mundo.",
        "",
        "💖 Te amo infinitamente 💖"
    ]
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        time += dt
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        # Actualizar animaciones
        pulse_scale = 1.0 + 0.1 * math.sin(time * 3)
        
        if fade_in:
            text_alpha = min(255, text_alpha + 2)
            if text_alpha >= 255:
                fade_in = False
        
        # Crear partículas en el centro
        if random.random() < 0.3:
            particles.append(Particle(WIDTH//2 + random.randint(-50, 50), HEIGHT//2))
            
        if random.random() < 0.1:
            heart_particles.append(HeartParticle(WIDTH//2 + random.randint(-30, 30), HEIGHT//2 + 50))
        
        # Actualizar partículas
        particles = [p for p in particles if p.life > 0]
        heart_particles = [hp for hp in heart_particles if hp.life > 0]
        
        for particle in particles:
            particle.update()
            
        for heart_particle in heart_particles:
            heart_particle.update()
            
        # Actualizar corazones flotantes
        for heart in floating_hearts:
            heart['y'] -= heart['speed']
            if heart['y'] < -50:
                heart['y'] = HEIGHT + 50
                heart['x'] = random.randint(0, WIDTH)
        
        # Dibujar todo
        draw_gradient_background(screen)
        
        # Dibujar corazones flotantes de fondo
        for heart in floating_hearts:
            alpha_surface = pygame.Surface((heart['size']*4, heart['size']*4))
            alpha_surface.set_alpha(100)
            draw_heart(alpha_surface, heart['size']*2, heart['size']*2, heart['size']/2, heart['color'])
            screen.blit(alpha_surface, (heart['x'] - heart['size']*2, heart['y'] - heart['size']*2))
        
        # Dibujar corazón principal
        main_heart_size = 60 * pulse_scale
        draw_heart(screen, WIDTH//2, HEIGHT//2 - 100, main_heart_size, RED)
        
        # Dibujar partículas
        for particle in particles:
            particle.draw(screen)
            
        for heart_particle in heart_particles:
            heart_particle.draw(screen)
        
        # Dibujar texto de la carta
        y_offset = HEIGHT//2 - 50
        for i, message in enumerate(messages):
            if message:  # Solo dibujar si no está vacío
                # Crear superficie con alpha para el texto
                text_surface = font_medium.render(message, True, DARK_PINK)
                if text_alpha < 255:
                    text_surface.set_alpha(text_alpha)
                
                # Centrar el texto
                text_rect = text_surface.get_rect()
                text_rect.centerx = WIDTH // 2
                text_rect.y = y_offset + i * 30
                
                # Efecto de sombra
                shadow_surface = font_medium.render(message, True, (100, 100, 100))
                shadow_rect = text_rect.copy()
                shadow_rect.x += 2
                shadow_rect.y += 2
                screen.blit(shadow_surface, shadow_rect)
                
                screen.blit(text_surface, text_rect)
        
        # Dibujar título
        title = "💕 Mi Amor Eterno 💕"
        title_surface = font_large.render(title, True, DEEP_PINK)
        title_rect = title_surface.get_rect()
        title_rect.centerx = WIDTH // 2
        title_rect.y = 50
        
        # Sombra del título
        title_shadow = font_large.render(title, True, (100, 100, 100))
        title_shadow_rect = title_rect.copy()
        title_shadow_rect.x += 3
        title_shadow_rect.y += 3
        screen.blit(title_shadow, title_shadow_rect)
        screen.blit(title_surface, title_rect)
        
        # Instrucciones
        instruction = "Presiona ESC para salir"
        inst_surface = font_small.render(instruction, True, PURPLE)
        inst_rect = inst_surface.get_rect()
        inst_rect.centerx = WIDTH // 2
        inst_rect.y = HEIGHT - 30
        screen.blit(inst_surface, inst_rect)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()