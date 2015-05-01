from bokeh.charts import Histogram, Scatter, vplot
from bokeh.plotting import figure, output_file, show
from git import Repo


def diff_size(diff):
    if diff.a_blob and diff.b_blob:
        return abs(diff.a_blob.size - diff.b_blob.size)
    else:
        return 0


def commit_diff_size(commit):
    return sum(diff_size(d) for d in commit.diff())


def message_length_hist(repo, branch='master'):
    lengths = [len(c.message) for c in repo.iter_commits('master')]

    return Histogram(lengths, bins=100,
                     legend=True,
                     title='Commit message sizes',
                     ylabel='Size (bytes)')


def diff_size_hist(repo, branch='master'):
    diffs = [commit_diff_size(c)
             for c in repo.iter_commits('master')]
    return Histogram(diffs, bins=100,
                     title='Diff sizes',
                     ylabel='Size (bytes)')


def message_length_v_diff_size(repo, branch='master'):
    diff_data = [(len(c.message), commit_diff_size(c))
                 for c in repo.iter_commits('master')]

    return Scatter([diff_data],
                   title='Message length vs. Diff size',
                   xlabel='Commit message length',
                   ylabel='Diff size')


output_file("git_stuff.html")

repo = Repo('/users/sixtynorth/projects/cosmic-ray')

plots = [message_length_hist(repo),
         diff_size_hist(repo),
         message_length_v_diff_size(repo)]

show(vplot(*plots))
