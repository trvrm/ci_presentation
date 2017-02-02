from invoke import task

@task
def serve(context):
    
    context.run("jupyter-nbconvert --to slides Continous\ Integration.ipynb --post serve --ServePostProcessor.ip='0.0.0.0' --ServePostProcessor.open_in_browser=False")
 
@task
def markdown(context):
    context.run("jupyter-nbconvert --to markdown Continous\ Integration.ipynb ")
