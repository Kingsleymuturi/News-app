from app import create_app
from app.models import Articles, Sources
from waitress import serve

app = create_app('development')

@app.shell_context_processor
def make_shell_context():
    """Makes the shell context, allowing for specific variables, and classes
       to be known by the interactive Python session on startup."""
    return {'Articles': Articles, 'Sources': Sources}


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=800)
