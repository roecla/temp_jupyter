Temporary Jupyter Notebooks
=============================

The problem
------------

ipython has the advantage that wherever you are in your current terminal, you can open up python and test something, e.g. inspect a pickled DataFrame. However, compared to a jupyter notebook this lacks quite a few useful features and is visually very unappealing. jupyter notebooks are visually appealing and have more features but are tedious to open in a specific folder and create files and folders that can get lost or may need to be removed later. Both have the disadvantage that you may need to type import statements a dozen times a day.

The solution
-------------

### The setup

1.) Create a notebook folder somewhere on your computer where you want your notebooks to be saved.

2.) Clone this repository to your notebook folder. import_statements.ipynb is the notebook template so feel free to adjust its content.

3.) Copy the following to the alias section of your .bashrc:

```bash
ijupyter() {
    cd [path_to_your_notebook_folder]
    rm -f Untitled.ipynb
    python create_untitled_notebook.py "$OLDPWD"
    jupyter notebook Untitled.ipynb </dev/null &>/dev/null &
}

alias nb = "cd [path_to_your_notebook_folder] && rm -f Untitled.ipynb && cp -fp import_statements.ipynb Untitled.ipynb && jupyter notebook Untitled.ipynb </dev/null &>/dev/null &"
```

and insert the absolute path to your notebook folder.

### Usage

Whenever you want a notebook at a specific path you go in a terminal to that path and execute `ijupyter`. When you don't care about the cwd of the notebook `nb`  will simply open a notebook with the cwd in your temporary notebook folder. This gives you a small speed advantage.

**In both cases a possibly existing Untitled.ipynb in your temporary notebook folder is removed.**

Then a notebook with the supplied import statements is created as Untitled.ipynb and opened up for you directly.

#### Warning!

**If you wish to keep a notebook you need to change its name before you use one of the two commands again, including if you want to use ijupyter again before closing the earlier ijupyter tab.**


Pressing ``Shift + Enter`` runs the import statements (and changes the working directory to where you want to be if using ijupyter). With another ``Enter`` you are in the second cell and can start exploring!

At the same time you can use your terminal as if you never opened a jupyter notebook because the server runs silently in the background. Closing the terminal or pressing Ctrl + c won't affect it.


### Shutting Down Jupyter Servers

As the jupyter notebook server is started silently in the background, you might want to close unused servers at some point in time. This is easy, as long as you use jupyter_client > 0.5.1. In that case you can inspect the list of running jupyter servers with

    jupyter notebook list

This gives you the ports (e.g. 8888) which allow you to shutdown the server with e.g.

    jupyter notebook stop 8888

At the moment it seems impossible to shut down more than one server at a time with this command.


Remaining problems / Outlook
------------------------------

- Opening a notebook this way takes longer than starting ipython. Most of this seems to just be the time to fire up the jupyter server.

- The ijupyter command would allow arguments, e.g. passing directly a name for the notebook or a path to which the cwd of the notebook should be changed.

- It would be nice to have the jupyter server to shutdown when the browser tab is closed.

- It would be nice to have the same behavior as on the jupyter server homepage that Untitled.ipynb does not get removed but that the name of the latest notebook gets incremented from the previous. That way there'd be no danger of a notebook being unwillingly deleted. It would also help with the problem that the command can only be used once until the notebook is renamed.

