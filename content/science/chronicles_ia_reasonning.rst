============================================
AIs that break down questions reason better
============================================

:date: 2025-06-20
:tags: science, research, AI, chronicle, AI chronicle

.. image:: ../science/attachments/ai_thinking.jpg
   :align: right
   :scale: 15 %
   :class: small
   :alt: Image generated with "LeChat", with the prompt "Please generate an image of an AI that is thinking deeply. Philosophical references may be welcomed, for instance like the classic hamlet holding skull cliché."

The key to the most powerful conversational AIs is to reason by breaking
down a complex task into simpler subproblems. Why is this crucial, and
how does it work?

.. note::

   This post was originally published in French as part of my scientific
   chronicle in `Les Echos
   <https://www.lesechos.fr/idees-debats/sciences-prospective/les-ia-qui-decomposent-les-questions-raisonnent-mieux-2151428>`_.


The recent release of the conversational AI "DeepSeek R1" shook the
financial markets because it showed a significant reduction in the costs
of reasoning models. But what are these reasoning models?

To understand the challenges of reasoning in conversational AIs, we can
ask them to solve riddles. I tried various logical riddles on different
AIs, such as the puzzle where a man has to get a fox, a chicken, and a
sack of corn across a river without one eating the other. The AI responds
brilliantly. But how can we ensure that the AI is truly reasoning and not
just reciting answers it has seen before? By replacing them with other
equivalent animals (wolf, lamb, and hay), the AI does just as well. But
it could have solved the problem by analogy with the previous classic
one, rather than with reasonning. Indeed language models are very good at
analogies. A conversational AI typically works by proposing a answer
inspired by the flow of words (and corresponding concepts) in the texts
on which it was trained.

If, instead of a riddle resembling a story, we try to play tic-tac-toe,
the weaknesses appear. Most conversational AIs are very bad at
tic-tac-toe, even going so far as to declare victory when faced with a
defeat. Perhaps this is because analogy is not as useful. But activating
the "reasoning" option makes them unbeatable. What is behind this option?

A third task helps to understand the reasoning mechanisms of a
conversational AI: let's ask it how many "L"s there are in
"LOLLAPALOUZA". There is a catch: ChatGPT was able to give me the correct
for the number of Ls in "LOLLAPALOOZA", a question often used in the past
to show its limits. For "LOLLAPALOUZA", it fails. Or rather, it needs
help: if we tell it to spell out the word, then count the "L"s, it gives
the correct answer. With the right intermediate steps, a problem is often
much simpler. These decompositions into subproblems are called chains of
thought in conversational AIs. The "reasoning" option of some AIs
generates such chains.

DeepSeek R1 received much attention due to its excellence in breaking
down problems to reason in such a way. To do this, it has been trained to
generate reasoning patterns from questions, using reinforcement learning:
through trial and error, on many problems generated with the associated
answer, like math problems. Faced with a task, the AI still proceeds by
analogy with the tasks it has seen during this learning phase, but it
uses this analogy to sketch a battle plan, rather than a response. Each
subproblem is then easier, and the AI can tackle it by analogy to
problems already seen. By observing the chains of thought, we can even
see the AI verifying its intermediate results. These chains of thought
are not always visible, but we can guess them from the AI's response
time.

|

With these reasoning mechanisms, a conversational AI is as good as I am
at tic-tac-toe. But using such a model to play tic-tac-toe is like using
a sledgehammer to crush a fly: it is very inefficient in computational
cost compared to a specialized program for tic-tac-toe, which we have
known how to do for decades.

|

.. topic:: AI chronicles

    Find all my AI chronicles `here <https://gael-varoquaux.info/tag/ai-chronicle.html>`_

