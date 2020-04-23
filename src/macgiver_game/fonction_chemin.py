import os


def path_to_image(name):
    """
    Return the path to the image we want.

    Parameter :

    :param name : the file name of the image we want.
    :type name : str

    Return :

    :rtype : str
    """

    path = os.path.join(os.path.dirname(__file__), '..', 'image', name)
    return path


def path_to_labyrinth():
    """
    Return the path to the file labyrinth.

    Return :

    :rtype : str
    """

    path = os.path.join(os.path.dirname(__file__), '..', 'labyrinth')
    return path
