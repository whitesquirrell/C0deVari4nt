// Code generated by https://github.com/gagliardetto/codebox. DO NOT EDIT.

//go:build !windows
// +build !windows

package main

import "syscall"

func TaintStepTest_SyscallStringSlicePtr_B0I0O0(sourceCQL interface{}) interface{} {
	fromString127 := sourceCQL.([]string)
	intoByte483 := syscall.StringSlicePtr(fromString127)
	return intoByte483
}

func RunAllTaints_Syscall_Non_Windows() {
	{
		source := newSource(4)
		out := TaintStepTest_SyscallStringSlicePtr_B0I0O0(source)
		sink(4, out)
	}
}
