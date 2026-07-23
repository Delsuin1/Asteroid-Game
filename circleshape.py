import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass


    def collides_with(self, other) -> bool:
        player_position = self.position.distance_to(self.position)
        player_radius = self.radius
        asteroid_position = other.position.distance_to(self.position)
        asteroid_radius = other.radius
        
        combined_position = player_position + asteroid_position
        combined_radius = player_radius + asteroid_radius
        if combined_position <= combined_radius:
            return True
        return False
