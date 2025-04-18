#! /bin/env python

import toolspath
from testing import Xv6Build, Xv6Test

class test1(Xv6Test):
   name = "test_1"
   description = "Tests to make sure everything compiles"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test2(Xv6Test):
   name = "test_2"
   description = "Tests to make sure default number of tickets is 1"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test3(Xv6Test):
   name = "test_3"
   description = "Tests to make sure setting number of tickets doesn't fail for small ticket numbers"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test4(Xv6Test):
   name = "test_4"
   description = "Tests to make sure setting number of tickets doesn't fail for large ticket numbers"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test5(Xv6Test):
   name = "test_5"
   description = "Tests to make sure setting number of tickets fails for 0"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1


class test6(Xv6Test):
   name = "test_6"
   description = "Tests to make sure setting number of tickets fails for negative numbers"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test7(Xv6Test):
   name = "test_7"
   description = "Test to make sure getpinfo fails for pid 0"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test8(Xv6Test):
   name = "test_8"
   description = "Test to make sure getpinfo fails for large pids"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test9(Xv6Test):
   name = "test_9"
   description = "Test to check that parent and child pids equal"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test10(Xv6Test):
   name = "test_10"
   description = "Test to make sure the right number of processes are schedualed with fork"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test11(Xv6Test):
   name = "test_11"
   description = "Test to make sure schedular selects right processes"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test12(Xv6Test):
   name = "test_12"
   description = "Test to make sure schedular selects right processes during multiple forks"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test13(Xv6Test):
   name = "test_13"
   description = "Test to make sure schedular's internals are properly updating"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test14(Xv6Test):
   name = "test_14"
   description = "Check to make sure default tickets are properly set"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test15(Xv6Test):
   name = "test_15"
   description = "Test to make sure strides are properly set"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

class test16(Xv6Test):
   name = "test_16"
   description = "Test to make sure processes with different numbers of tickets are scheduled properly"
   tester = "ctests/" + name + ".c"
   make_qemu_args = "CPUS=1"
   point_value = 1

import toolspath
from testing.runtests import main
main(Xv6Build, all_tests=[test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13,test14,test15,test16])
