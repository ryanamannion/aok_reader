#AOK_Reader: A reader for the Atticus Open Contract (AOK) Dataset Reader

The purpose of this package is to privde tools to read the AOK corpus into 
python to make working with the corpus easier

## Basic Usage

```python
import aok_reader

aok_path = 'path_to/aok/top/dir'

reader = aok_reader.Reader(path=aok_path)

# --------------------------------------

# to load all (right now just master_csv)
reader.load()

# or to load just master_csv
reader.load_master_csv()        # loads to attribute
print(type(reader.master_csv))
# <class 'list'>
# master_csv loads as a list of dictionaries, each dict a document from 
# master_csv

# or return master_csv
master_csv = reader.load_master_csv()       # still loads attribute

# --------------------------------------
# Return dicts for all docs by column in master_csv
by_exclusivity = reader.index_master('Exclusivity-Answer')
print(type(by_exclusivity))
# <class 'dict'>
# For Exclusivity-Answer, the set of answers is {True, False}, so by_exclusivity
# would be a dict of len 2, and True would point to all documents with an 
# Exclusivity-Answer of True and likewise for False
print(len(by_exclusivity))
# 2
print(by_exclusivity[True][0])
# {'Filename': 'FulucaiProductionsLtd_20131223_10-Q_EX-10.9_8368347_EX-10.9_Content License Agreement.pdf', 'Document Name': 'CONTENT DISTRIBUTION AND LICENSE AGREEMENT (Page 1)', 'Document Name-Answer': 'CONTENT DISTRIBUTION AND LICENSE AGREEMENT', 'Parties': ['CONVERGTV,ÊINC. (Page 2)', '"ConvergTV" (Page 2)', 'Fulucai Productions Ltd. (Page 2)', '"Producer" (Page 2)'], 'Parties-Answer': 'CONVERGTV,ÊINC.Ê("ConvergTV"); Fulucai Productions Ltd. ("Producer")', 'Agreement Date': 'NovemberÊ15,Ê2012 (Page 2)', 'Agreement Date-Answer': '11/15/12', 'Effective Date': 'NovemberÊ15,Ê2012 (Page 2)', 'Effective Date-Answer': '11/15/12', 'Expiration Date': None, 'Expiration Date-Answer': None, 'Renewal Term': 'License Term Perpetual, unlimited runs x Other: 2 years Commencing: November 15, 2012 (Page 1)', 'Renewal Term-Answer': 'perpetual, 11/15/2014', 'Notice Period to Terminate Renewal': None, 'Notice Period to Terminate Renewal- Answer': None, 'Governing Law': 'All questions with respect to the construction of this Agreement, and the rights and liabilities of the Parties hereto, shall be governed by the laws of the State of Florida. (Page 6)', 'Governing Law-Answer': 'Florida', 'Most Favored Nation': None, 'Most Favored Nation-Answer': False, 'Non-Compete': None, 'Non-Compete-Answer': False, 'Exclusivity': 'During the License Term (which is identified in the Deal Terms), Producer agrees that ConvergTV has the exclusive right to exercise the rights granted to it under this Agreement with respect to the Program, including those in Section 1, within the Licensed Territory. (Page 3)', 'Exclusivity-Answer': True, 'No-Solicit of Customers': None, 'No-Solicit of Customers-Answer': False, 'No-Solicit of Employees': None, 'No-Solicit of Employees-Answer': False, 'Non-Disparagement': None, 'Non-Disparagement-Answer': False, 'Termination for Convenience': None, 'Termination for Convenience-Answer': False, 'ROFR/ROFO/ROFN': None, 'ROFR/ROFO/ROFN-Answer': False, 'Change of Control': None, 'Change of Control-Answer': False, 'Anti-assignment': None, 'Anti-assignment-Answer': False, 'Revenue/Profit Sharing': ['Revenue Share as specified in this CONTENT DISTRIBUTION AND LICENSE AGREEMENT. (Page 1)', 'The revenue share for the Program is stated in Exhibit B. (Page 3)'], 'Revenue/Profit Sharing-Answer': True, 'Price Restrictions': None, 'Price Restrictions-Answer': False, 'Minimum Commitment': None, 'Minimum Commitment-Answer': False, 'Volume Restriction': None, 'Volume Restriction-Answer': False, 'IP Ownership Assignment': None, 'IP Ownership Assignment-Answer': False, 'Joint IP Ownership': None, 'Joint IP Ownership-Answer': False, 'License Grant': ['"LicensedÊRights"ÊtoÊConvergTVÊandÊConvergTV Channels and/or Distribution Outlets x All, including but not limited to: xSimultaneous Internet Streaming x OTT Television x Internet Protocol Television x Radio, short wave, microwave, fiber optic x Alternative, secondary and specialty distribution x Stored as VOD, Content Distribution Networks/Company Servers x Full Television Broadcast Rights: x Free: Terrestrial, Cable, Satellite x Pay: Terrestrial, Cable, Satellite x Direct Satellite IP Distribution Systems (Page 1)', 'For the License Term and within the Licensed Territory, Producer hereby grants to ConvergTV a right and license to Distribute theprogram, file or video listed on the Deal Terms above (the "Program") consisting of (check one) __ episodes (series) or x one-offs,for unlimited runs for the License Term through ConvergTV channels and/or other distribution outlets, in accordance with theLicense Rights.  (Page 2)', 'Producer further grants to ConvergTV the right and license to Distribute the Program on any ConvergTV channel, and/or other distribution outlets, that exists today or that is created or developed in the future and this right includes the right to Distribute on any channels of a ConvergTV affiliate and/or other distribution outlets without limitation. (Page 2)', 'Producer further grants to ConvergTV the right and license to Distribute and re-Distribute, including relicensing or sublicensing, the Program at such dates and times as are determined by ConvergTV in its sole discretion. (Page 2)', 'Producer further grants to ConvergTV the right and license to create (re-edit), at its sole cost and expense, new and different versions of the Program, create foreign language, subtitled or translated versions of the Program as well as to create closed captioned versions of the Program, including NTCS, PAL, SEACAM standards, or other standards, including those yet to be developed. (Page 2)', 'Producer further grants to ConvergTV the right and license to utilize any and all footage from the Program for promotional and marketing purposes related to the Distribution of the Program and for promotion of channels or other distribution methods. (Page 3)', 'The grant of rights and license pursuant to this Section 1 shall include, but not be limited to, the right of ConvergTV to Distribute and re-Distribute all or any portions of the Program and Promotional Works, including excerpts therefrom, and any new and different versions of the Program, on simultaneous internet transmission or streaming, internet protocol television and any television networks and stations, and/or other distribution outlets, via domestic or foreign television signals, as well as through CATV and DBS systems, satellite, microwave, fiber optic and/or other modes of Distribution yet to be developed, but which may be utilized by ConvergTV in the future. (Page 3)'], 'License Grant-Answer': True, 'Non-Transferable License': None, 'Non-Transferable License-Answer': False, 'Affiliate License-Licensor': None, 'Affiliate License-Licensor-Answer': False, 'Affiliate License-Licensee': 'Producer further grants to ConvergTV the right and license to Distribute the Program on any ConvergTV channel, and/or other distribution outlets, that exists today or that is created or developed in the future and this right includes the right to Distribute on any channels of a ConvergTV affiliate and/or other distribution outlets without limitation. (Page 2)', 'Affiliate License-Licensee-Answer': True, 'Unlimited/All-You-Can-Eat License': ['For the License Term and within the Licensed Territory, Producer hereby grants to ConvergTV a right and license to Distribute the program, file or video listed on the Deal Terms above (the "Program") consisting of (check one) [ ] episodes (series) or [ ] one-offs, for unlimited runs for the License Term through ConvergTV channels and/or other distribution outlets, in accordance with the License Rights. (Page 2)', 'Producer further grants to ConvergTV the right and license to Distribute the Program on any ConvergTV channel, and/or other distribution outlets, that exists today or that is created or developed in the future and this right includes the right to Distribute on any channels of a ConvergTV affiliate and/or other distribution outlets without limitation. (Page 2)'], 'Unlimited/All-You-Can-Eat License-Answer': True, 'Irrevocable or Perpetual License': None, 'Irrevocable or Perpetual License-Answer': False, 'Source Code Escrow': None, 'Source Code Escrow-Answer': False, 'Post-termination Services': None, 'Post-termination Services-Answer': False, 'Audit Rights': 'EachÊofÊtheÊPartiesÊmay,ÊatÊitsÊownÊexpense,ÊauditÊtheÊotherÊPartyÕsÊcomplianceÊwithÊthisÊAgreement,ÊincludingÊbutÊnotÊlimitedÊto, auditingÊtheÊotherÊPartyÕsÊrepresentationsÊandÊwarranties. (Page 7)', 'Audit Rights-Answer': True, 'Uncapped Liability': None, 'Uncapped Liability-Answer': False, 'Cap on Liability': None, 'Cap on Liability-Answer': False, 'Liquidated Damages': None, 'Liquidated Damages-Answer': False, 'Warranty Duration': None, 'Warranty Duration-Answer': False, 'Insurance': None, 'Insurance-Answer': False, 'Covenant not to Sue': None, 'Covenant not to Sue-Answer': False, 'Third Party Beneficiary': None, 'Third Party Beneficiary-Answer': False}
```

## Design Principles:
1. aok_reader assumes the user has access to the dataset, can provide a path to 
   the top-level dir
    * Perhaps in the future it can download it for you like a spaCy.load()
2. aok_reader reads the documents into python data structures
    * To that end, some values are changed in master_contracts.csv:
        * '' --> None
        * Yes --> True
        * No --> False
        * Any cell where multiple items are separated by '\n\n' is split into a
        list

