// Code generated by https://github.com/gagliardetto/codebox. DO NOT EDIT.

package main

import (
	"io"
	"net/mail"
)

func TaintStepTest_NetMailParseAddress_B0I0O0(sourceCQL interface{}) interface{} {
	fromString656 := sourceCQL.(string)
	intoAddress414, _ := mail.ParseAddress(fromString656)
	return intoAddress414
}

func TaintStepTest_NetMailParseAddressList_B0I0O0(sourceCQL interface{}) interface{} {
	fromString518 := sourceCQL.(string)
	intoAddress650, _ := mail.ParseAddressList(fromString518)
	return intoAddress650
}

func TaintStepTest_NetMailReadMessage_B0I0O0(sourceCQL interface{}) interface{} {
	fromReader784 := sourceCQL.(io.Reader)
	intoMessage957, _ := mail.ReadMessage(fromReader784)
	return intoMessage957
}

func TaintStepTest_NetMailAddressParserParse_B0I0O0(sourceCQL interface{}) interface{} {
	fromString520 := sourceCQL.(string)
	var mediumObjCQL mail.AddressParser
	intoAddress443, _ := mediumObjCQL.Parse(fromString520)
	return intoAddress443
}

func TaintStepTest_NetMailAddressParserParseList_B0I0O0(sourceCQL interface{}) interface{} {
	fromString127 := sourceCQL.(string)
	var mediumObjCQL mail.AddressParser
	intoAddress483, _ := mediumObjCQL.ParseList(fromString127)
	return intoAddress483
}

func TaintStepTest_NetMailHeaderGet_B0I0O0(sourceCQL interface{}) interface{} {
	fromHeader989 := sourceCQL.(mail.Header)
	intoString982 := fromHeader989.Get("")
	return intoString982
}

func RunAllTaints_NetMail() {
	{
		source := newSource(0)
		out := TaintStepTest_NetMailParseAddress_B0I0O0(source)
		sink(0, out)
	}
	{
		source := newSource(1)
		out := TaintStepTest_NetMailParseAddressList_B0I0O0(source)
		sink(1, out)
	}
	{
		source := newSource(2)
		out := TaintStepTest_NetMailReadMessage_B0I0O0(source)
		sink(2, out)
	}
	{
		source := newSource(3)
		out := TaintStepTest_NetMailAddressParserParse_B0I0O0(source)
		sink(3, out)
	}
	{
		source := newSource(4)
		out := TaintStepTest_NetMailAddressParserParseList_B0I0O0(source)
		sink(4, out)
	}
	{
		source := newSource(5)
		out := TaintStepTest_NetMailHeaderGet_B0I0O0(source)
		sink(5, out)
	}
}
