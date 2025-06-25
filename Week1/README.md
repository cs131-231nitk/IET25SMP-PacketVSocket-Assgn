# Week 1 Solutions

The best solutions are submitted by:
- Assignment 1 - Anirudh Nayak
- Assignment 2 - Roshan Vishwanath

## Solution for Packet Tracer:
The issue was the PCs were in different network configurations. To rectify it up, we've to enable **ip-routing** by using a router.
- Add a new Switch to the configuration and connect the PC with IP:`192.168.1.x` to it.
- Let the two PCs with IP:`192.168.0.x` remain in the same switch.
- Insert a Router to the configuration (prefer the latests ones - 4331).
- Join the interfaces anyway you please as below:
    - Switch0 (`192.168.0.x`) to Router's `GigabitEthernet0/0/0`
    - Switch1 (`192.168.1.x`) to Router's `GigabitEthernet0/0/1`
- After connecting, you'll have to **enable** the interface, and assign an IP to the interface:
    - Assign `GigabitEthernet0/0/0` with an IP unassigned in `192.168.0.x`, preferrably `192.168.0.1`.
    - Assign `GigabitEthernet0/0/1` with an IP unassigned in `192.168.1.x`, preferrably `192.168.1.1`.
    - Enable the interfaces by **Ticking ON** on the Port-Status in the Config panel of the Router.
- Just wait for a few moment until all interfaces are up. (STP/RSTP to be done with)
- Try pinging :) Should work.

## Solution for Python:
Nothing real fancy, just code out some questions. A sample is here:
```python
points=0
print("What comes after A?\n\tA. B\n\tB. D\n\tC. A\n\tD. C")
c = input()
if (c=="c" or c=="C"):
    print("Right!")
    points+=1
else:
    print("Nope, Answer was C.")

# ... Just repeat something similar
```
---

This was Week 1's solution :)

Kudos to the submitters and best-solution providers. :')