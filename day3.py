#Day 3

#Part 1:
# For example, suppose you have the following list of contents from six rucksacks:
#
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGL rsFMfFZSrLrFZsSL
# PmmdzqPrV vPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
#
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

# s= "vJrwpWtwJgWrhcsFMMfFFhFp"
# s1 = "vJrwpWtwJgWr"
# print(len(s))
# print(len(s1))

# Analysis:
# Input: a list of string
# Output: 1. get common string  of each half part of string
#         2. map to get their priorty
#         3. sum the priority the score for all string
#

def get_priority_map():

    # Generate lowercase Mapping
    lowercase_map = {chr(i+96):i for i in range(1,27)}
    # print(lowercase_map)

    # Generate UPPERCASE Mapping
    uppercase_map = {chr(i+64):i+26 for i in range(1,27)}
    # print(uppercase_map)

    return {**lowercase_map, **uppercase_map}


def sum_priorities_part1(rucksacks):
    if not rucksacks:
        return 0
    rucksacks = rucksacks.split('\n')
    #well, I could use list here instead
    char_map = {}
    priorities_map = get_priority_map()

    for rucksack in rucksacks:
        idx = int(len(rucksack)/2)
        common_char = ""

        #dedup 1st compartment before finding the common letter
        for char in list(set(rucksack[:idx])):
            if char in rucksack[idx:]:
                common_char += char
        char_map[rucksack] = common_char

    # print(f"char_map: {char_map} ")
    sum_priorities = sum([priorities_map[char] for char in char_map.values() if char in priorities_map.keys()]) if char_map else 0

    print(sum_priorities)
    return sum_priorities


def sum_priorities_part2(rucksacks):
    if not rucksacks:
        return 0
    rucksacks = rucksacks.split('\n')
    # print(rucksacks)
    char_map = {}

    i = 0
    while i <= (len(rucksacks) - 3):
        # print(i)
        common_char = ""
        #dedup 1st compartment before finding the common letter
        for char in list(set(rucksacks[i])):
            if (char in rucksacks[i+1]) & (char in rucksacks[i+2]):
                common_char += char if char not in common_char else ""
        char_map[i] = common_char
        i += 3

    # print(f"char_map: {char_map} ")
    priorities_map = get_priority_map()
    sum_priorities = sum([priorities_map[char] for char in char_map.values() if char in priorities_map.keys()]) if char_map else 0

    print(sum_priorities)
    return sum_priorities

rucksacks1="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
sum_priorities_part1(rucksacks1)
sum_priorities_part2(rucksacks1)




