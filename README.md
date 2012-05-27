OpenSND
=======

OpenSND is an open clone of the now abandoned Seek and Dread Online.

Background
==========

Seek and Dread Online used a game middleware product called Multimedia Fusion
1.5, and this employed a small virtual machine that ran the game. I have
reconstructed the source code by converting the middleware VM bytecode to native
Python sources, but at the moment, it's quite a mess. This is mostly due to the
coding style that the middleware advocates, and the idea is to clean up the code
and to eventually make a better implementation.

Help and donations
==================

Since I am doing this in my spare time, I could desperately need some assistance.
The biggest task is to clean up frame6.py, which consists of about 20K LOC. A
lot of code duplication is going on, and I'm sure we can get the file down to
about 10~5K LOC.

If you would like to donate to this cause, feel free to send me a donation
by the donation button on http://mp2.dk.