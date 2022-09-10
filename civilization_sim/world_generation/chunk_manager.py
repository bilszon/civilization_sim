""" Chunk manager: manages communication between game's logic and graphic engine and the internal chunk system."""

import PIL
import PIL.ImageTk

from world_generation import chunk

class ChunkManager():
    """Manages communication between game's logic and graphic engine and the internal chunk system. Static class.
    """

    # A dictionary of dictionaries. Each entry contains keys: "chunk" - Chunk object itself, "updated" - if it has been updated since last image retrieval, "image" - chunk's image.
    _chunks = {}
    
    def get_chunk(x: int, y: int) -> chunk.Chunk:
        """Get the chunk with coordinates (x,y).
        NOT intended for getting chunk's image, use get_chunk_image() instead.
        If the chunk doesn't exist, generates it.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).

        Returns:
            chunk.Chunk: Chunk at the given location.
        """

        if (x,y) not in ChunkManager._chunks: # If chunk doesn't exist, generate it.
            new_chunk = chunk.Chunk(x, y)
            ChunkManager._chunks[(x,y)] = {"chunk":new_chunk, "updated":False, "image":ChunkManager._RGB_to_Image(new_chunk.RGB_array())}
        
        ChunkManager._chunks[(x,y)]["updated"] = True #TODO: More accurate system to check if a chunk has been updated and needs to be rerendered. For now assume that it's modified anytime someone get's access to it.
        return ChunkManager._chunks[(x,y)]["chunk"]

    def get_chunk_image(x: int, y: int) -> PIL.ImageTk.PhotoImage:
        """Get the PhotoImage of the chunk at coordinates (x, y).
        If the chunk doesn't exist, generates it.

        Args:
            x (int): x (horizontal) coordinate of the chunk (in chunk coords, not tile/world).
            y (int): y (vertical) coordinate of the chunk (in chunk coords, not tile/world).

        Returns:
            PIL.ImageTk.PhotoImage: Image, ready to be rendered.
        """

        if (x,y) not in ChunkManager._chunks: # If chunk doesn't exist, generate it.
            new_chunk = chunk.Chunk(x, y)
            ChunkManager._chunks[(x,y)] = {"chunk":new_chunk, "updated":False, "image":ChunkManager._RGB_to_Image(new_chunk.RGB_array())}
        else:
            if ChunkManager._chunks[(x,y)]["updated"]: # If chunk has been updated since last time it's image was accessed, rerender it. Otherwise just return cashed image.
                ChunkManager._chunks[(x,y)]["image"] = ChunkManager._RGB_to_Image(ChunkManager._chunks[(x,y)]["chunk"].RGB_array())
                ChunkManager._chunks[(x,y)]["updated"] = False # We have generated a new image and cashed it, so it is definitely up-to-date now.
                print("Generating new chunk image for chunk (" + str(x) + ", " + str(y) + ").")
        
        return ChunkManager._chunks[(x,y)]["image"]

    def _RGB_to_Image(RGB_array):
        image1 = PIL.Image.fromarray(RGB_array, mode="RGB")
        return PIL.ImageTk.PhotoImage(image1)