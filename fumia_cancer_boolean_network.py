#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fumia cancer network Boolean update rules
"""

from sympy import symbols

x00, x01, x02, x03, x04, x05 = symbols('x00, x01, x02, x03, x04, x05')
x06, x07, x08, x09, x10 = symbols('x06, x07, x08, x09, x10')
x11, x12, x13, x14, x15, x16, x17, x18, x19, x20 = symbols('x11:21')
x21, x22, x23, x24, x25, x26, x27, x28, x29, x30 = symbols('x21:31')
x31, x32, x33, x34, x35, x36, x37, x38, x39, x40 = symbols('x31:41')
x41, x42, x43, x44, x45, x46, x47, x48, x49, x50 = symbols('x41:51')
x51, x52, x53, x54, x55, x56, x57, x58, x59, x60 = symbols('x51:61')
x61, x62, x63, x64, x65, x66, x67, x68, x69, x70 = symbols('x61:71')
x71, x72, x73, x74, x75, x76, x77, x78, x79, x80 = symbols('x71:81')
x81, x82, x83, x84, x85, x86, x87, x88, x89, x90 = symbols('x81:91')
x91, x92, x93, x94, x95 = symbols('x91:96')

num_states = 96

x_state_string = 'x{std:d}:{ed:d}'
x_state = symbols(x_state_string.format(std=0, ed=num_states))
x_state = list(x_state)
x_state[0:10] = x00, x01, x02, x03, x04, x05, x06, x07, x08, x09
x_state = tuple(x_state)

x00k, x01k, x02k, x03k, x04k, x05k = symbols(
    'x00k, x01k, x02k, x03k, x04k, x05k')
x06k, x07k, x08k, x09k, x10k = symbols('x06k, x07k, x08k, x09k, x10k')
x11k, x12k, x13k, x14k, x15k, x16k, x17k, x18k, x19k, x20k = symbols(
    'x11k, x12k, x13k, x14k, x15k, x16k, x17k, x18k, x19k, x20k')
x21k, x22k, x23k, x24k, x25k, x26k, x27k, x28k, x29k, x30k = symbols(
    'x21k, x22k, x23k, x24k, x25k, x26k, x27k, x28k, x29k, x30k')
x31k, x32k, x33k, x34k, x35k, x36k, x37k, x38k, x39k, x40k = symbols(
    'x31k, x32k, x33k, x34k, x35k, x36k, x37k, x38k, x39k, x40k')
x41k, x42k, x43k, x44k, x45k, x46k, x47k, x48k, x49k, x50k = symbols(
    'x41k, x42k, x43k, x44k, x45k, x46k, x47k, x48k, x49k, x50k')
x51k, x52k, x53k, x54k, x55k, x56k, x57k, x58k, x59k, x60k = symbols(
    'x51k, x52k, x53k, x54k, x55k, x56k, x57k, x58k, x59k, x60k')
x61k, x62k, x63k, x64k, x65k, x66k, x67k, x68k, x69k, x70k = symbols(
    'x61k, x62k, x63k, x64k, x65k, x66k, x67k, x68k, x69k, x70k')
x71k, x72k, x73k, x74k, x75k, x76k, x77k, x78k, x79k, x80k = symbols(
    'x71k, x72k, x73k, x74k, x75k, x76k, x77k, x78k, x79k, x80k')
x81k, x82k, x83k, x84k, x85k, x86k, x87k, x88k, x89k, x90k = symbols(
    'x81k, x82k, x83k, x84k, x85k, x86k, x87k, x88k, x89k, x90k')
x91k, x92k, x93k, x94k, x95k = symbols('x91k, x92k, x93k, x94k, x95k')

xk_state_string = 'x{std:d}:{ed:d}k'
xk_state = symbols(xk_state_string.format(std=0, ed=num_states))
xk_state = list(xk_state)
xk_state[0:10] = x00k, x01k, x02k, x03k, x04k, x05k, x06k, x07k, x08k, x09k
xk_state = tuple(xk_state)


# six input states
ic00, ic01, ic02, ic03, ic04, ic05 = symbols(
    'ic00, ic01, ic02, ic03, ic04, ic05')
ic00 = (ic00).subs({ic00: False})
ic01 = (ic01).subs({ic01: True})
ic02 = (ic02).subs({ic02: True})
ic03 = (ic03).subs({ic03: False})
ic04 = (ic04).subs({ic04: False})
ic05 = (ic05).subs({ic05: False})

# six constant states
c16, c27, c39, c50, c69, c71 = symbols('c16, c27, c39, c50, c69, c71')
c16 = (c16).subs({c16: True})
c27 = (c27).subs({c27: True})
c39 = (c39).subs({c39: True})
c50 = (c50).subs({c50: False})
c69 = (c69).subs({c69: True})
c71 = (c71).subs({c71: False})


# output
# x76: Apoptosis
# x78: Glut1
# x90: DNA Repair
# x95: AcidLactic

##########################################################
# update rule: x(k+1) = f[x(k)]
##########################################################
update_rule = {
    x00: ic00,
    x01: ic01,
    x02: ic02,
    x03: ic03,
    x04: ic04,
    x05: ic05,
    x06: x33k,
    x07: x00k | x71k,
    x08: x43k & x60k,
    x09: ~ x01k,
    x10: ~ x11k,
    x11: x12k | x25k,
    x12: x02k,
    x13: x01k & ~ x03k,
    x14: x12k | ~ x10k,
    x15: x14k | x78k,
    x16: c16,
    x17: (x15k & ~ x16k) | (x15k & ~ x92k) | (~ x16k & ~ x92k),
    x18: x17k | x33k | x37k,
    x19: (x11k & x24k & x32k) | (x11k & x24k & x82k) | (x11k & x32k & x82k) | (x24k & x32k & x82k) | (x11k & x24k & ~ x36k) | (x11k & x24k & ~ x43k) | (x11k & x32k & ~ x36k) | (x11k & x32k & ~ x43k) | (x11k & x82k & ~ x36k) | (x11k & x82k & ~ x43k) | (x24k & x32k & ~ x36k) | (x24k & x32k & ~ x43k) | (x24k & x82k & ~ x36k) | (x24k & x82k & ~ x43k) | (x32k & x82k & ~ x36k) | (x32k & x82k & ~ x43k) | (x11k & ~ x36k & ~ x43k) | (x24k & ~ x36k & ~ x43k) | (x32k & ~ x36k & ~ x43k) | (x82k & ~ x36k & ~ x43k),
    x20: (x17k & x19k) | (x19k & x95k) | (x19k & ~ x76k) | (x17k & x95k & ~ x76k),
    x21: x11k | x14k,
    x22: x21k,
    x23: x18k | x22k,
    x24: x17k & x18k,
    x25: x04k & ~ x43k,
    x26: x25k,
    x27: c27,
    x28: (~ x23k & ~ x24k) | (~ x23k & ~ x26k) | (~ x23k & ~ x32k) | (~ x24k & ~ x26k) | (~ x24k & ~ x32k) | (~ x26k & ~ x32k),
    x29: x27k & x28k,
    x30: ~ x29k & ~ x43k,
    x31: (x20k & x84k) | (x20k & ~ x08k) | (x84k & ~ x08k),
    x32: (x13k | x24k) & (x13k | x42k) & (x24k | x42k) & (x13k | ~ x72k) & (x24k | ~ x72k) & (x42k | ~ x72k),
    x33: (x03k & x32k & ~ x35k) | (x03k & x37k & ~ x35k) | (x32k & x37k & ~ x35k) | (x03k & ~ x35k & ~ x36k) | (x03k & ~ x35k & ~ x43k) | (x03k & ~ x35k & ~ x69k) | (x32k & ~ x35k & ~ x36k) | (x32k & ~ x35k & ~ x43k) | (x32k & ~ x35k & ~ x69k) | (x37k & ~ x35k & ~ x36k) | (x37k & ~ x35k & ~ x43k) | (x37k & ~ x35k & ~ x69k) | (x03k & x32k & x37k & ~ x36k) | (x03k & x32k & x37k & ~ x43k) | (x03k & x32k & x37k & ~ x69k) | (~ x35k & ~ x36k & ~ x43k) | (~ x35k & ~ x36k & ~ x69k) | (~ x35k & ~ x43k & ~ x69k) | (x03k & x32k & ~ x36k & ~ x43k) | (x03k & x32k & ~ x36k & ~ x69k) | (x03k & x32k & ~ x43k & ~ x69k) | (x03k & x37k & ~ x36k & ~ x43k) | (x03k & x37k & ~ x36k & ~ x69k) | (x03k & x37k & ~ x43k & ~ x69k) | (x32k & x37k & ~ x36k & ~ x43k) | (x32k & x37k & ~ x36k & ~ x69k) | (x32k & x37k & ~ x43k & ~ x69k) | (x03k & ~ x36k & ~ x43k & ~ x69k) | (x32k & ~ x36k & ~ x43k & ~ x69k) | (x37k & ~ x36k & ~ x43k & ~ x69k),
    x34: x33k,
    x35: ~ x03k & ~ x71k,
    x36: x71k | ~ x03k,
    x37: x38k & x39k & ~ x06k & ~ x40k & ~ x63k,
    x38: (x04k & x20k & x22k) | (x04k & x20k & x49k) | (x04k & x20k & x70k) | (x04k & x20k & x84k) | (x04k & x22k & x49k) | (x04k & x22k & x70k) | (x04k & x22k & x84k) | (x04k & x49k & x70k) | (x04k & x49k & x84k) | (x04k & x70k & x84k) | (x20k & x22k & x49k) | (x20k & x22k & x70k) | (x20k & x22k & x84k) | (x20k & x49k & x70k) | (x20k & x49k & x84k) | (x20k & x70k & x84k) | (x22k & x49k & x70k) | (x22k & x49k & x84k) | (x22k & x70k & x84k) | (x49k & x70k & x84k) | (x04k & x20k & ~ x33k) | (x04k & x22k & ~ x33k) | (x04k & x49k & ~ x33k) | (x04k & x70k & ~ x33k) | (x04k & x84k & ~ x33k) | (x20k & x22k & ~ x33k) | (x20k & x49k & ~ x33k) | (x20k & x70k & ~ x33k) | (x20k & x84k & ~ x33k) | (x22k & x49k & ~ x33k) | (x22k & x70k & ~ x33k) | (x22k & x84k & ~ x33k) | (x49k & x70k & ~ x33k) | (x49k & x84k & ~ x33k) | (x70k & x84k & ~ x33k),
    x39: c39,
    x40: x33k,
    x41: (x33k & x43k & x72k & ~ x21k) | (x33k & x43k & x72k & ~ x22k) | (x33k & x43k & x72k & ~ x23k) | (x33k & x43k & x72k & ~ x24k) | (x33k & x43k & ~ x21k & ~ x22k) | (x33k & x43k & ~ x21k & ~ x23k) | (x33k & x43k & ~ x21k & ~ x24k) | (x33k & x43k & ~ x22k & ~ x23k) | (x33k & x43k & ~ x22k & ~ x24k) | (x33k & x43k & ~ x23k & ~ x24k) | (x33k & x72k & ~ x21k & ~ x22k) | (x33k & x72k & ~ x21k & ~ x23k) | (x33k & x72k & ~ x21k & ~ x24k) | (x33k & x72k & ~ x22k & ~ x23k) | (x33k & x72k & ~ x22k & ~ x24k) | (x33k & x72k & ~ x23k & ~ x24k) | (x43k & x72k & ~ x21k & ~ x22k) | (x43k & x72k & ~ x21k & ~ x23k) | (x43k & x72k & ~ x21k & ~ x24k) | (x43k & x72k & ~ x22k & ~ x23k) | (x43k & x72k & ~ x22k & ~ x24k) | (x43k & x72k & ~ x23k & ~ x24k) | (x33k & ~ x21k & ~ x22k & ~ x23k) | (x33k & ~ x21k & ~ x22k & ~ x24k) | (x33k & ~ x21k & ~ x23k & ~ x24k) | (x33k & ~ x22k & ~ x23k & ~ x24k) | (x43k & ~ x21k & ~ x22k & ~ x23k) | (x43k & ~ x21k & ~ x22k & ~ x24k) | (x43k & ~ x21k & ~ x23k & ~ x24k) | (x43k & ~ x22k & ~ x23k & ~ x24k) | (x72k & ~ x21k & ~ x22k & ~ x23k) | (x72k & ~ x21k & ~ x22k & ~ x24k) | (x72k & ~ x21k & ~ x23k & ~ x24k) | (x72k & ~ x22k & ~ x23k & ~ x24k) | (~ x21k & ~ x22k & ~ x23k & ~ x24k),
    x42: ~ x41k,
    x43: (x33k & x88k) | (x33k & ~ x44k) | (x33k & ~ x60k) | (x88k & ~ x44k) | (x88k & ~ x60k) | (~ x44k & ~ x60k),
    x44: x20k & (~ x43k | ~ x45k) & (~ x43k | ~ x46k) & (~ x45k | ~ x46k),
    x45: (x43k | x68k) & (x43k | ~ x33k) & (x43k | ~ x44k) & (x68k | ~ x33k) & (x68k | ~ x44k) & (~ x33k | ~ x44k),
    x46: ~ x21k & ~ x23k & ~ x24k & ~ x33k,
    x47: ~ x43k & ~ x46k,
    x48: (~ x51k | ~ x52k) & (~ x51k | ~ x53k) & (~ x51k | ~ x54k) & (~ x51k | ~ x60k) & (~ x52k | ~ x53k) & (~ x52k | ~ x54k) & (~ x52k | ~ x60k) & (~ x53k | ~ x54k) & (~ x53k | ~ x60k) & (~ x54k | ~ x60k),
    x49: ~ x48k & (x49k | ~ x51k) & (x49k | ~ x52k) & (~ x51k | ~ x52k),
    x50: c50,
    x51: (x51k | x80k | x81k) & (x51k | x80k | ~ x48k) & (x51k | x80k | ~ x56k) & (x51k | x80k | ~ x58k) & (x51k | x80k | ~ x59k) & (x51k | x81k | ~ x48k) & (x51k | x81k | ~ x56k) & (x51k | x81k | ~ x58k) & (x51k | x81k | ~ x59k) & (x80k | x81k | ~ x48k) & (x80k | x81k | ~ x56k) & (x80k | x81k | ~ x58k) & (x80k | x81k | ~ x59k) & (x51k | ~ x48k | ~ x56k) & (x51k | ~ x48k | ~ x58k) & (x51k | ~ x48k | ~ x59k) & (x51k | ~ x56k | ~ x58k) & (x51k | ~ x56k | ~ x59k) & (x51k | ~ x58k | ~ x59k) & (x80k | ~ x48k | ~ x56k) & (x80k | ~ x48k | ~ x58k) & (x80k | ~ x48k | ~ x59k) & (x80k | ~ x56k | ~ x58k) & (x80k | ~ x56k | ~ x59k) & (x80k | ~ x58k | ~ x59k) & (x81k | ~ x48k | ~ x56k) & (x81k | ~ x48k | ~ x58k) & (x81k | ~ x48k | ~ x59k) & (x81k | ~ x56k | ~ x58k) & (x81k | ~ x56k | ~ x59k) & (x81k | ~ x58k | ~ x59k) & (~ x48k | ~ x56k | ~ x58k) & (~ x48k | ~ x56k | ~ x59k) & (~ x48k | ~ x58k | ~ x59k) & (~ x56k | ~ x58k | ~ x59k),
    x52: ~ x43k & ~ x55k & ~ x56k & ~ x58k & ~ x59k,
    x53: (x04k & x20k & x37k & x58k & x59k & x64k & x69k & x70k & x84k & ~ x28k) | (x04k & x20k & x28k & x37k & x58k & x59k & x70k & x84k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x37k & x58k & x64k & x70k & x84k & ~ x59k & ~ x69k) | (x04k & x20k & x28k & x37k & x58k & x69k & x70k & x84k & ~ x59k & ~ x64k) | (x04k & x20k & x28k & x37k & x59k & x64k & x70k & x84k & ~ x58k & ~ x69k) | (x04k & x20k & x28k & x37k & x59k & x69k & x70k & x84k & ~ x58k & ~ x64k) | (x04k & x20k & x28k & x37k & x64k & x69k & x70k & x84k & ~ x58k & ~ x59k) | (x04k & x20k & x37k & x58k & x59k & x64k & x70k & x84k & ~ x28k & ~ x69k) | (x04k & x20k & x37k & x58k & x59k & x69k & x70k & x84k & ~ x28k & ~ x64k) | (x04k & x20k & x37k & x58k & x64k & x69k & x70k & x84k & ~ x28k & ~ x59k) | (x04k & x20k & x37k & x59k & x64k & x69k & x70k & x84k & ~ x28k & ~ x58k) | (x04k & x20k & x28k & x37k & x58k & x70k & x84k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x37k & x59k & x70k & x84k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x37k & x64k & x70k & x84k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x20k & x28k & x37k & x69k & x70k & x84k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x20k & x37k & x58k & x59k & x64k & x70k & ~ x28k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x58k & x59k & x64k & x84k & ~ x28k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x58k & x59k & x69k & x70k & ~ x28k & ~ x64k & ~ x84k) | (x04k & x20k & x37k & x58k & x59k & x69k & x84k & ~ x28k & ~ x64k & ~ x70k) | (x04k & x20k & x37k & x58k & x59k & x70k & x84k & ~ x28k & ~ x64k & ~ x69k) | (x04k & x20k & x37k & x58k & x64k & x69k & x70k & ~ x28k & ~ x59k & ~ x84k) | (x04k & x20k & x37k & x58k & x64k & x69k & x84k & ~ x28k & ~ x59k & ~ x70k) | (x04k & x20k & x37k & x58k & x64k & x70k & x84k & ~ x28k & ~ x59k & ~ x69k) | (x04k & x20k & x37k & x58k & x69k & x70k & x84k & ~ x28k & ~ x59k & ~ x64k) | (x04k & x20k & x37k & x59k & x64k & x69k & x70k & ~ x28k & ~ x58k & ~ x84k) | (x04k & x20k & x37k & x59k & x64k & x69k & x84k & ~ x28k & ~ x58k & ~ x70k) | (x04k & x20k & x37k & x59k & x64k & x70k & x84k & ~ x28k & ~ x58k & ~ x69k) | (x04k & x20k & x37k & x59k & x69k & x70k & x84k & ~ x28k & ~ x58k & ~ x64k) | (x04k & x20k & x37k & x64k & x69k & x70k & x84k & ~ x28k & ~ x58k & ~ x59k) | (x04k & x20k & x58k & x59k & x64k & x70k & x84k & ~ x28k & ~ x37k & ~ x69k) | (x04k & x20k & x58k & x59k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x64k) | (x04k & x20k & x58k & x64k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x59k) | (x04k & x20k & x59k & x64k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k) | (x04k & x37k & x58k & x59k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x69k) | (x04k & x37k & x58k & x59k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x64k) | (x04k & x37k & x58k & x64k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x59k) | (x04k & x37k & x59k & x64k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k) | (x20k & x37k & x58k & x59k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x69k) | (x20k & x37k & x58k & x59k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x64k) | (x20k & x37k & x58k & x64k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x59k) | (x20k & x37k & x59k & x64k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k) | (x04k & x20k & x28k & x37k & x58k & x70k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x28k & x37k & x58k & x84k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x28k & x37k & x59k & x70k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x28k & x37k & x59k & x84k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x28k & x37k & x64k & x70k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x20k & x28k & x37k & x64k & x84k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x20k & x28k & x37k & x69k & x70k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x20k & x28k & x37k & x69k & x84k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x20k & x28k & x37k & x70k & x84k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x58k & x70k & x84k & ~ x37k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x59k & x70k & x84k & ~ x37k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x20k & x28k & x64k & x70k & x84k & ~ x37k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x20k & x28k & x69k & x70k & x84k & ~ x37k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x20k & x37k & x58k & x59k & x70k & ~ x28k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x58k & x59k & x84k & ~ x28k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x58k & x64k & x70k & ~ x28k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x58k & x64k & x84k & ~ x28k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x58k & x69k & x70k & ~ x28k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x20k & x37k & x58k & x69k & x84k & ~ x28k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x20k & x37k & x58k & x70k & x84k & ~ x28k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x37k & x59k & x64k & x70k & ~ x28k & ~ x58k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x59k & x64k & x84k & ~ x28k & ~ x58k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x59k & x69k & x70k & ~ x28k & ~ x58k & ~ x64k & ~ x84k) | (x04k & x20k & x37k & x59k & x69k & x84k & ~ x28k & ~ x58k & ~ x64k & ~ x70k) | (x04k & x20k & x37k & x59k & x70k & x84k & ~ x28k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x20k & x37k & x64k & x69k & x70k & ~ x28k & ~ x58k & ~ x59k & ~ x84k) | (x04k & x20k & x37k & x64k & x69k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x70k) | (x04k & x20k & x37k & x64k & x70k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x20k & x37k & x69k & x70k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x20k & x58k & x59k & x70k & x84k & ~ x28k & ~ x37k & ~ x64k & ~ x69k) | (x04k & x20k & x58k & x64k & x70k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x69k) | (x04k & x20k & x58k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x64k) | (x04k & x20k & x59k & x64k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x69k) | (x04k & x20k & x59k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x64k) | (x04k & x20k & x64k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k) | (x04k & x28k & x37k & x58k & x70k & x84k & ~ x20k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x28k & x37k & x59k & x70k & x84k & ~ x20k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x28k & x37k & x64k & x70k & x84k & ~ x20k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x28k & x37k & x69k & x70k & x84k & ~ x20k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x37k & x58k & x59k & x70k & x84k & ~ x20k & ~ x28k & ~ x64k & ~ x69k) | (x04k & x37k & x58k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x69k) | (x04k & x37k & x58k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x64k) | (x04k & x37k & x59k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x69k) | (x04k & x37k & x59k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x64k) | (x04k & x37k & x64k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k) | (x20k & x28k & x37k & x58k & x70k & x84k & ~ x04k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x28k & x37k & x59k & x70k & x84k & ~ x04k & ~ x58k & ~ x64k & ~ x69k) | (x20k & x28k & x37k & x64k & x70k & x84k & ~ x04k & ~ x58k & ~ x59k & ~ x69k) | (x20k & x28k & x37k & x69k & x70k & x84k & ~ x04k & ~ x58k & ~ x59k & ~ x64k) | (x20k & x37k & x58k & x59k & x70k & x84k & ~ x04k & ~ x28k & ~ x64k & ~ x69k) | (x20k & x37k & x58k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x69k) | (x20k & x37k & x58k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x64k) | (x20k & x37k & x59k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x69k) | (x20k & x37k & x59k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x64k) | (x20k & x37k & x64k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k) | (x04k & x20k & x28k & x37k & x70k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x28k & x37k & x84k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x28k & x70k & x84k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x37k & x58k & x59k & ~ x28k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x58k & x64k & ~ x28k & ~ x59k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x58k & x69k & ~ x28k & ~ x59k & ~ x64k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x58k & x70k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x58k & x84k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x59k & x64k & ~ x28k & ~ x58k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x59k & x69k & ~ x28k & ~ x58k & ~ x64k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x59k & x70k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x59k & x84k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x64k & x69k & ~ x28k & ~ x58k & ~ x59k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x64k & x70k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x64k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x69k & x70k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x20k & x37k & x69k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x20k & x37k & x70k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x58k & x59k & x70k & ~ x28k & ~ x37k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x58k & x59k & x84k & ~ x28k & ~ x37k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x58k & x64k & x70k & ~ x28k & ~ x37k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x20k & x58k & x64k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x20k & x58k & x69k & x70k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x20k & x58k & x69k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x20k & x58k & x70k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x20k & x59k & x64k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x69k & ~ x84k) | (x04k & x20k & x59k & x64k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x69k & ~ x70k) | (x04k & x20k & x59k & x69k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x84k) | (x04k & x20k & x59k & x69k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x70k) | (x04k & x20k & x59k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x20k & x64k & x69k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x84k) | (x04k & x20k & x64k & x69k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x70k) | (x04k & x20k & x64k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x20k & x69k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x28k & x37k & x70k & x84k & ~ x20k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x37k & x58k & x59k & x70k & ~ x20k & ~ x28k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x37k & x58k & x59k & x84k & ~ x20k & ~ x28k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x37k & x58k & x64k & x70k & ~ x20k & ~ x28k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x37k & x58k & x64k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x37k & x58k & x69k & x70k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x37k & x58k & x69k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x37k & x58k & x70k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x37k & x59k & x64k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x69k & ~ x84k) | (x04k & x37k & x59k & x64k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x69k & ~ x70k) | (x04k & x37k & x59k & x69k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x84k) | (x04k & x37k & x59k & x69k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x70k) | (x04k & x37k & x59k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x37k & x64k & x69k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x84k) | (x04k & x37k & x64k & x69k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x70k) | (x04k & x37k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x37k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x58k & x59k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x64k & ~ x69k) | (x04k & x58k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x69k) | (x04k & x58k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x64k) | (x04k & x59k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x69k) | (x04k & x59k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x64k) | (x04k & x64k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k) | (x20k & x28k & x37k & x70k & x84k & ~ x04k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x37k & x58k & x59k & x70k & ~ x04k & ~ x28k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x37k & x58k & x59k & x84k & ~ x04k & ~ x28k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x37k & x58k & x64k & x70k & ~ x04k & ~ x28k & ~ x59k & ~ x69k & ~ x84k) | (x20k & x37k & x58k & x64k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x69k & ~ x70k) | (x20k & x37k & x58k & x69k & x70k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x84k) | (x20k & x37k & x58k & x69k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x70k) | (x20k & x37k & x58k & x70k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x37k & x59k & x64k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x69k & ~ x84k) | (x20k & x37k & x59k & x64k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x69k & ~ x70k) | (x20k & x37k & x59k & x69k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x84k) | (x20k & x37k & x59k & x69k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x70k) | (x20k & x37k & x59k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x69k) | (x20k & x37k & x64k & x69k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x84k) | (x20k & x37k & x64k & x69k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x70k) | (x20k & x37k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x69k) | (x20k & x37k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k) | (x20k & x58k & x59k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x64k & ~ x69k) | (x20k & x58k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x59k & ~ x69k) | (x20k & x58k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x59k & ~ x64k) | (x20k & x59k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x69k) | (x20k & x59k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x64k) | (x20k & x64k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k) | (x37k & x58k & x59k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x64k & ~ x69k) | (x37k & x58k & x64k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x59k & ~ x69k) | (x37k & x58k & x69k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x59k & ~ x64k) | (x37k & x59k & x64k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x69k) | (x37k & x59k & x69k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x64k) | (x37k & x64k & x69k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k) | (x04k & x20k & x28k & x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x28k & x70k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x28k & x84k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x37k & x58k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x59k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x64k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x69k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k & ~ x84k) | (x04k & x20k & x37k & x70k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x37k & x84k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x58k & x70k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x58k & x84k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x59k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x59k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x20k & x64k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x20k & x64k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x20k & x69k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x20k & x69k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x20k & x70k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x28k & x37k & x70k & ~ x20k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x28k & x37k & x84k & ~ x20k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x28k & x70k & x84k & ~ x20k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x37k & x58k & x70k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x37k & x58k & x84k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x37k & x59k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x37k & x59k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x37k & x64k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x37k & x64k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x37k & x69k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x37k & x69k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x37k & x70k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x58k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k) | (x04k & x59k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k) | (x04k & x64k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k) | (x04k & x69k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k) | (x20k & x28k & x37k & x70k & ~ x04k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x28k & x37k & x84k & ~ x04k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x28k & x70k & x84k & ~ x04k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x37k & x58k & x70k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x37k & x58k & x84k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x37k & x59k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x37k & x59k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x37k & x64k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x20k & x37k & x64k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x20k & x37k & x69k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x20k & x37k & x69k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x20k & x37k & x70k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x58k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x59k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k) | (x20k & x64k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k) | (x20k & x69k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k) | (x28k & x37k & x70k & x84k & ~ x04k & ~ x20k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x37k & x58k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k) | (x37k & x59k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k) | (x37k & x64k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k) | (x37k & x69k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x20k & x37k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x58k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x59k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x64k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x20k & x69k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x70k & ~ x84k) | (x04k & x20k & x70k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x20k & x84k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x37k & x58k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x37k & x59k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x37k & x64k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x37k & x69k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k & ~ x84k) | (x04k & x37k & x70k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x37k & x84k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x58k & x70k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x58k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x59k & x70k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x59k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x04k & x64k & x70k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x04k & x64k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x04k & x69k & x70k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x04k & x69k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x04k & x70k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x20k & x37k & x58k & ~ x04k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x20k & x37k & x59k & ~ x04k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k & ~ x84k)  | (x20k & x37k & x64k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k & ~ x84k) | (x20k & x37k & x69k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k & ~ x84k) | (x20k & x37k & x70k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x37k & x84k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x58k & x70k & ~ x04k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x58k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x59k & x70k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x59k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x64k & x70k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x20k & x64k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x20k & x69k & x70k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x20k & x69k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x20k & x70k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x37k & x58k & x70k & ~ x04k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x37k & x58k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x37k & x59k & x70k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x84k) | (x37k & x59k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x64k & ~ x69k & ~ x70k) | (x37k & x64k & x70k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x84k) | (x37k & x64k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x69k & ~ x70k) | (x37k & x69k & x70k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x84k) | (x37k & x69k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x70k) | (x37k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x58k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x59k & ~ x64k & ~ x69k) | (x59k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x64k & ~ x69k) | (x64k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x69k) | (x69k & x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k) | (x04k & x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x37k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x04k & x70k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x04k & x84k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x20k & x37k & ~ x04k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x20k & x70k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x20k & x84k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x37k & x70k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x37k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k) | (x70k & x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k) | (x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k) | (x20k & ~ x04k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k & ~ x84k)  | (x70k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x84k) | (x84k & ~ x04k & ~ x20k & ~ x28k & ~ x37k & ~ x58k & ~ x59k & ~ x64k & ~ x69k & ~ x70k),
    x54: x49k & ~ x48k & ~ x51k & ~ x58k & ~ x59k,
    x55: (x56k & ~ x51k) | (x56k & ~ x52k) | (~ x51k & ~ x52k),
    x56: x52k & ~ x55k,
    x57: (x51k & x52k) | (x51k & x56k) | (x51k & x57k) | (x52k & x56k) | (x52k & x57k) | (x56k & x57k) | (x51k & ~ x55k) | (x52k & ~ x55k) | (x56k & ~ x55k) | (x57k & ~ x55k),
    x58: (x33k | x62k | ~ x24k) & (x33k | x62k | ~ x37k) & (x33k | x62k | ~ x51k) & (x33k | x62k | ~ x52k) & (x33k | x62k | ~ x53k) & (x33k | ~ x24k | ~ x37k) & (x33k | ~ x24k | ~ x51k) & (x33k | ~ x24k | ~ x52k) & (x33k | ~ x24k | ~ x53k) & (x33k | ~ x37k | ~ x51k) & (x33k | ~ x37k | ~ x52k) & (x33k | ~ x37k | ~ x53k) & (x33k | ~ x51k | ~ x52k) & (x33k | ~ x51k | ~ x53k) & (x33k | ~ x52k | ~ x53k) & (x62k | ~ x24k | ~ x37k) & (x62k | ~ x24k | ~ x51k) & (x62k | ~ x24k | ~ x52k) & (x62k | ~ x24k | ~ x53k) & (x62k | ~ x37k | ~ x51k) & (x62k | ~ x37k | ~ x52k) & (x62k | ~ x37k | ~ x53k) & (x62k | ~ x51k | ~ x52k) & (x62k | ~ x51k | ~ x53k) & (x62k | ~ x52k | ~ x53k) & (~ x24k | ~ x37k | ~ x51k) & (~ x24k | ~ x37k | ~ x52k) & (~ x24k | ~ x37k | ~ x53k) & (~ x24k | ~ x51k | ~ x52k) & (~ x24k | ~ x51k | ~ x53k) & (~ x24k | ~ x52k | ~ x53k) & (~ x37k | ~ x51k | ~ x52k) & (~ x37k | ~ x51k | ~ x53k) & (~ x37k | ~ x52k | ~ x53k) & (~ x51k | ~ x52k | ~ x53k),
    x59: (x33k & x43k & x62k) | (x33k & x43k & ~ x24k) | (x33k & x43k & ~ x37k) | (x33k & x43k & ~ x78k) | (x33k & x62k & ~ x24k) | (x33k & x62k & ~ x37k) | (x33k & x62k & ~ x78k) | (x43k & x62k & ~ x24k) | (x43k & x62k & ~ x37k) | (x43k & x62k & ~ x78k) | (x33k & ~ x24k & ~ x37k) | (x33k & ~ x24k & ~ x78k) | (x33k & ~ x37k & ~ x78k) | (x43k & ~ x24k & ~ x37k) | (x43k & ~ x24k & ~ x78k) | (x43k & ~ x37k & ~ x78k) | (x62k & ~ x24k & ~ x37k) | (x62k & ~ x24k & ~ x78k) | (x62k & ~ x37k & ~ x78k) | (~ x24k & ~ x37k & ~ x78k),
    x60: (x24k & x43k) | (x24k & ~ x50k) | (x24k & ~ x87k) | (x43k & ~ x50k) | (x43k & ~ x87k) | (~ x50k & ~ x87k),
    x61: x05k | x06k,
    x62: x61k & x85k,
    x63: x61k,
    x64: x62k | x85k,
    x65: x05k,
    x66: x65k,
    x67: x66k,
    x68: x06k,
    x69: c69,
    x70: x22k | x68k,
    x71: c71,
    x72: x09k | x33k | x87k | ~ x02k,
    x73: (x43k & x45k & x66k & x67k) | (x43k & x45k & x66k & ~ x24k) | (x43k & x45k & x66k & ~ x44k) | (x43k & x45k & x66k & ~ x47k) | (x43k & x45k & x67k & ~ x24k) | (x43k & x45k & x67k & ~ x44k) | (x43k & x45k & x67k & ~ x47k) | (x43k & x66k & x67k & ~ x24k) | (x43k & x66k & x67k & ~ x44k) | (x43k & x66k & x67k & ~ x47k) | (x45k & x66k & x67k & ~ x24k) | (x45k & x66k & x67k & ~ x44k) | (x45k & x66k & x67k & ~ x47k) | (x43k & x45k & ~ x24k & ~ x44k) | (x43k & x45k & ~ x24k & ~ x47k) | (x43k & x45k & ~ x44k & ~ x47k) | (x43k & x66k & ~ x24k & ~ x44k) | (x43k & x66k & ~ x24k & ~ x47k) | (x43k & x66k & ~ x44k & ~ x47k) | (x43k & x67k & ~ x24k & ~ x44k) | (x43k & x67k & ~ x24k & ~ x47k) | (x43k & x67k & ~ x44k & ~ x47k) | (x45k & x66k & ~ x24k & ~ x44k) | (x45k & x66k & ~ x24k & ~ x47k) | (x45k & x66k & ~ x44k & ~ x47k) | (x45k & x67k & ~ x24k & ~ x44k) | (x45k & x67k & ~ x24k & ~ x47k) | (x45k & x67k & ~ x44k & ~ x47k) | (x66k & x67k & ~ x24k & ~ x44k) | (x66k & x67k & ~ x24k & ~ x47k) | (x66k & x67k & ~ x44k & ~ x47k) | (x43k & ~ x24k & ~ x44k & ~ x47k) | (x45k & ~ x24k & ~ x44k & ~ x47k) | (x66k & ~ x24k & ~ x44k & ~ x47k) | (x67k & ~ x24k & ~ x44k & ~ x47k),
    x74: x73k,
    x75: x66k | x74k,
    x76: ~ x20k | ~ x31k | ~ x95k,
    x77: (x24k & x33k) | (x24k & x37k) | (x33k & x37k),
    x78: x10k & x20k & x24k & x33k & x37k & ~ x43k & ~ x62k & ~ x91k,
    x79: x33k | x37k,
    x80: x49k & x54k,
    x81: x55k & x57k,
    x82: x05k,
    x83: x20k | x37k | x59k,
    x84: x30k & ~ x82k,
    x85: ~ x37k,
    x86: x18 | x32k,
    x87: x07k,
    x88: x87k,
    x89: x87k,
    x90: x23k | x86k,
    x91: ~ x90k,
    x92: x16k & x43k,
    x93: x33k & x37k,
    x94: x93k,
    x95: x20k & x61k & ~ x28k & ~ x43k
}