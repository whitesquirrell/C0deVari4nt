// Code generated by https://github.com/gagliardetto/codebox. DO NOT EDIT.

package main

import (
	"bytes"
	"io"
)

func TaintStepTest_BytesFields_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte656 := sourceCQL.([]byte)
	intoByte414 := bytes.Fields(fromByte656)
	return intoByte414
}

func TaintStepTest_BytesFieldsFunc_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte518 := sourceCQL.([]byte)
	intoByte650 := bytes.FieldsFunc(fromByte518, nil)
	return intoByte650
}

func TaintStepTest_BytesJoin_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte784 := sourceCQL.([][]byte)
	intoByte957 := bytes.Join(fromByte784, nil)
	return intoByte957
}

func TaintStepTest_BytesJoin_B0I1O0(sourceCQL interface{}) interface{} {
	fromByte520 := sourceCQL.([]byte)
	intoByte443 := bytes.Join(nil, fromByte520)
	return intoByte443
}

func TaintStepTest_BytesMap_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte127 := sourceCQL.([]byte)
	intoByte483 := bytes.Map(nil, fromByte127)
	return intoByte483
}

func TaintStepTest_BytesNewBuffer_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte989 := sourceCQL.([]byte)
	intoBuffer982 := bytes.NewBuffer(fromByte989)
	return intoBuffer982
}

func TaintStepTest_BytesNewBufferString_B0I0O0(sourceCQL interface{}) interface{} {
	fromString417 := sourceCQL.(string)
	intoBuffer584 := bytes.NewBufferString(fromString417)
	return intoBuffer584
}

func TaintStepTest_BytesNewReader_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte991 := sourceCQL.([]byte)
	intoReader881 := bytes.NewReader(fromByte991)
	return intoReader881
}

func TaintStepTest_BytesRepeat_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte186 := sourceCQL.([]byte)
	intoByte284 := bytes.Repeat(fromByte186, 0)
	return intoByte284
}

func TaintStepTest_BytesReplace_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte908 := sourceCQL.([]byte)
	intoByte137 := bytes.Replace(fromByte908, nil, nil, 0)
	return intoByte137
}

func TaintStepTest_BytesReplace_B0I1O0(sourceCQL interface{}) interface{} {
	fromByte494 := sourceCQL.([]byte)
	intoByte873 := bytes.Replace(nil, nil, fromByte494, 0)
	return intoByte873
}

func TaintStepTest_BytesReplaceAll_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte599 := sourceCQL.([]byte)
	intoByte409 := bytes.ReplaceAll(fromByte599, nil, nil)
	return intoByte409
}

func TaintStepTest_BytesReplaceAll_B0I1O0(sourceCQL interface{}) interface{} {
	fromByte246 := sourceCQL.([]byte)
	intoByte898 := bytes.ReplaceAll(nil, nil, fromByte246)
	return intoByte898
}

func TaintStepTest_BytesRunes_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte598 := sourceCQL.([]byte)
	intoRune631 := bytes.Runes(fromByte598)
	return intoRune631
}

func TaintStepTest_BytesSplit_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte165 := sourceCQL.([]byte)
	intoByte150 := bytes.Split(fromByte165, nil)
	return intoByte150
}

func TaintStepTest_BytesSplitAfter_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte340 := sourceCQL.([]byte)
	intoByte471 := bytes.SplitAfter(fromByte340, nil)
	return intoByte471
}

func TaintStepTest_BytesSplitAfterN_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte290 := sourceCQL.([]byte)
	intoByte758 := bytes.SplitAfterN(fromByte290, nil, 0)
	return intoByte758
}

func TaintStepTest_BytesSplitN_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte396 := sourceCQL.([]byte)
	intoByte707 := bytes.SplitN(fromByte396, nil, 0)
	return intoByte707
}

func TaintStepTest_BytesTitle_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte912 := sourceCQL.([]byte)
	intoByte718 := bytes.Title(fromByte912)
	return intoByte718
}

func TaintStepTest_BytesToLower_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte972 := sourceCQL.([]byte)
	intoByte633 := bytes.ToLower(fromByte972)
	return intoByte633
}

func TaintStepTest_BytesToLowerSpecial_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte316 := sourceCQL.([]byte)
	intoByte145 := bytes.ToLowerSpecial(nil, fromByte316)
	return intoByte145
}

func TaintStepTest_BytesToTitle_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte817 := sourceCQL.([]byte)
	intoByte474 := bytes.ToTitle(fromByte817)
	return intoByte474
}

