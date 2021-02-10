# parse-svg.py
# Description: Functions that turn a path contained in a SVG file into a mathematical complex function.

from svgpathtools import Path, svg2paths, wsvg
import matplotlib.pyplot as plt

def points_from_svg(svg_file_path):
    """ Takes a SVG file as an input and returns a list of points in the complex plane from its path. """

    # Read SVG into a list of curves.
    paths, attributes = svg2paths(svg_file_path)
    curves = paths[0]

    # Get a list of the coordinates from each curve.
    # Coordinates are given as points in the complex plane.
    num_samples = 10
    points_list = []
    for curve in curves:
        for i in range(num_samples):
            points_list.append(Path(curve).point(i/(float(num_samples)-1)))
    
    return points_list


def plot_complex_points(points):
    """ Given a list of points in the complex plane, plots all the points. """
    for point in points:
        plt.plot(point.real, point.imag,'b.')

    plt.show()