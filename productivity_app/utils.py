"""Utility stuff like database connection and layout"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utils.ipynb.

# %% auto 0
__all__ = ['db', 'footer', 'links', 'post_tbl', 'thread_tbl', 'status_opts', 'layout', 'Post', 'Thread', 'Todo']

# %% ../nbs/utils.ipynb 2
from fasthtml.common import *
from monsterui.all import *
from fasthtml.components import Uk_theme_switcher


# %% ../nbs/utils.ipynb 3
db = Database('productivity_app.db')

# %% ../nbs/utils.ipynb 5
footer = Section(
        DivCentered(
            H2("Get in Touch", cls=(TextT.center, TextT.lg, TextT.bold)),
            Subtitle("Let's connect and collaborate!", cls='mb-6'),
            Address(
                DivHStacked(
                    A(DivLAligned(UkIcon('github', cls='mr-2'), "GitHub"),
                      href="https://github.com/isaac-flath",
                      cls=(AT.primary, 'hover:opacity-80')),
                    A(DivLAligned(UkIcon('linkedin', cls='mr-2'), "LinkedIn"),
                      href="https://linkedin.com/in/isaacflath",
                      cls=(AT.primary, 'hover:opacity-80')),
                    A(DivLAligned(UkIcon('twitter', cls='mr-2'), "Twitter"),
                      href="https://x.com/isaac_flath",
                      cls=(AT.primary, 'hover:opacity-80')),
                    cls='space-x-8')),
            cls='space-y-4'),
        cls=(SectionT.muted, 'py-12 mt-12')),

# %% ../nbs/utils.ipynb 8
links = (Li(A('Home',href='/')),
         Li(A("Theme")),DropDownNavContainer(Div(Uk_theme_switcher(), cls='p-6 uk-drop-close'), cls='w-96'),
         Li(A('Blog', href='/blog')),
         Li(A('TIL', href='/til')),
         Li(A('Social', href='/social_media')),
         Li(A('Todo', href='/todo')))

# %% ../nbs/utils.ipynb 10
def layout(content, req):
    return Div(
        NavBar(links, H1("Isaac's Website", cls="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400")),
        Container(content, cls=ContainerT.sm),
        footer)

# %% ../nbs/utils.ipynb 12
@dataclass
class Post:
    id: str # Post Id (pid) is PK
    tid: int # Thread ID (tid)
    position: int # position in thread
    content: str # text content
    img_path: str = None # fpath to image is used
    username: str = "User" # For UI - no functional purpose
    handle: str = "@user" # For UI - no functional purpose
    created_at: str = "Just now" # For UI - no functional purpose
    modified_at: str = None # TODO: add mofified timestampe
        

# %% ../nbs/utils.ipynb 13
@dataclass
class Thread:
    id: str # tid
    name: str # human readable name
    user: str # user this is for, used for filtering down what is shown in UI
    created_on: str=None # TODO: Add created date for UI selection/sorting

# %% ../nbs/utils.ipynb 14
post_tbl = db.create(Post, 'posts')
thread_tbl = db.create(Thread, 'threads')

# %% ../nbs/utils.ipynb 16
status_opts = ("Todo", "In Progress", "Done", "Archived", "Someday", "Other")

# %% ../nbs/utils.ipynb 17
class Todo:
    title: str; id: int; updated_at: str; labels: str; repo_url: str; 
    html_url: str; repo_owner: str; repo_name: str; number: int;
    status: str 

# %% ../nbs/utils.ipynb 18
db.todos = db.create(Todo) 