func TaintStepTest_BytesToTitleSpecial_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte832 := sourceCQL.([]byte)
	intoByte378 := bytes.ToTitleSpecial(nil, fromByte832)
	return intoByte378
}

func TaintStepTest_BytesToUpper_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte541 := sourceCQL.([]byte)
	intoByte139 := bytes.ToUpper(fromByte541)
	return intoByte139
}

func TaintStepTest_BytesToUpperSpecial_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte814 := sourceCQL.([]byte)
	intoByte768 := bytes.ToUpperSpecial(nil, fromByte814)
	return intoByte768
}

func TaintStepTest_BytesToValidUTF8_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte468 := sourceCQL.([]byte)
	intoByte736 := bytes.ToValidUTF8(fromByte468, nil)
	return intoByte736
}

func TaintStepTest_BytesToValidUTF8_B0I1O0(sourceCQL interface{}) interface{} {
	fromByte516 := sourceCQL.([]byte)
	intoByte246 := bytes.ToValidUTF8(nil, fromByte516)
	return intoByte246
}

func TaintStepTest_BytesTrim_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte679 := sourceCQL.([]byte)
	intoByte736 := bytes.Trim(fromByte679, "")
	return intoByte736
}

func TaintStepTest_BytesTrimFunc_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte839 := sourceCQL.([]byte)
	intoByte273 := bytes.TrimFunc(fromByte839, nil)
	return intoByte273
}

func TaintStepTest_BytesTrimLeft_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte982 := sourceCQL.([]byte)
	intoByte458 := bytes.TrimLeft(fromByte982, "")
	return intoByte458
}

func TaintStepTest_BytesTrimLeftFunc_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte506 := sourceCQL.([]byte)
	intoByte213 := bytes.TrimLeftFunc(fromByte506, nil)
	return intoByte213
}

func TaintStepTest_BytesTrimPrefix_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte468 := sourceCQL.([]byte)
	intoByte219 := bytes.TrimPrefix(fromByte468, nil)
	return intoByte219
}

func TaintStepTest_BytesTrimRight_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte265 := sourceCQL.([]byte)
	intoByte971 := bytes.TrimRight(fromByte265, "")
	return intoByte971
}

func TaintStepTest_BytesTrimRightFunc_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte320 := sourceCQL.([]byte)
	intoByte545 := bytes.TrimRightFunc(fromByte320, nil)
	return intoByte545
}

func TaintStepTest_BytesTrimSpace_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte566 := sourceCQL.([]byte)
	intoByte497 := bytes.TrimSpace(fromByte566)
	return intoByte497
}

func TaintStepTest_BytesTrimSuffix_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte274 := sourceCQL.([]byte)
	intoByte783 := bytes.TrimSuffix(fromByte274, nil)
	return intoByte783
}

func TaintStepTest_BytesBufferBytes_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer905 := sourceCQL.(bytes.Buffer)
	intoByte389 := fromBuffer905.Bytes()
	return intoByte389
}

func TaintStepTest_BytesBufferNext_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer198 := sourceCQL.(bytes.Buffer)
	intoByte477 := fromBuffer198.Next(0)
	return intoByte477
}

func TaintStepTest_BytesBufferRead_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer544 := sourceCQL.(bytes.Buffer)
	var intoByte382 []byte
	fromBuffer544.Read(intoByte382)
	return intoByte382
}

func TaintStepTest_BytesBufferReadBytes_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer715 := sourceCQL.(bytes.Buffer)
	intoByte179, _ := fromBuffer715.ReadBytes(0)
	return intoByte179
}

func TaintStepTest_BytesBufferReadFrom_B0I0O0(sourceCQL interface{}) interface{} {
	fromReader366 := sourceCQL.(io.Reader)
	var intoBuffer648 bytes.Buffer
	intoBuffer648.ReadFrom(fromReader366)
	return intoBuffer648
}

func TaintStepTest_BytesBufferReadString_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer544 := sourceCQL.(bytes.Buffer)
	intoString484, _ := fromBuffer544.ReadString(0)
	return intoString484
}

func TaintStepTest_BytesBufferString_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer824 := sourceCQL.(bytes.Buffer)
	intoString754 := fromBuffer824.String()
	return intoString754
}

func TaintStepTest_BytesBufferWrite_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte680 := sourceCQL.([]byte)
	var intoBuffer722 bytes.Buffer
	intoBuffer722.Write(fromByte680)
	return intoBuffer722
}

