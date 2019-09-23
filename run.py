from PIL import Image
import io

from generator import generate

if __name__ == "__main__":
    avatar = generate() # can get "1antennas", "2antennas" exc.
    avatar.save("avatar.png")