from ggame import App, Color, LineStyle, Sprite

from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 0.1)
green = Color(0x00ff00, 0.1)
blue = Color(0x0000ff, 0.1)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(200, 200, thinline, red)
ellipse = EllipseAsset(50, 50, thinline, blue)
# Now display a rectangle
Sprite(rectangle, (850, 400))
Sprite(ellipse, (900, 450))

myapp = App()
myapp.run()
