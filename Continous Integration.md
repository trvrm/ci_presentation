
# Continuous Integration




![title](images/01_CD_the_idea_low-res.jpg)


# The problem

When creating and managing processes for large-scale, long term projects, mistakes can happen that aren't caught for years.

The cost of a mistake increases significantly with the length of time it takes to find it.

Waiting until launch can be *very* expensive

![explosion](images/Explosion_of_first_Ariane_5_flight_June_4_1996.jpg)


* $370 million
* Lots of PhD theses


# Old model


* Gather requirements
* Design
* Build
* Deploy


Some errors won't be found until the deployment stage.

# Fail Fast!

## Examples


### Toyota

We developed ICS - the Inspection Control System

Feedback is given at all stages of the manufacturing process

Defects are remedied as close as possible to their source




### TREC

#### Translating Research in Elder Care


http://www.trec.ualberta.ca/








Instruments:
* Facility
* Units
* Specialist
* Nurse
* Manager
* Health Care Aids

https://trec.svy.ca/app/account



Facility Management

https://hca.svy.ca/app/facilityunit/facilities




#### Considerations:

* Site (facility) management, including changes over time.
* Metadata management
* Data collection.
* Codebooks.
* Dashboards



## Continuous Integration

CI can be applied at several levels.


* Enterprise

* Processes

* Software development

Many of the same techniques apply, but I'll be focusing on software development.


# Tools

* Collaboration
* Metadata management
* Institutional memory
* Issue tracking
* Unit testing
* Source Control
* CI
* Dashboards



## Collaboration

### Realtime

* Face to face
* Skype
* Hangouts
* ...

### Near realtime

* Chatrooms
* Slack  (https://civictechto.slack.com/messages/general/team/jrootham/)
* Mattermost

* https://gitter.im/pydata/pandas

### Asynchonous

* Email

## Institutional Memory

The problem:

* People move on
* Processes aren't documented.
* The only person who knows how to import a certain file is a grad student who left 3 years ago
* The reasons *behind* processes aren't documented






Tools

* Wiki (https://github.com/pandas-dev/pandas/wiki)
* Evernote
* Sphinx (http://pandas.pydata.org/pandas-docs/stable/)
* Blogs  (https://trvrm.github.io/)

Record:

* What do we do
* How do we do it
* Why do we do it
* Who does it
* How do we know it's working


## Sharing Code, Processes, and documentation

https://try.jupyter.org/

https://nbviewer.jupyter.org/

Jupyter notebooks are an *incredible* tool.

* Write code
* Write documentation
* Write books
* Collaborate
* Explore


This presentation is written in Jupyter.

Sample use case

https://github.com/trvrm/notebooks/blob/master/bulk_psycopg2_inserts.ipynb

Publish to blog:

https://trvrm.github.io/bulk-psycopg2-inserts.html



![code](images/code_work.jpg)





Write the test before fixing the code!

https://github.com/pandas-dev/pandas/pull/11937/commits/7f00dbcd7dcef6c1354e36381e1501b5e95208ff
    
    

Choose the tool for your framework/library/language.


* write your tests concurrently with your code
* write regression tests  (e.g. nosetests)
* use code coverage tools  (e.g. coverage)
* use code quality tools (e.g. flake8)



## Source Control

* Git  (https://github.com/trvrm/pandas/commit/7f00dbcd7dcef6c1354e36381e1501b5e95208ff)
* Mercurial
* Subversion


**Track everything in source control**

Source control isn't just for code.  This presentation is available for collaboration at https://github.com/trvrm/ci_presentation


## Continuous Integration

https://travis-ci.org/pandas-dev/pandas
 

* Tests are run automatically on every commit.
* Failed tests prevent upstream merges

## Dashboards

This is a broader concept.

* KANBAN: https://en.wikipedia.org/wiki/Kanban
* Surveymedia

## Suggestions

- pick the right tools for your process
- don't be afraid to write your own
- automate everything that can be automated
- test everything
- Do end-to-end integration as soon as possible.
- Mistakes increase in cost the longer it takes to find them


## Resources

* https://github.com/
* https://www.mercurial-scm.org/
* https://about.mattermost.com/
* https://travis-ci.org/
* http://www.fabfile.org/
* http://www.pyinvoke.org/
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* http://www.mkdocs.org/
* https://try.jupyter.org/
* https://coverage.readthedocs.io/en/coverage-4.3.4/
* http://flake8.pycqa.org/en/latest/


```python

```


```python

```


```python

```


```python

```


```python
MMM
```
