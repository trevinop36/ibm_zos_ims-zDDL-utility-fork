class DBDInputParameters():
    DESTINATION = "IMSTESTL.ANS.DBDLIB"
    SOURCE = "IMSTESTL.ANSIBLE.DBD.SRC"
    SEQ_SOURCE = "IMSTESTL.ANS.SEQ"
    EMPTY_SEQ_SOURCE = "IMSTESTL.ANS.SEQEMP"
    FB_DESTINATION = "IMSTESTL.ANS.RECFOR"
    SYSLIB = ["IMSBLD.I15RTSMM.SDFSMAC", "SYS1.MACLIB"]
    REMOTE_DBDGEN02_SOURCE = "/tmp/dbdgen02.dbd"
    REMOTE_DBDGEN04_SOURCE = "/tmp/dbdgen04"
    LOCAL_EMPTY_SOURCE = "functional/modules/ims_dbd_gen/uss_file/data/dbdgenEmptyInput"
    DESTINATION_RF = "IMSTESTL.ANS.RECFOR"
    INVALID_SOURCE = "IMSTESTL.ANS.INVALID"
    INVALID_USS_SOURCE = "/tmp/invalid"
    INVALID_SEQ_SOURCE = "IMSTESTL.SEQ.INVALID"
    INVALID_DESTINATION = "IMSTESTL.DBDLIB.INVALID"
    INVALID_SYSLIB = ["IMSBLD.I15RTSMM.SDFSMAC", "SYS1.INVALID"]
    
class PSBInputParameters():
    DESTINATION = "IMSTESTL.ANS.PSBLIB"
    SOURCE = "IMSTESTL.ANSIBLE.PSB.SRC"
    SYSLIB = ["IMSBLD.I15RTSMM.SDFSMAC", "SYS1.MACLIB"]
    DESTINATION_RF = "IMSTESTL.ANS.RECFOR"
    INVALID_SOURCE = "IMSTESTL.ANS.INVALID"
    INVALID_USS_SOURCE = "/tmp/invalid"
    INVALID_SEQ_SOURCE = "IMSTESTL.SEQ.INVALID"
    INVALID_DESTINATION = "IMSTESTL.PSBLIB.INVALID"
    INVALID_SYSLIB = ["IMSBLD.I15RTSMM.SDFSMAC", "SYS1.INVALID"]
    FB_DESTINATION = "IMSTESTL.ANS.RECFOR"
    EMPTY_SEQ_SOURCE = "IMSTESTL.ANS.SEQEMP"
    SEQ_SOURCE = "IMSTESTL.ANS.PSB.SEQ"
    REMOTE_PSBGEN01_SOURCE = "/tmp/psbgen01"
    REMOTE_PSBGEN04_SOURCE = "/tmp/psbgen04"
    LOCAL_EMPTY_SOURCE = "functional/modules/ims_psb_gen/uss_file/data/psbgenEmptyInput"


class ACBInputParameters():
    JOB_CARD = """//ANSIBLE JOB 'testing',
//  CLASS=A,MSGLEVEL=(1,1),REGION=0M,
//  MSGCLASS=H,NOTIFY=&SYSUID"""

    COMMAND_INPUT_BUILD = "BUILD"
    COMMAND_INPUT_DELETE = "DELETE"
    PSBLIB = ["IMSTESTL.ANS.PSBLIB"]
    DBDLIB = ["IMSTESTL.ANS.DBDLIB"]
    ACBLIB = "IMSTESTL.ANS.ACBLIB"
    STEPLIB = ["IMSTESTL.IMS1.SDFSRESL"]
    RESLIB = ["IMSTESTL.IMS1.SDFSRESL"]
    PSB_NAME_ALL = "ALL"
    PSB_NAME = ["PSBGENL"]
    PSB_NAMES = ["PSBGENL", "PSBGENL", "PSBGENL", "PSBGENL", "PSBGENL", "PSBGENL", "PSBGENL"]
    DBD_NAME = ["DBFSAMD3"]
    DBD_NAMES = ["DH41SK01", "HOSPVARD", "DBFSAMD1", "DBFSAMD2", "DBFSAMD3", "DSVNTZ30", "DX41SK01", "DX41SK03", "DX41SK05", "DX41SK06", "DX41SK07", "DX41SK08", "DX41SK09"]
    DBD_NAMES_LIST = ["DH41SK01", "HOSPVARD", "DBFSAMD1", "DBFSAMD2", "DBFSAMD3", "DSVNTZ30"]
    COMP_PRE = "PRECOMP"
    COMP_POST = "POSTCOMP"
    COMP = "PRECOMP,POSTCOMP"   
    INVALID_PSBLIB = ["INVALID.PSBLIB"]
    INVALID_DBDLIB = ["INVALID.DBDLIB"]
    INVALID_ACBLIB = "INVALID.ACBLIB"
    INVALID_STEPLIB = ["INVALID.SDFSRESL"]
    INVALID_RESLIB = ["INVALID.SDFSRESL"]
    INVALID_PSB = "ALL789FG*@"
    INVALID_PSBS = ["PSB1%^*#((", "PSBGENL"]
    INVALID_DBD = ["DBD1$%HJ"]
    INVALID_DBDS = ["DBFSAMD3", "DBD1$%HJ"]
    INVALID_COMP = "INVALID"
    INVALID_RECFOR = "IMSTESTL.ANS.RECFOR" #invalid acblib with record format FB
    INVALID_PDSE = "IMSTESTL.ANS.PDSE"
    EMPTY_PSBLIB = "IMSTESTL.ANS.EMPTY.PSBLIB"
    EMPTY_DBDLIB = "IMSTESTL.ANS.EMPTY.DBDLIB"