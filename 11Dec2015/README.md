This is my solution to [The Riddler](https://fivethirtyeight.com/features/whats-the-best-way-to-drop-a-smartphone/?ex_cid=538fb) from 11 Dec 2015 from FiveThirtyEight.

My solution devises the following mechanism as the ideal scheme for dropping the smart phone.

1. Pick `n` between 1 and the number of floors in our building (`nFloors`).
2. Go up `n` floors and drop one of the phones. If it breaks, then go to floor 1 and drop the other phone on every floor between 1 and `n-1` until the phone breaks, this is then your maximum height (if it does not break by floor `n-1`, then your maximum floor is `n`). If it does not break, proceed to step 3.
3. Go up another `n` floors, to bring you to `2n` and drop one of the phones. If it breaks, drop the other phone on every floor between `n+1` and `2n-1` until the phone breaks, this is then your maximum height (again if it does not break by floor `2n-1`, then your maximum floor is `n`). If it does not break, proceed to step 4.
4. Repeat step 3, but bringing to floor `i*n` and drop the phone. If it breaks, drop the otehr phone on every floor between `(i-1)*n+1` and `i*n-1` until the phone breaks, this is then your maximum height. If it does not break, increment `i`, and repeat this step, unless `i*n>nFloors`, in which case proceed to step 5.
5. If `(i+1)*n` is greater than `nFloors`, then drop the phone on every floor from `i*n+1` to `nFloors` until it breaks.

I implement this scheme in the `trials` method of `PhoneDropper.py`, which takes the interval `n` as `intervals` and the floor which is the phone's maximum height as `breakFloor`. In the `findMax` method, for a particular interval `n`, `trials` is called for every possible `breakFloor` to determine the maximum number of drops needed for each interval `n`. At the end of the script, I then loop through all possible intervals and call `findMax` for each of these to determine the minimal number of drops. For `nFloors=100`, that minimum is 19 drops and for `nFloors=1000`, that minimum is 62.
