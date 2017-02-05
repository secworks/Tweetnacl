# tweetnacl
Python implementation of the TweetNaCl cryptograhic library

(Everybody implements TweetNaCl, so I want to do it too.)

This is a pure Python3 implementation of the
[https://tweetnacl.cr.yp.to/](TweetNacl) cryptographic library. This
implementation is inspired by the
[https://github.com/dchest/tweetnacl-js](tweetnacl-js) library.


## Plan

Starting out getting the functionality in place, including a lot of test
cases. Hopefully adding test cases from
[https://github.com/google/wycheproof](Whycheproof). Then moving towards
performance improved implemenation. This means that in comparison to
tweetnacl-js, there will not be two different versions.

I want to learn how to write best Python modules according to best
practive and will spend time ensuring that I try to do that. If I'm not,
please add issue/comment with good pointers. Thanks!

[http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html](Currently
following this structure description)


## Implementation

**NOTE** Python does not allow cycle accurate control of execution. Even
though the code is (will be) written to avoid loops etc that can cause
data dependent timing variance (leading to possible leakage), the code
should not be considered leakage resistant.


## Status

Just starting out. This is even before possible Dragons.
