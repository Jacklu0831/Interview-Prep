"""

For this exercise we are going to implement an HTTPRouter like you would find in a typical
web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple 
string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", 
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. 
In a dynamic web server, the content will often come from a block of code called a handler.

"""

from collections import defaultdict

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)


    def insert(self, path, handler):
        # recursively add nodes
        # assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for ch in path:
        	node = node.children[ch]
        node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for ch in path:
        	if ch not in node.children:
        		return None
        	node = node.children[ch]
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # Could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path, handler):
        # Add a handler for a path
        # Will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = Router.split_path(path)
        self.trie.insert(path, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # can return None if it's not found or
        # return the "not found" handler if added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = Router.split_path(path)
        handler = self.trie.find(path)
        if handler:
        	return handler
        else:
        	return self.not_found_handler


    @staticmethod
    def split_path(path):
        # need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [c for c in path.split("/") if c]


# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # root handler
print(router.lookup("/home")) # not found handler
print(router.lookup("/home/about")) # about handler
print(router.lookup("/home/about/")) # about handler
print(router.lookup("/home/about/me")) # not found handler

