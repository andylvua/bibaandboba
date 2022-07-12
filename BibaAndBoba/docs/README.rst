**Python package for analyzing Telegram chats and finding correlations between people**

=====
About
=====

**BibaAndBoba** is a tool for analyzing files containing Telegram chat
history.

It will allow you to identify the so-called parasite words for each
person you are talking to, and will also allow you to find the
correlation coefficient between your two interlocutors. Such a
coefficient represents the probability that these two people communicate
with each other.
    This approach is based on the fact that people tend
    to adopt the words used by the interlocutor.

=====
Usage
=====

Installation
------------
First of all you have to install the BibaAndBoba package using pip

.. code-block:: python
   :caption: Installation

   pip install BibaAndBoba

Preparing Telegram chat history files
-------------------------------------
How to choose chats
*******************
Analysis requires at least 2 chats. One chat will be used as the base and the other will be used
as an auxiliary to identify words that are unique to your interlocutor.

.. note::
   For a correct analysis, the auxiliary chat should be selected in such a way
   that this person communicates as little as possible with the one you want to analyze.

It takes at least 3 chats, *preferably 4*, to find the correlation coefficient between two people.
2 of them are with people, the correlation between which you want to find.
2 auxiliary chats will also be required, chosen according to the principle described above.
   If you know a person who does not communicate with any of the ones you want to analyze,
   you can use the chat with them for both base chats. However, remember that such approach will still reduce
   the accuracy of the analysis, so choose a different support chat for each individual if possible.

Exporting chat history files
****************************
1. **Navigate to the chat you want to analyze.**

Find the three dots menu, and select the ``Export chat history`` option:

.. image:: ../assets/exporting-0.png
   :alt: exporting-0
   :width: 300px

2. **Configure chat export settings as shown below.**

* Disable the ``Photos`` option.
* Set ``Size limit`` to 500 MB.

.. image:: ../assets/exporting-1.png
   :alt: exporting-0
   :width: 300px

* Set ``Format`` to ``Machine-readable JSON``.
* Set ``Path`` to your desired export directory.

.. image:: ../assets/exporting-2.png
   :alt: exporting-0
   :width: 300px

**Click** ``Export`` and wait for the export to finish.

**The file that will be used for analysis will be located in the path you selected under the name** ``result.json``

   I recommend to immediately rename the source files to the name of your interlocutor for your convenience.
   For example, if you export a chat with *Pavlo*, rename the file ``result.json`` to ``pavlo.json``.

Now we are ready to go.

Code
----
Finding parasite words
**********************
Assuming you have the following project structure:

.. image:: ../assets/project-structure.png
   :alt: exporting-0
   :width: 300px

For example, you want to find words that ``Pavlo`` uses often.
At the same time, you know that the ``Roma`` hardly or not at all communicate with him - see `How to choose chats`_.

BibaAndBoba uses the :meth:`BibaAndBoba <nltk_analyzer.BibaAndBoba>` class to analyze chat history files.

.. code-block:: python
        :caption: Example

        from BibaAndBoba import BibaAndBoba


        def main():
            pavlo = BibaAndBoba("resources/pavlo.json", "resources/roma.json")

            print(pavlo.freq_dist())


        if __name__ == "__main__":
            main()

Finding the correlation coefficient
***********************************
It's pretty easy to do.

Create 2 objects for the people you want to find the correlation between and pass them to the
:meth:`Comparator <BibaAndBoba.comparator.Comparator>` class using the :meth:`~BibaAndBoba.comparator.Comparator.get_correlation()` method.

.. code-block:: python
        :caption: Example

        from BibaAndBoba import BibaAndBoba, Comparator


        def main():
            pavlo = BibaAndBoba("resources/pavlo.json", "resources/roma.json")
            andrii = BibaAndBoba("resources/andrii.json", "resources/nasta.json")

            correlation = Comparator(pavlo, andrii).get_correlation()
            print(correlation)


        if __name__ == "__main__":
            main()

========
Contents
========
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   BibaAndBoba

Here you can find the complete documentation of the classes and methods used by BibaAndBoba.

:class:`~biba_and_boba.BibaAndBoba`
-----------------------------------

:class:`~comparator.Comparator`
-------------------------------