func TaintStepTest_BytesBufferWriteString_B0I0O0(sourceCQL interface{}) interface{} {
	fromString506 := sourceCQL.(string)
	var intoBuffer121 bytes.Buffer
	intoBuffer121.WriteString(fromString506)
	return intoBuffer121
}

func TaintStepTest_BytesBufferWriteTo_B0I0O0(sourceCQL interface{}) interface{} {
	fromBuffer293 := sourceCQL.(bytes.Buffer)
	var intoWriter151 io.Writer
	fromBuffer293.WriteTo(intoWriter151)
	return intoWriter151
}

func TaintStepTest_BytesReaderRead_B0I0O0(sourceCQL interface{}) interface{} {
	fromReader849 := sourceCQL.(bytes.Reader)
	var intoByte322 []byte
	fromReader849.Read(intoByte322)
	return intoByte322
}

func TaintStepTest_BytesReaderReadAt_B0I0O0(sourceCQL interface{}) interface{} {
	fromReader339 := sourceCQL.(bytes.Reader)
	var intoByte478 []byte
	fromReader339.ReadAt(intoByte478, 0)
	return intoByte478
}

func TaintStepTest_BytesReaderReset_B0I0O0(sourceCQL interface{}) interface{} {
	fromByte399 := sourceCQL.([]byte)
	var intoReader426 bytes.Reader
	intoReader426.Reset(fromByte399)
	return intoReader426
}

func TaintStepTest_BytesReaderWriteTo_B0I0O0(sourceCQL interface{}) interface{} {
	fromReader628 := sourceCQL.(bytes.Reader)
	var intoWriter197 io.Writer
	fromReader628.WriteTo(intoWriter197)
	return intoWriter197
}