rucksacks2 ="""dtddvvhwttHJhwdhJPddhwJGppmGjgpQgTjQplQpTljwpg
BfzSzRSVVMVNRMDDNBSNSnfBmbrglGQbmNpQggFjpgpbQlQb
ZSBffLnVZdCCPJjhhL
RGCZpWWWFlHQQbgvFssg
jLnMzjnrnjjNjhrjdwbHscsVVgDVQPvPwh
nfJnLMLzjJMtnjNnnBbZtBWBqqbTTTBRpT
nddlhBtqTBqTVSlBtmCmVcRVmZggfWbcZc
jDjvPrPSNPwrDNRWbbgWCjRRCcWm
DzDwSpFrvrvFPQLzQnsqztBthTJnGJqlsJ
gssGmzwgRgsNmTsqgDnDJnbDHHhhzFdDDh
WQVFjMWrVQrVvVVjVctSSLSMZhnJZPBnbdnhbnHZZBDJBh
VCtcccVQLrfvrSlGmfTfNgfmlFgm
DsmfsBbNNZhDWsbmWmNbbPDHLFjcctjjGcnZGzncnctcGH
SwVQJrjVwpgSVRpjpVRrlTMCFFCLCFFcHzzGMcHrtHHH
ppVwTwSwpwvSlSlJTjVVbPhsvvBssWsNfsqWPvWs
BJwqwJtqqDDDrGDnPFzPFfpphD
TgZscCHQLSHgZcfMzpjFFjzsshfj
LcNlTVQCCVLLZTLNvpRtpvBBvRJmNB
bDBGQBBCTTNPGPPwPzcHfVHrDtLWLVrWVjjHWr
gpssqqsqlMFfLZQWftjVpr
lvqqFMRlFcQvbzCNCG
fhhMDdPhWMJMWvhhSfwRSGlzFbSFNlzw
LcqTCqcgZqjTggVjcwbFRwbDBTzbRGRwTS
cHLpZgnCHpQsDdsmQp
jwStJjJhtgJStpgwJMggQWqQTNTfNTWfbNNMCCNG
zRZnFPRZPVncPGVFRlRmGHCTqfCCPCHHfLfbTQCbTq
lnVmFZRZDnRVBFZcrZlhjpggvppthGhphpwprS
lcttSptHHllQbMcsrltSQGpvNBzpgWBBBDDGWzvgLz
PdjPVRFhFqFjRRCjzvRWnWLBLgbBBLzg
hhCCFbPTmjPdhZjhPhZCmTjjMsrJSfHrcmHJrHHmlcJSsmft
WhWnLZSSnSzQQhfLLNSfmDHrCFDDHtpjGGtTGQCG
gJbJBcMVwJlRRdbwvwJBVtjdtHHTmptpHTCtTFrFCp
JwwgvRMJlvJwgqgvqRMcnWWhLPzzsqfnZWnfWWnj
zdwTSvzHMvVSzDCtZhtGmbTGhm
lcBHfFjjgtsmDCgshD
cJPBnqNFnLfHJFPqljclqJzQvSSVWvSnMwvSzSWWdMWM
pNJMcZrsZDLDcbcccMpQffHqvgdwdFFmdmqwvqmgmzsw
hhnWjTTStRCGSMgvvgvdqvdFjvVz
hCTSWhPGttTCGBWMRlTCMSnPBDJpbDfDpNpbbNJfJDJbpJpN
lbcQcSNFchhQNqHLLqhLqrMpqM
WfsnsszPWfBBVpHdprrpdnGL
WTzWfwjtTBzwwBDzmfSSQmmbFZcpQNcbZZbv
PwSJSlmtPPgwgmHhPPvRvGHLRLQRBQGCQVGb
rnsFDnnfGGRWQRnW
dfTTfTFdfrfFFFzQFPJPSSlhqtllNPzgwS
MMbTFZrcrGZMDqNStWScDtzS
dvWmhQggQvCnfnqPqDnDjnfP
lgvdvLClWCQlgdhlrMBBHpGlwbHHGH
CQHgQpPdCQpsCpzRwSVRSzRZwZ
JbNBbcbrJvbJnqVznwwTzrzz
wNbfLvvfDNNBHPFLhddFsQss
VVzqvwzpqvzqNVVHGNqjHpNfSQDWdWwJdPWrWccdQrWrrDdd
nLcbtBRtBhcnWSJQlJSgll
tFbLLLRRhMtsBMtRCRsLCMBVjjvHTNjHHjzcvFFppGHzTT
QCPrPWNPlWjGGZqGmvdPGd
JgpHpSfphhfpVmBSgnTvdtddGvZVdvddDv
LhphBfHpSwSwfHcMgfpmBWWWbsNCjFWsljNbbjlLjb
QJmQbRmdfmdSQRQZSJltTltNvTrtDtrlftDD
wpZcHVwwMgBpWMVgWpHLphztDvvGvDPlnGvDLlNrDPnNPl
McgWFWHHHzVpMgZQFqbjsdjqqRCq
JPhLFfMJDLQnjNCvWWpdjjdM
crSwnwVnwSRBcNBNjjWCdC
GlbTGbsSzrtbmbfhnJQP
fDLSWVDRHHfVWHgPcZlDlZbbQhBcZQbb
jrmFmprTpFztmddjdjrpvBQlQZGhQbTsQbGcQbcbQs
nvqdpmjFnwpLSWlfnVNnWl
nZBRbBJzznNNCnJZwnBSCJMcpcTpcwhcqhmsmWMwFWLL
jQfvjgtfvPlHHqWpvWThpWqWch
VljjjgjQjrTDlDgrHtVCbnJZzNzNbnRNNJZrJR
MQtJnttlMLlJQsNhQrVVrFVWRRbbVFdJDD
vGjvzmjzgHqSjjSzmSGHTWbfDFWrbFzFfdDVrfRWDb
qPRqvTSPggqGgHCmllnCNLtnhcnnsnnw
zrlZsQMFrsgQFMMjMCbjVDCTCW
NqHNRdBppcJJcTpdmRfHThpdDWDtvbWVtbLjWbttWqqCCbLt
mhJpJHTJmBhcJhwhgwzsQwSSlzQQzGlZ
TvsszlvnzRRVTqzVrqrjjZGPfQPFqPqG
mcNhDNchppWmWSNhdSmSCQNjPFjrfGjrgPFCrgFPgPgrLf
SDddWpdMWSwNDmMNwlJRQwJlsVRRvzlsHt
DTtggjsFFFTlPJhvctBqBqSRmSMBSRnmnRcm
fGfwZdrbHVLdbGdHHwwQGVwBBCMMfvCNRNSMMMSRBmmRCN
dGZzGHGVVbvHvHwbzpGbHLrwFDDFTtsglhFspgJshslTDJjT
CbzspssWwCPcvvplrfqfDCJrDqdllB
LjttnjNTNGgQQJdBrffTwB
nVtLSgggjFwtMczhvzpZbSZW
HCzCHHvWthWFHhssWCVmnqZrnqVrmrmgnbrqmN
wPPGBjQQGwGbSlSLwgnpnrBZnBBmnMNnMN
jTTbJlJjPPLPGHHTthhhHcFWTT
qRdvvPDrCpzPHzcdrrcRqtbJJgjhgtWjJgbWJtgCFb
GTwGwNscLllGTZmGSTZGlSBMnhggjbgtgbtbsgWFFMhbMF
ZSQBSmlmzcrdQRqz
cSpTRphwwghRfgSScqPpnDqDCjDjJJJJDvDLCvvn
BVmmQFQBQVNBVmsWlbQFGBBlCHTJznzHLHvvCnjjNLHJDLHD
MFsZZMbBGblbQTmQsFsQMMfPcPcwSpwtStgPphZtctPc
QZbbZBdjPBjbQQbZnSSltlfwWvlvwNtNjwFMMN
DLVqTJqpSVtfsptwfWpv
rcRRVVTSbPQBPrBZ
tjSgSjLFSnVjDWRsQj
lcdqhfFpqZGpZqznrVRWPrnWRVBsVG
FHddNNNHwTHMHvvS
qCSDSQlwBHNbgJrHnLJH
GRpRpRfnmRWWVWgVrF
jhdZjpnvGfTZZQPlCtqQQSsS
FMZSGWWBrZjMBZMrBWMGjjZDnCRqpgPnbRwPbFnvvqFnDR
QHcpfVVslfdVlQclcctqRgqgbsCwbCwPCCCPwD
NLHfLhclmmhdfNNpfQMBmZWBrJMmZWBzMrjj
pBMpRgBMQwzRthmzLC
HPcJvrvDbjvrFDcvWrHfHfWHmdddtdTLztmtdtfllmNdNhNz
DvPFDvnPJLngQsggMGGQ
BbcFHvbhhDbbTSvZmwwgJPPlDlZldd
prCrNLMNgWWJBdrJ
fQMLCfLLtpqsNNMnnfBhcBSVGbhhhcqVbcjc
ZchcZZjmmNpgmJtgmM
RLrHllWrQZQGlBpbGFGFFM
RQnLHrqPLnZHzqjfVPcvVTfCvPTC
fMtwjfMwrbjfGrtrpPGrwpNNVNVqcbdVqHZTFNbcHSNL
mgzvDnJmnJhFJHSTNqZLHncHLS
vRzhzslJFhRffPPQMjGtGl
VMMNjWppQVwzNWrZdrrtMCMZCtMT
ngDScLcvPPgDPDGhGDPGSHVbHTHmZtTSrBHZbZBmBb
LhlglLghnVlplswJjs
bGJQZZTQQLJJbQZlTZLjCGQTsDhWFhmshhvjWVFVVrgtDsst
NScqwHcwwnnzBwqPqqsmVNhgsDDVtsghrFFg
pcrcwnpcffrcBzfbCRLpRLMMRlRLQl
hzCzCzpRgCzzzCctNsNWNqsZqZhPqNPb
TdBwmdrrrDmvwTvqNsSRssPlsWsq
FDBRRHDMTmBfmrmngnpjGgVptMgLCp
ZPLLnSPMFGvFZMSvHhDhqHfqvfqbDW
GgcppCgBcrQBBgplrVddhDqqqfdHgWdfqb
CcCjQszmGBQjrcCwCmCccPwPTPnMPTnMJSMMRZSPJL
LcVVcqqSHRLzRnCfNnGzNW
LZPPdljlCggMjgNM
PTvwlPtwtlJvZTQvbcHppFLHVVTcFssF
fpWzvzNgWJBVfBJzWzBVJNzWbZcbHhlbthjlrrPrjZZPHZhJ
hRDmGCFDwQnStncrjnccHcMP
GmmsGRmFTsFwSCsRQDsCSqqpfvfgzddWggvqdpfBWzVh
wjRBFljJGDFwwlGGpBSjGDtwTVtTgHHHsHHsVTVzsHqq
CPLNPdbWvbMWbcmvPNdLVqtsHqgCqHChZhhsVsHt
PWcPfPvmvNQbbWdWpJjJBDptGnDFjftn
mFFmJpDMmmnJFjWDVclsSpcflSsQwSsc
HrjNNjHNfVwLNSSl
tdZbhjHZHPbdCTvbbhhrGbbHMFmRMvnRRFmmvJMDmgJDJMnq
szJZhshbsfZJjbttchPctdTnWnRWVWMMnBdLRpMnBz
SrNwvDSwrCmnVRvjpWLBBn
ggGmgNFrgSDwmNgrCmtPsZPsjQGsqPcsqqJP
gjSWSjJSWrWzppzW
MCMzHNGNqHfscsFtrtwscVcr
qGHNGNHLCnLmTCHfMMmNTzzldzgJlJZZgJljgTdD
QGTQtQzTmdTsGTLcdFTGzdtBBjtwvBBJDvDMHJgjJvww
lPlqsZWnDJjZvZgV
ShCfCRnWGFsRRRrF
lwGtndCrrmGCwdmhzQrBzrHvLVggPgHv
fjMjDZJqSDJfJqDNDjJffjZLHPHHFvVFzHBLgLFpFpBSgL
MsTZWRNZfJZZqMGVGhhlhhccRnhC
MMvncqvcHcSnsdzzgvdfQjpljpQVTdDQDRTRlVpQ
wLCrNtBFFHHThRlH
bPJtHmCWssqgGPvq
LvTLsmDWvTWqTsmqjRTmjwgdwgnMHMMFgdtHmBmFVn
rlSCJzCSfpGGlhznQdnwFhtHgBFwtV
SGZJJSSrVfCbGJLjPsWbvjRsPTqR
pNqVVDCMVMBpqJVdMNHrccGHrtNtTFFFrQ
hwmllWbvvbnPvbSvtrFhhJzzHztcTztT
WSnbnPbbbvlWlRvnsqqMgLRMjLgVLCJdRV
GphVTGVMtQwtJmtCJP
FRRsBBsFqRNZNNrgqBdRfCZvbmPgmQzJQPnmJbJmQPJPPmwj
RNqsFrRfZZsZWvNqWRFvrBZvWhhCGVplhlWTlTpSCLpMhWMD
RZRjgbZHjjhsSnRsZstDRStsTVpFhBqFphMqPPpTFQVMPFTM
zrcGJwNNdwJrfNdJWvGdJzdTlTFlqTVPFTVFPPBpqNTbBP
WwLdLGfrRLStCZbD
mrmTqJWTvDDppTDb
DGzBfCzNDzdMwnLlbn
FVZPFZFFZPgjmWZsDtsq
TpnFTnFRCgRgldMRnDnRcrcdbdPBHbtPqbVcccrH
WNWLfQQmfhhSNwmrcbSVqPtbZDZcPb
LQhwLQvQvNfJhJRDMGFRlCMDMD
vLFTDmjVvLgnNHPphN
lMClGCmsRdCnPzCccngCpz
dlGZwRsRrRwswGsdSbbZSbVDrVBmDWWWFJrTrFvFTmqV
SGsZRqGLWLLtZRHRRcLHGTlJjzgJpjzTpNTNJNWpTm
MPMPvFFvFBrPPDPMQMPChjgpNpSNTmmmpNlTDljlTz
vnhrvMvnhSRqqLqnfn
mGFrlBmFQNQFljhqqqqbmHMsTPRbWWCsLMWRsb
wnwtvpwVzDVpvzzwZppnctMLtMPWWCstTsWTsTLffRRW
vwDJgZnvZJFqgLBFGqgl
QdGltnWNWqTdqQWvWsMJcrTcFcrgshJRMs
BzPLCDPzzzzCCLLfCBzfSDmLMrDJMglrcRbbhRsFhMrRJcsM
fjSzwwHfSzPzfCVBHlpdjGnZqnZptqQWjGvG
VbJZbgVzvzmhQpQWpQzhDp
tHPPcGcFBlCctCGtGcBBNlDLMGfMLwWfwwqMLLJwQWwp
dCHTPTPJdTBFPdrZjgsjrjnmdgms
JJpBvJQBZVvcFqqnsWdWvjsn
DCfbDbTtbgfCSHqqNdFMPhPDFnPPDWsPjM
bTmzTNCTNmfqTgJQcpLrpZLzVlVL
dtTLntTjzTftnmwnqGGQHNmm
SWbShCPMBgBRRFSFtRZZmm
DlJPCJCgPWhttzpvdjcpVl
WdzsNvWMzNsMHWddWCVffqmSmScLPvLPgLgLPplrrPmL
BtnzbnBhbwttwtZlmmlgcwSrLgmmpm
bFhQtbGBTnjBBbjTtFBbVDzddDDfjdDDqNWVjWHj
ppmtpgLLZLCbMQvQQThdtrvPhV
BBlHBwHRjHqBzzbHHqjjQdDQTDhPQDvnQlrQDQvr
HGjFzwHNczbzRFcGzHGFSJSpspsmpssMLLSZCppmfs
MpGrMMMcTsHMVHcvbwwmmcRSmDmDmv
zCNptqCBQQLCNLCzbfvSvbSzSDRDSmSv
CNNqNgNQJNgQtCqLlllZdZhTrThsnHpVVssPTsGP
jhSGcShDrLcLLFcw
MVzQvQNZVLHvHPdhLW
qzhhQlVbgqjmSjJDsgmR
CFzSPCgcsVVzFgzSCsBJwjdwJtNllnwglJlp
QrvbqWvvLbmvDMMmbdwFWpNNwwwwptjJWn
RZRZZqvvvDbDHCRTGchHFSGG
SszgPSPPVltDlqtz
WfTdTBdQdFnWBBBhBhNjVJtpNsVlDDDHHJWp
hQhrLFsBwdQPggbRgPwRMg
frRppMMDMpDnJfprnZhrrhpzWgvvGCvvFzWFvzvVVWFGJB
TcmLwTsccqwqbPwsdwqdTPSvBvzzztvggVvQCGWQCLBvCv
sswNjscwmqjwSssjdZNMfHHlHhfrnrgnfR
JpBJBdmdzZzzpngmbCnlqnNbNM
MMTHGccLTLvwRMlRnnQnbblnRnSs
vVGtvMcjLVGHfHDrPPWZppBpJpfZZZ
FGJtlttPdPtGFldlPRGpJTVzSBSSggHgJjVmBMHjJm
rhbvqrQLrWqrWLLfqbjjgNmVNSgzTmNgNS
hsffZQqnqCfZzlPPGlRlcwDs
HDDdZpcFwHFRFcZqDctpRDHpwTCVwjrBTQTBLBLBJJBjjQTJ
ldlMzhlPshPbLrrVrQQCMQjB
glzNfWlvbHqSdNNNcF
jZCMtnZZHCZwBWMwCwtMmfPFfvHDvzHFLPmFDfvh
RcrQdRRdGTzGvDGmfgjh
TsQscdQsQNTNqQQpRrRVCCBMMJJWMMVNVjnNJM
zVPWhVzLzWBWHZnlqBllqlpRbGNdffscGNdbDRnNSfcG
MtvSFQQwMcpsGRNGFR
vvTwJJSgmCSMmjVPPJWWhzllWLVV
RjdfnJfmbVvVJVFQcs
rZDZGBBZVvLZLHFW
qPzTDPlVrjNgfCdmPd
bcjmQPrnbmVmsLVrLrjmcHGRWlZHHRwHpZRHWWwH
nFhqzFqJzDJfvfSFqFfGHWZZHGRJRWHZWdpWwZ
hBCtDSSFCTqCCFzSnzMrLNmrMNPTNMQPMmNL
qvNBSJVDJGGVSJbVDDVhDbbqPjpWpWzWrnpWvvWPMjnWnpWz
mlTltwcwMWTPfNTN
CtCwFmCgmcmlRFmFCtRCHgmDJsbBhVqsbBHVDbNHDHJqqb
csBFBsLrBGBWcgLcBvRgpRhbwRwlbQwbwQgD
DCqmDmtTRtRlhdlh
qnCmTNPmmCnSSzmzNzGLzLccGDBzGrBLvvcW
FjfBjHnHzPFwhvFFqh
bjRpGsNsPqQvPclb
NWGGWGrrZVZjsCLmDMMgzgrSnzSm
MDgmmsNCmZMWmHCZLrvnLBBjPLVlPVbW
zcJGQwJdFRnrBVzqzvPr
hTQwhJwcfTFddFdGSfcRQQGFsggsgsHHnSmgsgsmgCnHNZpC
BPfwzfsgsvfszvBRbQpttRVpJbJpVg
LhTmHLbmbcFTFrWCbFqhFHLHVRpVtQpZVVDVprnDMJtJQnVZ
TGWWbTFFGTqlHhqhSdNdNfNSldjjBfjv
zCzpWTccHlWcPzMljMttbJfjmlfm
DqqQVZZqVsqJnbbnmjbJJQ
ZRmDZsSgVmGLsVqsLDFvrcccHrcTWCgWHBCHcCWp
cvGlQMtQlPtQWWMlcGsrFwFdbgdbdGGDCDCwdd
VChVZNBVjTTfhNTFgzrzrJgSdzgzwf
THThZTqZRHZRqNVZNTVLjRCMmQsntQctMnsPmMmMcWtLMQ
pNRHrbNlNnRLNpMMMTrcGcGTcccz
ZttBmsJmZdjsvTTvvdBMjDhfMGWGDfDfcScjfD
CmtTtwvtCsgllNHPPFbLpC
NpQcvwwRHvdfRvQsNfBQNvfRhVmVMqsZMmMshjMMtWZtMmrm
CGHbSSzFLSSHzTnbLnCWMrtWMtjnZMhZrqZtqW
FzCPPzLbPgFJbHSPldNRpgNfvvccgvwf
nSjpnnhNchMQZMSScnshshncJCGwHGClwmHPZlJPTVZCwHJf
LvtzBTgLWgLPlPwHPLPJ
dTBDqRqFzzhQFhshhNhM
HjjdPsjnllHsbnnDnbTBzLBFBZLLpRFRcCHRFz
wqqWwQhQQMCQffqqhtwMGhpZFRRZvzWzFvBvpvmcRvZm
fGfghtNhthqJrQqMqMMSgDdbPjbssDbdSnjCdd
cqPwJJnnffBFqSfJFnDDPVplLdglGgLVjzGLdVSzVt
WHRTWNHsQTNbzsbCbTsvWrWtjlgVdLgLdvdgvmLjpGlgtm
ZMQrTbNHZNsHHrQCZrNDFzhwnMJcfnDhJPPPFh
LRCFbjNjbCZDmtmqmRRmLtFJBgWBBpvJMwBJvGjBBvMBgw
TTrlfHzccVllZhdQgdGMJWvgWgBndwpG
fVSshSVlsfslhsSHHSZtZZNmNFmtmbFCDF
SPGCBPDMtbcbCtchSMccDTTrrrTFTrsrMTWHTHFVWF
JmnzqVmmwwfpJpmdHRTRsdsTrFdrQp
LqwLgzJgnjqLwgGcVbtjDGjcVbhv
PQcMvrvMsvmdSPPVccmSJcSpGBWWWbBHfWWnfttJWnWJpJ
wDzqhjzmqRzDRwqDzNDbWtjWBBBtGbtHpHnnBf
zglRhDqqDZgRNmZQVCdcCPQvvdZv
RpVjRgvFjGBNWtBWFDtt
dcqQwlqMMsCLLfbgQmtD
snlgzsggTzSTSJTr
dLHhDdtlMngFcFsFLFzzsj
vWRGGRVrrWvvGQQJBRsmQzmsqnffqcNfNcfz
vSRVJBVBwTvWTnHphTgDgtMpDl
bvvGnnJbfPmfdgJJSVtwwCpTScVfNpSC
sjsZWDqBqqMRZsDjbWMVwtwNNcNtScRHpRRttp
hzhDqqWDzZzDZzZLQPJPdPnPvlrbGdlnFQ
PwWHTwzFvNHsNzmmMwzNWGQrCqCFjpZbpnGqrqnpbr
gRVRgJRJlDLSJddDccQVrtZnCqjndnrZdnqnqpdq
chhgSSJfQhRRcSSSSBLVfzmzHTNzMNsTNWHMMvMP
lftqSpBSvhlDBDlhBSczQGmcFMcMVVFMmGFWsm
rHLHTNdggsLLnwLHbTTgdrTMPPmMGWZGQQMzQVQFZQGM
gbJnrHHjnbrgLrRrHpBJvSBDDsfJsDtstq
dBTtFLTtVmpdLhMprSRSWMRSMR
QvJvQbjbCgCQRBhzzRsNWNBC
bjgGqQGbQnjGQgnQgbGgjJnDLHLdfPVtdDmLZdBFVVZttdTf"""

print("result for part 2 with input 2")

sum_priorities_part1(rucksacks2)
sum_priorities_part2(rucksacks2)









