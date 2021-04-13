# [GoogleKickStart 2020](https://codingcompetitions.withgoogle.com/kickstart/archive/2020) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-32%20%2F%2032-ff69b4.svg)

Python solutions of Google Kick Start 2020. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

* [Kick Start 2019](https://github.com/kamyu104/GoogleKickStart-2019)
* [Round A](https://github.com/kamyu104/GoogleKickStart-2020#round-a)
* [Round B](https://github.com/kamyu104/GoogleKickStart-2020#round-b)
* [Round C](https://github.com/kamyu104/GoogleKickStart-2020#round-c)
* [Round D](https://github.com/kamyu104/GoogleKickStart-2020#round-d)
* [Round E](https://github.com/kamyu104/GoogleKickStart-2020#round-e)
* [Round F](https://github.com/kamyu104/GoogleKickStart-2020#round-f)
* [Round G](https://github.com/kamyu104/GoogleKickStart-2020#round-g)
* [Round H](https://github.com/kamyu104/GoogleKickStart-2020#round-h)
* [Kick Start 2021](https://github.com/kamyu104/GoogleKickStart-2021)

## Round A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Allocation](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56)| [Python](./Round%20A/allocation.py)| _O(N)_ | _O(MAX_A)_ | Easy | | Greedy, Counting Sort |
|B| [Plates](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb)| [Python](./Round%20A/plates.py) | _O(N * P * K)_ | _O(P)_ | Easy | | DP, Prefix Sum |
|C| [Workout](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b)| [Python](./Round%20A/workout.py)| _O(Nlog(MAX_DIFF))_ | _O(1)_ | Easy | | Binary Search, Greedy |
|D| [Bundling](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3)| [Python](./Round%20A/bundling.py) | _O(N * L)_ | _O(T)_ | Medium | | Trie, Greedy, DFS, Stack |

## Round B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Bike Tour](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6)| [Python](./Round%20B/bike_tour.py)| _O(N)_ | _O(1)_ | Easy | | Array |
|B| [Bus Routes](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf)| [Python](./Round%20B/bus_routes.py) | _O(N)_ | _O(1)_ | Easy | | Greedy |
|C| [Robot Path Decoding](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc)| [Python](./Round%20B/robot_path_decoding.py)| _O(N)_ | _O(N)_ | Easy | | Stack |
|D| [Wandering Robot](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565)| [Python](./Round%20B/wandering_robot.py) [Python](./Round%20B/wandering_robot2.py) | _O(W + H)_ | _O(W + H)_ | Hard | | Binomial Coefficients, Probability, Log Representation, Prefix Sum |

## Round C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Countdown](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2)| [Python](./Round%20C/countdown.py)| _O(N)_ | _O(1)_ | Easy | | Array |
|B| [Stable Wall](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb)| [Python](./Round%20C/stable_wall.py) | _O(R * C)_ | _O(1)_ | Easy | | Topological Sort, DFS |
|C| [Perfect Subarray](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb)| [PyPy](./Round%20C/perfect_subarray.py)| _O(N * sqrt(N * MAX_A))_ | _O(N * MAX_A)_ | Medium | | Math, Prefix Sum |
|D| [Candies](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d)| [Python](./Round%20C/candies.py) | _O(N + QlogN)_ | _O(N)_ | Medium | | BIT, Fenwick Tree |

## Round D
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Record Breaker](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171)| [Python](./Round%20D/record_breaker.py)| _O(N)_ | _O(1)_ | Easy | | Array |
|B| [Alien Piano](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174)| [Python](./Round%20D/alien_piano.py) | _O(K)_ | _O(1)_ | Easy | | Greedy |
|C| [Beauty of Tree](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd)| [Python](./Round%20D/beauty_of_tree.py)| _O(N)_ | _O(N)_ | Medium | | DFS, Math |
|D| [Locked Doors](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c)| [PyPy](./Round%20D/locked_doors.py) | _O(NlogN + QlogN)_ | _O(N)_ | Hard | | Cartesian Tree, Binary Lifting |

## Round E
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Longest Arithmetic](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed)| [Python](./Round%20E/longest_arithmetic.py)| _O(N)_ | _O(1)_ | Easy | | Array |
|B| [High Buildings](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73)| [Python](./Round%20E/high_buildings.py) | _O(N)_ | _O(N)_ | Easy | | Construction |
|C| [Toys](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bede9)| [Python](./Round%20E/toys.py)| _O(NlogN)_ | _O(N)_ | Medium | | Greedy, Heap |
|D| [Golden Stone](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29)| [Python](./Round%20E/golden_stone.py) [Python](./Round%20E/golden_stone2.py) | _O((N * S + M * S + R * N) * log(N * S))_ | _O(N * S + M)_ | Hard | | Dijkstra's Algorithm |

## Round F
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [ATM Queue](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8)| [Python](./Round%20F/atm_queue.py)| _O(NlogN)_ | _O(1)_ | Easy | | Sort |
|B| [Metal Harvest](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4b8b)| [Python](./Round%20F/metal_harvest.py) | _O(NlogN)_ | _O(1)_ | Easy | | Sort |
|C| [Painters' Duel](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f47fb)| [Python](./Round%20F/painters_duel.py)| _O(2^(S^2))_ | _O(2^(S^2))_ | Medium | | Memoization, Alpha Beta Pruning |
|D| [Yeetzhee](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4dea)| [Python](./Round%20F/yeetzhee.py) | _O(M * S)_ | _O(M * S)_ | Hard | | Math, Expected Value, Memoization, Greedy |

## Round G
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Kick_Start](https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb)| [Python](./Round%20G/kick_start.py)| _O(N)_ | _O(1)_ | Easy | | Math |
|B| [Maximum Coins](https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23)| [Python](./Round%20G/maximum_coins.py) [Python](./Round%20G/maximum_coins2.py)| _O(N^2)_ | _O(1)_ | Easy | | Matrix |
|C| [Combination Lock](https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24)| [Python](./Round%20G/combination_lock.py) [Python](./Round%20G/combination_lock2.py)| _O(WlogW)_ | _O(1)_ | Easy | | Math, Prefix Sum |
|D| [Merge Cards](https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054)| [Python](./Round%20G/merge_cards2.py) [Python](./Round%20G/merge_cards3.py) | _O(N)_ | _O(N)_ | Medium | | Math, Expected Value, DP, Precompute, Prefix Sum |

## Round H
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Retype](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7)| [Python](./Round%20H/retype.py)| _O(1)_ | _O(1)_ | Easy | | Math |
|B| [Boring Numbers](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6)| [Python](./Round%20H/boring_numbers.py)| _O(logR)_ | _O(1)_ | Easy | | Math |
|C| [Rugby](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027)| [Python](./Round%20H/rugby.py)| _O(NlogN)_ | _O(N)_ | Medium | | Math |
|D| [Friends](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043aee7)| [PyPy](./Round%20H/friends.py) [PyPy](./Round%20H/friends2.py) | _O(A^3 + L^2 * (N + Q))_ | _O(A^2)_ | Medium | | Floyd-Warshall Algorithm |