func RunAllTaints_Bytes() {
	{
		source := newSource(0)
		out := TaintStepTest_BytesFields_B0I0O0(source)
		sink(0, out)
	}
	{
		source := newSource(1)
		out := TaintStepTest_BytesFieldsFunc_B0I0O0(source)
		sink(1, out)
	}
	{
		source := newSource(2)
		out := TaintStepTest_BytesJoin_B0I0O0(source)
		sink(2, out)
	}
	{
		source := newSource(3)
		out := TaintStepTest_BytesJoin_B0I1O0(source)
		sink(3, out)
	}
	{
		source := newSource(4)
		out := TaintStepTest_BytesMap_B0I0O0(source)
		sink(4, out)
	}
	{
		source := newSource(5)
		out := TaintStepTest_BytesNewBuffer_B0I0O0(source)
		sink(5, out)
	}
	{
		source := newSource(6)
		out := TaintStepTest_BytesNewBufferString_B0I0O0(source)
		sink(6, out)
	}
	{
		source := newSource(7)
		out := TaintStepTest_BytesNewReader_B0I0O0(source)
		sink(7, out)
	}
	{
		source := newSource(8)
		out := TaintStepTest_BytesRepeat_B0I0O0(source)
		sink(8, out)
	}
	{
		source := newSource(9)
		out := TaintStepTest_BytesReplace_B0I0O0(source)
		sink(9, out)
	}
	{
		source := newSource(10)
		out := TaintStepTest_BytesReplace_B0I1O0(source)
		sink(10, out)
	}
	{
		source := newSource(11)
		out := TaintStepTest_BytesReplaceAll_B0I0O0(source)
		sink(11, out)
	}
	{
		source := newSource(12)
		out := TaintStepTest_BytesReplaceAll_B0I1O0(source)
		sink(12, out)
	}
	{
		source := newSource(13)
		out := TaintStepTest_BytesRunes_B0I0O0(source)
		sink(13, out)
	}
	{
		source := newSource(14)
		out := TaintStepTest_BytesSplit_B0I0O0(source)
		sink(14, out)
	}
	{
		source := newSource(15)
		out := TaintStepTest_BytesSplitAfter_B0I0O0(source)
		sink(15, out)
	}
	{
		source := newSource(16)
		out := TaintStepTest_BytesSplitAfterN_B0I0O0(source)
		sink(16, out)
	}
	{
		source := newSource(17)
		out := TaintStepTest_BytesSplitN_B0I0O0(source)
		sink(17, out)
	}
	{
		source := newSource(18)
		out := TaintStepTest_BytesTitle_B0I0O0(source)
		sink(18, out)
	}
	{
		source := newSource(19)
		out := TaintStepTest_BytesToLower_B0I0O0(source)
		sink(19, out)
	}
	{
		source := newSource(20)
		out := TaintStepTest_BytesToLowerSpecial_B0I0O0(source)
		sink(20, out)
	}
	{
		source := newSource(21)
		out := TaintStepTest_BytesToTitle_B0I0O0(source)
		sink(21, out)
	}
	{
		source := newSource(22)
		out := TaintStepTest_BytesToTitleSpecial_B0I0O0(source)
		sink(22, out)
	}
	{
		source := newSource(23)
		out := TaintStepTest_BytesToUpper_B0I0O0(source)
		sink(23, out)
	}
	{
		source := newSource(24)
		out := TaintStepTest_BytesToUpperSpecial_B0I0O0(source)
		sink(24, out)
	}
	{
		source := newSource(25)
		out := TaintStepTest_BytesToValidUTF8_B0I0O0(source)
		sink(25, out)
	}
	{
		source := newSource(26)
		out := TaintStepTest_BytesToValidUTF8_B0I1O0(source)
		sink(26, out)
	}
	{
		source := newSource(27)
		out := TaintStepTest_BytesTrim_B0I0O0(source)
		sink(27, out)
	}
	{
		source := newSource(28)
		out := TaintStepTest_BytesTrimFunc_B0I0O0(source)
		sink(28, out)
	}
	{
		source := newSource(29)
		out := TaintStepTest_BytesTrimLeft_B0I0O0(source)
		sink(29, out)
	}
	{
		source := newSource(30)
		out := TaintStepTest_BytesTrimLeftFunc_B0I0O0(source)
		sink(30, out)
	}
	{
		source := newSource(31)
		out := TaintStepTest_BytesTrimPrefix_B0I0O0(source)
		sink(31, out)
	}
	{
		source := newSource(32)
		out := TaintStepTest_BytesTrimRight_B0I0O0(source)
		sink(32, out)
	}
	{
		source := newSource(33)
		out := TaintStepTest_BytesTrimRightFunc_B0I0O0(source)
		sink(33, out)
	}
	{
		source := newSource(34)
		out := TaintStepTest_BytesTrimSpace_B0I0O0(source)
		sink(34, out)
	}
	{
		source := newSource(35)
		out := TaintStepTest_BytesTrimSuffix_B0I0O0(source)
		sink(35, out)
	}
	{
		source := newSource(36)
		out := TaintStepTest_BytesBufferBytes_B0I0O0(source)
		sink(36, out)
	}
	{
		source := newSource(37)
		out := TaintStepTest_BytesBufferNext_B0I0O0(source)
		sink(37, out)
	}
	{
		source := newSource(38)
		out := TaintStepTest_BytesBufferRead_B0I0O0(source)
		sink(38, out)
	}
	{
		source := newSource(39)
		out := TaintStepTest_BytesBufferReadBytes_B0I0O0(source)
		sink(39, out)
	}
	{
		source := newSource(40)
		out := TaintStepTest_BytesBufferReadFrom_B0I0O0(source)
		sink(40, out)
	}
	{
		source := newSource(41)
		out := TaintStepTest_BytesBufferReadString_B0I0O0(source)
		sink(41, out)
	}
	{
		source := newSource(42)
		out := TaintStepTest_BytesBufferString_B0I0O0(source)
		sink(42, out)
	}
	{
		source := newSource(43)
		out := TaintStepTest_BytesBufferWrite_B0I0O0(source)
		sink(43, out)
	}
	{
		source := newSource(44)
		out := TaintStepTest_BytesBufferWriteString_B0I0O0(source)
		sink(44, out)
	}
	{
		source := newSource(45)
		out := TaintStepTest_BytesBufferWriteTo_B0I0O0(source)
		sink(45, out)
	}
	{
		source := newSource(46)
		out := TaintStepTest_BytesReaderRead_B0I0O0(source)
		sink(46, out)
	}
	{
		source := newSource(47)
		out := TaintStepTest_BytesReaderReadAt_B0I0O0(source)
		sink(47, out)
	}
	{
		source := newSource(48)
		out := TaintStepTest_BytesReaderReset_B0I0O0(source)
		sink(48, out)
	}
	{
		source := newSource(49)
		out := TaintStepTest_BytesReaderWriteTo_B0I0O0(source)
		sink(49, out)
	}
}
