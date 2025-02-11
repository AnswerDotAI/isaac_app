"""Entry point for the app"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/main.ipynb.

# %% auto 0
__all__ = ['app', 'rt', 'redir_path', 'skip', 'client', 'oauth', 'index', 'theme', 'Auth', 'login', 'logout']

# %% ../nbs/main.ipynb
from fasthtml.common import *
from monsterui.all import *
from fasthtml.oauth import *
from functools import partial

# %% ../nbs/main.ipynb
from social_media import ar as ar_social
from blog import ar as ar_blog
from utils import *

# %% ../nbs/main.ipynb
app, rt = fast_app(hdrs = Theme.blue.headers(highlightjs=True), 
                   routes = (Mount('/blog/static', StaticFiles(directory='posts/static')),),
                   body_wrap=layout, live=True)

# %% ../nbs/main.ipynb
@rt
def index(): 
    return DivCentered(
        PicSumImg(cls='rounded-full w-96 h-96 object-cover mb-6'),
        H1("Isaac Flath"))

# %% ../nbs/main.ipynb
@rt
def index():
    _href = partial(A, cls=AT.primary, target='_blank')
    def _project_slider_card(title, subtitle, href=None,cls=''):
        return Card(
                A(H3(title), href=href, cls=AT.primary if href else '', target='_blank', disabled=href is None), 
                Subtitle(subtitle), 
                cls=cls)
    def _section(*c):
        return Section(Article(*c, cls='prose max-w-5xl mx-auto space-y-5 pt-16'), cls=('uk-padding-remove-vertical',))
    
    return Div(
        # Header section with profile
        Section(
            DivCentered(
                Img(src='street.jpg', cls='h-96 w-96 rounded-full object-cover shadow-lg'),
                H1("Isaac Flath", cls=TextT.center),
                P("AI & Tech Generalist", cls=(TextT.center, TextT.muted)),
                cls='space-y-4 mt-12'),
            cls='uk-padding-remove-vertical'),
        _section(
                P("Hi! I'm ", Strong("Isaac Flath"), ", a Tech Generalist passionate about creating beautiful, functional, useful things.  ",
                  "While this often means AI it often means Web App Development, Dev Ops, System Administration, and other things.  ", 
                  Em("AI is only a component (sometimes a relatively small one) of a successful AI application."))),
        _section(
                DivCentered(H3(U("Current Projects"))),
                Slider(
                    _project_slider_card("MonsterUI", 
                                         "A UI framework for FastHTML that makes styling painless and fast - all within python!",
                                         'https://monsterui.answer.ai/'),
                    _project_slider_card("FastHTML Gallery", 
                                         "A gallery of examples to help people learn and use FastHTML for web development",
                                         'https://gallery.fastht.ml/'),
                    _project_slider_card("Solveit", 
                                         "A course that teaches people to use AI in a productive way for learning and building.",
                                         'https://solveit.fast.ai/'),
                    _project_slider_card("Virgil", 
                                         "A tech powered law firm.",
                                         'https://tryvirgil.com/'),
                    _project_slider_card("Plash", 
                                         "No information here!  How mysterious...",
                                        None),
                    uk_slider='finite: true',
                    items_cls='uk-child-width-1-3 ml-1 mr-20 gap-4'
                )),
    _section(
        DivCentered(H3(U("My Hobbies"))),
        P("My primary hobby is dance. I used to teach ballroom dance full time, which is where I met my partner.",
          "  My partner runs her own ", _href('dance instruction business', href='https://artofmovementdc.com/'), " here in D.C."),
        P("We have a couple videos up of us dancing causual ",
              _href("social style", href="https://www.youtube.com/watch?v=nUdMfll0YJo", ), " performances and ",
              _href("routine style", href="https://www.youtube.com/watch?v=Y7R82kgeUbY", cls=AT.primary), " performances.")),
    _section(
        DivCentered(H3(U("Career Journey"))),
        DivLAligned(H4("My Start:"),P("Assembly line worker ➢ assembly line management ➢ assembly line efficiency optimization")),
        DivLAligned(H4("Moving Up :"),P("Business process engineering ➢ product management")),
        DivLAligned(H4("Starting Technical Journey:"),P("Data analyst ➢ dynamics CRM developer")),
        DivLAligned(H4("Trying New Things:"),P("Accounting ➢ call center ➢ full-time ballroom dance teacher")),
        DivLAligned(H4("Finding my home ❤️:"),P("Product owner ➢ machine learning researcher ➢ data science ➢ AI and tech generalist"))))

# %% ../nbs/main.ipynb
@rt
def theme():
    return ThemePicker()

# %% ../nbs/main.ipynb
ar_social.to_app(app)
# ar_todo.to_app(app)
ar_blog.to_app(app)

# %% ../nbs/main.ipynb
redir_path = '/redirect'
skip = ('/login', '/blog', '/blog/', r'/blog/.*', '/','social_media/share_thread','social_media/share_thread*', 
        redir_path, r'/.*\.(png|jpg|ico|css|js)', )

class Auth(OAuth):
    def get_auth(self, info, ident, session, state):
        email = info.email or ''
        session['user_name'] = email
        if info.email_verified and email.split('@')[-1] == 'answer.ai': return RedirectResponse('/', status_code=303)
        
client = GoogleAppClient(os.environ.get('GOOGLE_CLIENT_ID'), os.environ.get('GOOGLE_SECRET'))
oauth = Auth(app, client, skip=skip, redir_path=redir_path)

@rt
def login(req):
    return Container(Card(
        H3("Login"),
        Subtitle("This page is just for Isaac's use!"),
        P("If you're interested in what's here, reach out and I'm happy to give you a demo.  It's an app I built that help me with my own productivity."),
        A('Log in', href=oauth.login_link(req), cls='uk-button'+ButtonT.primary)))

@rt
def logout(sess):
    del sess["user_name"]
    return oauth.logout(sess)

# %% ../nbs/main.ipynb
serve(port=5005)
