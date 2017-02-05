# tweetnacl
Python implementation of the TweetNaCl cryptograhic library

(Everybody implements TweetNaCl, so I want to do it too.)

This is a pure Python3 implementation of the
[TweetNacl](https://tweetnacl.cr.yp.to/) cryptographic library. This
implementation is inspired by the
[tweetnacl-js](https://github.com/dchest/tweetnacl-js) library.


## Plan

Starting out getting the functionality in place, including a lot of test
cases. Hopefully adding test cases from
[Whycheproof](https://github.com/google/wycheproof). Then moving towards
performance improved implemenation. This means that in comparison to
tweetnacl-js, there will not be two different versions.

I want to learn how to write best Python modules according to best
practive and will spend time ensuring that I try to do that. If I'm not,
please add issue/comment with good pointers. Thanks!

[Currently following this structure description](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html)


## Implementation

**NOTE** Python does not allow cycle accurate control of execution. Even
though the code is (will be) written to avoid loops etc that can cause
data dependent timing variance (leading to possible leakage), the code
should not be considered leakage resistant.


## Status

Just starting out. This is even before possible Dragons.
