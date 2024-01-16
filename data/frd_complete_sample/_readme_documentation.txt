Complete Bundle (Stocks, ETFs, Futures, Indices, Crypto) Historical Datasets
============================================================================

NOTE: Only minutes with trading volume are included. Bars with zero volume are excluded.

 
Timeframes : 1-minute, 5-minutes, 30-minutes, 1-hour, 1-day

This bundle contains historical intraday data for :

- 7492 most liquid US stocks 
  [includes all active Russell 3000, S&P500, Nasdaq 100, and DJI stocks)
- 2518 most liquid US ETFs  
- 259 most actively traded futures contracts
- 117 most popular US indices
- 54 most active cryptocurrencies
- 73 most active FX crosses



Stock / ETF Data
-----------------

We provide three types of data:
Unadjusted - actual historic traded prices with no adjustments (only the 1-minute and 1-day timeframes are available for unadjusted data)
Split Adjusted - prices adjusted for stock splits and reverse splits only
Split+Dividend Adjusted - prices adjusted for both splits and dividends



Futures Data 
--------------

We provide both continuous data (ie a single series of chained contracts) as well as individual contract data (ie data for each futures contract delivered in a single file per contract).

We provide two types of continuous data :
Unadjusted - actual historic traded prices with no adjustments 
Adjusted - prices adjusted for price jumps on contract roll date, more details are available at

In addition, indivudal futures contracts in the 1-min and 1-day timeframes are included.


More details on the adjustment process for stocks, ETFs and Futures is at https://firstratedata.com/about/price_adjustment


Format
-------
Data is in the format : {DateTime (yyyy-MM-dd HH:mm:ss), Open, High, Low, Close, Volume}  
(daily futures data also included open interest in the final field)

- Volume Numbers are in individual shares, contracts (or for FX the base currency)
- Timestamps run from the start of the period (eg 1min bars stamped 09:30 run from 09:30.00 to 09:30.59)
- Times with zero volume are omitted (thus gaps in the data sequence are when there have been no trades)



Updates
-------
This dataset is updated daily (update files are available by 3am on the following trading day).

New stock and ETF tickers are added at the end of every week.

 

Notes
-----
 
- Timezone is US Eastern Time    
- Excel will usually fail to open large files directly. 
  To use the data in Excel, open the files using notepad and then break into smaller files or copy/paste into Excel 
- Data license is available at https://firstratedata.com/about/license
 


Included Sample Files (2 weeks data):

Stock : AMZN (Amazon), MSFT (Microsoft)   
ETF : SPY (SPDR S&P 500 ETF), QQQ (Invesco QQQ Trust) 
Futures : ES(S&P 500 E-Mini) 
Crypto : BTC (Bitcoin) 
Index : SPX (S&P 500 Index)

 

Tickers
========



Futures Tickers
----------------
A6 (Australian Dollar Futures (CME) ) Continuous Futures : Start Date:2008-01-02
A6 (Australian Dollar Futures (CME) ) Individual Contracts : First Contract:A6Z08 -> Last Contract:A6Z24
AD (Canadian Dollar Futures (CME) ) Continuous Futures : Start Date:2008-01-02
AD (Canadian Dollar Futures (CME) ) Individual Contracts : First Contract:ADZ08 -> Last Contract:ADZ24
ALI (Aluminum (CME) ) Continuous Futures : Start Date:2009-01-01
ALI (Aluminum (CME) ) Individual Contracts : First Contract:ALIZ09 -> Last Contract:ALIZ24
B6 (British Pound Futures (CME) ) Continuous Futures : Start Date:2008-01-02
B6 (British Pound Futures (CME) ) Individual Contracts : First Contract:B6Z08 -> Last Contract:B6Z24
BFX (Bel 20 (EuroNext) ) Continuous Futures : Start Date:2008-01-21
BFX (Bel 20 (EuroNext) ) Individual Contracts : First Contract:BFXZ08 -> Last Contract:BFXZ24
BR (Brazilian Real Futures (CME) ) Continuous Futures : Start Date:2008-03-13
BR (Brazilian Real Futures (CME) ) Individual Contracts : First Contract:BRZ08 -> Last Contract:BRZ24
BTC (Bitcoin Futures (CME) ) Continuous Futures : Start Date:2017-12-17
BTC (Bitcoin Futures (CME) ) Individual Contracts : First Contract:BTCZ17 -> Last Contract:BTCZ24
BZ (Brent Last Day Financial Futures (NYMEX) ) Continuous Futures : Start Date:2008-03-17
BZ (Brent Last Day Financial Futures (NYMEX) ) Individual Contracts : First Contract:BZZ08 -> Last Contract:BZZ24
C (CocoaÂ Futures (ICE) ) Continuous Futures : Start Date:2008-03-12
C (CocoaÂ Futures (ICE) ) Individual Contracts : First Contract:CZ08 -> Last Contract:CZ24
CB (Cash-Settled Butter (CME) ) Continuous Futures : Start Date:2008-02-29
CB (Cash-Settled Butter (CME) ) Individual Contracts : First Contract:CBZ08 -> Last Contract:CBZ24
CC (Cocoa (ICE) ) Continuous Futures : Start Date:2008-02-01
CC (Cocoa (ICE) ) Individual Contracts : First Contract:CCZ08 -> Last Contract:CCZ24
CL (Crude Oil Wti Futures (NYMEX) ) Continuous Futures : Start Date:2008-01-01
CL (Crude Oil Wti Futures (NYMEX) ) Individual Contracts : First Contract:CLZ08 -> Last Contract:CLZ24
CNH (USD/Offshore RMB Continuous Backadjusted (CME) ) Continuous Futures : Start Date:2013-02-24
CNH (USD/Offshore RMB Continuous Backadjusted (CME) ) Individual Contracts : First Contract:CNHZ13 -> Last Contract:CNHZ24
CSC (Cash-Settled Cheese (CME) ) Continuous Futures : Start Date:2010-07-12
CSC (Cash-Settled Cheese (CME) ) Individual Contracts : First Contract:CSCZ10 -> Last Contract:CSCZ24
CT (Cotton #2 Futures (ICE) ) Continuous Futures : Start Date:2008-02-11
CT (Cotton #2 Futures (ICE) ) Individual Contracts : First Contract:CTZ08 -> Last Contract:CTZ24
DC (Class Iii Milk (CME) ) Continuous Futures : Start Date:2008-02-28
DC (Class Iii Milk (CME) ) Individual Contracts : First Contract:DCZ08 -> Last Contract:DCZ24
DX (US Dollar Index Future (ICE) ) Continuous Futures : Start Date:2008-01-01
DX (US Dollar Index Future (ICE) ) Individual Contracts : First Contract:DXZ08 -> Last Contract:DXZ24
E1 (Swiss Franc Futures (CME) ) Continuous Futures : Start Date:2008-01-02
E1 (Swiss Franc Futures (CME) ) Individual Contracts : First Contract:E1Z08 -> Last Contract:E1Z24
E6 (Euro FX Futures (CME) ) Continuous Futures : Start Date:2008-01-02
E6 (Euro FX Futures (CME) ) Individual Contracts : First Contract:E6Z08 -> Last Contract:E6Z24
E7 (E-Mini Euro Fx (CME) ) Continuous Futures : Start Date:2008-01-02
E7 (E-Mini Euro Fx (CME) ) Individual Contracts : First Contract:E7Z08 -> Last Contract:E7Z24
EBM (Milling Wheat Futures (EUREX) ) Continuous Futures : Start Date:2008-03-11
EBM (Milling Wheat Futures (EUREX) ) Individual Contracts : First Contract:EBMZ08 -> Last Contract:EBMZ24
ED (Eurodollar Futures (CME) ) Continuous Futures : Start Date:2008-01-02
ED (Eurodollar Futures (CME) ) Individual Contracts : First Contract:EDZ08 -> Last Contract:EDZ24
ES (E-Mini S&P 500 Futures (CME) ) Continuous Futures : Start Date:2008-01-02
ES (E-Mini S&P 500 Futures (CME) ) Individual Contracts : First Contract:ESZ08 -> Last Contract:ESZ24
ESG (E-Mini S&P 500 ESG Futures (CME) ) Continuous Futures : Start Date:2019-11-18
ESG (E-Mini S&P 500 ESG Futures (CME) ) Individual Contracts : First Contract:ESGZ19 -> Last Contract:ESGZ24
EW (E-Mini S&P 400 Midcap Futures (CME) ) Continuous Futures : Start Date:2008-01-02
EW (E-Mini S&P 400 Midcap Futures (CME) ) Individual Contracts : First Contract:EWZ08 -> Last Contract:EWZ24
FBON (Euro-Bono Futures (EUREX) ) Continuous Futures : Start Date:2015-11-02
FBON (Euro-Bono Futures (EUREX) ) Individual Contracts : First Contract:FBONZ15 -> Last Contract:FBONZ24
FBTM (Mid-Term Euro-BTP Futures (EUREX) ) Continuous Futures : Start Date:2011-10-26
FBTM (Mid-Term Euro-BTP Futures (EUREX) ) Individual Contracts : First Contract:FBTMZ11 -> Last Contract:FBTMZ24
FBTP (Euro BTP Long-Bond Futures (EUREX) ) Continuous Futures : Start Date:2009-10-13
FBTP (Euro BTP Long-Bond Futures (EUREX) ) Individual Contracts : First Contract:FBTPZ09 -> Last Contract:FBTPZ24
FBTS (Short-Term Euro-Btp (EUREX) ) Continuous Futures : Start Date:2011-09-19
FBTS (Short-Term Euro-Btp (EUREX) ) Individual Contracts : First Contract:FBTSZ11 -> Last Contract:FBTSZ24
FCE (CAC40 Futures (Euronext) ) Continuous Futures : Start Date:2008-02-15
FCE (CAC40 Futures (Euronext) ) Individual Contracts : First Contract:FCEZ08 -> Last Contract:FCEZ24
FDAX (DAX Futures (EUREX) ) Continuous Futures : Start Date:2008-01-02
FDAX (DAX Futures (EUREX) ) Individual Contracts : First Contract:FDAXZ08 -> Last Contract:FDAXZ24
FDIV (Divdax (EUREX) ) Continuous Futures : Start Date:2013-04-23
FDIV (Divdax (EUREX) ) Individual Contracts : First Contract:FDIVZ13 -> Last Contract:FDIVZ24
FDXM (Mini DAX (EUREX) ) Continuous Futures : Start Date:2015-10-28
FDXM (Mini DAX (EUREX) ) Individual Contracts : First Contract:FDXMZ15 -> Last Contract:FDXMZ24
FDXS (Micro DAX (EUREX) ) Continuous Futures : Start Date:2021-04-19
FDXS (Micro DAX (EUREX) ) Individual Contracts : First Contract:FDXSZ21 -> Last Contract:FDXSZ24
FESX (Euro Stoxx 50 Futures (EUREX) ) Continuous Futures : Start Date:2008-01-02
FESX (Euro Stoxx 50 Futures (EUREX) ) Individual Contracts : First Contract:FESXZ08 -> Last Contract:FESXZ24
FEU3 (Three-Month Euribor (EUREX) ) Continuous Futures : Start Date:2008-01-02
FEU3 (Three-Month Euribor (EUREX) ) Individual Contracts : First Contract:FEU3Z08 -> Last Contract:FEU3Z24
FGBL (Euro Bund Futures (EUREX) ) Continuous Futures : Start Date:2008-03-05
FGBL (Euro Bund Futures (EUREX) ) Individual Contracts : First Contract:FGBLZ08 -> Last Contract:FGBLZ24
FGBM (Euro Bobl Futures (EUREX) ) Continuous Futures : Start Date:2008-03-05
FGBM (Euro Bobl Futures (EUREX) ) Individual Contracts : First Contract:FGBMZ08 -> Last Contract:FGBMZ24
FGBS (Euro-Schatz (EUREX) ) Continuous Futures : Start Date:2008-03-05
FGBS (Euro-Schatz (EUREX) ) Individual Contracts : First Contract:FGBSZ08 -> Last Contract:FGBSZ24
FGBX (Euro-Buxl (EUREX) ) Continuous Futures : Start Date:2008-03-07
FGBX (Euro-Buxl (EUREX) ) Individual Contracts : First Contract:FGBXZ08 -> Last Contract:FGBXZ24
FOAM (Mid-Term Euro-OAT Futures (EUREX) ) Continuous Futures : Start Date:2013-03-12
FOAM (Mid-Term Euro-OAT Futures (EUREX) ) Individual Contracts : First Contract:FOAMZ13 -> Last Contract:FOAMZ24
FOAT (Euro-OAT (EUREX) ) Continuous Futures : Start Date:2012-04-16
FOAT (Euro-OAT (EUREX) ) Individual Contracts : First Contract:FOATZ12 -> Last Contract:FOATZ24
FSMX (Mini-Mdax (EUREX) ) Continuous Futures : Start Date:2021-11-08
FSMX (Mini-Mdax (EUREX) ) Individual Contracts : First Contract:FSMXZ21 -> Last Contract:FSMXZ24
FTDD (FTSE 100 Index Total Return Futures (EUREX) ) Continuous Futures : Start Date:2009-01-01
FTDD (FTSE 100 Index Total Return Futures (EUREX) ) Individual Contracts : First Contract:FTDDZ09 -> Last Contract:FTDDZ24
FTDX (Tecdax (EUREX) ) Continuous Futures : Start Date:2008-01-02
FTDX (Tecdax (EUREX) ) Individual Contracts : First Contract:FTDXZ08 -> Last Contract:FTDXZ24
FTI (Amsterdam Index Futures (Euronext) ) Continuous Futures : Start Date:2008-02-15
FTI (Amsterdam Index Futures (Euronext) ) Individual Contracts : First Contract:FTIZ08 -> Last Contract:FTIZ24
FTUK (FTSE 100 Futures (ICE) ) Continuous Futures : Start Date:2008-01-02
FTUK (FTSE 100 Futures (ICE) ) Individual Contracts : First Contract:FTUKZ08 -> Last Contract:FTUKZ24
FVSA (VstoxxÂ Futures (EUREX) ) Continuous Futures : Start Date:2011-09-08
FVSA (VstoxxÂ Futures (EUREX) ) Individual Contracts : First Contract:FVSAZ11 -> Last Contract:FVSAZ24
FXXP (Stoxx Europe 600 Index (EUREX) ) Continuous Futures : Start Date:2010-09-24
FXXP (Stoxx Europe 600 Index (EUREX) ) Individual Contracts : First Contract:FXXPZ10 -> Last Contract:FXXPZ24
G (10-Year Long Gilt Futures (ICE) ) Continuous Futures : Start Date:2008-01-02
G (10-Year Long Gilt Futures (ICE) ) Individual Contracts : First Contract:GZ08 -> Last Contract:GZ24
GC (Gold Futures (CME) ) Continuous Futures : Start Date:2008-01-31
GC (Gold Futures (CME) ) Individual Contracts : First Contract:GCZ08 -> Last Contract:GCZ24
GF (Feeder Cattle Futures (CME) ) Continuous Futures : Start Date:2008-01-02
GF (Feeder Cattle Futures (CME) ) Individual Contracts : First Contract:GFZ08 -> Last Contract:GFZ24
GSCI (S&P GSCI Futures (CME) ) Continuous Futures : Start Date:2008-03-18
GSCI (S&P GSCI Futures (CME) ) Individual Contracts : First Contract:GSCIZ08 -> Last Contract:GSCIZ24
HE (Lean Hog Futures (CME) ) Continuous Futures : Start Date:2008-01-23
HE (Lean Hog Futures (CME) ) Individual Contracts : First Contract:HEZ08 -> Last Contract:HEZ24
HG (Copper Futures (CME) ) Continuous Futures : Start Date:2008-01-01
HG (Copper Futures (CME) ) Individual Contracts : First Contract:HGZ08 -> Last Contract:HGZ24
HH (Natural Gas Henry Hub Last-Day Financial Futures (NYMEX) ) Continuous Futures : Start Date:2010-08-30
HH (Natural Gas Henry Hub Last-Day Financial Futures (NYMEX) ) Individual Contracts : First Contract:HHZ10 -> Last Contract:HHZ24
HO (Ny Harbor Ulsd (NYMEX) ) Continuous Futures : Start Date:2008-02-26
HO (Ny Harbor Ulsd (NYMEX) ) Individual Contracts : First Contract:HOZ08 -> Last Contract:HOZ24
HRC (U.S. Midwest Domestic Hot-Rolled Coil Steel (CME) ) Continuous Futures : Start Date:2022-02-25
HRC (U.S. Midwest Domestic Hot-Rolled Coil Steel (CME) ) Individual Contracts : First Contract:HRCZ22 -> Last Contract:HRCZ24
ISE (Iseq 20 (EuroNext) ) Continuous Futures : Start Date:2009-01-01
ISE (Iseq 20 (EuroNext) ) Individual Contracts : First Contract:ISEZ09 -> Last Contract:ISEZ24
J1 (Japanese Yen Futures (CME) ) Continuous Futures : Start Date:2008-01-02
J1 (Japanese Yen Futures (CME) ) Individual Contracts : First Contract:J1Z08 -> Last Contract:J1Z24
J7 (E-Mini Japanese Yen (CME) ) Continuous Futures : Start Date:2008-01-02
J7 (E-Mini Japanese Yen (CME) ) Individual Contracts : First Contract:J7Z08 -> Last Contract:J7Z24
KC (Coffee Futures (ICE) ) Continuous Futures : Start Date:2008-01-02
KC (Coffee Futures (ICE) ) Individual Contracts : First Contract:KCZ08 -> Last Contract:KCZ24
KRW (Krw/USD (CME) ) Continuous Futures : Start Date:2009-11-30
KRW (Krw/USD (CME) ) Individual Contracts : First Contract:KRWZ09 -> Last Contract:KRWZ24
L (3 Month Sterling Futures (ICE) ) Continuous Futures : Start Date:2008-01-02
L (3 Month Sterling Futures (ICE) ) Individual Contracts : First Contract:LZ08 -> Last Contract:LZ24
LBS (Random Length Lumber Futures (CME) ) Continuous Futures : Start Date:2008-10-19
LBS (Random Length Lumber Futures (CME) ) Individual Contracts : First Contract:LBSZ08 -> Last Contract:LBSZ24
LE (Live Cattle Futures (CME) ) Continuous Futures : Start Date:2008-01-16
LE (Live Cattle Futures (CME) ) Individual Contracts : First Contract:LEZ08 -> Last Contract:LEZ24
M2K (Micro E-Mini Russell 2000 Index Futures (CME) ) Continuous Futures : Start Date:2019-05-05
M2K (Micro E-Mini Russell 2000 Index Futures (CME) ) Individual Contracts : First Contract:M2KZ19 -> Last Contract:M2KZ24
MAX (Aex Mini (EuroNext) ) Continuous Futures : Start Date:2022-03-28
MAX (Aex Mini (EuroNext) ) Individual Contracts : First Contract:MAXZ22 -> Last Contract:MAXZ24
MBT (Micro Bitcoin Futures (CME) ) Continuous Futures : Start Date:2021-05-02
MBT (Micro Bitcoin Futures (CME) ) Individual Contracts : First Contract:MBTZ21 -> Last Contract:MBTZ24
MCL (Micro Wti Crude Oil Futures (NYMEX) ) Continuous Futures : Start Date:2021-07-11
MCL (Micro Wti Crude Oil Futures (NYMEX) ) Individual Contracts : First Contract:MCLZ21 -> Last Contract:MCLZ24
MES (Micro E-Mini S&P 500 Futures (CME) ) Continuous Futures : Start Date:2019-05-05
MES (Micro E-Mini S&P 500 Futures (CME) ) Individual Contracts : First Contract:MESZ19 -> Last Contract:MESZ24
MET (Ether Micro (CME) ) Continuous Futures : Start Date:2021-12-05
MET (Ether Micro (CME) ) Individual Contracts : First Contract:METZ21 -> Last Contract:METZ24
MFC (Cac 40 Mini (EuroNext) ) Continuous Futures : Start Date:2014-10-09
MFC (Cac 40 Mini (EuroNext) ) Individual Contracts : First Contract:MFCZ14 -> Last Contract:MFCZ24
MFS (Mini MSCI Eafe Futures (ICE) ) Continuous Futures : Start Date:2009-09-08
MFS (Mini MSCI Eafe Futures (ICE) ) Individual Contracts : First Contract:MFSZ09 -> Last Contract:MFSZ24
MGC (Micro Gold Futures (CME) ) Continuous Futures : Start Date:2010-10-03
MGC (Micro Gold Futures (CME) ) Individual Contracts : First Contract:MGCZ10 -> Last Contract:MGCZ24
MME (MSCI Emerging Markets Index Futures (ICE) ) Continuous Futures : Start Date:2009-09-08
MME (MSCI Emerging Markets Index Futures (ICE) ) Individual Contracts : First Contract:MMEZ09 -> Last Contract:MMEZ24
MNQ (Micro E-Mini Nasdaq-100 Futures (CME) ) Continuous Futures : Start Date:2019-05-05
MNQ (Micro E-Mini Nasdaq-100 Futures (CME) ) Individual Contracts : First Contract:MNQZ19 -> Last Contract:MNQZ24
MP (Mexican Peso Futures (CME) ) Continuous Futures : Start Date:2008-01-02
MP (Mexican Peso Futures (CME) ) Individual Contracts : First Contract:MPZ08 -> Last Contract:MPZ24
MURA (MSCI China (EUREX) ) Continuous Futures : Start Date:2021-10-22
MURA (MSCI China (EUREX) ) Individual Contracts : First Contract:MURAZ21 -> Last Contract:MURAZ24
N6 (New Zealand Dollar Futures (CME) ) Continuous Futures : Start Date:2008-01-02
N6 (New Zealand Dollar Futures (CME) ) Individual Contracts : First Contract:N6Z08 -> Last Contract:N6Z24
NG (Henry Hub Natural Gas Futures (NYMEX) ) Continuous Futures : Start Date:2008-02-24
NG (Henry Hub Natural Gas Futures (NYMEX) ) Individual Contracts : First Contract:NGZ08 -> Last Contract:NGZ24
NIY (Nikkei 225 Yen Futures (CME) ) Continuous Futures : Start Date:2008-03-14
NIY (Nikkei 225 Yen Futures (CME) ) Individual Contracts : First Contract:NIYZ08 -> Last Contract:NIYZ24
NKD (Nikkei 225 Dollar Futures (CME) ) Continuous Futures : Start Date:2008-03-07
NKD (Nikkei 225 Dollar Futures (CME) ) Individual Contracts : First Contract:NKDZ08 -> Last Contract:NKDZ24
NOK (Norwegian Krone (CME) ) Continuous Futures : Start Date:2008-05-14
NOK (Norwegian Krone (CME) ) Individual Contracts : First Contract:NOKZ08 -> Last Contract:NOKZ24
NQ (E-Mini Nasdaq-100 Futures (CME) ) Continuous Futures : Start Date:2008-01-02
NQ (E-Mini Nasdaq-100 Futures (CME) ) Individual Contracts : First Contract:NQZ08 -> Last Contract:NQZ24
OJ (Orange Juice Futures (ICE) ) Continuous Futures : Start Date:2008-02-20
OJ (Orange Juice Futures (ICE) ) Individual Contracts : First Contract:OJZ08 -> Last Contract:OJZ24
PA (Palladium Futures (NYMEX) ) Continuous Futures : Start Date:2008-01-01
PA (Palladium Futures (NYMEX) ) Individual Contracts : First Contract:PAZ08 -> Last Contract:PAZ24
PL (Platinum Futures (NYMEX) ) Continuous Futures : Start Date:2008-01-01
PL (Platinum Futures (NYMEX) ) Individual Contracts : First Contract:PLZ08 -> Last Contract:PLZ24
PRK (Pork Cutout (CME) ) Continuous Futures : Start Date:2020-11-09
PRK (Pork Cutout (CME) ) Individual Contracts : First Contract:PRKZ20 -> Last Contract:PRKZ24
PSI (Psi 20 (EuroNext) ) Continuous Futures : Start Date:2008-01-02
PSI (Psi 20 (EuroNext) ) Individual Contracts : First Contract:PSIZ08 -> Last Contract:PSIZ24
QG (Natural Gas Mini Futures (NYMEX) ) Continuous Futures : Start Date:2008-02-26
QG (Natural Gas Mini Futures (NYMEX) ) Individual Contracts : First Contract:QGZ08 -> Last Contract:QGZ24
RB (Rbob Gasoline Futures (NYMEX) ) Continuous Futures : Start Date:2008-02-26
RB (Rbob Gasoline Futures (NYMEX) ) Individual Contracts : First Contract:RBZ08 -> Last Contract:RBZ24
RM (Robusta Coffee Futures (ICE) ) Continuous Futures : Start Date:2008-10-07
RM (Robusta Coffee Futures (ICE) ) Individual Contracts : First Contract:RMZ08 -> Last Contract:RMZ24
RP (Euro-British Pound Futures (CME) ) Continuous Futures : Start Date:2008-01-02
RP (Euro-British Pound Futures (CME) ) Individual Contracts : First Contract:RPZ08 -> Last Contract:RPZ24
RS (Canola Futures (ICE) ) Continuous Futures : Start Date:2008-03-16
RS (Canola Futures (ICE) ) Individual Contracts : First Contract:RSZ08 -> Last Contract:RSZ24
RTY (E-Mini Russell 2000 (CME) ) Continuous Futures : Start Date:2008-01-02
RTY (E-Mini Russell 2000 (CME) ) Individual Contracts : First Contract:RTYZ08 -> Last Contract:RTYZ24
RU (Russian Ruble Futures (CME) ) Continuous Futures : Start Date:2008-03-14
RU (Russian Ruble Futures (CME) ) Individual Contracts : First Contract:RUZ08 -> Last Contract:RUZ24
SB (Sugar #11 Futures (ICE) ) Continuous Futures : Start Date:2008-02-29
SB (Sugar #11 Futures (ICE) ) Individual Contracts : First Contract:SBZ08 -> Last Contract:SBZ24
SEK (Swedish Krona (CME) ) Continuous Futures : Start Date:2009-01-23
SEK (Swedish Krona (CME) ) Individual Contracts : First Contract:SEKZ09 -> Last Contract:SEKZ24
SI (Silver Futures (CME) ) Continuous Futures : Start Date:2008-01-01
SI (Silver Futures (CME) ) Individual Contracts : First Contract:SIZ08 -> Last Contract:SIZ24
SIL (Micro Silver Futures (CME) ) Continuous Futures : Start Date:2013-06-17
SIL (Micro Silver Futures (CME) ) Individual Contracts : First Contract:SILZ13 -> Last Contract:SILZ24
SIR (Inr/USD (CME) ) Continuous Futures : Start Date:2013-01-29
SIR (Inr/USD (CME) ) Individual Contracts : First Contract:SIRZ13 -> Last Contract:SIRZ24
SR1 (1 Month Sofr Futures (CME) ) Continuous Futures : Start Date:2018-05-06
SR1 (1 Month Sofr Futures (CME) ) Individual Contracts : First Contract:SR1Z18 -> Last Contract:SR1Z24
SR3 (3 Month Sofr Futures (CME) ) Continuous Futures : Start Date:2018-05-06
SR3 (3 Month Sofr Futures (CME) ) Individual Contracts : First Contract:SR3Z18 -> Last Contract:SR3Z24
T6 (South African Rand Futures (CME) ) Continuous Futures : Start Date:2008-03-18
T6 (South African Rand Futures (CME) ) Individual Contracts : First Contract:T6Z08 -> Last Contract:T6Z24
TN (Ultra 10-Year Us Treasury Note Futures (CBOT) ) Continuous Futures : Start Date:2016-01-10
TN (Ultra 10-Year Us Treasury Note Futures (CBOT) ) Individual Contracts : First Contract:TNZ16 -> Last Contract:TNZ24
UB (Ultra Us Treasury Bond Futures (CBOT) ) Continuous Futures : Start Date:2010-01-10
UB (Ultra Us Treasury Bond Futures (CBOT) ) Individual Contracts : First Contract:UBZ10 -> Last Contract:UBZ24
US (30 Year Us Treasury Bond Future (CBOT) ) Continuous Futures : Start Date:2008-01-01
US (30 Year Us Treasury Bond Future (CBOT) ) Individual Contracts : First Contract:USZ08 -> Last Contract:USZ24
VX (VIX Futures (CBOE) ) Continuous Futures : Start Date:2008-08-05
VX (VIX Futures (CBOE) ) Individual Contracts : First Contract:VXZ08 -> Last Contract:VXZ24
VXM (Mini VIX Futures (CBOE) ) Continuous Futures : Start Date:2020-08-09
VXM (Mini VIX Futures (CBOE) ) Individual Contracts : First Contract:VXMZ20 -> Last Contract:VXMZ24
XAE (E-Mini Energy Select Sector Futures (CME) ) Continuous Futures : Start Date:2011-05-02
XAE (E-Mini Energy Select Sector Futures (CME) ) Individual Contracts : First Contract:XAEZ11 -> Last Contract:XAEZ24
XAF (E-Mini Financial Select Sector Futures (CME) ) Continuous Futures : Start Date:2011-04-27
XAF (E-Mini Financial Select Sector Futures (CME) ) Individual Contracts : First Contract:XAFZ11 -> Last Contract:XAFZ24
XAI (E-Mini Industrial Select Sector Futures (CME) ) Continuous Futures : Start Date:2011-04-14
XAI (E-Mini Industrial Select Sector Futures (CME) ) Individual Contracts : First Contract:XAIZ11 -> Last Contract:XAIZ24
XC (Corn Mini Futures (CBOT) ) Continuous Futures : Start Date:2008-03-16
XC (Corn Mini Futures (CBOT) ) Individual Contracts : First Contract:XCZ08 -> Last Contract:XCZ24
YM (Dow Futures Mini (CBOT) ) Continuous Futures : Start Date:2008-01-01
YM (Dow Futures Mini (CBOT) ) Individual Contracts : First Contract:YMZ08 -> Last Contract:YMZ24
ZC (Corn Futures (CBOT) ) Continuous Futures : Start Date:2008-02-19
ZC (Corn Futures (CBOT) ) Individual Contracts : First Contract:ZCZ08 -> Last Contract:ZCZ24
ZF (5-Year Treasury Note Futures (CBOT) ) Continuous Futures : Start Date:2008-01-01
ZF (5-Year Treasury Note Futures (CBOT) ) Individual Contracts : First Contract:ZFZ08 -> Last Contract:ZFZ24
ZK (Ethanol Futures (CBOT) ) Continuous Futures : Start Date:2008-03-06
ZK (Ethanol Futures (CBOT) ) Individual Contracts : First Contract:ZKZ08 -> Last Contract:ZKZ24
ZL (Soybean Oil Futures (CBOT) ) Continuous Futures : Start Date:2008-01-01
ZL (Soybean Oil Futures (CBOT) ) Individual Contracts : First Contract:ZLZ08 -> Last Contract:ZLZ24
ZM (Soybean Meal Futures (CBOT) ) Continuous Futures : Start Date:2008-02-19
ZM (Soybean Meal Futures (CBOT) ) Individual Contracts : First Contract:ZMZ08 -> Last Contract:ZMZ24
ZN (10-Year Treasury Note Futures (CBOT) ) Continuous Futures : Start Date:2008-01-01
ZN (10-Year Treasury Note Futures (CBOT) ) Individual Contracts : First Contract:ZNZ08 -> Last Contract:ZNZ24
ZO (Oats Futures (CBOT) ) Continuous Futures : Start Date:2008-02-19
ZO (Oats Futures (CBOT) ) Individual Contracts : First Contract:ZOZ08 -> Last Contract:ZOZ24
ZQ (30 Day Fed Funds Future (CBOT) ) Continuous Futures : Start Date:2008-03-02
ZQ (30 Day Fed Funds Future (CBOT) ) Individual Contracts : First Contract:ZQZ08 -> Last Contract:ZQZ24
ZR (Rough Rice Futures (CBOT) ) Continuous Futures : Start Date:2008-02-19
ZR (Rough Rice Futures (CBOT) ) Individual Contracts : First Contract:ZRZ08 -> Last Contract:ZRZ24
ZRPA (MSCI Europe (EUREX) ) Continuous Futures : Start Date:2018-06-20
ZRPA (MSCI Europe (EUREX) ) Individual Contracts : First Contract:ZRPAZ18 -> Last Contract:ZRPAZ24
ZS (Soybean Futures (CBOT) ) Continuous Futures : Start Date:2008-02-19
ZS (Soybean Futures (CBOT) ) Individual Contracts : First Contract:ZSZ08 -> Last Contract:ZSZ24
ZT (2-Year Treasury Note Futures (CBOT) ) Continuous Futures : Start Date:2008-01-01
ZT (2-Year Treasury Note Futures (CBOT) ) Individual Contracts : First Contract:ZTZ08 -> Last Contract:ZTZ24
ZTWA (MSCI Emerging Markets Asia (EUREX) ) Continuous Futures : Start Date:2014-01-07
ZTWA (MSCI Emerging Markets Asia (EUREX) ) Individual Contracts : First Contract:ZTWAZ14 -> Last Contract:ZTWAZ24
ZW (Wheat Futures (CBOT) ) Continuous Futures : Start Date:2008-01-01
ZW (Wheat Futures (CBOT) ) Individual Contracts : First Contract:ZWZ08 -> Last Contract:ZWZ24






Stock Tickers
---------------
A (Agilent Technologies Inc) Start Date:2005-01-03
AA (Alcoa Corporation) Start Date:2016-10-18
AACG (Ata Creativity Global American Depositary Shares) Start Date:2008-01-29
AACT (Ares Acquisition Ii) Start Date:2023-06-12
AADI (Aadi Bioscience) Start Date:2017-08-08
AAIC (Arlington Asset Investment Class A) Start Date:2009-06-10
AAL (American Airlines) Start Date:2013-12-09
AAMC (Altisource Asset Management Com) Start Date:2012-12-13
AAME (Atlantic American) Start Date:2007-05-16
AAN (Aaron's) Start Date:2020-12-01
AAOI (Applied Optoelectronics) Start Date:2013-09-26
AAON (Aaon) Start Date:2007-05-16
AAP (Advance Auto Parts) Start Date:2005-01-03
AAPL (Apple) Start Date:2005-01-03
AAT (American Assets Trust) Start Date:2011-01-13
AAU (Almaden Minerals Common Shares) Start Date:2007-05-16
AB (Alliancebernstein Holding L.P.) Start Date:2007-01-03
ABBNY (Abb Ltd.) Start Date:2007-05-01
ABBV (Abbvie) Start Date:2013-01-02
ABCB (Ameris Bancorp) Start Date:2007-05-16
ABCL (Abcellera Biologics) Start Date:2020-12-11
ABCM (Abcam Plc) Start Date:2020-11-02
ABEO (Abeona Therapeutics) Start Date:2007-05-16
ABEV (Ambev S.A. American Depositary Shares) Start Date:2013-11-11
ABG (Asbury Automotive) Start Date:2007-05-01
ABIO (Arca Biopharma) Start Date:2009-01-28
ABLV (Able View Global Inc) Start Date:2022-09-12
ABM (Abm Industries Incorporated) Start Date:2007-01-03
ABNB (Airbnb) Start Date:2020-12-10
ABOS (Acumen Pharmaceuticals) Start Date:2021-07-01
ABR (Arbor Realty Trust) Start Date:2007-05-02
ABSI (Absci) Start Date:2021-07-22
ABT (Abbott Laboratories) Start Date:2005-01-03
ABTS (Abits Inc) Start Date:2014-04-10
ABUS (Arbutus Biopharma) Start Date:2010-11-15
ABVC (Abvc Biopharma) Start Date:2021-08-03
AC (Associated Capital) Start Date:2015-11-09
ACA (Arcosa) Start Date:2018-10-30
ACAC (Acri Capital Acquisition Corporation) Start Date:2022-08-08
ACAD (Acadia Pharmaceuticals) Start Date:2007-01-03
ACAX (Alset Capital Acquisition) Start Date:2022-03-24
ACB (Aurora Cannabis Common Shares) Start Date:2018-10-23
ACCD (Accolade) Start Date:2020-07-02
ACCO (Acco Brands) Start Date:2007-05-02
ACDC (Profrac Holding) Start Date:2022-05-13
ACEL (Accel Entertainment) Start Date:2017-08-24
ACER (Acer Therapeutics) Start Date:2007-05-16
ACET (Adicet Bio) Start Date:2018-01-26
ACGL (Arch Capital Ltd.) Start Date:2007-01-03
ACGN (Aceragen Inc) Start Date:2007-12-10
ACHC (Acadia Healthcare Company) Start Date:2012-01-11
ACHL (Achilles Therapeutics Plc) Start Date:2021-03-31
ACHR (Archer Aviation) Start Date:2020-12-18
ACHV (Achieve Life Sciences Common Shares) Start Date:2008-08-22
ACI (Albertsons Companies) Start Date:2020-06-26
ACIC (American Coastal Insurance Corp) Start Date:2008-10-28
ACIU (Ac Immune Sa) Start Date:2016-09-23
ACIW (Aci Worldwide) Start Date:2007-07-25
ACLS (Axcelis Technologies) Start Date:2007-05-01
ACLX (Arcellx) Start Date:2022-02-04
ACM (Aecom) Start Date:2007-05-10
ACMR (Acm Research, Class A) Start Date:2017-11-03
ACN (Accenture Plc) Start Date:2009-09-01
ACNB (Acnb) Start Date:2007-05-16
ACNT (Ascent Industries) Start Date:2007-05-16
ACON (Aclarion) Start Date:2022-04-22
ACONW (Aclarion Warrant) Start Date:2022-04-22
ACOR (Acorda Therapeutics) Start Date:2007-04-25
ACP (Aberdeen Income Credit Strategies Fund Common Shares) Start Date:2011-01-27
ACQRU (Independence Holdings Units) Start Date:2021-03-09
ACQRW (Independence Holdings Warrant) Start Date:2021-05-17
ACR (Acres Commercial Realty) Start Date:2021-02-17
ACRE (Ares Commercial Real) Start Date:2012-04-26
ACRS (Aclaris Therapeutics,) Start Date:2015-10-07
ACRV (Acrivon Therapeutics) Start Date:2022-11-15
ACRX (Acelrx Pharmaceuticals) Start Date:2011-02-11
ACST (Acasti Pharma Class A) Start Date:2013-01-07
ACTG (Acacia Research) Start Date:2007-05-03
ACU (Acme United Corporation.) Start Date:2007-05-16
ACV (Alberto-Culver Co.) Start Date:2015-05-22
ACVA (Acv Auctions) Start Date:2021-03-24
ACXP (Acurx Pharmaceuticals) Start Date:2021-06-25
ADAG (Adagene) Start Date:2021-02-09
ADAP (Adaptimmune Therapeutics Plc American Depositary Shares) Start Date:2015-05-06
ADBE (Adobe Systems Inc) Start Date:2005-01-03
ADC (Agree Realty Corporation) Start Date:2007-01-03
ADD (Color Star Technology) Start Date:2008-06-16
ADEA (Adeia) Start Date:2007-04-26
ADES (Advanced Emissions Solutions) Start Date:2007-05-16
ADI (Analog Devices) Start Date:2005-01-03
ADIL (Adial Pharmaceuticals Inc) Start Date:2018-07-27
ADILW (Adial Pharmaceuticals Inc Warrant) Start Date:2018-07-27
ADM (Archer-Daniels-Midland Co) Start Date:2005-01-03
ADMA (Adma Biologics Cmn) Start Date:2013-10-17
ADN (Advent Technologies Holdings Class A) Start Date:2018-11-16
ADNT (Adient) Start Date:2016-10-17
ADNWW (Advent Technologies Holdings Warrant) Start Date:2019-01-24
ADP (Automatic Data Processing) Start Date:2005-01-03
ADPT (Adaptive Biotechnologies Corporation) Start Date:2019-06-27
ADRT (Ault Disruptive Technologies) Start Date:2022-02-09
ADSE (ADS-Tec Energy Plc Ordinary Shares) Start Date:2021-12-23
ADSEW (ADS-Tec Energy Plc Warrant) Start Date:2021-12-23
ADSK (Autodesk) Start Date:2005-01-03
ADT (Adt) Start Date:2018-01-19
ADTH (Adtheorent Holding Company) Start Date:2021-12-23
ADTHW (Adtheorent Holding Company Warrants) Start Date:2021-04-20
ADTN (Adtran) Start Date:2007-04-30
ADTX (Aditx Therapeutics) Start Date:2020-06-30
ADUS (Addus Homecare) Start Date:2009-10-28
ADV (Advantage Solutions Class A) Start Date:2019-09-09
ADVM (Adverum Biotechnologies) Start Date:2014-07-31
ADVWW (Advantage Solutions Warrant) Start Date:2016-09-15
ADX (Adams Diversified Equity Fund) Start Date:2007-05-08
ADXN (Addex Therapeutics American Depositary Shares) Start Date:2020-01-29
AE (Adams Resources) Start Date:2007-05-16
AEE (Ameren Corp) Start Date:2005-01-03
AEF (Aberdeen Emerging Markets Equity Income Fund) Start Date:2007-10-02
AEG (Aegon N.V.) Start Date:2007-01-03
AEHL (Antelope Enterprise Holdings) Start Date:2010-01-25
AEHR (Aehr Test Systems) Start Date:2007-05-16
AEI (Alset Ehome International) Start Date:2020-11-24
AEIS (Advanced Energy Inds) Start Date:2007-04-30
AEL (American Equity Investment Life Holding Company) Start Date:2007-01-03
AEM (Agnico Eagle Mines Limited) Start Date:2007-01-03
AEMD (Aethlon Medical) Start Date:2007-05-16
AENT (Bldrs Asia 50 ADR Index Fund) Start Date:2021-03-24
AENZ (Aenza S.A.A. American Depositary Shares) Start Date:2018-07-06
AEO (American Eagle Outfitters) Start Date:2007-03-08
AEP (American Electric Power) Start Date:2005-01-03
AEPPZ (American Electric Power Company Corporate Units) Start Date:2020-10-01
AER (Aercap Holdings N.V.) Start Date:2007-01-03
AES (Aes Corp) Start Date:2005-01-03
AESC (The Aes Corporate Units) Start Date:2021-03-15
AESE (Allied Esports Entertainment) Start Date:2017-10-25
AESI (Atlas Energy Solutions) Start Date:2023-03-09
AEVA (Aeva Technologies,) Start Date:2020-02-27
AEY (Addvantage Technologies) Start Date:2007-05-16
AEYE (Audioeye) Start Date:2018-09-04
AEZS (Aeterna Zentaris) Start Date:2007-05-17
AFAR (Aura Fat Projects Acquisition Corp) Start Date:2022-06-03
AFB (Alliancebernstein National Municipal Income Fund Inc) Start Date:2007-05-16
AFBI (Affinity Bancshares) Start Date:2020-07-23
AFCG (Afc Gamma) Start Date:2021-03-19
AFG (American Financial) Start Date:2007-01-03
AFGE (American Financial  4.500% Subordinated Debentures Due 2060) Start Date:2020-09-18
AFIB (Acutus Medical) Start Date:2020-08-06
AFL (Aflac Inc) Start Date:2005-01-03
AFMD (Affimed N.V.) Start Date:2014-09-12
AFRI (Forafric Global Plc Ordinary Shares) Start Date:2022-06-10
AFRIW (Forafric Global Plc Warrants) Start Date:2022-06-10
AFRM (Affirm) Start Date:2021-01-13
AFT (Apollo Senior Floating Rate Fund) Start Date:2011-02-24
AFYA (Afya Limited) Start Date:2019-07-19
AG (First Majestic Silver) Start Date:2010-12-15
AGAE (Allied Gaming & Entertainment) Start Date:2017-10-25
AGBA (Agba Holding) Start Date:2019-07-30
AGCO (Agco Corporation) Start Date:2009-05-04
AGD (Aberdeen Global Dynamic Dividend Fund) Start Date:2007-05-02
AGE (Agex Therapeutics) Start Date:2018-11-29
AGEN (Agenus) Start Date:2007-05-09
AGFY (Agrify) Start Date:2021-01-28
AGGRU (Agile Growth Units) Start Date:2021-03-10
AGGRW (Agile Growth Warrant.) Start Date:2021-05-05
AGI (Alamos Gold) Start Date:2015-07-06
AGIL (Agilethought Class A) Start Date:2020-01-14
AGILW (Agilethought Warrant) Start Date:2020-01-14
AGIO (Agios Pharmaceuticals) Start Date:2013-07-24
AGL (Agilon Health) Start Date:2021-04-15
AGM (Federal Agricultural Mortgage) Start Date:2007-05-04
AGMH (Agm Holdings Class A Ordinary Shares) Start Date:2018-04-18
AGNC (Agnc Investment) Start Date:2008-05-15
AGNCN (Agnc Investment Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 7.00% Series C Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2017-08-28
AGNCP (Agnc Investment Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 6.125% Series F Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2020-02-04
AGO (Assured Guaranty Ltd.) Start Date:2007-01-03
AGR (Avangrid) Start Date:2015-12-17
AGRI (Agriforce Growing Systems) Start Date:2021-07-08
AGRIW (Agriforce Growing Systems Warrant) Start Date:2021-07-08
AGRO (Adecoagro S.A.) Start Date:2011-01-28
AGRX (Agile Therapeutics Commo) Start Date:2014-05-23
AGS (Playags) Start Date:2018-01-26
AGTI (Agiliti) Start Date:2021-04-23
AGX (Argan) Start Date:2007-08-22
AGYS (Agilysys) Start Date:2007-05-03
AHCO (Adapthealth Corp) Start Date:2018-05-24
AHG (Akso Health ADS) Start Date:2017-11-03
AHH (Armada Hoffler Properties) Start Date:2013-08-05
AHI (Advanced Human Imaging Limited. American Depositary Shares) Start Date:2021-11-19
AHPI (Allied Healthcare Products) Start Date:2007-05-16
AHT (Ashford Hospitality Trust Inc) Start Date:2007-05-04
AI (C3 Ai) Start Date:2020-12-09
AIF (Apollo Tactical Income Fund) Start Date:2013-02-26
AIG (American International) Start Date:2005-01-03
AIH (Aesthetic Medical International Holdings American Depositary Shares) Start Date:2019-10-25
AIHS (Senmiao Technology) Start Date:2018-03-16
AIKI (Aikido Pharma) Start Date:2009-11-16
AIM (Aim Immunotech) Start Date:2007-05-07
AIMAU (Aimfinity Investment I) Start Date:2022-04-26
AIMAW (Aimfinity Investment I Warrant) Start Date:2022-06-17
AIMD (Ainos) Start Date:2007-05-16
AIN (Albany International) Start Date:2007-01-03
AINC (Ashford) Start Date:2014-11-07
AIO (Virtus Artificial Intelligence & Technology Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2019-10-29
AIP (Arteris) Start Date:2007-05-17
AIR (Aar) Start Date:2007-05-02
AIRC (Taxable Apartment Income Reit) Start Date:2020-12-15
AIRG (Airgain) Start Date:2016-08-12
AIRI (Air Industries) Start Date:2007-07-16
AIRS (Airsculpt Technologies) Start Date:2021-10-29
AIRT (Air T) Start Date:2007-05-16
AIRTP (Air T Air T Funding Alpha Income Trust Preferred Securities) Start Date:2019-06-11
AIT (Applied Industrial Technologies) Start Date:2007-01-03
AIU (Meta Data ADS) Start Date:2022-05-02
AIV (Apartment Investment & Management) Start Date:2009-07-21
AIXI (Xiao-I Corporation) Start Date:2023-03-09
AIZ (Assurant) Start Date:2005-01-03
AJG (Arthur J. Gallagher & Co.) Start Date:2005-01-03
AJX (Great Ajax Corp) Start Date:2015-02-13
AKA (A.K.A. Brands Holding) Start Date:2021-09-22
AKAM (Akamai Technologies Inc) Start Date:2005-01-03
AKAN (Akanda Common Shares) Start Date:2022-03-15
AKBA (Akebia Therapeutics Comm) Start Date:2014-03-20
AKLI (Akili) Start Date:2021-06-30
AKO.A (Embotelladora Andina S.A.) Start Date:2007-05-16
AKO.B (Embotelladora Andina S.A.) Start Date:2007-05-16
AKR (Acadia Realty Trust) Start Date:2007-05-01
AKRO (Akero Therapeutics) Start Date:2019-06-20
AKTS (Akoustis Technologies) Start Date:2017-03-13
AKTX (Akari Therapeutics Plc ADS) Start Date:2014-01-31
AKUMQ (Akumin Inc) Start Date:2020-09-03
AKYA (Akoya Biosciences) Start Date:2021-04-16
AL (Air Lease Corporation) Start Date:2011-04-19
ALAR (Alarum Technologies) Start Date:2018-09-11
ALB (Albemarle Corp) Start Date:2005-01-03
ALBT (Avalon Globocare) Start Date:2018-03-26
ALC (Alcon) Start Date:2019-04-09
ALCE (Alternus Clean Energy Inc) Start Date:2022-04-20
ALCO (Alico) Start Date:2007-05-16
ALCY (Alchemy Investments Acquisition 1) Start Date:2023-06-26
ALDX (Aldeyra Therapeutics,) Start Date:2014-05-02
ALE (Allete) Start Date:2007-01-03
ALEC (Alector) Start Date:2019-02-07
ALEX (Alexander & Baldwin) Start Date:2012-07-02
ALFIW (Alfi Warrant) Start Date:2021-05-04
ALG (Alamo) Start Date:2007-05-16
ALGM (Allegro Microsystems) Start Date:2020-11-02
ALGN (Align Technology) Start Date:2007-05-01
ALGS (Aligos Therapeutics) Start Date:2020-10-16
ALGT (Allegiant Travel) Start Date:2007-05-16
ALHC (Alignment Healthcare) Start Date:2021-03-26
ALIM (Alimera Sciences) Start Date:2010-04-22
ALIT (Alight,) Start Date:2020-07-17
ALK (Alaska Air Inc) Start Date:2005-01-03
ALKS (Alkermes Plc) Start Date:2007-01-03
ALKT (Alkami Technology) Start Date:2021-04-14
ALL (Allstate Corp) Start Date:2005-01-03
ALLE (Allegion) Start Date:2013-11-18
ALLG (Allego N.V.) Start Date:2022-03-17
ALLK (Allakos) Start Date:2018-07-19
ALLO (Allogene Therapeutics) Start Date:2018-10-11
ALLR (Allarity Therapeutics) Start Date:2021-12-21
ALLT (Allot Ordinary Shares) Start Date:2007-04-27
ALLY (Ally Financial) Start Date:2014-04-10
ALNT (Allient Inc) Start Date:2007-05-16
ALNY (Alnylam Pharmaceuticals) Start Date:2007-01-03
ALOT (Astronova) Start Date:2007-05-16
ALPN (Alpine Immune Sciences) Start Date:2015-06-17
ALPP (Alpine 4 Holdings Class A) Start Date:2017-01-13
ALPS (Alpine Summit Energy Partners Class A Subordinate) Start Date:2022-09-28
ALRM (Alarm.com Holdings) Start Date:2015-06-26
ALRN (Aileron Therapeutics) Start Date:2017-06-29
ALRS (Alerus Finl Corp) Start Date:2007-05-17
ALSN (Allison Transmission Holdings) Start Date:2012-03-15
ALTG (Alta Equipment) Start Date:2019-04-25
ALTI (Alvarium Tiedemann Holdings Class A) Start Date:2021-04-27
ALTO (Alto Ingredients,) Start Date:2007-04-25
ALTR (Altair Engineering) Start Date:2017-11-01
ALV (Autoliv) Start Date:2007-01-03
ALVO (Alvotech Ordinary Shares) Start Date:2022-06-16
ALVOW (Alvotech Warrant) Start Date:2022-06-16
ALVR (Allovir) Start Date:2020-07-30
ALX (Alexander's) Start Date:2007-05-16
ALXO (Alx Oncology Holdings) Start Date:2020-07-17
ALYA (Alithya  Class A Subordinate Voting Shares) Start Date:2018-11-01
ALZN (Alzamend Neuro) Start Date:2021-06-15
AM (Antero Midstream Corporation) Start Date:2017-05-04
AMAL (Amalgamated Bank) Start Date:2018-08-09
AMAM (Ambrx Biopharma) Start Date:2021-06-18
AMAT (Applied Materials) Start Date:2005-01-03
AMBA (Ambarella) Start Date:2012-10-10
AMBC (Ambac Financial) Start Date:2013-05-01
AMBI (Ambipar Emergency Response) Start Date:2020-09-09
AMBO (Ambow Education Holding ADS Each Representing Two Class A Ordinary Shares) Start Date:2018-06-01
AMBP (Ardagh Metal Packaging S.A. Ordinary Shares) Start Date:2020-09-29
AMC (Amc Entertainment) Start Date:2013-12-18
AMCR (Amcor Plc) Start Date:2019-06-11
AMCX (Amc Networks) Start Date:2011-06-16
AMD (Advanced Micro Devices Inc) Start Date:2005-01-03
AME (Ametek) Start Date:2005-01-03
AMED (Amedisys) Start Date:2007-01-03
AMEH (Apollo Medical) Start Date:2015-06-03
AMG (Affiliated Managers Inc) Start Date:2005-01-03
AMGN (Amgen) Start Date:2005-01-03
AMH (American Homes 4 Rent) Start Date:2013-08-01
AMK (Assetmark Financial) Start Date:2019-07-18
AMKR (Amkor Technology) Start Date:2007-01-03
AMLI (American Lithium) Start Date:2023-01-10
AMLX (Amylyx Pharmaceuticals,) Start Date:2022-01-07
AMN (Amn Healthcare Services) Start Date:2007-06-04
AMNB (American National) Start Date:2007-05-16
AMP (Ameriprise Financial) Start Date:2005-10-03
AMPE (Ampio Pharmaceuticals) Start Date:2011-05-19
AMPG (Amplitech) Start Date:2021-02-17
AMPH (Amphastar Pharmaceuticals) Start Date:2014-06-25
AMPL (Amplitude, Class A) Start Date:2021-09-28
AMPS (Altus Power Class A) Start Date:2021-02-01
AMPX (Amprius Technologies) Start Date:2022-09-15
AMPY (Amplify Energy) Start Date:2017-05-19
AMR (Alpha Metallurgical Resources,) Start Date:2016-08-18
AMRC (Ameresco) Start Date:2010-07-22
AMRK (A-Mark Precious Metals C) Start Date:2014-03-17
AMRN (Amarin Plc) Start Date:2008-02-19
AMRS (Amyris) Start Date:2010-09-28
AMRX (Amneal Pharmaceuticals) Start Date:2018-05-07
AMS (American Shared Hospital Services) Start Date:2007-05-16
AMSC (American Superconductor Corpor) Start Date:2007-04-30
AMSF (Amerisafe) Start Date:2007-05-08
AMST (Amesite) Start Date:2020-09-25
AMSWA (American Software) Start Date:2007-05-09
AMT (American Tower) Start Date:2012-01-03
AMTB (Amerant Bancorp) Start Date:2018-08-29
AMTD (Amtd Idea American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2022-01-31
AMTI (Applied Molecular Transport) Start Date:2020-06-05
AMTX (Aemetis) Start Date:2007-12-11
AMWD (American Woodmark) Start Date:2007-04-20
AMWL (Amwell Health) Start Date:2020-09-17
AMX (America Movil S.A.B. De C.V. American Depository Receipt Series L) Start Date:2007-04-30
AMZN (Amazon.com) Start Date:2005-01-03
AN (Autonation) Start Date:2005-01-03
ANAB (Anaptysbio) Start Date:2017-01-26
ANDE (Andersons) Start Date:2007-05-02
ANEB (Anebulo Pharmaceuticals) Start Date:2021-05-07
ANET (Arista Networks) Start Date:2014-06-06
ANF (Abercrombie & Fitch Company) Start Date:2005-01-03
ANGH (Anghami Ordinary Shares) Start Date:2022-02-04
ANGHW (Anghami Warrants) Start Date:2022-02-04
ANGI (Angi Homeservices) Start Date:2017-10-02
ANGO (Angiodynamics) Start Date:2007-05-07
ANIK (Anika Therapeutics) Start Date:2007-04-27
ANIP (Ani Pharmaceuticals) Start Date:2007-11-05
ANIX (Anixa Biosciences) Start Date:2007-05-16
ANL (Adlai Nortye Ltd.) Start Date:2023-09-29
ANNX (Annexon Biosciences) Start Date:2020-07-24
ANSS (Ansys) Start Date:2005-01-03
ANTE (Airnet Technology American Depositary Shares) Start Date:2007-11-07
ANTX (An2 Therapeutics) Start Date:2022-03-25
ANVS (Annovis Bio) Start Date:2020-01-29
ANY (Sphere 3D Common Shares) Start Date:2014-07-07
AOD (Aberdeen Total Dynamic Dividend Fund) Start Date:2007-05-16
AOMR (Angel Oak Mortgage) Start Date:2021-06-17
AON (Aon Plc) Start Date:2007-04-30
AONC (American Oncology Network Inc) Start Date:2021-05-05
AORT (Artivion) Start Date:2007-05-10
AOS (A.O. Smith Corp) Start Date:2007-04-02
AOSL (Alpha & Omega) Start Date:2010-04-29
AOUT (American Outdoor Brands) Start Date:2020-08-21
AP (Ampco-Pittsburgh) Start Date:2007-05-09
APA (Apache Corporation) Start Date:2005-01-03
APAM (Artisan Partners Asset Management) Start Date:2013-03-07
APCX (Apptech Payments) Start Date:2017-05-08
APCXW (Apptech Payments Warrant) Start Date:2022-01-05
APD (Air Products & Chemicals Inc) Start Date:2005-01-03
APDN (Applied Dna Sciences) Start Date:2007-05-16
APE (Amc Entertainment Holdings Amc Preferred Equity Units) Start Date:2022-08-22
APEI (American Public Education) Start Date:2007-11-09
APGB (Apollo Strategic Growth Capital Ii Class A Ordinary Shares) Start Date:2021-04-05
APGE (Apogee Therapeutics) Start Date:2023-07-14
APH (Amphenol Corp) Start Date:2005-01-03
API (Agora) Start Date:2020-06-26
APLD (Applied Blockchain) Start Date:2009-12-10
APLE (Apple Hospitality Reit) Start Date:2015-05-18
APLS (Apellis Pharmaceuticals) Start Date:2017-11-09
APLT (Applied Therapeutics) Start Date:2019-05-14
APM (Aptorum Class A Ordinary Shares) Start Date:2018-12-18
APO (Apollo Global Management) Start Date:2011-03-30
APOG (Apogee Enterprises) Start Date:2007-05-08
APP (Applovin) Start Date:2021-04-15
APPF (Appfolio) Start Date:2015-06-26
APPH (Appharvest,) Start Date:2020-06-12
APPHW (Appharvest Warrants) Start Date:2020-06-16
APPN (Appian Corporation) Start Date:2017-05-25
APPS (Digital Turbine) Start Date:2007-11-26
APRE (Aprea Therapeutics) Start Date:2019-10-03
APRN (Blue Apron Holdings Class A) Start Date:2017-06-29
APT (Alpha Pro Tech) Start Date:2007-05-16
APTM (Alpha Partners Technology Merger Class A Ordinary Shares) Start Date:2021-09-23
APTMU (Alpha Partners Technology Merger Unit) Start Date:2021-07-28
APTMW (Alpha Partners Technology Merger Warrant) Start Date:2021-09-27
APTO (Aptose Biosciences Common Shares) Start Date:2008-10-31
APTV (Aptiv Plc) Start Date:2011-11-17
APVO (Aptevo Therapeutics) Start Date:2016-07-20
APWC (Asia Pacific Wire & Cable Ordinary Shares) Start Date:2011-04-29
APYX (Apyx Medical Corp) Start Date:2007-05-16
AQB (Aquabounty Technologies) Start Date:2017-01-11
AQMS (Aqua Metals) Start Date:2015-07-31
AQN (Algonquin Power & Utilities) Start Date:2016-11-29
AQNU (Algonquin Power & Utilities Corporate Units) Start Date:2021-06-29
AQST (Aquestive Therapeutics) Start Date:2018-07-25
AQU (Aquaron Acquisition) Start Date:2022-10-19
AR (Antero Resources Corp) Start Date:2013-10-10
ARAV (Aravive) Start Date:2014-03-21
ARAY (Accuray) Start Date:2007-05-16
ARBB (Arb Iot Limited) Start Date:2023-04-05
ARBE (Arbe Robotics Ordinary Shares) Start Date:2021-10-08
ARBEW (Arbe Robotics Warrant) Start Date:2021-10-08
ARBK (Argo Blockchain Plc American Depositary Shares) Start Date:2021-09-23
ARC (Arc Document Solutions) Start Date:2007-05-03
ARCB (Arcbest O) Start Date:2007-04-27
ARCC (Ares Capital Corporation) Start Date:2012-10-08
ARCE (Arco Platform Limited) Start Date:2018-09-26
ARCH (Arch Resources) Start Date:2016-10-05
ARCKU (Arbor Rapha Capital Bioholdings I Units) Start Date:2021-10-29
ARCKW (Arbor Rapha Capital Bioholdings I Warrants) Start Date:2021-12-20
ARCO (Arcos Dorados Holdings) Start Date:2011-04-14
ARCT (Arcturus Therapeutics) Start Date:2013-05-22
ARDC (Ares Dynamic Credit Allocation Fund Common Shares) Start Date:2012-11-28
ARDX (Ardelyx) Start Date:2014-06-19
ARE (Alexandria Real Estate Equities) Start Date:2005-01-03
AREB (American Rebel Holdings) Start Date:2018-01-23
AREBW (American Rebel Holdings Warrants) Start Date:2022-02-07
AREC (American Resources Class A) Start Date:2015-11-25
AREN (The Arena Holdings) Start Date:2022-02-09
ARES (Ares Management Corporation) Start Date:2014-05-02
ARGO (Argo International) Start Date:2018-03-14
ARGUW (Argus Capital Warrant) Start Date:2021-11-12
ARGX (Argenx Se) Start Date:2017-05-18
ARHS (Arhaus) Start Date:2021-11-04
ARI (Apollo Commercial) Start Date:2009-09-24
ARIS (Aris Water Solutions Class A) Start Date:2021-10-22
ARKO (Arko) Start Date:2020-12-23
ARKOW (Arko Warrant) Start Date:2020-12-23
ARKR (ARKRestaurants) Start Date:2007-05-16
ARL (American Realty Investors) Start Date:2007-05-16
ARLO (Arlo Technologies) Start Date:2018-08-03
ARLP (Alliance Resource Partners Lp) Start Date:2007-04-26
ARM (Arm Holdings Limited) Start Date:2023-09-14
ARMK (Aramark) Start Date:2013-12-12
ARMP (Armata Pharmaceuticals) Start Date:2015-08-21
AROC (Archrock) Start Date:2007-08-21
AROW (Arrow Financial) Start Date:2007-05-02
ARQQ (Arqit Quantum Ordinary Shares) Start Date:2021-09-07
ARQQW (Arqit Quantum Warrants) Start Date:2021-09-07
ARQT (Arcutis Biotherapeutics) Start Date:2020-01-31
ARR (Armour Residential Reit) Start Date:2009-11-10
ARRY (Array Technologies) Start Date:2020-10-15
ARTE (Artemis Strategic Investment Class A) Start Date:2021-11-23
ARTEU (Artemis Strategic Investment Unit) Start Date:2021-09-30
ARTEW (Artemis Strategic Investment Warrant) Start Date:2021-11-22
ARTL (Artelo Biosciences) Start Date:2017-11-14
ARTLW (Artelo Biosciences Warrant) Start Date:2019-06-21
ARTNA (Artesian Resource) Start Date:2007-05-16
ARTW (Art's-Way Manufacturing Co.) Start Date:2007-05-16
ARVL (Arrival Ordinary Shares) Start Date:2021-03-25
ARVN (Arvinas) Start Date:2018-09-27
ARW (Arrow Electronics) Start Date:2007-01-03
ARWR (Arrowhead Pharmaceuticals) Start Date:2007-05-16
ASA (Asa Gold And Precious Metals Limited) Start Date:2007-05-01
ASAI (Sendas Distribuidora S A ADS) Start Date:2021-03-08
ASAN (Asana) Start Date:2020-09-30
ASB (Associated Banc-Corp) Start Date:2014-12-23
ASC (Ardmore Shipping Corp) Start Date:2013-08-01
ASCA (A SPAC I Acquisition) Start Date:2022-03-18
ASCB (A SPAC Ii Acquisition Corporation) Start Date:2022-05-31
ASG (Liberty All-Star Growth Fund) Start Date:2007-05-16
ASGI (Aberdeen Standard Global Infrastructure Income Fund Common Shares Of Beneficial Interest) Start Date:2020-07-29
ASGN (Asgn Incorporated) Start Date:2012-08-31
ASH (Ashland Global Holdings) Start Date:2005-01-03
ASIX (Advansix) Start Date:2016-09-15
ASLE (Aersale) Start Date:2020-12-15
ASLN (Aslan Pharmaceuticals American Depositary Shares) Start Date:2018-05-04
ASM (Avino Silver & Gold Mines Common Shares) Start Date:2018-01-08
ASMB (Assembly Biosciences Com) Start Date:2010-12-17
ASML (Asml Holding) Start Date:2007-04-30
ASND (Ascendis Pharma A/S American Depositary Shares) Start Date:2015-01-28
ASNS (Actelis Networks) Start Date:2022-05-13
ASO (Amsouth Ban) Start Date:2020-10-02
ASPI (Asp Isotopes) Start Date:2022-11-10
ASPN (Aspen Aerogels) Start Date:2014-06-13
ASPS (Altisource Portfolio) Start Date:2009-08-10
ASR (Grupo Aeroportuario Del Sureste S.A. De C.V.) Start Date:2007-05-02
ASRT (Assertio Holdings) Start Date:2007-04-26
ASRV (Ameriserv Financial) Start Date:2007-05-16
ASST (Asset Entities) Start Date:2023-02-03
ASTC (Astrotech Corporation) Start Date:2009-05-04
ASTE (Astec Industries) Start Date:2007-05-03
ASTI (Ascent Solar Technologies) Start Date:2007-05-16
ASTL (Algoma Steel  Common Shares) Start Date:2021-10-20
ASTLW (Algoma Steel  Warrant) Start Date:2021-10-20
ASTR (Astra Space, Class A) Start Date:2021-06-28
ASTS (Ast Spacemobile, Class A) Start Date:2019-11-01
ASTSW (Ast Spacemobile Warrant) Start Date:2019-11-01
ASUR (Asure Software) Start Date:2010-01-21
ASX (Ase Technology Holding Co. Ltd.) Start Date:2018-05-01
ASXC (Asensus Surgical) Start Date:2021-03-05
ASYS (Amtech Systems) Start Date:2007-05-16
ATAI (Atai Life Sciences) Start Date:2021-06-18
ATAK (Aurora Technology Acquisition) Start Date:2022-03-21
ATAT (Atour Lifestyle Holdings) Start Date:2022-11-11
ATAX (America First Multifamily Investors L.P. Beneficial Unit Certificates) Start Date:2008-07-01
ATEC (Alphatec) Start Date:2007-05-16
ATEN (A10 Networks) Start Date:2014-03-21
ATER (Aterian) Start Date:2019-06-12
ATEX (Anterix) Start Date:2015-02-03
ATGE (Devry) Start Date:2007-05-01
ATGL (Alpha Technology Limited) Start Date:2023-10-31
ATHA (Athira Pharma) Start Date:2020-09-18
ATHE (Alterity Therapeutics American Depositary Shares) Start Date:2019-04-09
ATHM (Autohome) Start Date:2013-12-11
ATHX (Athersys) Start Date:2007-12-12
ATI (Allegheny Technologies Incorporated) Start Date:2005-01-03
ATIF (Atif Holdings Ordinary Shares) Start Date:2019-05-03
ATIP (Ati Physical Therapy,) Start Date:2020-10-02
ATKR (Atkore Intl) Start Date:2016-06-10
ATLC (Atlanticus) Start Date:2007-04-27
ATLO (Ames National) Start Date:2007-05-16
ATLX (Atlas Lithium) Start Date:2023-01-10
ATMC (Alphatime Acquisition Corp) Start Date:2023-01-19
ATMU (Atmus Filtration Technologies) Start Date:2023-05-26
ATMV (Alphavest Acquisition Corp) Start Date:2023-01-25
ATNF (180 Life Sciences) Start Date:2020-06-08
ATNFW (180 Life Sciences Warrant) Start Date:2017-06-27
ATNI (Atn International) Start Date:2007-05-04
ATNM (Actinium Pharmaceuticals) Start Date:2014-03-26
ATNX (Athenex) Start Date:2017-06-14
ATO (Atmos Energy Corp) Start Date:2005-01-03
ATOM (Atomera) Start Date:2016-08-05
ATOS (Atossa Therapeutics,) Start Date:2012-11-08
ATR (Aptargroup) Start Date:2007-05-02
ATRA (Atara Biotherapeutics) Start Date:2014-10-16
ATRC (Atricure) Start Date:2007-05-16
ATRI (Atrion) Start Date:2007-05-16
ATRO (Astronics) Start Date:2007-05-16
ATS (Ats Corporation) Start Date:2023-05-25
ATSG (Air Transport Srvcs) Start Date:2008-05-16
ATTO (Atento S.A. Ordinary Shares) Start Date:2014-10-02
ATUS (Altice Usa) Start Date:2017-06-22
ATVI (Activision Blizzard) Start Date:2007-04-30
ATXG (Addentax) Start Date:2016-12-12
ATXI (Avenue Therapeutics) Start Date:2017-06-27
ATXS (Astria Therapeutics) Start Date:2015-06-25
AU (Anglogold Ashanti Limited) Start Date:2007-01-03
AUB (Atlantic Union Bankshares Corp) Start Date:2014-11-28
AUBN (Auburn National Bancorp) Start Date:2007-05-16
AUDC (Audiocodes Ltd) Start Date:2007-05-01
AUGX (Augmedix) Start Date:2021-03-31
AUID (Ipsidy) Start Date:2021-07-19
AULT (Ault Alliance) Start Date:2008-03-12
AUMN (Golden Minerals Company) Start Date:2007-07-16
AUPH (Aurinia Pharmaceuticals Inc) Start Date:2013-11-08
AUR (Aurora Innovation, Class A) Start Date:2021-05-10
AURA (Aura Biosciences) Start Date:2021-10-29
AUROW (Aurora Innovation Warrant) Start Date:2021-11-04
AUST (Austin Gold Common Shares) Start Date:2022-05-04
AUTL (Autolus Therapeutics Plc American Depositary Share) Start Date:2018-06-22
AUUD (Auddia) Start Date:2021-02-17
AUUDW (Auddia Warrants) Start Date:2021-02-17
AUVI (Applied Uv) Start Date:2020-08-31
AVA (Avista Corporation) Start Date:2007-01-03
AVAH (Aveanna Healthcare Holdings) Start Date:2021-04-29
AVAL (Grupo Aval Acciones Y Valores S.A.) Start Date:2014-09-23
AVAV (Aerovironment) Start Date:2007-05-16
AVB (Avalonbay Communities) Start Date:2005-01-03
AVCO (Avalon Globocare) Start Date:2016-12-06
AVCT (American Virtual Cloud Technologies) Start Date:2017-08-08
AVCTW (American Virtual Cloud Technologies Warrant Expiring 4/7/2025) Start Date:2017-08-08
AVD (American Vanguard) Start Date:2007-05-02
AVDL (Avadel Pharmaceuticals Plc American Depositary Shares) Start Date:2007-05-04
AVDX (Avidxchange Holdings,) Start Date:2021-10-13
AVGO (Broadcom) Start Date:2016-02-01
AVGOP (Broadcom 8.00% Mandatory Convertible Preferred Stock Series A) Start Date:2019-09-25
AVGR (Avinger) Start Date:2015-01-30
AVHI (Achari Ventures Holdings I) Start Date:2021-11-17
AVID (Avid Technology) Start Date:2007-04-27
AVIR (Atea Pharmaceuticals) Start Date:2020-11-02
AVK (Advent Convertible And Income Fund) Start Date:2007-04-25
AVNS (Avanos Medical) Start Date:2014-11-03
AVNT (Avient Corporation) Start Date:2007-05-01
AVNW (Aviat Networks) Start Date:2010-01-29
AVO (Mission Produce) Start Date:2020-10-01
AVPT (Avepoint, Class A) Start Date:2021-06-28
AVPTW (Avepoint Warrant) Start Date:2019-11-05
AVRO (Avrobio) Start Date:2018-06-21
AVT (Avnet) Start Date:2007-01-03
AVTA (Avantax) Start Date:2007-04-30
AVTE (Aerovate Therapeutics) Start Date:2021-06-30
AVTR (Avantor) Start Date:2019-05-17
AVTX (Avalo Therapeutics) Start Date:2015-11-13
AVXL (Anavex Life Sciences) Start Date:2015-10-28
AVY (Avery Dennison Corp) Start Date:2005-01-03
AVYA (Avaya Corp) Start Date:2017-12-19
AWF (Alliancebernstein Global High Income Fund) Start Date:2007-05-03
AWH (Aspira Women's Health) Start Date:2010-01-27
AWI (Armstrong World Industries) Start Date:2007-01-03
AWIN (Aerwins Technologies) Start Date:2021-10-12
AWK (American Water Works Company Inc) Start Date:2008-04-23
AWP (Aberdeen Global Premier Properties Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
AWR (American States Water) Start Date:2007-05-02
AWRE (Aware) Start Date:2007-05-16
AWX (Avalon Holdings) Start Date:2007-05-16
AX (Axos Financial) Start Date:2007-05-16
AXAC (Axios Sustainable Growth Acquisition Corporation) Start Date:2022-03-25
AXDX (Accelerate Diagnostics C) Start Date:2007-05-16
AXGN (Axogen) Start Date:2007-05-16
AXL (American Axle & Mfg) Start Date:2007-05-02
AXLA (Axcella Health) Start Date:2019-05-09
AXNX (Axonics Modulation Technologies) Start Date:2018-10-31
AXON (Axon Enterprise,) Start Date:2007-05-01
AXP (American Express Co) Start Date:2005-01-03
AXR (Amrep) Start Date:2007-04-27
AXS (Axis Capital Holdings Limited) Start Date:2007-01-03
AXSM (Axsome Therapeutics) Start Date:2015-11-19
AXTA (Axalta Coating Systems Ltd.) Start Date:2014-11-12
AXTI (Axt) Start Date:2007-05-03
AY (Atlantica Sustainable Infrastructure Plc) Start Date:2014-06-13
AYI (Acuity Brands) Start Date:2005-01-03
AYRO (Ayro) Start Date:2007-05-16
AYTU (Aytu Bioscience) Start Date:2017-10-20
AYX (Alteryx) Start Date:2017-03-24
AZ (A2z Smart Technologies Common Shares) Start Date:2022-01-05
AZEK (Azek Company) Start Date:2020-06-12
AZN (Astrazeneca Plc American Depositary Shares) Start Date:2007-04-27
AZO (Autozone Inc) Start Date:2005-01-03
AZPN (Aspen Technology) Start Date:2007-05-02
AZTA (Azenta) Start Date:2007-05-02
AZTR (Azitra) Start Date:2023-06-16
AZUL (Azul S.A. American Depositary Shares) Start Date:2017-04-11
AZZ (Azz) Start Date:2007-05-09
B (Barnes) Start Date:2007-06-04
BA (Boeing Company) Start Date:2005-01-03
BABA (Alibaba Holding American Depositary Shares Each Representing Eight Ordinary Share) Start Date:2014-09-19
BAC (Bank Of America Corp) Start Date:2005-01-03
BACK (Imac Holdings) Start Date:2019-02-13
BAER (Bridger Aerospace Holdings) Start Date:2023-01-25
BAFN (Bayfirst Financial) Start Date:2021-11-30
BAH (Booz Allen Hamilton Holding Corporation) Start Date:2010-11-17
BAK (Braskem Sa ADR) Start Date:2019-10-24
BALL (Ball Corp) Start Date:2005-01-03
BALY (Bally's Corporation) Start Date:2019-03-29
BAM (Brookfield Asset Management Inc) Start Date:2007-05-01
BAMR (Bam Reinsurance) Start Date:2021-06-28
BANC (Banc Of California Commo) Start Date:2007-05-17
BAND (Bandwidth) Start Date:2017-11-10
BANF (Bancfirst) Start Date:2007-05-16
BANFP (Bancfirst - Bfc Capital Trust Ii Cumulative Trust Preferred Securities) Start Date:2007-05-16
BANL (Cbl International Limited) Start Date:2023-03-23
BANR (Banner) Start Date:2007-05-07
BANX (Arrowmark Financial) Start Date:2013-11-07
BAOS (Baosheng Media) Start Date:2021-02-08
BAP (Credicorp Ltd.) Start Date:2007-01-03
BARK (The Original Bark Company) Start Date:2020-12-18
BASE (Couchbase) Start Date:2021-07-22
BATL (Battalion Oil) Start Date:2020-02-20
BATRA (Liberty Media Series A Lbty Braves) Start Date:2016-04-18
BATRK (Liberty Media Series C Lbty Braves) Start Date:2016-04-18
BAX (Baxter International) Start Date:2005-01-03
BAYA (Bayview Acquisition Corp) Start Date:2023-12-29
BB (Blackberry Limited) Start Date:2007-04-25
BBAI (Bigbear.AI) Start Date:2021-12-08
BBAR (Banco Bbva Argentina S.A. ADS) Start Date:2007-05-16
BBBY (Bed Bath & Beyond) Start Date:2005-01-03
BBCP (Concrete Pumping) Start Date:2017-08-21
BBD (Banco Bradesco S.A.) Start Date:2007-01-03
BBDC (Barings Bdc,) Start Date:2007-05-16
BBDO (Banco Bradesco Sa American Depositary Shares) Start Date:2012-03-13
BBGI (Beasley Broadcast  Class A) Start Date:2007-05-16
BBIO (Bridgebio Pharma) Start Date:2019-06-27
BBLG (Bone Biologics) Start Date:2021-10-13
BBLGW (Bone Biologics Warrants) Start Date:2021-10-13
BBLN (Babylon Holdings Class A Ordinary Shares) Start Date:2021-10-22
BBN (Blackrock Taxable Municipal Bond Trust Common Shares Of Beneficial Interest) Start Date:2010-08-27
BBSI (Barrett Business Services) Start Date:2007-05-16
BBU (Brookfield Business Partners) Start Date:2016-06-01
BBUC (Brookfield Business Class A Exchangeable Subordinate Voting Shares) Start Date:2022-03-15
BBVA (Banco Bilbao Vizcaya Argentaria S.A.) Start Date:2009-12-14
BBW (Build-A-Bear Workshop) Start Date:2007-04-27
BBWI (Bath & Body Works,) Start Date:2007-04-27
BBY (Best Buy Co.) Start Date:2005-01-03
BC (Brunswick Corporation) Start Date:2005-01-03
BCAB (Bioatla) Start Date:2020-12-16
BCAN (Bynd Cannasoft Enterprises) Start Date:2022-05-31
BCAT (Blackrock Capital Allocation Trust) Start Date:2020-09-25
BCBP (Bcb Bancorp) Start Date:2007-05-16
BCC (Boise Cascade) Start Date:2013-02-06
BCDA (Biocardia) Start Date:2008-11-28
BCDAW (Biocardia Warrant) Start Date:2019-08-02
BCE (Bce) Start Date:2007-01-03
BCEL (Atreca) Start Date:2019-06-20
BCH (Banco De Chile Banco De Chile ADS) Start Date:2007-05-16
BCLI (Brainstorm Cell Therapeutics I) Start Date:2007-05-16
BCML (Baycom Corp) Start Date:2007-05-16
BCO (The Brink's Company) Start Date:2007-01-03
BCOR (Blucora) Start Date:2007-04-30
BCOV (Brightcove) Start Date:2012-02-17
BCOW (1895 Bancorp Of Wisconsin) Start Date:2019-01-09
BCPC (Balchem) Start Date:2007-05-16
BCRX (Biocryst Pharmaceuticals) Start Date:2007-04-30
BCS (Barclays Plc) Start Date:2007-01-03
BCSF (Bain Capital Specialty Finance) Start Date:2018-11-15
BCTX (Briacell Therapeutics Common Shares) Start Date:2021-02-24
BCTXW (Briacell Therapeutics Warrant) Start Date:2021-02-24
BCV (Bancroft Fund Ltd.) Start Date:2007-05-16
BCX (Blackrock Resources Common Shares Of Beneficial Interest) Start Date:2011-03-29
BCYC (Bicycle Therapeutics Plc American Depositary Shares) Start Date:2019-05-23
BDC (Belden) Start Date:2007-05-02
BDJ (Blackrock Enhanced Equity Dividend Trust) Start Date:2007-05-02
BDL (Flanigan's Enterprises) Start Date:2007-05-16
BDN (Brandywine Realty Trust) Start Date:2007-05-01
BDRX (Biodexa Pharmaceuticals Plc) Start Date:2015-12-07
BDSX (Biodesix Inc) Start Date:2020-11-02
BDTX (Black Diamond Therapeutics) Start Date:2020-01-30
BDX (Becton Dickinson) Start Date:2005-01-03
BE (Bloom Energy Corp) Start Date:2018-07-25
BEAM (Beam Therapeutics) Start Date:2020-02-06
BEAT (Heartbeam,) Start Date:2021-11-11
BECN (Beacon Roofing Supply) Start Date:2007-04-30
BEDU (Bright Scholar Education Holdings American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2017-05-18
BEEM (Beam Global) Start Date:2020-12-15
BEEMW (Beam Global Warrant) Start Date:2019-04-16
BEKE (Ke) Start Date:2020-08-13
BELFA (Bel Fuse Class A) Start Date:2007-05-16
BELFB (Bel Fuse) Start Date:2007-05-09
BEN (Franklin Resources) Start Date:2005-01-03
BEP (Brookfield Renewable Partners L.P.) Start Date:2007-05-16
BEPC (Brookfield Renewable Class A Subordinate Voting Shares) Start Date:2020-07-24
BERY (Berry Global) Start Date:2012-10-04
BEST (Best) Start Date:2019-02-19
BETS (Bit Brother Ltd.) Start Date:2019-02-20
BF.A (Brown-Forman) Start Date:2007-05-16
BF.B (Brown-Forman) Start Date:2005-01-03
BFAM (Bright Horizons Family Solutions) Start Date:2013-01-25
BFC (Bank First Corp) Start Date:2007-05-17
BFH (Bread Financial) Start Date:2007-04-30
BFI (Burgerfi International) Start Date:2018-03-26
BFIIW (Burgerfi International Warrant) Start Date:2018-03-26
BFIN (Bankfinancial) Start Date:2007-05-10
BFK (Blackrock Municipal Income Trust) Start Date:2007-05-16
BFLY (Butterfly Network) Start Date:2020-07-13
BFRG (Bullfrog AI Holdings) Start Date:2023-02-14
BFRI (Biofrontera) Start Date:2021-10-29
BFRIW (Biofrontera Warrants) Start Date:2021-10-29
BFS (Saul Centers) Start Date:2007-05-08
BFST (Business First Bancshares) Start Date:2018-04-11
BFX (Nautilus Inc) Start Date:2007-04-30
BFZ (Blackrock California Municipal Income Trust) Start Date:2007-05-16
BG (Bunge Limited) Start Date:2007-01-03
BGB (Blackstone Strategic Credit Fund Common Shares) Start Date:2012-09-26
BGC (Bgc Inc) Start Date:2008-04-02
BGFV (Big 5 Sporting Goods Corp) Start Date:2007-05-04
BGH (Barings Global Short Duration High Yield Fund Common Shares Of Beneficial Interests) Start Date:2012-10-26
BGI (Birks) Start Date:2007-05-16
BGNE (Beigene American Depositary Shares) Start Date:2016-02-03
BGR (Blackrock Energy And Resources Trust) Start Date:2007-05-07
BGRYW (Berkshire Grey Warrant) Start Date:2021-02-12
BGS (B&G Foods) Start Date:2007-05-23
BGSF (Bg Staffing) Start Date:2014-04-29
BGT (Blackrock Floating Rate Income Trust) Start Date:2007-05-16
BGX (Blackstone Long Short Credit Income Fund Common Shares) Start Date:2011-01-27
BGXX (Bright Green) Start Date:2022-05-17
BGY (Blackrock Enhanced International Dividend Trust) Start Date:2007-05-25
BH (Biglari) Start Date:2018-05-01
BH.A (Biglari) Start Date:2018-05-01
BHAT (Blue Hat Interactive Entertainment Technology Ordinary Shares) Start Date:2019-07-26
BHB (Bar Harbor Bankshares) Start Date:2007-05-16
BHC (Bausch Health Companies) Start Date:2007-04-27
BHE (Benchmark Electronics) Start Date:2007-04-26
BHF (Brighthouse Financial) Start Date:2017-07-17
BHFAL (Brighthouse Financial 6.25% Junior Subordinated Debentures Due 2058) Start Date:2018-09-14
BHFAP (Brighthouse Financial Depositary Shares 6.6% Non-Cumulative Preferred Stock Series A) Start Date:2019-03-26
BHG (Bright Health) Start Date:2021-06-24
BHIL (Benson Hill) Start Date:2021-09-27
BHK (Blackrock Core Bond Trust Blackrock Core Bond Trust) Start Date:2007-05-07
BHLB (Berkshire Hills Bancorp) Start Date:2007-04-25
BHM (Bluerock Homes Trust Class A) Start Date:2022-09-28
BHP (Bhp American Depositary Shares) Start Date:2007-04-30
BHR (Braemar Hotels & Resorts) Start Date:2013-11-20
BHSE (Bull Horn Holdings) Start Date:2020-12-17
BHSEW (Bull Horn Holdings Warrants) Start Date:2020-12-17
BHV (Blackrock Virginia Municipal Bond Trust) Start Date:2007-05-16
BHVN (Biohaven Pharmaceutical Holding Company Ltd.) Start Date:2017-05-04
BIAF (Bioaffinity Technologies) Start Date:2022-09-01
BIDU (Bidu) Start Date:2005-08-05
BIG (Big Lots) Start Date:2006-09-01
BIGC (Bigcommerce) Start Date:2020-08-05
BIGZ (Blackrock Innovation And Growth Trust Common Shares Of Beneficial Interest) Start Date:2021-03-26
BIIB (Biogen) Start Date:2005-01-03
BILI (Bilibili) Start Date:2018-03-28
BILL (Bill.com Holdings) Start Date:2019-12-12
BIMI (Bimi International Medical) Start Date:2010-10-04
BIO (Bio-Rad Laboratories) Start Date:2007-05-08
BIO.B (Bio-Rad Laboratories) Start Date:2007-05-16
BIOC (Biocept) Start Date:2014-02-05
BIOL (Biolase) Start Date:2007-05-07
BIOR (Biora Therapeutics) Start Date:2020-06-19
BIOX (Bioceres Crop Solutions Ordinary Shares) Start Date:2019-03-15
BIP (Brookfield Infrastructure Partners L.P.) Start Date:2008-01-31
BIPC (Brookfield Infrastructure Corporation) Start Date:2020-04-20
BIRD (Allbirds, Class A) Start Date:2021-11-03
BIRK (Birkenstock Holding Limited) Start Date:2023-10-11
BIT (Blackrock Multi-Sector Income Trust Common Shares Of Beneficial Interest) Start Date:2013-02-26
BITF (Bitfarms) Start Date:2021-06-21
BIVI (Biovie Class A) Start Date:2019-08-15
BJ (Bj's Wholesale Club Holdings) Start Date:2018-06-28
BJDX (Bluejay Diagnostics,) Start Date:2021-11-10
BJRI (Bj's Restaurants) Start Date:2007-05-08
BK (The Bank Of New York Mellon) Start Date:2007-07-02
BKCC (Blackrock Capital Investment) Start Date:2007-06-27
BKD (Brookdale Senior Living) Start Date:2007-05-04
BKE (Buckle) Start Date:2007-04-30
BKH (Black Hills Corporation) Start Date:2007-01-03
BKI (Black Knight) Start Date:2017-10-02
BKKT (Bakkt Holdings,) Start Date:2021-10-18
BKN (Blackrock Investment Quality Municipal Trust) Start Date:2007-05-16
BKNG (Booking Holdings Inc) Start Date:2007-04-30
BKR (Baker Hughes Company) Start Date:2017-07-05
BKSC (Bank Of South Carolina) Start Date:2007-05-16
BKSY (Blacksky Technology) Start Date:2019-12-20
BKT (Blackrock Income Trust) Start Date:2007-05-16
BKTI (Bk Technologies) Start Date:2007-04-26
BKU (Bankunited) Start Date:2011-01-28
BKYI (Bio-Key International) Start Date:2006-12-11
BL (Blackline) Start Date:2016-10-28
BLAC (Bellevue Life Sciences Acquisition) Start Date:2023-03-17
BLBD (Perseon Corp) Start Date:2014-03-20
BLBX (Blackboxstocks) Start Date:2016-01-22
BLCO (Bausch + Lomb Common Shares) Start Date:2022-05-06
BLD (Topbuild) Start Date:2015-06-29
BLDE (Blade Air Mobility, Class A) Start Date:2019-11-05
BLDEW (Blade Air Mobility Warrants) Start Date:2020-01-03
BLDP (Ballard Power Systems) Start Date:2007-04-30
BLDR (Builders Firstsource) Start Date:2007-01-03
BLE (Blackrock Municipal Income Trust Ii) Start Date:2007-05-16
BLEU (Bleuacacia Class A Ordinary Shares) Start Date:2022-01-10
BLEUR (Bleuacacia Rights) Start Date:2022-01-10
BLEUU (Bleuacacia Unit) Start Date:2021-11-18
BLEUW (Bleuacacia Warrants) Start Date:2022-01-10
BLFS (Biolife Solutions) Start Date:2007-05-16
BLFY (Blue Foundry Bancorp) Start Date:2021-07-16
BLIN (Bridgeline Digital) Start Date:2007-06-29
BLK (Blackrock) Start Date:2005-01-03
BLKB (Blackbaud) Start Date:2007-01-03
BLMN (Bloomin Brands) Start Date:2012-08-08
BLND (Blend Labs) Start Date:2021-07-16
BLNK (Blink Charging Co.) Start Date:2018-02-14
BLNKW (Blink Charging Co. Warrant) Start Date:2018-02-14
BLPH (Bellerophon Therapeutics) Start Date:2015-02-13
BLRX (Biolinerx American Depositary Shares) Start Date:2011-07-25
BLTE (Belite Bio Inc American Depositary Shares) Start Date:2022-04-29
BLUE (Bluebird Bio) Start Date:2013-06-19
BLW (Blackrock Duration Income Trust) Start Date:2007-05-07
BLX (Banco Latinoamericano) Start Date:2007-05-10
BLZE (Backblaze, Class A) Start Date:2021-11-11
BMA (Banco Macro S.A. ADR) Start Date:2007-05-11
BMBL (Bumble) Start Date:2021-02-11
BME (Blackrock Health Sciences Trust) Start Date:2007-05-16
BMEA (Biomea Fusion) Start Date:2021-04-16
BMEZ (Blackrock Health Sciences Trust Ii Common Shares Of Beneficial Interest) Start Date:2020-01-29
BMI (Badger Meter) Start Date:2007-05-09
BMN (Blackrock 2037 Municipal Target Term Trust Of Beneficial Interest) Start Date:2022-10-27
BMO (Bank Of Montreal) Start Date:2007-01-03
BMR (Beamr Imaging) Start Date:2023-02-28
BMRA (Biomerica) Start Date:2007-05-17
BMRC (Bank Of Marin) Start Date:2007-05-16
BMRN (Biomarin Pharmaceutical) Start Date:2009-07-21
BMTX (Bm Technologies) Start Date:2018-09-21
BMY (Bristol-Myers Squibb) Start Date:2005-01-03
BN (Brookfield Class A) Start Date:2007-05-01
BNED (Barnes & Noble Education Inc) Start Date:2015-07-23
BNGO (Bionano Genomics,) Start Date:2018-09-21
BNGOW (Bionano Genomics Warrant) Start Date:2018-09-21
BNL (Broadstone Net Lease) Start Date:2020-09-17
BNOX (Bionomics ADS) Start Date:2021-12-16
BNR (Burning Rock Biotech) Start Date:2020-06-12
BNRE (Brookfield Reinsurance Class A Exchangeable) Start Date:2022-12-14
BNRG (Brenmiller Energy Ordinary Shares) Start Date:2022-05-25
BNS (Bank Of Nova Scotia) Start Date:2007-05-08
BNSO (Bonso Electronics International) Start Date:2007-05-16
BNTC (Benitec Biopharma) Start Date:2015-08-18
BNTX (Biontech Se) Start Date:2019-10-10
BNY (Blackrock New York Municipal Income Trust) Start Date:2007-05-16
BNZI (Banzai International Inc) Start Date:2021-02-12
BOC (Boston Omaha Class A) Start Date:2017-06-16
BODY (The Beachbody Company,) Start Date:2021-06-28
BOE (Blackrock Enhanced Global Dividend Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BOF (Branchout Food) Start Date:2023-06-16
BOH (Bank Of Hawaii Corporation) Start Date:2007-01-03
BOKF (Bok Financial) Start Date:2007-05-16
BOLT (Bolt Biotherapeutics) Start Date:2021-02-05
BON (Bon Natural Life) Start Date:2009-06-16
BOOM (Dmc Global) Start Date:2007-05-01
BOOT (Boot Barn) Start Date:2014-10-30
BORR (Borr Drilling Common Shares) Start Date:2019-07-31
BOSC (B.O.S. Better Online Solutions) Start Date:2007-05-16
BOTJ (Bank Of The James Financial) Start Date:2012-01-25
BOWL (Bowlero Class A) Start Date:2021-04-23
BOWN (Bowen Acquisition Corp) Start Date:2023-08-17
BOX (Box) Start Date:2015-01-23
BOXD (Boxed) Start Date:2021-12-09
BOXL (Boxlight Class A) Start Date:2017-11-30
BP (Bp P.L.C.) Start Date:2007-04-30
BPMC (Blueprint Medicines Corporation) Start Date:2015-04-30
BPOP (Popular) Start Date:2007-01-03
BPRN (The Bank Of Princeton) Start Date:2016-07-12
BPT (Bp Prudhoe Bay Royalty Trust) Start Date:2007-04-30
BPTH (Bio-Path Holdings) Start Date:2008-03-04
BPTS (Biophytis) Start Date:2021-02-10
BPYPP (Brookfield Property Partners L.P. 6.50% Class A Cumulative Redeemable Perpetual Preferred Units) Start Date:2019-03-22
BQ (Boqii Holding) Start Date:2020-09-30
BR (Broadridge Financial Solutions) Start Date:2007-05-01
BRAG (Bragg Gaming  Common Shares) Start Date:2021-08-27
BRBR (Bellring Brands) Start Date:2019-10-17
BRBS (Blue Ridge Bankshares) Start Date:2010-08-24
BRC (Brady) Start Date:2007-04-26
BRCC (Brc) Start Date:2022-02-09
BRDG (Bridge Investment) Start Date:2021-07-16
BRDS (Bird Global Class A) Start Date:2021-03-01
BREA (Brera Holdings Plc) Start Date:2023-01-27
BRFH (Barfresh Food) Start Date:2022-01-20
BRFS (Brf S.A.) Start Date:2009-12-10
BRID (Bridgford Foods) Start Date:2007-05-16
BRIV (B. Riley Principal 250 Merger Class A) Start Date:2021-07-06
BRIVU (B. Riley Principal 250 Merger Units) Start Date:2021-05-07
BRIVW (B. Riley Principal 250 Merger Warrant) Start Date:2021-06-29
BRK.A (Berkshire Hathaway) Start Date:2007-05-16
BRK.B (Berkshire Hathaway) Start Date:2007-05-02
BRKL (Brookline Bancorp) Start Date:2007-05-01
BRKR (Bruker) Start Date:2007-05-04
BRLT (Brilliant Earth  Class A) Start Date:2021-09-23
BRN (Barnwell Industries) Start Date:2007-05-16
BRNS (Barinthus Biotherapeutics Plc) Start Date:2021-04-30
BRO (Brown & Brown) Start Date:2007-01-03
BROG (Brooge Energy Ordinary Shares) Start Date:2018-07-13
BROGW (Brooge Holdings Warrant Expiring 12/20/2024) Start Date:2018-07-13
BROS (Dutch Bros) Start Date:2021-09-15
BRP (Brp) Start Date:2019-10-24
BRQS (Borqs Technologies) Start Date:2015-11-05
BRSH (Bruush Oral Care) Start Date:2022-08-03
BRSP (Brightspire Capital Class A) Start Date:2018-02-01
BRT (Brt Apartments Corp) Start Date:2007-05-16
BRTX (Biorestorative Therapies) Start Date:2021-11-05
BRW (Saba Capital Income & Opportunities Fund Sbi) Start Date:2007-05-03
BRX (Brixmor Property) Start Date:2013-10-30
BRY (Berry Corp) Start Date:2018-07-20
BRZE (Braze) Start Date:2021-11-17
BSAC (Banco Santander-Chile) Start Date:2007-04-27
BSBK (Bogota Financial Corp) Start Date:2020-01-16
BSBR (Banco Santander) Start Date:2009-10-07
BSET (Bassett Furniture Industries Incorporated) Start Date:2007-05-16
BSFC (Blue Star Foods) Start Date:2020-04-28
BSGM (Biosig Technologies) Start Date:2018-09-21
BSIG (Brightsphere Investment) Start Date:2014-10-09
BSKYU (Big Sky Growth Partners Unit) Start Date:2021-04-29
BSKYW (Big Sky Growth Partners Warrant) Start Date:2021-06-21
BSL (Blackstone Senior Floating Rate Term Fund Common Shares Of Beneficial Interest) Start Date:2010-05-26
BSM (Black Stone Minerals, L.P.) Start Date:2015-05-01
BSQR (Bsquare) Start Date:2007-05-10
BSRR (Sierra) Start Date:2007-05-16
BST (Blackrock Science And Technology Trust Common Shares Of Beneficial Interest) Start Date:2014-10-29
BSTZ (Blackrock Science And Technology Trust Ii Common Shares Of Beneficial Interest) Start Date:2019-06-26
BSVN (Bank7) Start Date:2018-09-20
BSX (Boston Scientific) Start Date:2005-01-03
BSY (Bentley Systems Inc) Start Date:2020-09-23
BTA (Blackrock Long-Term Municipal Advantage Trust Blackrock Long-Term Municipal Advantage Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BTAI (Bioxcel Therapeutics) Start Date:2018-03-08
BTBD (Bt Brands) Start Date:2021-11-12
BTBDW (Bt Brands Warrant) Start Date:2021-11-12
BTBT (Bit Digital Ordinary Shares) Start Date:2018-03-20
BTCM (Bit Mining ADS) Start Date:2013-11-22
BTCS (Btcs) Start Date:2021-09-14
BTCT (Btc Digital Ltd.) Start Date:2018-10-17
BTCY (Biotricity) Start Date:2016-02-18
BTG (B2gold) Start Date:2008-10-29
BTI (British American Tobacco Industries P.L.C. ADR) Start Date:2007-05-11
BTM (Bitcoin Depot Inc) Start Date:2022-04-19
BTMD (Biote Class A) Start Date:2021-04-28
BTMDW (Biote Warrant) Start Date:2021-04-29
BTN (Ballantyne Strong) Start Date:2007-05-16
BTO (John Hancock Financial Opportunities Fund) Start Date:2007-05-16
BTOG (Bit Origin Ordinary Shares) Start Date:2019-08-14
BTT (Blackrock Municipal 2030 Target Term Trust) Start Date:2012-08-29
BTTR (Better Choice Company) Start Date:2021-06-29
BTTX (Better Therapeutics) Start Date:2021-10-29
BTU (Peabody Energy Corporation) Start Date:2017-04-03
BTWNU (Bridgetown Holdings Units) Start Date:2020-10-16
BTWNW (Bridgetown Holdings Warrants) Start Date:2020-12-07
BTX (Brooklyn Immunotherapeutics,) Start Date:2021-03-26
BTZ (Blackrock Credit Allocation Income Trust) Start Date:2007-05-16
BUD (Anheuser-Busch Inbev Sa) Start Date:2009-09-16
BUI (Blackrock Utility Infrastructure & Power Opportunities Trust) Start Date:2011-11-23
BUJA (Bukit Jalil Global Acquisition 1 Ltd.) Start Date:2023-08-21
BUR (Burford Capital Ordinary Shares) Start Date:2016-04-06
BURL (Burlington Stores) Start Date:2013-10-02
BURU (Nuburu) Start Date:2023-02-01
BUSE (First Busey) Start Date:2007-05-16
BV (Brightview) Start Date:2018-06-28
BVH (Bluegreen Vacations Holding Corporation) Start Date:2017-07-13
BVN (Compania De Minas Buenaventura S.A.A.) Start Date:2007-01-03
BVS (Bioventus) Start Date:2021-02-11
BW (Babcock & Wilcox Enterprises,) Start Date:2015-07-01
BWA (Borgwarner) Start Date:2005-01-03
BWAQ (Blue World Acquisition Corporation) Start Date:2022-03-16
BWAY (Brainsway American Depositary Shares) Start Date:2019-04-17
BWB (Bridgewater Bancshares) Start Date:2018-03-14
BWEN (Broadwind) Start Date:2008-03-04
BWFG (Bankwell Financial) Start Date:2014-05-15
BWG (Brandywineglobal Global Income Opportunities Fund) Start Date:2012-03-28
BWMN (Bowman Consulting) Start Date:2021-05-07
BWMX (Betterware De Mexico, S.A.B. De C.V.) Start Date:2020-03-16
BWXT (Bwx Technologies) Start Date:2010-08-02
BX (Blackstone) Start Date:2007-06-22
BXC (Bluelinx) Start Date:2007-05-03
BXMT (Blackstone Mortgage Trust) Start Date:2007-05-02
BXMX (Nuveen S&P 500 Buy-Write Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
BXP (Boston Properties) Start Date:2005-01-03
BXRX (Baudax Bio) Start Date:2019-11-14
BXSL (Blackstone Secured Lending Fund Common Shares Of Beneficial Interest) Start Date:2021-10-28
BY (Byline Bancorp) Start Date:2017-06-30
BYD (Boyd Gaming Corporation) Start Date:2007-01-03
BYFC (Broadway Financial) Start Date:2007-05-17
BYM (Blackrock Municipal Income Quality Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BYND (Beyond Meat) Start Date:2019-05-02
BYNO (Bynordic Acquisition Corporation) Start Date:2022-04-05
BYON (Beyond Inc) Start Date:2007-04-26
BYRN (Byrna Technologies) Start Date:2021-05-05
BYSI (Beyondspring) Start Date:2017-03-09
BYU (Baiyu Holdings Inc) Start Date:2015-04-22
BZ (Kanzhun) Start Date:2021-06-11
BZFD (Buzzfeed Class A) Start Date:2021-12-06
BZFDW (Buzzfeed Warrant) Start Date:2021-03-05
BZH (Beazer Homes Usa) Start Date:2007-04-27
BZUN (Baozun) Start Date:2015-05-21
C (Citigroup) Start Date:2011-05-09
C.K (Citigroup Dep Shs Repstg 1/1000Th Pfd Ser K) Start Date:2007-04-26
CAAP (Corporacion America Airports S.A.) Start Date:2018-02-01
CAAS (China Automotive Systems) Start Date:2007-04-11
CABA (Cabaletta Bio) Start Date:2019-10-25
CABO (Cable One) Start Date:2015-06-11
CAC (Camden National) Start Date:2007-05-16
CACC (Credit Acceptance) Start Date:2007-05-08
CACI (Caci International) Start Date:2009-05-04
CACO (Caravelle International) Start Date:2022-12-19
CADE (Cadence Bancorporation) Start Date:2017-04-13
CADL (Candel Therapeutics) Start Date:2021-07-27
CAE (Cae) Start Date:2009-07-02
CAF (Morgan Stanley China A Share Fund) Start Date:2007-05-08
CAG (Conagra Brands) Start Date:2005-01-03
CAH (Cardinal Health) Start Date:2005-01-03
CAKE (Cheesecake Factory) Start Date:2007-04-27
CAL (Caleres) Start Date:2007-04-30
CALA (Calithera Biosciences Co) Start Date:2014-10-02
CALB (California Bancorp) Start Date:2017-07-03
CALC (Calcimedica Inc) Start Date:2020-09-25
CALM (Cal-Maine Foods) Start Date:2007-05-10
CALT (Calliditas Therapeutics) Start Date:2020-06-05
CALX (Calix) Start Date:2010-03-24
CAMP (Calamp) Start Date:2007-04-30
CAMT (Camtek) Start Date:2007-04-24
CAN (Canaan American Depositary Shares) Start Date:2019-11-21
CANB (Can B) Start Date:2011-04-29
CANF (Can-Fite Biopharma Sponsored ADR) Start Date:2012-11-01
CANG (Cango American Depositary Shares Each Representing Two) Start Date:2018-07-26
CANO (Cano Health,) Start Date:2020-07-06
CAPD (iPath Shiller Cape ETN) Start Date:2012-10-11
CAPL (Crossamerica Partners Lp Common Units Representing Partner Interests) Start Date:2012-10-25
CAPR (Capricor Therapeutics) Start Date:2008-05-13
CAPT (Captivision Inc) Start Date:2022-04-04
CAR (Avis Budget) Start Date:2006-09-05
CARA (Cara Therapeutics Common) Start Date:2014-01-31
CARE (Carter Bankshares) Start Date:2007-05-16
CARG (Cargurus) Start Date:2017-10-12
CARM (Carisma Therapeutics Inc) Start Date:2014-02-06
CARR (Carrier Global) Start Date:2020-03-19
CARS (Cars Com) Start Date:2017-05-18
CART (Instacart) Start Date:2023-09-19
CARV (Carver Bancorp) Start Date:2007-07-10
CASA (Casa Systems) Start Date:2017-12-15
CASH (Meta Financial) Start Date:2007-05-16
CASI (Casi Pharmaceuticals) Start Date:2007-04-24
CASS (Cass Information Systems) Start Date:2007-05-16
CASY (Casey's General Stores) Start Date:2007-01-03
CAT (Caterpillar) Start Date:2005-01-03
CATC (Cambridge Bancorp) Start Date:2007-05-18
CATO (Cato) Start Date:2009-10-16
CATX (Perspective Therapeutics Inc) Start Date:2007-05-16
CATY (Cathay General Bancorp) Start Date:2007-01-03
CAUD (Collective Audience Inc) Start Date:2021-09-03
CAVA (Cava) Start Date:2023-06-15
CB (Chubb Limited) Start Date:2008-07-18
CBAN (Colony Bankcorp) Start Date:2007-05-16
CBAT (Cbak Energy Technology) Start Date:2007-05-03
CBAY (Cymabay Therapeutics Comm) Start Date:2014-01-27
CBD (Companhia Brasileira De Distribuicao) Start Date:2007-01-03
CBFV (Cb Financial Svc Cmn) Start Date:2007-05-22
CBH (Allianzgi Convertible & Income 2024 Target Term Fund) Start Date:2017-06-28
CBL (Cbl & Associates Properties) Start Date:2021-11-02
CBNK (Capital Bancorp) Start Date:2018-09-26
CBOE (Cboe Global Markets) Start Date:2010-06-15
CBRE (Cbre) Start Date:2017-01-03
CBRG (Chain Bridge I Class A Ordinary Shares) Start Date:2022-01-04
CBRGU (Chain Bridge I Units) Start Date:2021-11-10
CBRGW (Chain Bridge I Warrants) Start Date:2021-12-31
CBRL (Cracker Barrel Old Country Store) Start Date:2007-01-03
CBSH (Commerce Bancshares) Start Date:2007-05-02
CBT (Cabot Corporation) Start Date:2007-01-03
CBTX (Cbtx) Start Date:2017-11-08
CBU (Community Bank System) Start Date:2007-01-03
CBUS (Cibus Inc) Start Date:2017-07-20
CBZ (Cbiz) Start Date:2007-05-03
CC (Chemours Company) Start Date:2015-06-19
CCAP (Crescent Capital Bdc) Start Date:2020-02-03
CCB (Coastal Financial) Start Date:2018-07-18
CCBG (Capital City Bank) Start Date:2007-05-09
CCCC (C4 Therapeutics) Start Date:2020-10-02
CCCS (Ccc Intelligent Solutions Holdings) Start Date:2021-08-02
CCEL (Cryo-Cell International) Start Date:2007-05-16
CCEP (Coca-Cola European Partners Plc) Start Date:2018-11-07
CCF (Chase) Start Date:2007-05-16
CCI (Crown Castle International) Start Date:2005-01-03
CCJ (Cameco Corporation) Start Date:2007-01-03
CCK (Crown Holdings) Start Date:2005-01-03
CCL (Carnival) Start Date:2005-01-03
CCLD (Carecloud) Start Date:2014-07-23
CCLP (CSI Compressco Lp Common Units) Start Date:2011-06-15
CCM (Concord Medical Services Holdings ADS) Start Date:2009-12-11
CCNC (Code Chain New Continent) Start Date:2015-12-29
CCNE (Cnb Financial) Start Date:2007-05-16
CCO (Clear Channel Outdoor Holdings,) Start Date:2007-05-08
CCOI (Cogent Communications Holdings) Start Date:2007-01-03
CCRD (Corecard) Start Date:2007-05-18
CCRN (Cross Country Healthcare) Start Date:2007-04-27
CCS (Century Communities) Start Date:2014-06-18
CCSI (Consensus Cloud Solutions,) Start Date:2021-09-30
CCU (Compania Cervecerias Unidas S.A.) Start Date:2007-04-30
CCV (Churchill Capital V Class A) Start Date:2021-02-05
CCVI (Churchill Capital Vi Class A) Start Date:2021-04-05
CCZ (Comcast Holdings Zones) Start Date:2018-09-25
CD (Chindata) Start Date:2020-09-30
CDAK (Codiak Biosciences) Start Date:2020-10-14
CDAY (Ceridian Hcm Holding) Start Date:2018-04-26
CDE (Couer Mining) Start Date:2007-04-30
CDIO (Cardio Diagnostics Holdings) Start Date:2022-01-14
CDLX (Cardlytics) Start Date:2018-02-09
CDMO (Avid Bioservices) Start Date:2007-04-25
CDNA (Caredx) Start Date:2014-07-17
CDNS (Cadence Design Systems) Start Date:2005-10-31
CDP (Copt Defense Properties) Start Date:2007-01-03
CDRE (Cadre Holdings) Start Date:2021-11-04
CDRO (Codere Online Luxembourg S.A. Ordinary Shares) Start Date:2021-12-01
CDROW (Codere Online Luxembourg S.A. Warrants) Start Date:2021-12-01
CDT (Conduit Pharmaceuticals Inc) Start Date:2022-03-28
CDTX (Cidara Therapeutics) Start Date:2015-04-15
CDW (Cdw Corporation) Start Date:2013-06-27
CDXC (Chromadex) Start Date:2008-07-15
CDXS (Codexis) Start Date:2010-04-22
CDZI (Cadiz) Start Date:2007-05-16
CDZIP (Cadiz Depositary Shares) Start Date:2021-07-08
CE (Celanese) Start Date:2005-03-01
CEAD (Cea Industries) Start Date:2022-02-11
CEADW (Cea Industries Warrant) Start Date:2022-02-11
CECE (Ceco Environmental) Start Date:2007-05-16
CECO (Ceco Environmental) Start Date:2007-05-16
CEE (The Central And Eastern Europe Fund) Start Date:2007-05-10
CEG (Constellation Energy) Start Date:2022-01-19
CEI (Camber Energy) Start Date:2016-11-30
CEIX (Consol Energy) Start Date:2017-11-14
CELC (Celcuity) Start Date:2017-09-20
CELH (Celsius) Start Date:2010-02-10
CELL (Phenomex Inc) Start Date:2020-07-17
CELU (Celularity Class A) Start Date:2019-08-08
CELUW (Celularity Warrant) Start Date:2021-07-19
CELZ (Creative Medical Technology Holdings) Start Date:2021-12-03
CEM (Clearbridge Mlp And Midstream Fund) Start Date:2010-06-25
CEN (Center Coast Brookfield Mlp & Energy Infrastructure Fund) Start Date:2013-09-26
CENN (Cenntro Electric) Start Date:2013-02-15
CENQW (Cenaq Energy Warrant) Start Date:2021-10-04
CENT (Central Garden & Pet) Start Date:2007-04-30
CENTA (Central Garden & Pet) Start Date:2007-05-16
CENX (Century Aluminum) Start Date:2007-04-27
CEPU (Central Puerto S.A. ADS) Start Date:2018-02-02
CEQP (Crestwood Equity Partners Lp) Start Date:2010-03-24
CERE (Cerevel Therapeutics Holdings,) Start Date:2020-07-30
CERS (Cerus) Start Date:2007-05-02
CERT (Certara) Start Date:2020-12-11
CET (Central Securities) Start Date:2007-05-16
CETU (Cetus Capital Acquisition) Start Date:2023-03-24
CETX (Cemtrex) Start Date:2015-06-25
CETXP (Cemtrex Series 1 Preferred Stock) Start Date:2017-02-17
CEV (Eaton Vance California Municipal Income Trust Shares Of Beneficial Interest) Start Date:2007-05-16
CEVA (Ceva) Start Date:2007-05-16
CF (Cf Industries Holdings Inc) Start Date:2005-10-03
CFB (Crossfirst Bankshares) Start Date:2019-08-15
CFBK (Cf Bankshares) Start Date:2007-05-16
CFFI (C&F Financial) Start Date:2007-05-16
CFFN (Capitol Federal Financial) Start Date:2007-05-02
CFG (Citizens Financial) Start Date:2014-09-24
CFLT (Confluent) Start Date:2021-06-24
CFMS (Conformis) Start Date:2015-07-01
CFR (Cullen/Frost Bankers) Start Date:2007-01-03
CFRX (Contrafect Common) Start Date:2014-09-12
CFSB (Cfsb Bancorp) Start Date:2022-01-13
CG (The Carlyle) Start Date:2012-05-03
CGA (China Green Agriculture) Start Date:2009-03-09
CGAU (Centerra Gold Common Shares) Start Date:2021-04-15
CGBD (Tcg Bdc,) Start Date:2017-06-14
CGC (Canopy Growth Corporation) Start Date:2018-05-24
CGEM (Cullinan Oncology) Start Date:2021-01-08
CGEN (Compugen Ltd) Start Date:2007-05-16
CGNT (Cognyte Software) Start Date:2021-02-02
CGNX (Cognex Corporation) Start Date:2007-01-03
CGRN (Capstone Green Energy) Start Date:2007-05-02
CGTX (Cognition Therapeutics) Start Date:2021-10-08
CHAA (Catcha Investment Class A Ordinary Shares) Start Date:2021-04-05
CHCI (Comstock Holding Companies Class A) Start Date:2007-05-02
CHCO (City Holding) Start Date:2007-05-10
CHCT (Community Healthcare Trust) Start Date:2015-05-21
CHD (Church & Dwight) Start Date:2004-01-02
CHDN (Churchill Downs Incorporated) Start Date:2007-01-03
CHE (Chemed) Start Date:2007-05-08
CHEA (Chenghe Acquisition Co.) Start Date:2022-06-27
CHEF (Chefs Warehouse) Start Date:2011-07-28
CHEK (Check-Cap Ordinary Share) Start Date:2015-03-18
CHEKZ (Check-Cap Series C Warrant) Start Date:2018-05-04
CHGG (Chegg) Start Date:2013-11-13
CHH (Choice Hotels International) Start Date:2007-01-03
CHK (Chesapeake Energy Corporation) Start Date:2021-02-10
CHKEL (Chesapeake Energy Class C Warrants) Start Date:2021-02-10
CHKEW (Chesapeake Energy Class A Warrants) Start Date:2021-02-10
CHKEZ (Chesapeake Energy Class B Warrants) Start Date:2021-02-10
CHKP (Check Point Software Technologies Ltd) Start Date:2004-01-02
CHMG (Chemung Financial) Start Date:2007-05-18
CHMI (Cherry Hill Mortgage Investmen) Start Date:2013-10-04
CHN (China Fund) Start Date:2007-05-11
CHNR (China Natural Resources) Start Date:2007-05-16
CHPT (Chargepoint Holdings,) Start Date:2019-09-16
CHR (Cheer Holding Inc) Start Date:2018-09-12
CHRD (Chord Energy) Start Date:2020-11-20
CHRS (Coherus Biosciences Comm) Start Date:2014-11-06
CHRW (C. H. Robinson Worldwide) Start Date:2006-01-03
CHS (Chico's Fas) Start Date:2007-04-30
CHSCL (Chs Inc Class B Cumulative Redeemable Preferred Stock Series 4) Start Date:2015-01-22
CHSCM (Chs Inc Class B Reset Rate Cumulative Redeemable Preferred Stock Series 3) Start Date:2014-09-10
CHSCN (Chs Inc Preferred Class B Series 2 Reset Rate) Start Date:2014-03-06
CHSCO (Chs Class B Cumulative Redeemable Preferred Stock) Start Date:2013-09-23
CHSN (Chanson International Holding) Start Date:2023-03-30
CHT (Chunghwa Telecom Co. Ltd.) Start Date:2007-04-27
CHTR (Charter Communications) Start Date:2010-09-14
CHUY (Chuy's) Start Date:2012-07-24
CHWY (Chewy) Start Date:2019-06-14
CHX (Championx Holding) Start Date:2018-04-27
CI (Cigna) Start Date:2004-01-02
CIA (Citizens) Start Date:2007-05-07
CIB (Bancolombia S.A.) Start Date:2007-05-03
CIEN (Ciena Corporation) Start Date:2006-12-01
CIF (Mfs Intermediate High Income Fund) Start Date:2007-05-16
CIFR (Cipher Mining) Start Date:2021-08-25
CIFRW (Cipher Mining Warrant) Start Date:2020-12-07
CIG (Companhia Energetica De Minas Gerais) Start Date:2007-01-03
CIGI (Colliers International  Subordinate Voting Shares) Start Date:2007-05-16
CII (Blackrock Capital And Income Fund) Start Date:2007-05-16
CIIGU (Ciig Capital Partners Ii Unit) Start Date:2021-09-15
CIIGW (Ciig Capital Partners Ii Warrant) Start Date:2021-11-05
CIK (Credit Suisse Asset Management Income Fund) Start Date:2007-05-08
CIM (Chimera Investment Corporation) Start Date:2007-11-16
CINF (Cincinnati Financial) Start Date:2004-01-02
CING (Cingulate) Start Date:2021-12-08
CINGW (Cingulate Warrants) Start Date:2021-12-08
CINT (Ci&T Inc) Start Date:2021-11-10
CIO (City Office Reit) Start Date:2014-04-15
CION (Cion Investment) Start Date:2021-10-05
CIR (Circor International) Start Date:2007-05-10
CISO (Cerberus Cyber Sentinel) Start Date:2020-06-26
CISS (C3is Inc) Start Date:2023-06-13
CIVB (Civista Bancshares) Start Date:2007-05-16
CIVI (Civitas Resources,) Start Date:2014-09-17
CIX (Compx International) Start Date:2007-05-16
CIXX (Ci Financial) Start Date:2020-11-05
CIZN (Citizens Holding Company) Start Date:2007-05-16
CJJD (China Jo-Jo Drugstores) Start Date:2010-04-22
CKPT (Checkpoint Therapeutics) Start Date:2016-12-19
CKX (Ckx Lands) Start Date:2007-05-17
CL (Colgate-Palmolive) Start Date:2004-01-02
CLAR (Clarus Corp) Start Date:2017-09-01
CLB (Core Laboratories N.V.) Start Date:2007-04-27
CLBK (Columbia Financial) Start Date:2018-04-20
CLBT (Cellebrite Di Ordinary Shares) Start Date:2021-08-31
CLBTW (Cellebrite Di Warrants) Start Date:2021-08-31
CLDT (Chatham Lodging) Start Date:2010-04-16
CLDX (Celldex Therapeutics, Inc) Start Date:2008-10-01
CLEU (China Liberal Education Holdings) Start Date:2020-05-08
CLF (Cleveland-Cliffs) Start Date:2004-01-02
CLFD (Clearfield) Start Date:2008-01-02
CLGN (Collplant Biotechnologies Ordinary Shares) Start Date:2018-01-31
CLH (Clean Harbors) Start Date:2008-12-15
CLIR (Clearsign Technologies) Start Date:2012-04-25
CLLS (Cellectis S.A. American Depositary Shares) Start Date:2015-03-25
CLM (Cornerstone Strategic Value Fund New) Start Date:2007-05-04
CLMB (Climb Global Solutions) Start Date:2007-05-16
CLMT (Calumet Specialty Products Partners, L.P.) Start Date:2007-05-16
CLNE (Clean Energy Fuels) Start Date:2007-05-25
CLNN (Clene) Start Date:2020-12-31
CLNNW (Clene Warrant) Start Date:2020-12-31
CLOE (Clover Leaf Capital Class A) Start Date:2021-09-10
CLOER (Clover Leaf Capital Rights) Start Date:2021-09-10
CLOV (Clover Health Investments, Corp) Start Date:2021-01-08
CLPR (Clipper Realty) Start Date:2017-02-10
CLPS (Clps Incorporation) Start Date:2018-05-24
CLPT (Clearpoint Neuro) Start Date:2019-07-03
CLRB (Cellectar Biosciences) Start Date:2010-02-24
CLRC (Climaterock Class A Ordinary Shares) Start Date:2022-06-02
CLRCR (Climaterock Right) Start Date:2022-06-02
CLRCU (Climaterock Unit) Start Date:2022-04-28
CLRCW (Climaterock Warrant) Start Date:2022-06-02
CLRO (Clearone) Start Date:2007-05-16
CLS (Celestica,) Start Date:2007-04-30
CLSD (Clearside Biomedical) Start Date:2016-06-02
CLSK (Cleanspark Inc) Start Date:2012-07-18
CLST (Catalyst Bancorp) Start Date:2021-10-13
CLVR (Clever Leaves Holdings Common Shares) Start Date:2020-12-18
CLVRW (Clever Leaves Holdings Warrant) Start Date:2020-12-18
CLVS (Clovis Oncology) Start Date:2011-11-16
CLVT (Clarivate Plc) Start Date:2018-10-29
CLW (Clearwater) Start Date:2008-12-17
CLWT (Euro Tech Holdings Company) Start Date:2007-04-17
CLX (The Clorox Company) Start Date:2004-01-02
CM (Canadian Imperial Bank Of Commerce) Start Date:2007-01-03
CMA (Comerica) Start Date:2004-01-02
CMAX (Caremax) Start Date:2021-06-04
CMAXW (Caremax Warrant) Start Date:2020-09-28
CMBM (Cambium Networks Corp) Start Date:2019-06-26
CMC (Commercial Metals Company) Start Date:2007-01-03
CMCL (Caledonia Mining Corp) Start Date:2017-06-29
CMCM (Cheetah Mobile American Depositary Shares Each Representing 10 Class Ordinary Shares) Start Date:2014-05-08
CMCO (Columbus Mckinnon) Start Date:2007-04-27
CMCSA (Comcast) Start Date:2004-01-02
CMCT (Cim Commercial Trust) Start Date:2007-05-16
CME (Cme) Start Date:2004-01-02
CMG (Chipotle Mexican Grill) Start Date:2006-01-26
CMI (Cummins) Start Date:2004-01-02
CMLS (Cumulus Media Class A) Start Date:2018-08-01
CMMB (Chemomab Therapeutics American Depositary Share) Start Date:2019-02-12
CMND (Clearmind Medicine) Start Date:2022-11-15
CMP (Compass Minerals) Start Date:2007-04-30
CMPO (Composecure Class A) Start Date:2021-12-28
CMPOW (Composecure Warrant) Start Date:2020-11-19
CMPR (Cimpress) Start Date:2019-12-05
CMPS (Compass Pathways Plc) Start Date:2020-09-18
CMPX (Compass Therapeutics) Start Date:2021-08-13
CMRA (Comera Life Sciences Holdings) Start Date:2022-05-20
CMRAW (Comera Life Sciences Holdings Warrant) Start Date:2022-05-20
CMRE (Costamare) Start Date:2010-11-04
CMRX (Chimerix) Start Date:2013-04-11
CMS (Cms Energy) Start Date:2004-01-02
CMT (Core Molding Technologies Inc) Start Date:2007-04-20
CMTG (Claros Mortgage Trust) Start Date:2021-11-03
CMTL (Comtech Telecommunications) Start Date:2007-05-03
CMU (Mfs Municipal Income Trust) Start Date:2007-05-16
CNA (Cna Financial Corporation) Start Date:2007-01-03
CNC (Centene Corporation) Start Date:2004-01-02
CNDT (Conduent) Start Date:2016-12-13
CNET (Zw Data Action Technologies) Start Date:2010-09-14
CNEY (Cn Energy) Start Date:2021-02-05
CNF (Cnfinance Holdings American Depositary Shares Each Representing Twenty) Start Date:2018-11-07
CNFR (Conifer Holdings) Start Date:2015-08-13
CNHI (Cnh Industrial N.V.) Start Date:2013-09-30
CNI (Canadian National Railway) Start Date:2007-05-01
CNK (Cinemark) Start Date:2007-05-16
CNM (Core & Main) Start Date:2021-07-23
CNMD (Conmed) Start Date:2020-04-14
CNNE (Cannae Holdings) Start Date:2017-11-20
CNOB (Connectone Bancorp) Start Date:2007-05-16
CNP (Centerpoint Energy) Start Date:2004-01-02
CNQ (Canadian Natural Resources Limited) Start Date:2007-01-03
CNS (Cohen & Steers) Start Date:2007-01-03
CNSL (Consolidated Comm) Start Date:2007-05-03
CNSP (Cns Pharmaceuticals) Start Date:2019-11-08
CNTA (Centessa Pharmaceuticals) Start Date:2021-05-28
CNTB (Connect Biopharma) Start Date:2021-03-19
CNTG (Centogene Bv) Start Date:2019-11-07
CNTX (Context Therapeutics) Start Date:2021-10-20
CNTY (Century Casinos) Start Date:2007-05-07
CNVS (Cinedigm Corp) Start Date:2008-11-28
CNX (Cnx Resources Corporation) Start Date:2004-01-02
CNXA (Connexa Sports Technologies) Start Date:2022-06-15
CNXC (Concentrix) Start Date:2020-11-24
CNXN (Pc Connection) Start Date:2007-05-01
COCO (The Vita Coco Company) Start Date:2021-10-21
COCP (Cocrystal Pharma) Start Date:2018-03-12
CODA (Coda Octopus) Start Date:2017-07-19
CODI (Compass Diversified) Start Date:2007-05-11
CODX (Co-Diagnostics) Start Date:2017-07-12
COE (China Online Education American Depositary Shares Each Representing 15 Class A Ordinary Shares) Start Date:2016-06-10
COEP (Coeptis Therapeutics Holdings) Start Date:2008-12-09
COF (Capital One Financial) Start Date:2004-01-02
COFS (Choiceone Financial) Start Date:2007-05-16
COGT (Cogent Biosciences) Start Date:2018-03-29
COHN (Cohen & Company) Start Date:2010-01-04
COHR (Coherent) Start Date:2007-05-03
COHU (Cohu) Start Date:2007-05-02
COIN (Coinbase) Start Date:2021-04-14
COKE (Coca-Cola Bottling) Start Date:2007-05-16
COLB (Columbia Banking System) Start Date:2007-01-03
COLD (Americold Realty Trust) Start Date:2018-01-19
COLIU (Colicity Units) Start Date:2021-02-24
COLIW (Colicity Warrant) Start Date:2021-04-16
COLL (Collegium Pharmaceutical) Start Date:2015-05-07
COLM (Columbia Sportswear Company) Start Date:2007-01-03
COMM (Commscope Holding Company) Start Date:2013-10-25
COMP (Compass) Start Date:2021-04-01
COMS (Comsovereign Holding) Start Date:2021-01-22
COMSW (Comsovereign Holding Warrants) Start Date:2021-01-22
CONN (Conn's) Start Date:2007-05-04
CONX (Conx) Start Date:2020-12-21
CONXU (Conx Unit) Start Date:2020-11-02
CONXW (Conx Warrant) Start Date:2020-12-21
COO (The Cooper Companies) Start Date:2004-01-02
COOK (Traeger) Start Date:2021-07-29
COOP (Mr. Cooper) Start Date:2012-03-28
COP (Conocophillips) Start Date:2004-01-02
COR (Cencora Inc) Start Date:2005-01-03
CORR (Corenergy Infrastructure) Start Date:2007-05-16
CORT (Corcept Therapeutics) Start Date:2007-05-16
CORZ (Core Scientific) Start Date:2021-04-08
COSM (Cosmos Holdings) Start Date:2012-10-11
COST (Costco Wholesale) Start Date:2007-04-30
COTY (Coty) Start Date:2013-06-13
COUR (Coursera) Start Date:2021-03-31
COYA (Coya Therapeutics) Start Date:2022-12-29
CP (Canadian Pacific Railway Limited) Start Date:2007-01-03
CPA (Copa Holdings S.A.) Start Date:2007-01-03
CPAC (Cementos Pacasmayo S.A.A. American Depositary Shares) Start Date:2013-02-11
CPB (Campbell Soup) Start Date:2004-01-02
CPE (Callon Petroleum Company) Start Date:2007-05-04
CPF (Central Pacific Financial) Start Date:2007-05-02
CPG (Crescent Point Energy) Start Date:2014-01-22
CPHC (Canterbury Park Holding 'New') Start Date:2016-07-01
CPHI (China Pharma Holdings) Start Date:2007-05-16
CPIX (Cumberland Pharmaceuticals) Start Date:2009-08-11
CPK (Chesapeake Utilities) Start Date:2007-05-16
CPLP (Capital Product Partners L.P. Common Units) Start Date:2007-05-16
CPNG (Coupang) Start Date:2021-03-11
CPOP (Pop Culture) Start Date:2021-06-30
CPRI (Capri Holdings) Start Date:2011-12-15
CPRT (Copart Inc) Start Date:2004-01-02
CPRX (Catalyst Pharmaceutical) Start Date:2007-05-16
CPS (Cooper Standard) Start Date:2013-10-17
CPSH (Cps Technologies) Start Date:2007-05-16
CPSI (Computer Programs And Sys) Start Date:2007-05-02
CPSS (Consumer Portfolio Services) Start Date:2007-05-16
CPT (Camden Property Trust) Start Date:2007-01-03
CPTN (Cepton) Start Date:2022-02-11
CPTNW (Cepton Warrant) Start Date:2021-03-23
CPZ (Calamos Long/Short Equity & Dynamic Income Trust) Start Date:2019-11-26
CQP (Cheniere Energy Partners L.P.) Start Date:2007-03-21
CR (Crane Co.) Start Date:2023-04-03
CRAI (Cra International) Start Date:2007-05-10
CRBG (Corebridge Financial) Start Date:2022-09-15
CRBP (Corbus Pharmaceuticals) Start Date:2015-04-16
CRBU (Caribou Biosciences) Start Date:2021-07-23
CRC (California Resources Corp) Start Date:2020-11-02
CRCT (Cricut) Start Date:2021-03-25
CRD.A (Crawford & Company) Start Date:2007-05-16
CRD.B (Crawford & Company) Start Date:2007-05-10
CRDF (Cardiff Oncology) Start Date:2010-03-02
CRDL (Cardiol Therapeutics Class A Common Shares) Start Date:2021-08-10
CRDO (Credo Technology Holding) Start Date:2022-01-27
CREG (Smart Powerr) Start Date:2010-03-22
CRESW (Cresud S.A.C.I.F. Y A. Warrant) Start Date:2021-06-25
CRESY (Cresud S.A.C.I.F. Y A. American Depositary Shares) Start Date:2007-05-01
CREX (Creative Realities) Start Date:2018-11-15
CREXW (Creative Realities Warrant) Start Date:2018-11-15
CRF (Cornerstone Total Return Fund) Start Date:2007-05-16
CRGE (Charge Enterprises) Start Date:2022-04-12
CRGO (Freightos) Start Date:2023-01-26
CRGX (Cargo Therapeutics) Start Date:2023-11-10
CRGY (Crescent Energy Company Class A) Start Date:2021-12-08
CRH (Crh Plc) Start Date:2007-01-03
CRHC (Cohn Robbins Holdings) Start Date:2020-11-02
CRI (Carter's) Start Date:2007-01-03
CRIS (Curis Inc) Start Date:2007-05-07
CRK (Comstock Resources) Start Date:2007-04-30
CRKN (Crown Electrokinetics) Start Date:2021-01-26
CRL (Charles River Laboratories International) Start Date:2007-01-03
CRM (Salesforce.com) Start Date:2004-06-23
CRMD (Cormedix) Start Date:2010-05-13
CRMT (America's Car-Mart) Start Date:2007-04-27
CRNC (Cerence) Start Date:2019-09-16
CRNT (Ceragon Networks Ordinary Shares) Start Date:2007-05-10
CRNX (Crinetics Pharmaceuticals) Start Date:2018-07-18
CRON (Cronos) Start Date:2018-02-27
CROX (Crocs) Start Date:2017-01-18
CRS (Carpenter Technology) Start Date:2007-04-27
CRSP (Crispr Therapeutics Ag) Start Date:2016-10-19
CRSR (Corsair Gaming) Start Date:2020-09-23
CRT (Cross Timbers Royalty Trust) Start Date:2007-05-16
CRTDW (Creatd Warrant) Start Date:2020-09-11
CRTO (Criteo S.A. American Depositary Shares) Start Date:2013-10-30
CRUS (Cirrus Logic) Start Date:2007-01-03
CRVL (Corvel) Start Date:2007-04-17
CRVO (Cervomed Inc) Start Date:2016-11-14
CRVS (Corvus Pharmaceuticals) Start Date:2016-03-23
CRWD (Crowdstrike Holdings) Start Date:2019-06-12
CRWS (Crown Crafts Inc) Start Date:2007-05-16
CRZNU (Corazon Capital V838 Monoceros Unit) Start Date:2021-03-24
CSAN (Cosan S.A. ADS) Start Date:2021-03-08
CSBR (Champions Oncology) Start Date:2015-08-26
CSCO (Cisco Systems) Start Date:2004-01-02
CSCW (Color Star Technology Co. Ordinary Shares) Start Date:2008-12-23
CSGP (Costar) Start Date:2007-05-03
CSGS (Csg Systems International) Start Date:2007-04-30
CSIQ (Canadian Solar Common Shares) Start Date:2007-04-30
CSL (Carlisle Companies) Start Date:2007-05-03
CSPI (Csp) Start Date:2007-05-16
CSR (Centerspace) Start Date:2007-11-01
CSSE (Chicken Soup For The Soul Entertainment Class A) Start Date:2017-08-18
CSTE (Caesarstone) Start Date:2012-03-22
CSTL (Castle Biosciences) Start Date:2019-07-25
CSTM (Constellium Se Class A Ordinary Shares) Start Date:2013-05-23
CSTR (Capstar Financial) Start Date:2016-09-22
CSV (Carriage Services) Start Date:2007-05-16
CSWC (Capital Southwest Corp) Start Date:2007-05-16
CSWI (Csw Industrials) Start Date:2015-09-30
CSX (Csx) Start Date:2004-01-02
CTAS (Cintas Corporation) Start Date:2004-01-02
CTBI (Community Trust Bancorp) Start Date:2007-05-07
CTG (Computer Task) Start Date:2007-05-16
CTGO (Contango Ore) Start Date:2010-12-20
CTHR (Charles & Colvard) Start Date:2007-05-08
CTKB (Cytek Biosciences) Start Date:2021-07-23
CTLP (Cantaloupe,) Start Date:2007-05-16
CTLT (Catalent) Start Date:2014-07-31
CTM (Castellum) Start Date:2022-10-13
CTMX (Cytomx Therapeutics) Start Date:2015-10-08
CTNT (Cheetah Net Supply Chain Service) Start Date:2023-08-01
CTO (Cto Realty Growth) Start Date:2007-05-16
CTOS (Custom Truck One Source,) Start Date:2017-10-06
CTR (Clearbridge Mlp And Midstream Total Return Fund) Start Date:2012-06-27
CTRA (Coterra Energy) Start Date:2007-04-27
CTRE (Caretrust Reit) Start Date:2014-05-23
CTRM (Castor Maritime Common Shares) Start Date:2019-02-11
CTRN (Citi Trends) Start Date:2007-04-30
CTS (Cts) Start Date:2007-05-03
CTSH (Cognizant Technology Solutions) Start Date:2004-01-02
CTSO (Cytosorbents Corp) Start Date:2014-12-23
CTV (Innovid) Start Date:2021-04-05
CTVA (Corteva) Start Date:2019-05-24
CTXR (Citius Pharmaceuticals) Start Date:2017-08-03
CUBA (Herzfeld Caribbean Basin Fund) Start Date:2007-05-16
CUBE (Cubesmart) Start Date:2007-05-01
CUBI (Customers Bancorp Common) Start Date:2013-05-16
CUE (Cue Biopharma) Start Date:2018-01-02
CUEN (Cuentas) Start Date:2021-02-02
CUK (Carnival & Plc) Start Date:2007-01-03
CULL (Cullman Bancorp) Start Date:2009-10-09
CULP (Culp) Start Date:2007-05-16
CURI (Curiositystream Class A) Start Date:2020-01-08
CURIW (Curiositystream Warrant) Start Date:2020-01-07
CURO (Curo  Corp) Start Date:2017-12-07
CURV (Torrid Holdings) Start Date:2021-07-01
CUTR (Cutera) Start Date:2007-05-04
CUZ (Cousins Properties Incorporated) Start Date:2007-01-03
CVAC (Curevac N.V.) Start Date:2020-08-14
CVBF (Cvb Financial) Start Date:2009-07-22
CVCO (Cavco Industries) Start Date:2007-05-09
CVCY (Central Valley Comm Bank) Start Date:2007-05-16
CVE (Cenovus Energy) Start Date:2009-12-09
CVEO (Civeo Corporation) Start Date:2014-06-02
CVGI (Commercial Vehicle) Start Date:2007-05-02
CVGW (Calavo Growers) Start Date:2007-05-16
CVI (Cvr Energy) Start Date:2007-10-23
CVII (Churchill Capital Vii Class A) Start Date:2021-04-05
CVKD (Cadrenal Therapeutics) Start Date:2023-01-20
CVLG (Covenant Logistics  Class A) Start Date:2007-05-16
CVLT (Commvault Systems) Start Date:2007-05-08
CVLY (Codorus Valley Bancorp) Start Date:2007-05-16
CVM (Cel-Sci) Start Date:2007-05-16
CVNA (Carvana Co.) Start Date:2017-04-28
CVR (Chicago Rivet & Machine Co.) Start Date:2007-05-16
CVRX (Cvrx) Start Date:2021-06-30
CVS (Cvs Health) Start Date:2004-01-02
CVU (Cpi Aerostructures) Start Date:2022-10-05
CVV (Cvd Equipment) Start Date:2007-05-16
CVX (Chevron) Start Date:2004-01-02
CW (Curtiss-Wright Corporation) Start Date:2007-01-03
CWAN (Clearwater Analytics) Start Date:2021-09-24
CWBC (Community West Bancshares) Start Date:2007-05-16
CWBR (Cohbar) Start Date:2015-01-28
CWCO (Consolidated Water) Start Date:2007-05-10
CWD (Calibercos) Start Date:2023-05-17
CWEN (Clearway Energy) Start Date:2018-09-17
CWEN.A (Clearway Energy) Start Date:2018-09-17
CWK (Cushman & Wakefield Plc) Start Date:2018-08-02
CWST (Casella Waste Systems) Start Date:2007-01-03
CWT (California Water Service) Start Date:2007-01-03
CX (Cemex S.A.B. De C.V.) Start Date:2007-01-03
CXAI (Cxapp Inc) Start Date:2021-02-04
CXDO (Crexendo) Start Date:2015-01-13
CXE (Mfs High Income Municipal Trust) Start Date:2007-05-16
CXH (Mfs Investment Grade Municipal Trust) Start Date:2007-05-16
CXM (Sprinklr) Start Date:2021-06-23
CXT (Crane Nxt Co.) Start Date:2007-01-03
CXW (Corecivic) Start Date:2007-04-26
CYAD (Celyad Oncology Sa American Depositary Shares) Start Date:2015-06-19
CYAN (Cyanotech) Start Date:2007-05-16
CYBN (Cybin Common Shares) Start Date:2021-08-05
CYBR (Cyberark Software Ltd.) Start Date:2014-09-24
CYCC (Cyclacel Pharmaceuticals) Start Date:2007-05-16
CYCN (Cyclerion Therapeutics) Start Date:2019-03-18
CYD (China Yuchai International) Start Date:2007-05-04
CYH (Community Health Systems) Start Date:2007-04-26
CYN (Cyngn) Start Date:2021-10-20
CYRN (Cyren Ordinary Shares) Start Date:2007-05-16
CYRX (Cryoport) Start Date:2015-07-24
CYT (Cyteir Therapeutics) Start Date:2021-06-18
CYTH (Cyclo Therapeutics) Start Date:2011-02-18
CYTHW (Cyclo Therapeutics Warrant) Start Date:2020-12-09
CYTK (Cytokinetics Com) Start Date:2007-05-04
CYTO (Altamira Therapeutics Common Shares 0.01 Sf) Start Date:2014-08-06
CYXT (Cyxtera Technologies) Start Date:2020-11-02
CZFS (Citizens Financial Services) Start Date:2007-05-24
CZNC (Citizens And Northern) Start Date:2007-05-16
CZOO (Cazoo Class A Ordinary Shares) Start Date:2021-08-27
CZR (Caesars Entertainment Corporation) Start Date:2014-09-22
CZWI (Citizens Community Bancorp) Start Date:2007-05-16
D (Dominion Energy) Start Date:2005-01-03
DAC (Danaos Corporation) Start Date:2007-04-20
DADA (Dada Nexus Limited) Start Date:2020-06-05
DAIO (Data I/O) Start Date:2007-05-16
DAKT (Daktronics) Start Date:2007-04-30
DAL (Delta Air Lines) Start Date:2007-05-16
DALN (Dallasnews Series A) Start Date:2021-06-29
DAN (Dana) Start Date:2008-02-01
DAO (Youdao) Start Date:2019-10-25
DAR (Darling Ingredients) Start Date:2007-01-03
DARE (Dare Bioscience) Start Date:2014-04-10
DASH (Doordash) Start Date:2020-12-09
DATS (Datchat) Start Date:2021-08-13
DATSW (Datchat Series A Warrant) Start Date:2021-08-13
DAVA (Endava Plc American Depositary Shares) Start Date:2018-07-27
DAVE (Dave Class A) Start Date:2022-01-06
DAVEW (Dave Warrants) Start Date:2022-01-06
DAWN (Day One Biopharmaceuticals) Start Date:2021-05-27
DB (Deutsche Bank Aktiengesellschaft) Start Date:2007-01-03
DBGI (Digital Brands) Start Date:2021-05-14
DBGIW (Digital Brands  Warrant) Start Date:2021-05-14
DBI (Designer Brands) Start Date:2007-04-30
DBL (Doubleline Opportunistic Credit Fund Common Shares Of Beneficial Interest) Start Date:2012-01-27
DBRG (Digitalbridge ,) Start Date:2014-06-27
DBTX (Decibel Therapeutics) Start Date:2021-02-12
DBVT (DBv Technologies S.A.) Start Date:2014-10-22
DBX (Dropbox) Start Date:2018-03-23
DC (Dakota Gold) Start Date:2022-04-05
DCBO (Docebo) Start Date:2020-12-03
DCF (Bny Mellon Alcentra Global Credit Income 2024 Target Term Fund) Start Date:2017-10-27
DCFC (Tritium Dcfc) Start Date:2022-01-14
DCFCW (Tritium Dcfc Warrant) Start Date:2022-01-14
DCGO (Docgo) Start Date:2021-11-01
DCI (Donaldson) Start Date:2007-04-23
DCO (Ducommun) Start Date:2007-05-10
DCOM (Dime Community Bancshares) Start Date:2007-05-16
DCOMP (Dime Community Bancshares Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2020-02-13
DCPH (Deciphera Pharmaceuticals) Start Date:2017-09-28
DCTH (Delcath Systems) Start Date:2018-05-02
DD (Dupont De Nemours) Start Date:2019-06-03
DDC (Ddc Enterprise Limited) Start Date:2023-11-17
DDD (3D Systems) Start Date:2011-05-26
DDF (Delaware Investments Dividend & Income Fund) Start Date:2007-05-16
DDI (Doubledown Interactive Co. ADS) Start Date:2021-08-31
DDL (Dingdong) Start Date:2021-06-29
DDOG (Datadog) Start Date:2019-09-19
DDS (Dillard's) Start Date:2005-01-03
DDT (Dillard's Capital Trust I) Start Date:2007-05-16
DE (Deere & Co.) Start Date:2005-01-03
DEA (Easterly Government Properties) Start Date:2015-02-06
DECA (Denali Capital Acquisition) Start Date:2022-06-07
DECK (Deckers Outdoor Corporation) Start Date:2007-01-03
DEI (Douglas Emmett) Start Date:2007-01-03
DELL (Dell Technologies) Start Date:2018-12-26
DEN (Denbury) Start Date:2020-09-21
DENN (Denny's) Start Date:2007-04-27
DEO (Diageo Plc) Start Date:2007-04-27
DERM (Journey Medical) Start Date:2021-11-12
DESP (Despegar.com,) Start Date:2019-03-07
DEX (Delaware Enhanced Global Dividend Common Shares Of Beneficial Interest) Start Date:2007-06-27
DFH (Dream Finders Homes) Start Date:2021-01-21
DFIN (Donnelley Financial Solutions) Start Date:2016-09-26
DFLI (Dragonfly Energy Holdings) Start Date:2021-08-24
DFP (Flaherty & Crumrine Dynamic Preferred And Income Fund) Start Date:2013-05-24
DFS (Discover Financial Services) Start Date:2007-07-02
DG (Dollar General) Start Date:2009-11-13
DGHI (Digihost Technology Common Subordinate Voting Shares) Start Date:2021-11-15
DGICA (Donegal) Start Date:2007-05-08
DGICB (Donegal  Class B) Start Date:2019-03-01
DGII (Digi International) Start Date:2007-04-27
DGLY (Digital Ally) Start Date:2007-05-16
DGX (Quest Diagnostics) Start Date:2005-01-03
DH (Definitive Healthcare) Start Date:2021-09-15
DHBCU (Dhb Capital Unit) Start Date:2021-03-02
DHBCW (Dhb Capital Warrant) Start Date:2021-04-23
DHC (Diversified Healthcare Trust Common Shares Of Bene) Start Date:2007-04-30
DHF (Bny Mellon High Yield Strategies Fund) Start Date:2007-05-08
DHHCU (Diamondhead Holdings Unit) Start Date:2021-01-26
DHI (D. R. Horton) Start Date:2005-01-03
DHIL (Diamond Hill Investment) Start Date:2007-05-16
DHR (Danaher) Start Date:2005-01-03
DHT (Dht) Start Date:2012-07-17
DHX (Dhi) Start Date:2007-07-18
DHY (Credit Suisse High Yield Bond Fund) Start Date:2007-04-30
DIAX (Nuveen Dow 30Sm Dynamic Overwrite Fund Common Shares Of Beneficial Interest) Start Date:2014-12-22
DIBS (1Stdibs.com) Start Date:2021-06-10
DIN (Dine Brands Global) Start Date:2008-06-02
DINO (Hf Sinclair) Start Date:2019-01-04
DIOD (Diodes) Start Date:2007-04-26
DIS (The Walt Disney Company) Start Date:2005-01-03
DISH (Dish Network) Start Date:2005-01-03
DIST (Distoken Acquisition Corporation) Start Date:2023-03-30
DIT (Amcon Distributing Company) Start Date:2007-05-16
DJCO (Daily Journal) Start Date:2007-05-17
DK (Delek Us) Start Date:2007-04-27
DKL (Delek Logistics Partners, Lp) Start Date:2012-11-02
DKNG (Draftkings) Start Date:2019-07-25
DKS (Dick's Sporting Goods) Start Date:2007-01-03
DLA (Delta Apparel) Start Date:2007-05-16
DLB (Dolby Laboratories) Start Date:2007-05-01
DLHC (Dlh Holdings) Start Date:2008-05-19
DLNG (Dynagas Lng Partners Lp Common Units) Start Date:2013-11-13
DLO (Dlocal) Start Date:2021-06-03
DLPN (Dolphin Entertainment) Start Date:2017-12-21
DLR (Digital Realty Trust Inc) Start Date:2005-01-03
DLTH (Duluth) Start Date:2015-11-20
DLTR (Dollar Tree) Start Date:2007-04-27
DLX (Deluxe) Start Date:2005-01-03
DLY (Doubleline Yield Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2020-02-26
DM (Desktop Metal,) Start Date:2019-05-03
DMA (Destra Multi-Alternative Fund) Start Date:2022-01-13
DMAC (Diamedica Therapeutics) Start Date:2009-06-01
DMB (Bny Mellon Municipal Bond Infrastructure Fund) Start Date:2013-04-26
DMF (Bny Mellon Municipal Income) Start Date:2007-05-16
DMK (Dmk Pharmaceuticals Corp) Start Date:2010-04-07
DMLP (Dorchester Minerals Lp) Start Date:2007-05-03
DMO (Western Asset Mortgage Opportunity Fund) Start Date:2010-02-24
DMRC (Digimarc) Start Date:2007-05-02
DMSL (Digital Media Solutions Inc) Start Date:2020-07-16
DMTK (Dermtech) Start Date:2017-08-10
DMYY (Dmy Squared Technology) Start Date:2022-12-07
DNA (Ginkgo Bioworks Holdings,) Start Date:2021-04-19
DNAB (Social Capital Suvretta Holdings Ii Class A Ordinary Shares) Start Date:2021-06-30
DNAD (Social Capital Suvretta Holdings Iv Class A Ordinary Shares) Start Date:2021-06-30
DNAY (Codex Dna) Start Date:2021-06-18
DNB (Dun & Bradstreet Corporation) Start Date:2020-07-01
DNLI (Denali Therapeutics) Start Date:2017-12-08
DNMR (Danimer Scientific,) Start Date:2020-05-28
DNN (Denison Mines Corp) Start Date:2007-05-16
DNOW (Now) Start Date:2014-06-02
DNP (Dnp Select Income Fund) Start Date:2007-01-03
DNTH (Magenta Therapeutics Inc) Start Date:2018-06-21
DNUT (Krispy Kreme) Start Date:2021-07-01
DO (Diamond Offshore Drilling) Start Date:2022-03-30
DOC (Physicians Realty Trust) Start Date:2013-07-19
DOCN (Digitalocean) Start Date:2021-03-24
DOCS (Doximity) Start Date:2021-06-24
DOCU (Docusign) Start Date:2018-04-27
DOGZ (Dogness) Start Date:2017-12-20
DOLE (Dole) Start Date:2021-07-30
DOMA (Doma Holdings,) Start Date:2021-01-22
DOMH (Dominari Holdings) Start Date:2007-05-16
DOMO (Domo) Start Date:2018-06-29
DOOO (Brp Common Subordinate Voting Shares) Start Date:2013-07-16
DOOR (Masonite International Corp) Start Date:2013-09-09
DORM (Dorman Products) Start Date:2007-05-16
DOUG (Douglas Elliman) Start Date:2021-12-30
DOV (Dover) Start Date:2005-01-03
DOW (Dow) Start Date:2019-03-20
DOX (Amdocs Limited) Start Date:2007-01-03
DOYU (Douyu International Holdings Limited) Start Date:2019-07-17
DPG (Duff & Phelps Utility And Infrastructure Fund) Start Date:2011-07-27
DPRO (Draganfly Common Shares) Start Date:2021-07-30
DPSI (Decisionpoint Systems) Start Date:2020-12-08
DPZ (Domino's Pizza) Start Date:2005-01-03
DQ (Daqo New Energy American Depositary Shares Each Representing Five Ordinary Shares) Start Date:2010-10-07
DRCT (Direct Digital) Start Date:2022-02-11
DRCTW (Direct Digital Holdings Warrant) Start Date:2022-02-11
DRD (Drdgold American Depositary Shares) Start Date:2011-12-29
DRH (Diamondrock Hospitality) Start Date:2007-04-30
DRI (Darden Restaurants) Start Date:2005-01-03
DRIO (Dariohealth) Start Date:2016-03-04
DRMA (Dermata Therapeutics) Start Date:2021-08-13
DRMAW (Dermata Therapeutics Warrant) Start Date:2021-08-13
DRQ (Dril-Quip) Start Date:2007-04-27
DRRX (Durect) Start Date:2007-04-27
DRS (Leonardo Drs) Start Date:2022-11-29
DRTS (Alpha Tau Medical) Start Date:2022-03-08
DRTSW (Alpha Tau Medical Warrant) Start Date:2022-03-08
DRTT (Dirtt Environmental Solutions Common Shares) Start Date:2014-01-28
DRUG (Bright Minds Biosciences) Start Date:2021-11-08
DRVN (Driven Brands) Start Date:2021-01-15
DS (Drive Shack) Start Date:2007-05-02
DSGN (Design Therapeutics) Start Date:2021-03-26
DSGR (Distribution Solutions) Start Date:2007-05-16
DSGX (The Descartes Systems Inc) Start Date:2007-01-03
DSKE (Daseke) Start Date:2015-10-12
DSL (Doubleline Income Solutions Fund Common Shares Of Beneficial Interests) Start Date:2013-04-26
DSM (Bny Mellon Strategic Municipal Bond Fund) Start Date:2007-05-16
DSP (Viant Technology) Start Date:2021-02-10
DSS (Dss) Start Date:2007-05-16
DSU (Blackrock Debt Strategies Fund) Start Date:2007-05-04
DSWL (Deswell Industries Common Shares) Start Date:2007-05-16
DSX (Diana Shipping) Start Date:2007-05-08
DT (Dynatrace) Start Date:2019-08-01
DTC (Solo Brands) Start Date:2021-10-28
DTCK (Davis Commodities Limited) Start Date:2023-09-19
DTE (Dte Energy Co.) Start Date:2005-01-03
DTEA (Davidstea) Start Date:2015-06-05
DTF (Dtf Tax-Free Income 2028 Term Fund) Start Date:2007-05-16
DTIL (Precision Biosciences) Start Date:2019-03-28
DTM (Dt) Start Date:2021-06-18
DTOCU (Digital Transformation Opportunities Units) Start Date:2021-03-10
DTOCW (Digital Transformation Opportunities Warrant) Start Date:2021-05-13
DTSS (Datasea) Start Date:2018-12-19
DTST (Data Storage) Start Date:2021-05-14
DTW (Dte Energy Company 2017 Series E 5.25% Junior Subordinated Debentures Due 2077) Start Date:2017-11-22
DUK (Duke Energy) Start Date:2012-07-03
DUO (Fangdd Network American Depositary Shares) Start Date:2019-11-01
DUOL (Duolingo) Start Date:2021-07-28
DUOT (Duos Technologies) Start Date:2008-09-30
DV (Doubleverify) Start Date:2021-04-21
DVA (Davita) Start Date:2005-01-03
DVAX (Dynavax Technologies) Start Date:2007-04-18
DVN (Devon Energy) Start Date:2005-01-03
DWSN (Dawson Geophysical Company) Start Date:2007-05-09
DX (Dynex Capital) Start Date:2007-05-16
DXC (Dxc Technology) Start Date:2017-03-16
DXCM (Dexcom) Start Date:2005-05-02
DXF (Dunxin Financial Holdings American Depositary Shares) Start Date:2010-11-23
DXLG (Destination Xl) Start Date:2007-04-30
DXPE (Dxp Enterprises) Start Date:2007-05-07
DXR (Daxor) Start Date:2007-05-16
DXYN (Dixie) Start Date:2007-05-16
DY (Dycom Industries) Start Date:2007-04-24
DYAI (Dyadic International) Start Date:2008-01-16
DYN (Dyne Therapeutics) Start Date:2020-09-17
DYNT (Dynatronics) Start Date:2007-05-16
DZSI (Dzs) Start Date:2007-04-30
E (Eni S.P.A.) Start Date:2007-01-03
EA (Electronic Arts) Start Date:2007-04-30
EAD (Allspring Income Opportunities Fund Common Shares) Start Date:2007-05-04
EAI (Entergy Arkansas Llc First Mortgage Bonds 4.875% Series Due September 1 2066) Start Date:2016-08-17
EAR (Eargo) Start Date:2020-10-16
EARN (Ellington Residential Mortgage) Start Date:2013-05-01
EAST (Eastside Distilling) Start Date:2014-04-16
EAT (Brinker International) Start Date:2007-05-01
EB (Eventbrite) Start Date:2018-09-20
EBAY (Ebay) Start Date:2005-01-03
EBC (Eastern Bankshares) Start Date:2020-10-15
EBET (Esports Technologies) Start Date:2021-04-15
EBF (Ennis) Start Date:2007-05-02
EBIX (Ebix) Start Date:2007-05-16
EBMT (Eagle Bancorp Montana) Start Date:2007-05-23
EBON (Ebang International Holdings Class A Ordinary Shares) Start Date:2020-06-26
EBR (Centrais Eletricas Brasileiras S.A. - Eletrobras) Start Date:2016-10-13
EBS (Emergent Biosolutions) Start Date:2007-01-03
EBTC (Enterprise Bancorp) Start Date:2007-05-17
EC (Ecopetrol S.A.) Start Date:2008-09-18
ECAT (Blackrock ESG Capital Allocation Trust Common Shares Of Beneficial Interest) Start Date:2021-09-28
ECBK (Ecb Bancorp) Start Date:2022-07-28
ECC (Eagle Point Credit Company) Start Date:2014-10-08
ECDA (Ecd Automotive Design Inc) Start Date:2022-12-08
ECF (Ellsworth Growth And Income Fund Ltd.) Start Date:2007-05-16
ECL (Ecolab) Start Date:2005-01-03
ECOR (Electrocore) Start Date:2018-06-22
ECPG (Encore Capital) Start Date:2007-05-11
ECVT (Ecovyst) Start Date:2021-08-03
ECX (Ecarx Holdings Class A) Start Date:2022-12-21
ED (Consolidated Edison) Start Date:2005-01-03
EDAP (Edap Tms S.A. American Depositary Shares) Start Date:2007-05-16
EDBL (Edible Garden Ag Incorporated) Start Date:2022-05-05
EDBLW (Edible Garden Ag Incorporated Warrant) Start Date:2022-05-05
EDD (Morgan Stanley Emerging Markets Domestic Debt Fund Morgan Stanley Emerging Markets Domestic Debt Fund) Start Date:2007-05-16
EDF (Virtus Stone Harbor Emerging Markets Income Fund Common Shares Of Beneficial Interest) Start Date:2010-12-23
EDI (Virtus Stone Harbor Emerging Markets Total Income Fund Common Shares Of Beneficial Interest) Start Date:2012-10-26
EDIT (Editas Medicine) Start Date:2016-02-03
EDN (Empresa Distribuidora Y Comercializadora Norte S.A.) Start Date:2007-05-16
EDR (Endeavor Holdings) Start Date:2021-04-29
EDRY (Eurdry Drybulk) Start Date:2018-05-31
EDSA (Edesa Biotech Common Shares) Start Date:2010-06-21
EDTK (Skillful Craftsman) Start Date:2020-07-23
EDU (New Oriental Education & Technology) Start Date:2007-01-03
EDUC (Educational Development) Start Date:2007-05-17
EE (Excelerate Energy Class A) Start Date:2022-04-13
EEA (The European Equity Fund) Start Date:2007-05-16
EEFT (Euronet Worldwide) Start Date:2007-01-03
EEIQ (Elite Education) Start Date:2021-03-25
EEX (Emerald Holding) Start Date:2017-04-28
EFC (Ellington Financial) Start Date:2010-10-08
EFL (Eaton Vance Floating-Rate 2022 Target Term Trust Common Shares Of Beneficial Interest) Start Date:2017-07-27
EFOI (Energy Focus) Start Date:2007-05-16
EFR (Eaton Vance Senior Floating-Rate Fund Common Shares Of Beneficial Interest) Start Date:2007-04-30
EFSC (Enterprise Financial Svcs) Start Date:2007-05-16
EFSH (1847 Holdings Llc) Start Date:2022-08-03
EFT (Eaton Vance Floating Rate Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-03
EFTR (Effector Therapeutics,) Start Date:2021-03-01
EFTRW (Effector Therapeutics Warrant) Start Date:2021-03-01
EFX (Equifax) Start Date:2005-01-03
EFXT (Enerflex Ltd) Start Date:2022-10-13
EG (Everest Ltd.) Start Date:2005-01-03
EGAN (Egain) Start Date:2007-05-16
EGBN (Eagle Bancorp) Start Date:2007-05-16
EGF (Blackrock Enhanced Government Fund) Start Date:2007-05-16
EGHT (8 X 8) Start Date:2007-04-30
EGIO (Edgio) Start Date:2007-06-08
EGLE (Eagle Bulk Shipping Commo) Start Date:2007-05-01
EGLX (Enthusiast Gaming Holdings) Start Date:2019-10-21
EGO (Eldorado Gold Corporation) Start Date:2007-04-27
EGP (Eastgroup Properties) Start Date:2007-01-03
EGRX (Eagle Pharmaceuticals Co) Start Date:2014-02-12
EGY (Vaalco Energy) Start Date:2007-04-30
EH (Ehang Holdings ADS) Start Date:2019-12-12
EHAB (Enhabit) Start Date:2022-06-23
EHC (Encompass Health Corporation) Start Date:2007-05-07
EHI (Western Asset Global High Income Fund Inc) Start Date:2007-05-02
EHTH (Ehealth) Start Date:2007-01-03
EIC (Eagle Point Income Company) Start Date:2019-07-24
EIG (Employers) Start Date:2007-05-16
EIGR (Eiger Biopharmaceuticals) Start Date:2014-01-30
EIM (Eaton Vance Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
EIX (Edison Int'l) Start Date:2007-04-30
EJH (E-Home Household Service Holdings Ordinary Shares) Start Date:2021-05-14
EKSO (Ekso Bionics Holdings) Start Date:2014-01-16
EL (Estee Lauder Cos.) Start Date:2005-01-03
ELA (Envela Corp) Start Date:2016-05-31
ELAB (Elevai Labs) Start Date:2023-11-21
ELAN (Elanco Animal Health Incorporated) Start Date:2018-09-20
ELBM (Electra Battery Materials) Start Date:2022-04-27
ELDN (Eledon Pharmaceuticals) Start Date:2014-09-17
ELEV (Elevation Oncology) Start Date:2021-06-25
ELF (E.L.F. Beauty) Start Date:2016-09-22
ELLO (Ellomay Capital Ordinary Shares) Start Date:2008-10-27
ELMD (Electromed) Start Date:2010-08-13
ELME (Elme Communities) Start Date:2007-05-03
ELOX (Eloxx Pharmaceuticals) Start Date:2012-11-23
ELP (Companhia Paranaense De Energia - Copel) Start Date:2007-01-03
ELS (Equity Lifestyle Properties) Start Date:2007-01-03
ELSE (Electro-Sensors) Start Date:2007-05-16
ELTK (Eltek Ordinary Shares) Start Date:2007-05-16
ELTX (Angion Biomedica) Start Date:2021-02-05
ELUT (Elutia Inc) Start Date:2020-10-08
ELV (Elevance Health) Start Date:2007-04-30
ELVN (Enliven Therapeutics Inc) Start Date:2020-03-12
ELWS (Earlyworks Co.) Start Date:2023-07-25
ELYM (Eliem Therapeutics) Start Date:2021-08-10
ELYS (Elys Game Technology) Start Date:2020-11-10
EM (Smart Share Global) Start Date:2021-04-01
EMAN (Emagin) Start Date:2007-05-16
EMBC (Embecta Corp) Start Date:2022-04-01
EMBKW (Embark Technology Warrants) Start Date:2021-11-11
EMCG (WisdomTree Emerging Markets Consumer Growth Fund) Start Date:2022-09-30
EMD (Western Asset Emerging Markets Debt Fund Inc) Start Date:2007-05-08
EME (Emcor) Start Date:2007-01-03
EMF (Templeton Emerging Markets Fund) Start Date:2007-05-08
EMKR (Emcore) Start Date:2007-04-27
EML (Eastern) Start Date:2007-05-16
EMN (Eastman Chemical) Start Date:2005-01-03
EMO (Clearbridge Energy Midstream Opportunity Fund) Start Date:2011-06-10
EMP (Entergy Mississippi, Llc First Mortgage Bonds, 4.90% Series Due October 1, 2066) Start Date:2016-09-16
EMR (Emerson Electric Company) Start Date:2005-01-03
EMX (Emx Royalty Common Shares) Start Date:2008-10-27
ENB (Enbridge, Inc) Start Date:2007-04-30
ENCP (Energem Class A Ordinary Shares) Start Date:2022-01-10
ENCPW (Energem Warrant) Start Date:2022-01-10
ENFN (Enfusion Class A) Start Date:2021-10-21
ENG (Englobal) Start Date:2007-05-08
ENIC (Enel Chile S.A.) Start Date:2016-04-21
ENJ (Entergy New Orleans Llc First Mortgage Bonds 5.0% Series Due December 1 2052) Start Date:2012-12-05
ENLC (Enlink Midstream, Llc) Start Date:2014-03-10
ENLT (Enlight Renewable Energy) Start Date:2023-02-10
ENLV (Enlivex Therapeutics Ordinary Shares) Start Date:2014-07-31
ENO (Entergy New Orleans Llc First Mortgage Bonds 5.50% Series Due April 1 2066) Start Date:2016-03-24
ENOV (Enovis) Start Date:2008-05-08
ENPC (Executive Network Partnering) Start Date:2020-11-06
ENPH (Enphase Energy) Start Date:2012-03-30
ENR (Energizer Holdings) Start Date:2015-07-01
ENS (Enersys) Start Date:2007-01-03
ENSC (Ensysce Biosciences) Start Date:2021-07-02
ENSG (Ensign) Start Date:2007-11-12
ENSV (Enservco) Start Date:2007-05-16
ENTA (Enanta Pharmaceuticals C) Start Date:2013-03-21
ENTG (Entegris) Start Date:2007-01-03
ENTX (Entera Bio Ordinary Shares) Start Date:2018-06-28
ENTXW (Entera Bio Warrant) Start Date:2018-06-28
ENV (Envestnet) Start Date:2010-07-29
ENVA (Enova International) Start Date:2014-11-13
ENVB (Enveric Biosciences) Start Date:2015-07-10
ENVX (Enovix) Start Date:2021-07-12
ENX (Eaton Vance New York Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
ENZ (Enzo Biochem) Start Date:2007-04-27
EOD (Allspring Global Dividend Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
EOG (Eog Resources) Start Date:2005-01-03
EOI (Eaton Vance Enhance Equity Income Fund Eaton Vance Enhanced Equity Income Fund Shares Of Beneficial Interest) Start Date:2007-05-01
EOLS (Evolus) Start Date:2018-02-08
EOS (Eaton Vance Enhance Equity Income Fund Ii) Start Date:2007-04-26
EOSE (Eos Energy Enterprises Class A) Start Date:2020-11-02
EOSEW (Eos Energy Enterprises Warrant) Start Date:2020-06-03
EOT (Eaton Vance Municipal Income Trust Eaton Vance National Municipal Opportunities Trust) Start Date:2009-05-27
EP (Empire Petroleum) Start Date:2004-01-02
EPAC (Enerpac Tool) Start Date:2007-05-03
EPAM (Epam Systems) Start Date:2012-02-08
EPC (Edgewell Personal Care Co) Start Date:2007-04-26
EPD (Enterprise Products Partners L.P.) Start Date:2007-04-30
EPIX (Essa Pharma) Start Date:2015-03-13
EPM (Evolution Petroleum) Start Date:2007-05-16
EPOW (Sunrise New Energy Ltd) Start Date:2021-02-09
EPR (Epr Properties) Start Date:2007-01-03
EPRT (Essential Properties Realty Trust) Start Date:2018-06-21
EPSN (Epsilon Energy Common Share) Start Date:2019-02-19
EQ (Equillium) Start Date:2018-10-12
EQBK (Equity Bancshares) Start Date:2015-11-11
EQC (Equity Commonwealth) Start Date:2007-04-27
EQH (Equitable Holdings) Start Date:2018-05-10
EQIX (Equinix) Start Date:2005-01-03
EQNR (Equinor Asa) Start Date:2013-08-26
EQOS (Eqonex Ordinary Shares) Start Date:2019-05-16
EQR (Equity Residential) Start Date:2005-01-03
EQRX (Eqrx) Start Date:2021-06-03
EQRXW (Eqrx Warrant) Start Date:2021-12-20
EQS (Equus Total Return) Start Date:2007-05-16
EQT (Eqt Corporation) Start Date:2005-01-03
EQX (Equinox Gold) Start Date:2019-09-16
ERAS (Erasca) Start Date:2021-07-16
ERC (Allspring Multi-Sector Income Fund) Start Date:2007-05-10
ERF (Enerplus Corporation) Start Date:2007-04-26
ERH (Allspring Utilities And High Income Fund Common Shares) Start Date:2007-05-16
ERIC (Telefonaktiebolaget Lm Ericsson) Start Date:2007-01-03
ERIE (Erie Indemnity) Start Date:2007-04-27
ERII (Energy Recovery) Start Date:2008-07-02
ERJ (Embraer S.A.) Start Date:2007-04-30
ERNA (Eterna Therapeutics) Start Date:2021-03-26
ES (Eversource Energy) Start Date:2009-03-02
ESAB (Esab) Start Date:2022-04-05
ESBA (Empire State Realty Op, L.P. Series Es) Start Date:2013-10-02
ESCA (Escalade) Start Date:2007-05-16
ESE (Esco Technologies) Start Date:2007-04-30
ESEA (Euroseas) Start Date:2007-05-16
ESGL (Esgl Holdings Ltd.) Start Date:2022-04-07
ESGR (Enstar) Start Date:2007-05-16
ESGRO (Enstar Depository Shares 7.00% Perpetual Non-Cumulative Preference Shares Series E) Start Date:2018-12-03
ESGRP (Enstar Depositary Shares Each Representing 1/1000Th Of An Interest In Preference Shares) Start Date:2018-07-13
ESHA (Esh Acquisition) Start Date:2023-07-21
ESI (Element Solutions Inc) Start Date:2014-01-23
ESLT (Elbit Systems Ltd) Start Date:2010-06-01
ESMT (Engagesmart,) Start Date:2021-09-23
ESNT (Essent Ltd.) Start Date:2013-10-31
ESOA (Energy Services Of America) Start Date:2012-11-16
ESP (Espey Mfg. & Electronics) Start Date:2007-05-16
ESPR (Esperion Therapeutics Co) Start Date:2013-06-26
ESQ (Esquire Financial) Start Date:2017-06-27
ESRT (Empire State Realty Trust) Start Date:2013-10-02
ESS (Essex Property Trust) Start Date:2005-01-03
ESSA (Essa Bancorp) Start Date:2007-05-16
ESTA (Establishment Labs Holdings) Start Date:2018-07-19
ESTC (Elastic N.V.) Start Date:2018-10-05
ESTE (Earthstone Energy) Start Date:2007-05-16
ET (Energy Transfer Lp) Start Date:2007-05-02
ETB (Eaton Vance Tax-Managed Buy-Write Income Fund Eaton Vance Tax-Managed Buy-Write Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-03
ETD (Ethan Allen Interiors Inc) Start Date:2007-04-26
ETG (Eaton Vance Tax-Advantaged Global Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-03
ETJ (Eaton Vance Risk-Managed Diversified Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-07-27
ETN (Eaton Corporation) Start Date:2012-12-03
ETNB (89Bio) Start Date:2019-11-11
ETO (Eaton Vance Tax-Advantage Global Dividend Opp) Start Date:2007-05-16
ETON (Eton Pharmaceutcials) Start Date:2018-11-13
ETR (Entergy) Start Date:2005-01-03
ETRN (Equitrans Midstream Corp) Start Date:2018-10-31
ETSY (Etsy) Start Date:2015-04-16
ETV (Eaton Vance Eaton Vance Tax-Managed Buy-Write Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2007-04-26
ETW (Eaton Vance Eaton Vance Tax-Managed Global Buy-Write Opportunites Fund Common Shares Of Beneficial Interest) Start Date:2007-05-01
ETWO (E2open Parent Holdings,) Start Date:2020-06-15
ETX (Eaton Vance Municipal Income 2028 Term Trust Common Shares Of Beneficial Interest) Start Date:2013-03-26
ETY (Eaton Vance Tax-Managed Diversified Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
EU (Encore Energy) Start Date:2008-05-21
EUDA (Euda Health Holdings) Start Date:2021-12-14
EURN (Euronav Nv) Start Date:2015-01-23
EVA (Enviva Partners, Lp) Start Date:2015-04-29
EVAX (Evaxion Biotech) Start Date:2021-02-05
EVBG (Everbridge) Start Date:2016-09-16
EVBN (Evans Bancorp) Start Date:2007-05-16
EVC (Entravision Communication) Start Date:2007-05-02
EVCM (Evercommerce) Start Date:2021-07-01
EVER (Everquote) Start Date:2018-06-28
EVEX (Eve Holding) Start Date:2022-05-10
EVF (Eaton Vance Senior Income Trust) Start Date:2007-05-16
EVFM (Evofem Biosciences) Start Date:2014-11-20
EVG (Eaton Vance Short Diversified Income Fund Eaton Vance Short Duration Diversified Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
EVGN (Evogene Ordinary Shares) Start Date:2013-11-21
EVGO (Evgo Class A) Start Date:2020-11-20
EVGOW (Evgo Warrants) Start Date:2020-11-20
EVGR (Evergreen Class A Ordinary Share) Start Date:2022-04-06
EVGRU (Evergreen Unit) Start Date:2022-02-09
EVH (Evolent Health) Start Date:2015-06-05
EVI (Evi Industries) Start Date:2009-12-01
EVLO (Evelo Biosciences) Start Date:2018-05-09
EVLV (Evolv Technologies Holdings, Class A) Start Date:2020-09-22
EVLVW (Evolv Technologies Holdings Warrant) Start Date:2021-07-19
EVM (Eaton Vance California Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
EVN (Eaton Vance Municipal Income Trust) Start Date:2007-05-16
EVO (Evotec Se American Depositary Shares) Start Date:2021-11-04
EVOK (Evoke Pharma) Start Date:2013-09-25
EVR (Evercore) Start Date:2007-01-03
EVRG (Evergy) Start Date:2007-12-18
EVRI (Everi) Start Date:2007-05-08
EVT (Eaton Vance Tax Advantaged Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
EVTC (Evertec) Start Date:2013-12-04
EVTL (Vertical Aerospace Ordinary Shares) Start Date:2021-12-16
EVTV (Envirotech Vehicles) Start Date:2022-07-06
EVV (Eaton Vance Duration Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-01
EW (Edwards Lifesciences) Start Date:2005-01-03
EWBC (East West Bancorp) Start Date:2007-01-03
EWCZ (European Wax Center) Start Date:2021-08-05
EWTX (Edgewise Therapeutics) Start Date:2021-03-26
EXAI (Exscientia Plc American Depositary Shares) Start Date:2021-10-01
EXAS (Exact Sciences Corporation) Start Date:2007-01-03
EXC (Exelon) Start Date:2005-01-03
EXD (Eaton Vance Tax-Managed Buy-Write Strategy Fund Common Shares Of Beneficial Interest) Start Date:2010-06-25
EXEL (Exelixis) Start Date:2007-01-03
EXFY (Expensify, Class A) Start Date:2021-11-10
EXG (Eaton Vance Tax-Managed Global Diversified Equity Income Fund) Start Date:2007-02-23
EXK (Endeavour Silver) Start Date:2007-05-16
EXLS (Exlservice) Start Date:2007-05-02
EXN (Excellon Resources Common Shares) Start Date:2020-09-23
EXP (Eagle Materials) Start Date:2007-01-03
EXPD (Expeditors) Start Date:2005-06-06
EXPE (Expedia) Start Date:2005-08-09
EXPI (Exp World) Start Date:2013-11-19
EXPO (Exponent) Start Date:2007-01-03
EXPR (Express) Start Date:2010-05-13
EXR (Extra Space Storage) Start Date:2005-01-03
EXTO (Almacenes Exito Sa) Start Date:2023-08-23
EXTR (Extreme Networks) Start Date:2007-05-01
EYE (National Vision Holdings) Start Date:2017-10-26
EYEN (Eyenovia) Start Date:2018-01-25
EYPT (Eyepoint Pharmaceuticals) Start Date:2007-05-16
EZFL (Ezfill Holdings) Start Date:2021-09-15
EZGO (Ezgo Technologies) Start Date:2021-01-26
EZPW (Ezcorp) Start Date:2007-04-30
F (Ford Motor) Start Date:2005-01-03
FA (First Advantage) Start Date:2021-06-23
FAF (First American Financial Corporation) Start Date:2010-05-24
FAM (First Trust/Aberdeen Global Opportunity Income Fund First Trust/Aberdeen Global Opportunity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-25
FAMI (Farmmi,) Start Date:2018-02-16
FANG (Diamondback Energy) Start Date:2012-10-12
FANH (Fanhua American Depositary Shares) Start Date:2007-10-31
FARM (Farmer Bros) Start Date:2007-05-16
FARO (Faro Technologies) Start Date:2007-05-03
FAST (Fastenal Co) Start Date:2005-01-03
FAT (Fat Brands Class A) Start Date:2017-10-23
FATBB (Fat Brands Class B) Start Date:2021-08-24
FATBW (Fat Brands Warrant) Start Date:2020-07-14
FATE (Fate Therapeutics) Start Date:2013-10-01
FATH (Fathom Digital Manufacturing Class A) Start Date:2021-03-29
FAX (Aberdeen Asia-Pacific Income Fund Inc) Start Date:2007-05-03
FAZE (Faze Holdings) Start Date:2021-04-13
FBHS (Fortune Brands Home & Security) Start Date:2011-10-04
FBIN (Fortune Brands Innovations) Start Date:2011-10-04
FBIO (Fortress Biotech) Start Date:2011-11-17
FBIOP (Fortress Biotech 9.375% Series A Cumulative Redeemable Perpetual Preferred Stock) Start Date:2017-11-14
FBIZ (First Business Financial) Start Date:2007-05-16
FBK (Fb Financial Corp) Start Date:2016-09-16
FBMS (First Bancshares) Start Date:2007-05-17
FBNC (First Bancorp) Start Date:2007-05-16
FBP (First Bancorp) Start Date:2007-04-26
FBRT (Franklin Bsp Realty Trust) Start Date:2021-10-19
FBRX (Forte Biosciences) Start Date:2017-04-13
FC (Franklin Covey) Start Date:2007-05-16
FCAP (First Capital) Start Date:2007-05-24
FCBC (First Community) Start Date:2007-05-16
FCCO (First Community) Start Date:2007-05-16
FCEL (Fuelcell Energy) Start Date:2007-05-02
FCF (First Commonwealth) Start Date:2007-05-02
FCFS (Firstcash) Start Date:2007-01-03
FCN (Fti Consulting) Start Date:2007-01-03
FCNCA (First Citizens Bancshares) Start Date:2007-05-16
FCNCP (First Citizens Bancshares Depositary Shares) Start Date:2020-03-13
FCO (Aberdeen Global Income Fund) Start Date:2007-05-16
FCPT (Four Corners Property Trust) Start Date:2015-11-10
FCT (First Trust Senior Floating Rate Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
FCUV (Focus Universal) Start Date:2017-09-01
FCX (Freeport-Mcmoran) Start Date:2005-01-03
FDBC (Fidelity D & D Bancorp) Start Date:2007-05-16
FDEU (First Trust Dynamic Europe Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2015-09-25
FDMT (4D Molecular Therapeutics) Start Date:2020-12-11
FDP (Fresh Del Monte Produce) Start Date:2007-05-04
FDS (Factset Research Systems) Start Date:2007-05-01
FDUS (Fidus Investment) Start Date:2011-06-21
FDX (Fedex Corporation) Start Date:2005-01-03
FE (Firstenergy Corp) Start Date:2005-01-03
FEAM (5E Advanced Materials) Start Date:2022-03-15
FEBO (Fenbo Holdings Limited) Start Date:2023-11-30
FEDU (Four Seasons Education) Start Date:2017-11-08
FEI (First Trust Mlp And Energy Income Fund Common Shares Of Beneficial Interest) Start Date:2012-11-28
FEIM (Frequency Electronics) Start Date:2007-05-16
FELE (Franklin Electric) Start Date:2007-05-08
FEMY (Femasys) Start Date:2021-06-18
FEN (First Trust Energy Income And Growth Fund) Start Date:2007-05-16
FENC (Fennec Pharmaceuticals) Start Date:2017-09-13
FENG (Phoenix New Media American Depositary Shares Each Representing 48 Class A Ordinary Shares.) Start Date:2011-05-12
FEO (First Trust/Aberdeen Emerging Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
FERG (Ferguson Plc) Start Date:2021-03-08
FET (Forum Energy Technologies) Start Date:2012-04-12
FEXD (Fintech Ecosystem Development Class A) Start Date:2022-01-13
FEXDR (Fintech Ecosystem Development Right) Start Date:2022-01-13
FEXDW (Fintech Ecosystem Development Warrant) Start Date:2022-01-13
FF (Futurefuel) Start Date:2007-05-16
FFA (First Trust Enhanced Equity Income Fund) Start Date:2007-05-16
FFBC (First Financial Bancorp) Start Date:2007-05-01
FFC (Flaherty & Crumrine Preferred And Income Securities Fund Incorporated) Start Date:2007-05-02
FFHL (Fuwei Films) Start Date:2007-05-16
FFIC (Flushing Financial) Start Date:2007-05-01
FFIE (Faraday Future Intelligent Electric) Start Date:2020-09-02
FFIEW (Faraday Future Intelligent Electric Warrant) Start Date:2020-08-28
FFIN (First Financial Bankshares) Start Date:2007-01-03
FFIV (F5 Networks) Start Date:2005-01-03
FFNW (First Financial Northwest) Start Date:2007-10-10
FFWM (First Foundation) Start Date:2014-11-03
FG (F&G Annuities & Life) Start Date:2022-12-01
FGB (First Trust Specialty Finance And Financial Opportunities Fund) Start Date:2007-05-25
FGBI (First Guaranty Bancshares) Start Date:2015-11-05
FGEN (Fibrogen) Start Date:2014-11-14
FGF (Fg Financial) Start Date:2014-04-01
FGH (Fg Holdings) Start Date:2007-05-16
FGI (Fgi Industries Ordinary Shares) Start Date:2022-01-25
FGMC (Fg Merger) Start Date:2022-04-19
FGMCU (Fg Merger Unit) Start Date:2022-02-25
FGMCW (Fg Merger Warrant) Start Date:2022-04-21
FHB (First Hawaiian) Start Date:2016-08-04
FHI (Federated Hermes) Start Date:2007-05-01
FHLT (Future Health ESG) Start Date:2021-12-08
FHLTU (Future Health ESG Unit) Start Date:2021-09-10
FHLTW (Future Health ESG Warrant) Start Date:2021-12-09
FHN (First Horizon National Corporation) Start Date:2005-01-03
FHTX (Foghorn Therapeutics) Start Date:2020-11-02
FI (Fiserv Inc) Start Date:2005-01-03
FIBK (First Interstate Banc) Start Date:2010-03-24
FICO (Fair Isaac) Start Date:2009-08-18
FICV (Frontier Investment Class A Ordinary Shares) Start Date:2021-09-14
FICVU (Frontier Investment Units) Start Date:2021-07-01
FICVW (Frontier Investment Warrants) Start Date:2021-09-10
FIF (First Trust Energy Infrastructure Fund Common Shares Of Beneficial Interest) Start Date:2011-09-28
FIGS (Figs) Start Date:2021-05-27
FIHL (Fidelis Insurance Holdings Limited) Start Date:2023-06-29
FINMU (Marlin Technology Unit) Start Date:2021-01-13
FINMW (Marlin Technology Warrant) Start Date:2021-03-08
FINS (Angel Oak Financial Strategies Income Term Trust Common Shares Of Beneficial Interest) Start Date:2019-05-29
FINV (Finvolution American Depositary Shares) Start Date:2017-11-10
FINW (Finwise Bancorp) Start Date:2021-11-19
FIP (Ftai Infrastructure) Start Date:2022-07-20
FIS (Fidelity National Information Services) Start Date:2006-02-01
FISI (Financial Institutions) Start Date:2007-05-16
FISK (Empire State Realty Op, L.P. Series 250) Start Date:2013-10-08
FITB (Fifth Third Bancorp) Start Date:2011-01-20
FITBI (Fifth Third Bancorp Depositary Shares) Start Date:2013-12-06
FITBO (Fifth Third Bancorp Depositary Shares Each Representing A 1/1000Th Ownership Interest In A Share Of Non-Cumulative Perpetual Preferred Stock Series K) Start Date:2019-10-02
FITBP (Fifth Third Bancorp Depositary Shares Each Representing 1/40Th Share Of Fifth Third 6.00% Non-Cumulative Perpetual Class B Preferred Stock Series A) Start Date:2019-08-27
FIVE (Five Below) Start Date:2012-07-19
FIVN (Five9) Start Date:2014-04-04
FIX (Comfort Systems) Start Date:2007-05-01
FIXX (Homology Medicines) Start Date:2018-03-28
FIZZ (National Beverage) Start Date:2007-06-12
FKWL (Franklin Wireless) Start Date:2008-01-23
FL (Foot Locker Inc) Start Date:2005-01-03
FLC (Flaherty & Crumrine Total Return Fund Inc) Start Date:2007-05-16
FLEX (Flex Ltd) Start Date:2005-01-03
FLFV (Feutune Light Acquisition Corporation) Start Date:2022-08-08
FLGC (Flora Growth) Start Date:2021-05-11
FLGT (Fulgent Genetics) Start Date:2016-09-29
FLIC (First Of Long Island) Start Date:2007-05-16
FLJ (Flj) Start Date:2019-11-05
FLL (Full House Resorts) Start Date:2007-05-16
FLNC (Fluence Energy, Class A) Start Date:2021-10-28
FLNG (Flex Lng Ordinary Shares) Start Date:2019-06-17
FLNT (Fluent) Start Date:2016-09-26
FLO (Flowers Foods) Start Date:2007-01-03
FLR (Fluor) Start Date:2005-01-03
FLS (Flowserve Corporation) Start Date:2005-01-03
FLT (Fleetcor Technologies Inc) Start Date:2010-12-15
FLUX (Flux Power Holdings) Start Date:2012-06-15
FLWS (1-800 Flowers.com) Start Date:2007-05-02
FLXS (Flexsteel Industries) Start Date:2007-05-16
FLYW (Flywire) Start Date:2021-05-26
FMAO (Farmers & Merchants Bancorp) Start Date:2007-05-16
FMBH (First Mid Bancshares) Start Date:2007-05-17
FMC (Fmc Corporation) Start Date:2005-01-03
FMIVU (Forum Merger Iv Unit) Start Date:2021-03-18
FMIVW (Forum Merger Iv Warrant) Start Date:2021-05-26
FMN (Federated Hermes Premier Municipal Income Fund) Start Date:2007-05-16
FMNB (Farmers National Banc) Start Date:2007-05-16
FMS (Fresenius Medical Care Ag & Co. Kgaa) Start Date:2007-01-03
FMX (Fomento Economico Mexicano S.A.B. De C.V.) Start Date:2007-04-30
FMY (First Trust Motgage Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
FN (Fabrinet) Start Date:2010-06-25
FNA (Paragon 28) Start Date:2021-10-15
FNB (F.N.B. Corporation) Start Date:2007-01-03
FNCB (Fncb Bancorp) Start Date:2007-05-16
FNCH (Finch Therapeutics) Start Date:2021-03-19
FND (Floor & Decor Holdings) Start Date:2017-04-27
FNF (Fidelity National Financial) Start Date:2007-01-03
FNGR (Fingermotion) Start Date:2017-08-01
FNKO (Funko) Start Date:2017-11-02
FNLC (First Bancorp) Start Date:2007-05-16
FNV (Franco-Nevada Corporation) Start Date:2011-09-08
FNWB (First Northwest Bancorp) Start Date:2015-01-30
FNWD (Finward Bancorp) Start Date:2007-05-16
FOA (Finance Of America Companies Class A) Start Date:2019-04-18
FOCS (Focus Financial Partners) Start Date:2018-07-26
FOF (Cohen & Steers Closed-End Opportunity Fund) Start Date:2007-05-16
FOLD (Amicus Therapeutics) Start Date:2007-05-31
FONR (Fonar) Start Date:2007-05-15
FOR (Forestar) Start Date:2017-09-28
FORA (Forian) Start Date:2021-03-03
FORD (Forward Industries) Start Date:2007-05-02
FORM (Formfactor) Start Date:2007-01-03
FORR (Forrester Research) Start Date:2007-05-02
FORTY (Formula Systems) Start Date:2013-02-11
FOSL (Fossil) Start Date:2005-01-03
FOUR (Shift4 Payments) Start Date:2020-06-05
FOX (Twenty-First Century Fox Class B) Start Date:2007-04-30
FOXA (Twenty-First Century Fox Class A) Start Date:2019-02-27
FOXF (Fox Factory Holding) Start Date:2013-08-08
FOXO (Foxo Technologies Class A) Start Date:2022-09-16
FPAY (Flexshopper) Start Date:2012-01-24
FPF (First Trust Intermediate Duration Preferred & Income Fund Common Shares Of Beneficial Interest) Start Date:2013-05-24
FPH (Five Point Holdings, Llc Class A Common Shares) Start Date:2017-05-10
FPI (Farmland Partners) Start Date:2014-04-11
FPL (First Trust New Opportunities Mlp & Energy Fund) Start Date:2014-03-27
FR (First Industrial Realty Trust) Start Date:2007-01-03
FRA (Blackrock Floating Rate Income Strategies Fund Inc) Start Date:2007-05-16
FRAF (Franklin Finl Svcs Corp) Start Date:2007-05-17
FRBA (First Bank Williamstown) Start Date:2007-05-17
FRD (Friedman Industries) Start Date:2007-05-16
FREE (Whole Earth Brands Class A) Start Date:2019-05-14
FREEW (Whole Earth Brands Warrant) Start Date:2020-06-25
FRES (Fresh2 Ltd.) Start Date:2020-01-30
FREY (Freyr Battery) Start Date:2021-07-06
FRGE (Forge Global) Start Date:2022-03-22
FRGI (Fiesta Restaurant) Start Date:2012-04-26
FRGT (Freight Technologies Ordinary Shares) Start Date:2017-08-08
FRHC (Freedom Holding) Start Date:2011-09-30
FRLN (Freeline Therapeutics Plc) Start Date:2020-08-07
FRME (First Merchants) Start Date:2007-05-10
FRMEP (First Merchants Depository Shares) Start Date:2022-04-04
FRO (Frontline) Start Date:2007-05-01
FROG (Jfrog) Start Date:2020-09-16
FRPH (Frp) Start Date:2007-05-16
FRPT (Freshpet) Start Date:2014-11-07
FRSGU (First Reserve Sustainable Growth Unit) Start Date:2021-03-05
FRSH (Freshworks Class A) Start Date:2021-09-22
FRST (Primis Financial) Start Date:2007-05-16
FRSX (Foresight Autonomous Holdings American Depositary Shares) Start Date:2017-06-15
FRT (Federal Realty Investment Trust) Start Date:2005-01-03
FRTX (Fresh Tracks Therapeutics) Start Date:2007-05-01
FRZA (Forza X1) Start Date:2022-08-12
FSBC (Five Star Bancorp) Start Date:2021-05-05
FSBW (Fs Bancorp) Start Date:2012-07-10
FSCO (Fs Credit Opportunities) Start Date:2022-11-14
FSD (First Trust High Income Long Short Fund Common Shares Of Beneficial Interest) Start Date:2010-09-28
FSEA (First Seacoast Bancorp) Start Date:2019-07-17
FSFG (First Savings Financial) Start Date:2008-10-07
FSI (Flexible Solutions International) Start Date:2007-05-16
FSLR (First Solar) Start Date:2006-11-17
FSLY (Fastly) Start Date:2019-05-17
FSM (Fortuna Silver Mines) Start Date:2011-09-19
FSP (Franklin Street Pptys) Start Date:2007-05-03
FSR (Fisker) Start Date:2020-10-30
FSRD (Fast Radius Class A) Start Date:2021-04-06
FSRDW (Fast Radius Warrants) Start Date:2022-02-07
FSS (Federal Signal) Start Date:2007-05-01
FSSIU (Fortistar Sustainable Solutions Unit) Start Date:2021-01-27
FSSIW (Fortistar Sustainable Solutions Warrant) Start Date:2021-03-19
FSTR (Lb Foster) Start Date:2007-05-08
FSV (Firstservice Common Shares) Start Date:2015-06-02
FT (Franklin Universal Trust) Start Date:2007-05-16
FTAI (Fortress Transportation And Infrastructure Investors Llc) Start Date:2015-05-15
FTCH (Farfetch Limited) Start Date:2018-09-21
FTCI (Ftc Solar) Start Date:2021-04-28
FTDR (Frontdoor) Start Date:2018-09-13
FTEK (Fuel Tech) Start Date:2007-05-04
FTEL (Fitell Corporation) Start Date:2023-08-08
FTF (Franklin Duration Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-04
FTFT (Future Fintech) Start Date:2009-03-12
FTHM (Fathom Holdings) Start Date:2020-07-31
FTHY (First Trust High Yield Opportunities 2027 Term Fund) Start Date:2020-06-26
FTI (Technipfmc) Start Date:2017-01-17
FTII (Futuretech Ii Acquisition) Start Date:2022-04-08
FTK (Flotek Industries) Start Date:2007-05-08
FTNT (Fortinet) Start Date:2009-11-18
FTRE (Fortrea Holdings Inc) Start Date:2023-06-16
FTS (Fortis) Start Date:2016-10-14
FTV (Fortive Corp) Start Date:2016-07-05
FUBO (Fubotv /Fl) Start Date:2020-10-08
FUL (H.B. Fuller Company) Start Date:2007-01-03
FULC (Fulcrum Therapeutics) Start Date:2019-07-18
FULT (Fulton Financial) Start Date:2007-05-08
FULTP (Fulton Financial Depositary Shares Each Representing A 1/40Th Interest In A Share Of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2020-11-03
FUN (Cedar Fair L.P.) Start Date:2007-01-03
FUNC (First United) Start Date:2007-05-16
FUND (Sprott Focus Trust) Start Date:2007-05-16
FURY (Fury Gold Mines Common Shares) Start Date:2020-10-12
FUSB (First Us Bancshares) Start Date:2007-05-16
FUSN (Fusion Pharmaceuticals) Start Date:2020-06-26
FUTU (Futu Holdings Limited) Start Date:2019-03-08
FUV (Arcimoto,) Start Date:2017-09-21
FVCB (Fvcbankcorp) Start Date:2017-09-29
FVRR (Fiverr International Ltd.) Start Date:2019-06-13
FWBI (First Wave Biopharma) Start Date:2016-10-28
FWONA (Formula One) Start Date:2013-01-22
FWONK (Formula One) Start Date:2014-07-08
FWRD (Forward Air) Start Date:2007-05-04
FWRG (First Watch Restaurant) Start Date:2021-10-01
FXLV (F45 Training) Start Date:2021-07-15
FXNC (First National) Start Date:2007-05-16
FYBR (Frontier Communications Parent,) Start Date:2021-05-04
G (Genpact Limited) Start Date:2007-08-02
GAB (Gabelli Equity Trust) Start Date:2007-05-08
GABC (German American Bancorp) Start Date:2007-05-16
GAIA (Gaiam) Start Date:2007-05-07
GAIN (Gladstone Investment) Start Date:2007-05-09
GALT (Galectin Therapeutics) Start Date:2009-01-12
GAM (General American Investors) Start Date:2007-05-16
GAMB (Gambling.com) Start Date:2021-07-23
GAMC (Golden Arrow Merger Class A) Start Date:2021-05-07
GAMCU (Golden Arrow Merger Unit) Start Date:2021-03-17
GAMCW (Golden Arrow Merger Warrant) Start Date:2021-06-04
GAME (Engine Gaming And Media) Start Date:2021-06-17
GAN (Gan) Start Date:2020-05-08
GANX (Gain Therapeutics) Start Date:2021-03-18
GASS (Stealthgas) Start Date:2007-05-16
GATO (Gatos Silver) Start Date:2020-11-02
GATX (Gatx Corp) Start Date:2007-04-27
GAU (Galiano Gold) Start Date:2008-01-02
GB (Global Blue Holding Ag Ordinary Shares) Start Date:2018-06-27
GBAB (Guggenheim Taxable Municipal Bond & Investment Grade Debt Trust Common Shares Of Beneficial Interest) Start Date:2010-10-27
GBBK (Global Blockchain Acquisition) Start Date:2022-06-17
GBCI (Glacier Bancorp) Start Date:2014-03-04
GBIO (Generation Bio) Start Date:2020-06-12
GBLI (Global Indemnity) Start Date:2007-05-07
GBNH (Greenbrook Tms Common Shares) Start Date:2021-03-16
GBNY (Generations Bancorp Ny) Start Date:2021-01-13
GBOX (Greenbox Pos) Start Date:2021-02-17
GBR (New Concept Energy Inc) Start Date:2007-05-16
GBS (Gbs) Start Date:2020-12-23
GBTG (Global Business Travel  Class A) Start Date:2020-11-23
GBX (Greenbrier Companies) Start Date:2007-05-02
GCBC (Greene County Bancorp) Start Date:2007-05-16
GCI (Gannett Co.) Start Date:2014-02-04
GCMG (Gcm Grosvenor) Start Date:2020-11-16
GCMGW (Gcm Grosvenor Warrant) Start Date:2019-01-31
GCO (Genesco) Start Date:2007-05-01
GCT (Gigacloud Technology) Start Date:2022-08-18
GCTK (Glucotrack) Start Date:2022-03-11
GCV (Gabelli Convertible And Income Securities Fund) Start Date:2007-05-16
GD (General Dynamics) Start Date:2005-01-03
GDC (Gd Culture) Start Date:2015-12-29
GDDY (Godaddy) Start Date:2015-04-02
GDEN (Golden Entertainment) Start Date:2007-05-02
GDHG (Golden Heaven Holdings Ltd.) Start Date:2023-04-12
GDL (Gdl Fund The Common Shares Of Beneficial Interest) Start Date:2007-05-16
GDO (Western Asset Global Corporate Defined Opportunity Fund Western Asset Global Corporate Defined Opportunity Fund) Start Date:2009-11-24
GDOT (Green Dot Corporation) Start Date:2010-07-22
GDRX (Goodrx) Start Date:2020-09-23
GDS (Gds Holdings Limited) Start Date:2016-11-02
GDST (Goldenstone Acquisition Limited) Start Date:2022-04-14
GDTC (Cytomed Therapeutics Pte. Ltd.) Start Date:2023-04-14
GDV (Gabelli Dividend & Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-01
GDYN (Grid Dynamics) Start Date:2018-10-05
GE (General Electric) Start Date:2005-01-03
GECC (Great Elm Capital) Start Date:2016-11-04
GEF (Greif) Start Date:2007-05-07
GEF.B (Greif) Start Date:2007-05-16
GEG (Great Elm) Start Date:2007-04-26
GEHC (Ge Healthcare Technologies) Start Date:2022-12-15
GEL (Genesis Energy, L.P.) Start Date:2007-08-01
GEN (Gen Digital) Start Date:2007-04-27
GENC (Gencor Industries) Start Date:2007-12-20
GENE (Genetic Technologies ADS) Start Date:2007-05-16
GENI (Genius Sports Limited) Start Date:2020-10-05
GENK (Gen Restaurant) Start Date:2023-06-28
GENQ (Genesis Unicorn Capital Class A) Start Date:2022-04-07
GEO (Geo) Start Date:2007-05-03
GEOS (Geospace Technologies) Start Date:2007-05-09
GER (Goldman Sachs Mlp Energy Renaissance Fund) Start Date:2014-09-26
GERN (Geron) Start Date:2007-04-30
GES (Guess) Start Date:2007-05-01
GETR (Getaround) Start Date:2021-04-26
GETY (Getty Images Holdings Class A) Start Date:2022-07-25
GEVO (Gevo,) Start Date:2011-02-09
GF (New Germany Fund) Start Date:2007-05-16
GFAI (Guardforce Ai) Start Date:2021-09-29
GFAIW (Guardforce AI Co. Warrant) Start Date:2021-09-29
GFF (Griffon) Start Date:2007-04-30
GFI (Gold Fields Limited) Start Date:2007-01-03
GFL (Gfl Environmental) Start Date:2020-03-03
GFS (Globalfoundries Ordinary Shares) Start Date:2021-10-28
GGAL (Grupo Financiero Galicia S.A.) Start Date:2007-01-03
GGB (Gerdau S.A.) Start Date:2007-01-03
GGE (Green Giant) Start Date:2010-09-13
GGG (Graco) Start Date:2007-01-03
GGMC (Glenfarne Merger Class A) Start Date:2021-05-27
GGN (Gamco Global Gold Natural Resources & Income Trust) Start Date:2007-05-08
GGR (Gogoro) Start Date:2022-04-05
GGROW (Gogoro Warrant) Start Date:2022-04-05
GGT (Gabelli Multi-Media Trust) Start Date:2007-05-16
GGZ (Gabelli Global Small And Mid Cap Value Trust) Start Date:2014-06-12
GH (Guardant Health) Start Date:2018-10-04
GHC (Graham Holdings Company) Start Date:2007-05-16
GHG (Greentree Hospitality American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2018-03-27
GHI (Greystone Housing Impact Investors Lp) Start Date:2008-07-01
GHIX (Gores Holdings Ix Class A) Start Date:2022-03-22
GHL (Greenhill & Co) Start Date:2007-05-04
GHLD (Guild Co) Start Date:2020-11-02
GHM (Graham) Start Date:2007-05-16
GHRS (Gh Research Plc) Start Date:2021-06-25
GHSI (Guardion Health Sciences) Start Date:2019-04-05
GHY (Pgim Global High Yield Fund) Start Date:2012-12-21
GIA (Gigcapital 5) Start Date:2021-11-04
GIB (Cgi) Start Date:2007-05-10
GIC (Global Industrial Company) Start Date:2007-05-01
GIFI (Gulf Island Fabrication) Start Date:2007-04-30
GIGM (Gigamedia Ordinary Shares) Start Date:2007-04-30
GIII (G-Iii Apparel) Start Date:2007-05-16
GIIXU (Gores Holdings Viii Unit) Start Date:2021-02-25
GIIXW (Gores Holdings Viii Warrant) Start Date:2021-04-23
GIL (Gildan Activewear) Start Date:2007-01-03
GILD (Gilead Sciences) Start Date:2005-01-03
GILT (Gilat Satellite Networks Ltd) Start Date:2007-05-04
GIM (Templeton Global Income Fund) Start Date:2007-05-03
GIPR (Generation Income Properties) Start Date:2021-10-05
GIS (General Mills) Start Date:2005-01-03
GIWWW (Giginternational1 Warrant) Start Date:2021-07-12
GJO (Synthetic Fixed-Income Securities Synthetic Fixed-Income Securities On Behalf Of Strats) Start Date:2007-05-16
GJR (Synthetic Fixed-Income Securities Strats Trust For Procter&Gamble Securities Series 2006-1) Start Date:2007-05-17
GJS (Goldman Sachs Securities Strats Trust For Goldman Sachs Securities Series 2006-2) Start Date:2007-05-16
GJT (Synthetic Fixed-Income Securities Synthetic Fixed-Income Securities Floating Rate Structured Repackaged Asset-Backed Trust Securities Certificates Series 2006-3) Start Date:2007-05-16
GKOS (Glaukos) Start Date:2015-06-25
GL (Globe Life) Start Date:2007-05-01
GLAC (Global Lights Acquisition Corp) Start Date:2023-12-04
GLAD (Gladstone Capital) Start Date:2007-05-16
GLBE (Global-E Online) Start Date:2021-05-12
GLBL (Cartesian Growth Class A Ordinary Share) Start Date:2021-04-27
GLBLW (Cartesian Growth Warrant) Start Date:2021-04-28
GLBS (Globus Maritime) Start Date:2010-11-26
GLBZ (Glen Burnie Bancorp) Start Date:2007-05-16
GLDD (Great Lakes Dredge & Dock) Start Date:2007-05-16
GLDG (Goldmining Common Shares) Start Date:2020-10-06
GLLI (Globalink Investment) Start Date:2021-12-23
GLLIR (Globalink Investment Rights) Start Date:2021-12-23
GLLIU (Globalink Investment Unit) Start Date:2021-12-07
GLLIW (Globalink Investment Warrants) Start Date:2021-12-23
GLMD (Galmed Pharmaceuticals Ordinary Shares) Start Date:2014-03-13
GLNG (Golar Lng) Start Date:2007-05-11
GLO (Clough Global Opportunities Fund) Start Date:2007-04-30
GLOB (Globant S.A.) Start Date:2014-07-18
GLP (Global Partners Lp) Start Date:2007-05-16
GLPG (Galapagos Nv American Depositary Shares) Start Date:2015-05-14
GLPI (Gaming And Leisure Properties) Start Date:2013-10-14
GLQ (Clough Global Equity Fund Clough Global Equity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
GLRE (Greenlight Capital Re) Start Date:2007-05-24
GLSI (Greenwich Lifesciences) Start Date:2020-09-25
GLST (Global Star Acquisition,) Start Date:2022-11-10
GLT (Glatfelter Corp) Start Date:2007-04-30
GLTO (Galecto) Start Date:2020-11-02
GLU (Gabelli Global Utility Common Shares Of Beneficial Ownership) Start Date:2007-05-16
GLUE (Monte Rosa Therapeutics) Start Date:2021-06-24
GLV (Clough Global Dividend And Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
GLW (Corning) Start Date:2005-01-03
GLYC (Glycomimetics O) Start Date:2014-01-10
GM (General Motors) Start Date:2010-11-18
GMAB (Genmab A/S) Start Date:2019-07-18
GMBL (Esports Entertainment) Start Date:2010-07-07
GMBLW (Esports Entertainment  Warrant) Start Date:2020-04-14
GMBLZ (Esports Entertainment  Warrant) Start Date:2022-03-14
GMDA (Gamida Cell Ordinary Shares) Start Date:2018-10-26
GME (Gamestop Corporation) Start Date:2005-10-10
GMED (Globus Medical) Start Date:2012-08-03
GMGI (Golden Matrix) Start Date:2018-11-30
GMM (Global Mofy Metaverse Limited) Start Date:2023-10-10
GMRE (Global Medical Reit Commo) Start Date:2016-06-29
GMS (Gms) Start Date:2016-05-26
GMTX (Gemini Therapeutics) Start Date:2020-08-12
GMVD (G Medical Innovations Holdings Ordinary Shares) Start Date:2021-06-25
GMVDW (G Medical Innovations Holdings Warrants) Start Date:2021-06-25
GNE (Genie Energy) Start Date:2011-10-26
GNFT (Genfit S.A. American Depositary Shares) Start Date:2019-03-27
GNK (Genco Shipping & Trading) Start Date:2015-07-20
GNL (Global Net Lease) Start Date:2015-06-02
GNLN (Greenlane) Start Date:2019-04-18
GNLX (Genelux) Start Date:2023-01-26
GNPX (Genprex) Start Date:2018-03-29
GNRC (Generac Holdings) Start Date:2010-02-11
GNS (Genius Ordinary Shares) Start Date:2022-04-12
GNSS (Genasys) Start Date:2007-05-16
GNT (Gamco Natural Resources Gold & Income Trust) Start Date:2011-01-27
GNTA (Genenta Science S.P.A. American Depositary Shares) Start Date:2021-12-15
GNTX (Gentex Corporation) Start Date:2007-01-03
GNTY (Guaranty Bancshares) Start Date:2017-05-09
GNW (Genworth Financial Inc) Start Date:2005-01-03
GO (Grocery Outlet Holding) Start Date:2019-06-20
GOCO (Gohealth) Start Date:2020-07-15
GODN (Golden Star Acquisition Corporation) Start Date:2023-06-28
GOEV (Canoo Class A) Start Date:2019-04-16
GOEVW (Canoo Warrant) Start Date:2019-04-16
GOF (Guggenheim Strategic Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2007-07-27
GOGL (Golden Ocean) Start Date:2007-05-04
GOGO (Gogo) Start Date:2013-06-21
GOL (Gol Linhas Aereas Inteligentes S.A. Sponsored ADR Representing 2 Pfd Shares) Start Date:2007-04-30
GOLD (Barrick Gold) Start Date:2007-04-27
GOLF (Acushnet Holdings) Start Date:2016-10-28
GOOD (Gladstone Commercial) Start Date:2007-05-16
GOODO (Gladstone Commercial 6.00% Series G Cumulative Redeemable Preferred Stock Par Value $0.001 Per Share) Start Date:2021-06-28
GOOG (Alphabet Inc Class C) Start Date:2005-01-03
GOOGL (Alphabet Inc Class A) Start Date:2007-04-27
GOOS (Canada Goose Holdings) Start Date:2017-03-21
GORO (Gold Resource) Start Date:2007-05-16
GOSS (Gossamer Bio) Start Date:2019-02-08
GOTU (Gaotu Techedu American Depositary Shares) Start Date:2019-06-06
GOVX (Geovax Labs) Start Date:2020-09-25
GP (Georgia-Pacific) Start Date:2020-08-28
GPAK (Gamer Pakistan) Start Date:2023-10-09
GPC (Genuine Parts) Start Date:2005-01-03
GPCR (Structure Therapeutics) Start Date:2023-02-03
GPI (1 Automotive) Start Date:2007-04-30
GPK (Graphic Packaging Holding Company) Start Date:2007-01-03
GPMT (Granite Point Mortgage Trust) Start Date:2017-06-23
GPN (Global Payments) Start Date:2005-01-03
GPP (Green Plains Partners Lp Common Units) Start Date:2015-06-26
GPRE (Green Plains) Start Date:2007-05-16
GPRK (Geopark Limited) Start Date:2014-02-07
GPRO (Gopro  O) Start Date:2014-06-26
GPS (Gap) Start Date:2005-01-03
GRAB (Grab) Start Date:2021-12-02
GRABW (Grab Holdings Warrant) Start Date:2021-12-02
GRBK (Green Brick Energy) Start Date:2007-06-19
GRC (Gorman-Rupp Company) Start Date:2007-05-09
GRCL (Gracell Biotechnologies) Start Date:2021-01-08
GREE (Greenidge Generation Holdings Class A Common) Start Date:2021-09-15
GRF (Eagle Capital Growth Fund) Start Date:2007-06-08
GRFS (Grifols S.A.) Start Date:2011-06-02
GRFX (Graphex) Start Date:2022-08-17
GRI (Gri Bio Inc) Start Date:2021-02-10
GRIN (Grindrod Shipping Holdings Ordinary Shares) Start Date:2018-06-18
GRMN (Garmin Ltd.) Start Date:2005-01-03
GRNAW (Greenlight Biosciences Holdings Pbc Warrant) Start Date:2021-03-08
GRND (Grindr) Start Date:2021-01-14
GRNQ (Greenpro Capital) Start Date:2015-07-09
GRNT (Granite Ridge Resources) Start Date:2022-10-25
GROM (Grom Social Enterprises) Start Date:2021-06-17
GROMW (Grom Social Enterprises Warrants) Start Date:2021-06-17
GROV (Grove Collaborative Holdings Class A) Start Date:2021-05-13
GROW (U.S. Global Investors Class A) Start Date:2007-05-01
GROY (Gold Royalty) Start Date:2021-03-09
GRPH (Graphite Bio) Start Date:2021-06-25
GRPN (on) Start Date:2011-11-04
GRRR (Gorilla Technology) Start Date:2022-07-14
GRTS (Gritstone Oncology) Start Date:2018-09-28
GRTX (Galera Therapeutics) Start Date:2019-11-07
GRVY (Gravity Co. ADS) Start Date:2007-05-16
GRWG (Growgeneration) Start Date:2016-11-11
GRX (The Gabelli Healthcare & Wellness Trust Common Shares Of Beneficial Interest) Start Date:2007-06-29
GS (Goldman Sachs) Start Date:2005-01-03
GSAT (Globalstar,) Start Date:2007-05-08
GSBC (Great Southern Bancorp) Start Date:2007-05-16
GSBD (Goldman Sachs Bdc) Start Date:2015-03-18
GSD (Global Systems Dynamics Class A) Start Date:2021-09-28
GSDWU (Global Systems Dynamics Unit) Start Date:2021-08-05
GSEVU (Gores Holdings Vii Units) Start Date:2021-02-23
GSEVW (Gores Holdings Vii Warrant) Start Date:2021-04-15
GSHD (Goosehead Insurance) Start Date:2018-04-27
GSIT (Gsi Technology) Start Date:2007-05-16
GSIW (Garden Stage Limited) Start Date:2023-12-01
GSK (Glaxosmithkline Plc) Start Date:2007-05-01
GSL (Global Ship Lease,) Start Date:2008-08-15
GSM (Ferroglobe Plc Ordinary Shares) Start Date:2015-12-24
GSMGW (Glory Star New Media Holdings Warrant Expiring 2/13/2025) Start Date:2018-09-12
GSUN (Golden Sun Education) Start Date:2022-06-22
GT (The Goodyear Tire & Rubber Company) Start Date:2005-01-03
GTBP (Gt Biopharma) Start Date:2021-02-11
GTE (Gran Tierra Energy) Start Date:2008-04-08
GTEC (Greenland Technologies Holding Ordinary Shares) Start Date:2018-08-08
GTES (Gates Industrial Plc) Start Date:2018-01-25
GTH (Genetron Holdings) Start Date:2020-06-19
GTHX (G1 Therapeutics) Start Date:2017-05-17
GTIM (Good Times Restaurants) Start Date:2007-05-18
GTLB (Gitlab Class A) Start Date:2021-10-14
GTLS (Chart Industries) Start Date:2007-04-27
GTN (Gray Television) Start Date:2007-05-07
GTPBU (Gores Technology Partners Ii Units) Start Date:2021-03-12
GTPBW (Gores Technology Partners Ii Warrant) Start Date:2021-05-06
GTX (Garrett Technologies) Start Date:2021-05-03
GTXAP (Garrett Motion Series A Cumulative Convertible Preferred Stock) Start Date:2021-05-28
GTY (Getty Realty Corp) Start Date:2007-05-08
GUG (Guggenheim Active Allocation Fund Common Shares Of Beneficial Interest) Start Date:2021-11-24
GURE (Gulf Resources) Start Date:2009-10-27
GUT (Gabelli Utility Trust) Start Date:2007-05-16
GV (Visionary Education Technology Holdings Inc) Start Date:2022-05-17
GV (Visionary Education Technology Holdings Inc) Start Date:2023-08-01
GVA (Granite Construction) Start Date:2007-05-02
GVH (Globavend Holdings Limited) Start Date:2023-11-08
GVP (Gse Systems) Start Date:2007-05-16
GWAV (Greenwave Technology Solutions) Start Date:2015-04-09
GWH (Ess Tech,) Start Date:2021-10-11
GWRE (Guidewire Software) Start Date:2012-01-25
GWRS (Global Water Resources) Start Date:2016-04-28
GWW (Grainger) Start Date:2005-01-03
GXO (Gxo Logistics) Start Date:2021-08-02
GYRE (Gyre Therapeutics Inc) Start Date:2007-05-16
GYRO (Gyrodyne, Llc) Start Date:2015-09-01
H (Hyatt Hotels Corporation) Start Date:2009-11-05
HA (Hawaiian) Start Date:2007-05-09
HAE (Haemonetics Corporation) Start Date:2007-01-03
HAFC (Hanmi Financial) Start Date:2007-05-04
HAIN (The Hain Celestial) Start Date:2007-01-03
HAL (Halliburton Co.) Start Date:2005-01-03
HALL (Hallmark Financial Services) Start Date:2007-05-16
HALO (Halozyme Therapeutics) Start Date:2007-05-10
HARP (Harpoon Therapeutics) Start Date:2019-02-08
HAS (Hasbro) Start Date:2005-01-03
HAYN (Haynes International) Start Date:2007-05-16
HAYW (Hayward) Start Date:2021-03-12
HBAN (Huntington Bancshares) Start Date:2009-09-18
HBANM (Huntington Bancshares Incorporated Depositary Shares Each Representing A 1/1000Th Interest In A Share Of Huntington Series I Preferred Stock) Start Date:2021-06-10
HBB (Hamilton Beach Brands Hldg Co) Start Date:2017-10-02
HBCP (Home Bancorp) Start Date:2008-10-03
HBI (Hanesbrands Inc) Start Date:2006-09-06
HBIO (Harvard Bioscience) Start Date:2013-10-21
HBM (Hudbay Minerals) Start Date:2010-10-25
HBNC (Horizon Bancorp) Start Date:2007-05-16
HBT (Hbt Financial) Start Date:2019-10-11
HCA (Hca Holdings) Start Date:2011-03-10
HCAT (Health Catalyst) Start Date:2019-07-25
HCC (Warrior Met Coal) Start Date:2017-04-13
HCCI (Heritage-Crystal Clean) Start Date:2008-03-12
HCDI (Harbor Custom Development) Start Date:2020-08-28
HCDWQ (Harbor Custom Development Inc) Start Date:2021-06-10
HCDZQ (Harbor Custom Development Inc) Start Date:2021-10-05
HCI (Hci) Start Date:2012-10-25
HCICU (Hennessy Capital Investment V Units) Start Date:2021-01-15
HCICW (Hennessy Capital Investment V Warrant) Start Date:2021-03-08
HCIIU (Hudson Executive Investment Ii Unit) Start Date:2021-01-26
HCIIW (Hudson Executive Investment Ii Warrant) Start Date:2021-03-22
HCKT (Hackett) Start Date:2008-01-31
HCM (Hutchmed) Start Date:2016-03-17
HCMA (Hcm Acquisition Corp) Start Date:2022-03-16
HCP (Hashicorp) Start Date:2021-12-09
HCSG (Healthcare Services) Start Date:2007-05-02
HCTI (Healthcare Triangle) Start Date:2021-10-13
HCVI (Hennessy Capital Investment Vi Class A) Start Date:2021-11-24
HCVIU (Hennessy Capital Investment Vi Unit) Start Date:2021-09-29
HCWB (Hcw Biologics) Start Date:2021-07-20
HD (Home Depot) Start Date:2005-01-03
HDB (Hdfc Bank) Start Date:2007-04-27
HDSN (Hudson Technologies) Start Date:2007-05-16
HE (Hawaiian Electric Industries) Start Date:2007-01-03
HEAR (Turtle Beach Commo) Start Date:2012-03-22
HEES (H&E Equipment Services) Start Date:2007-05-03
HEI (Heico Corporation) Start Date:2007-01-03
HEI.A (Heico Corp) Start Date:2007-05-16
HELE (Helen Of Troy) Start Date:2007-04-30
HEP (Holly Energy Partners, L.P.) Start Date:2007-05-16
HEPA (Hepion Pharmaceuticals) Start Date:2014-02-10
HEPS (D-Market Electronic Services & Trading) Start Date:2021-07-01
HEQ (John Hancock Hedged Equity & Income Fund Common Shares Of Beneficial Interest) Start Date:2011-05-26
HES (Hess Corporation) Start Date:2007-04-27
HESM (Hess Midstream Lp Class A Share Representing A Partner Interest) Start Date:2017-04-05
HFBL (Home Federal Bancorp Of Louisiana) Start Date:2007-05-23
HFFG (Hf Foods) Start Date:2017-09-07
HFRO (Highland Income Fund) Start Date:2017-11-06
HFWA (Heritage Financial) Start Date:2007-05-16
HG (Hamilton Insurance) Start Date:2023-11-10
HGBL (Heritage Global) Start Date:2007-05-16
HGLB (Highland Global Allocation Fund) Start Date:2019-02-19
HGTY (Hagerty Class A) Start Date:2021-06-01
HGV (Hilton Grand Vacations) Start Date:2016-12-14
HHGC (Hhg Capital Ordinary Shares) Start Date:2021-11-11
HHGCW (Hhg Capital Warrant) Start Date:2021-11-11
HHH (Howard Hughes Holdings Inc) Start Date:2010-11-05
HHS (Harte-Hanks) Start Date:2021-12-01
HI (Hillenbrand) Start Date:2008-04-01
HIBB (Hibbett Sports) Start Date:2007-04-27
HIE (Miller/Howard High Income Equity Fund Common Shares Of Beneficial Interest) Start Date:2014-11-25
HIFS (Hingham Institution) Start Date:2007-05-16
HIG (Hartford Financial Svc.Gp.) Start Date:2005-01-03
HIHO (Highway Holdings) Start Date:2007-05-16
HII (Huntington Ingalls Industries) Start Date:2011-03-22
HIIIU (Hudson Executive Investment Iii Unit) Start Date:2021-02-24
HIMS (Hims & Hers Health,) Start Date:2019-09-13
HIMX (Himax Technologies American Depositary Shares) Start Date:2007-04-23
HIO (Western Asset High Income Opportunity Fund) Start Date:2007-05-09
HIPO (Hippo Holdings) Start Date:2021-07-29
HITI (High Tide Common Shares) Start Date:2021-06-02
HIVE (Hive Blockchain Technologies Common Shares) Start Date:2021-07-01
HIW (Highwoods Properties) Start Date:2007-01-03
HIX (Western Asset High Income Fund Ii) Start Date:2007-05-04
HKD (Amtd Digital) Start Date:2022-07-15
HKIT (Hitek Global) Start Date:2023-03-31
HL (Hecla Mining) Start Date:2007-04-30
HLAHU (Hamilton Lane Alliance Holdings I Unit) Start Date:2021-01-13
HLAHW (Hamilton Lane Alliance Holdings I Warrant) Start Date:2021-03-15
HLBZW (Helbiz Warrant) Start Date:2019-12-09
HLF (Herbalife Nutrition Ltd.) Start Date:2007-01-03
HLGN (Heliogen) Start Date:2021-05-07
HLI (Houlihan Lokey) Start Date:2015-08-13
HLIO (Helios Technologies) Start Date:2007-05-16
HLIT (Harmonic) Start Date:2007-05-01
HLLY (Holley) Start Date:2020-11-27
HLMN (Hillman Solutions) Start Date:2021-07-12
HLN (Haleon Plc) Start Date:2022-07-18
HLNE (Hamilton Lane Incorporated) Start Date:2017-03-01
HLP (Hongli) Start Date:2023-03-29
HLT (Hilton Worldwide Holdings Inc) Start Date:2013-12-12
HLTH (Cue Health) Start Date:2021-09-24
HLVX (Hillevax) Start Date:2022-04-29
HLX (Helix Energy Solutions) Start Date:2007-04-30
HMA (Heartland Media Acquisition) Start Date:2022-03-14
HMC (Honda Motor Company) Start Date:2007-05-01
HMN (Horace Mann Educators) Start Date:2007-05-01
HMNF (Hmn Financial) Start Date:2007-05-16
HMST (Homestreet) Start Date:2012-02-10
HMY (Harmony Gold Mining Company Limited) Start Date:2007-04-26
HNI (Hni) Start Date:2007-05-08
HNNA (Hennessy Advisors) Start Date:2007-05-16
HNRA (Hnr Acquisition Corp) Start Date:2022-04-06
HNRG (Hallador Energy Company) Start Date:2010-05-21
HNST (The Honest Company) Start Date:2021-05-05
HNVR (Hanover Bancorp) Start Date:2022-05-11
HNW (Pioneer Diversified High Income Fund) Start Date:2007-05-25
HOFT (Hooker Furniture) Start Date:2007-05-07
HOFV (Hall Of Fame Resort & Entertainment Company) Start Date:2020-07-02
HOFVW (Hall Of Fame Resort & Entertainment Company Warrant) Start Date:2020-07-02
HOG (Harley-Davidson) Start Date:2006-09-01
HOLI (Hollsys Automation Technologies International, Common) Start Date:2008-08-01
HOLO (Microcloud Hologram) Start Date:2021-08-06
HOLX (Hologic) Start Date:2005-01-03
HOMB (Home Bancshares) Start Date:2007-01-03
HON (Honeywell Int'l) Start Date:2005-01-03
HONE (Harborone Bancorp) Start Date:2016-06-30
HOOD (Robinhood Markets) Start Date:2021-07-29
HOOK (Hookipa Pharma) Start Date:2019-04-18
HOPE (Hope Bancorp) Start Date:2007-05-01
HOTH (Hoth Therapeutics) Start Date:2019-02-15
HOUR (Hour Loop) Start Date:2022-01-07
HOUS (Anywhere Real Estate) Start Date:2012-10-11
HOV (Hovnanian Enterprises, Class A) Start Date:2007-04-30
HOVNP (Hovnanian Enterprises Inc Dep Shr Srs A Pfd) Start Date:2007-05-16
HOWL (Werewolf Therapeutics) Start Date:2021-04-30
HP (Helmerich & Payne) Start Date:2005-01-03
HPCO (Hempacco Co.) Start Date:2022-08-30
HPE (Hewlett Packard Enterprise) Start Date:2015-11-02
HPF (John Hancock Pfd Income Fund Ii Pfd Income Fund Ii) Start Date:2007-05-16
HPI (John Hancock Preferred Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-23
HPK (Highpeak Energy,) Start Date:2020-08-24
HPKEW (Highpeak Energy Warrant) Start Date:2020-08-24
HPP (Hudson Pacific Properties) Start Date:2010-06-24
HPQ (Hp) Start Date:2005-01-03
HPS (John Hancock Preferred Income Fund Iii Preferred Income Fund Iii) Start Date:2007-05-08
HQH (Tekla Healthcare Investors) Start Date:2007-05-08
HQI (Hirequest) Start Date:2007-05-16
HQL (Teklalife Sciences Investors) Start Date:2007-05-04
HQY (Healthequity) Start Date:2014-07-31
HR (Healthcare Realty Trust Incorporated) Start Date:2007-01-03
HRB (Block H&R) Start Date:2005-01-03
HRI (Herc) Start Date:2007-05-02
HRL (Hormel Foods) Start Date:2005-01-03
HRMY (Harmony Biosciences) Start Date:2020-08-19
HROW (Harrow Health) Start Date:2013-02-08
HRT (Hireright Holdings Corporation) Start Date:2021-10-29
HRTG (Heritage Insurance In) Start Date:2014-05-23
HRTX (Heron Therapeutics Commo) Start Date:2007-05-16
HRYU (Hanryu Holdings) Start Date:2023-08-01
HRZN (Horizon Technology Finance) Start Date:2010-10-29
HSAI (Hesai) Start Date:2023-02-09
HSBC (Hsbc Holdings Plc.) Start Date:2007-04-27
HSCS (Heart Test Laboratories) Start Date:2022-06-15
HSCSW (Heart Test Laboratories Warrant) Start Date:2022-06-15
HSDT (Helius Medical Technologies Class A) Start Date:2014-06-27
HSHP (Himalaya Shipping Ltd.) Start Date:2023-03-31
HSIC (Henry Schein) Start Date:2005-01-03
HSII (Heidrick & Struggles) Start Date:2007-05-07
HSON (Hudson Global) Start Date:2007-04-30
HSPO (Horizon Space Acquisition I) Start Date:2023-01-26
HST (Host Hotels & Resorts) Start Date:2006-04-18
HSTM (Healthstream) Start Date:2007-05-16
HSTO (Histogen) Start Date:2013-07-25
HSY (The Hershey Company) Start Date:2005-01-03
HT (Hersha Hospitality) Start Date:2007-05-04
HTBI (Hometrust Bancshares) Start Date:2012-07-11
HTBK (Heritage Commerce) Start Date:2007-05-16
HTCR (Heartcore Enterprises) Start Date:2022-02-10
HTD (John Hancock Tax Advantaged Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
HTGC (Hercules Capital) Start Date:2007-05-08
HTGM (Htg Molecular Diagnostics) Start Date:2015-05-06
HTH (Hilltop) Start Date:2007-08-01
HTHT (Huazhu Limited) Start Date:2010-03-26
HTIA (Healthcare Trust 7.375% Series A Cumulative Redeemable Perpetual Preferred Stock) Start Date:2020-03-30
HTLD (Heartland Express) Start Date:2007-05-02
HTLF (Heartland Financial Usa) Start Date:2017-03-31
HTLFP (Heartland Financial Usa Depositary Shares Each Representing A 1/400Th Ownership Interest In A Share Of 7.00% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E) Start Date:2020-06-29
HTOO (Fusion Fuel Green Plc Class A Ordinary Shares) Start Date:2020-12-10
HTOOW (Fusion Fuel Green Plc Warrant) Start Date:2020-12-10
HTY (John Hancock Tax-Advantaged Global Shareholder Yield Fund Common Shares Of Beneficial Interest) Start Date:2007-09-26
HTZ (Hertz Global Holdings, Inc) Start Date:2021-11-09
HTZWW (Hertz Global Holdings Inc Warrant) Start Date:2021-11-09
HUBB (Hubbell Corp) Start Date:2009-10-29
HUBG (Hub) Start Date:2007-05-01
HUBS (Hubspot) Start Date:2014-10-09
HUDA (Hudson Acquisition I) Start Date:2022-12-27
HUDI (Huadi International Co., Ordinary Shares) Start Date:2021-01-22
HUGE (Fsd Pharma Class B Subordinate Voting Shares) Start Date:2020-01-09
HUIZ (Huize Holding) Start Date:2020-02-12
HUM (Humana) Start Date:2005-01-03
HUMA (Humacyte) Start Date:2021-08-23
HUMAW (Humacyte Warrant) Start Date:2020-11-24
HUN (Huntsman Corporation) Start Date:2007-01-03
HURC (Hurco Companies) Start Date:2007-05-11
HURN (Huron Consulting) Start Date:2007-05-04
HUSA (Houston American Energy) Start Date:2007-07-05
HUT (Hut 8 Mining Common Shares) Start Date:2021-06-15
HUYA (Huya) Start Date:2018-05-11
HVT (Haverty Furniture) Start Date:2007-05-04
HVT.A (Haverty Furniture Companies) Start Date:2007-05-16
HWBK (Hawthorn Bancshares) Start Date:2007-06-18
HWC (Hancock Whitney Corporation) Start Date:2007-05-03
HWKN (Hawkins) Start Date:2007-05-16
HWM (Howmet Aerospace) Start Date:2016-11-01
HXL (Hexcel Corporation) Start Date:2007-01-03
HY (Hyster-Yale Materials) Start Date:2012-10-01
HYAC (Haymaker Acquisition 4) Start Date:2023-09-15
HYB (New America High Income Fund) Start Date:2007-04-25
HYFM (Hydrofarm) Start Date:2020-12-10
HYI (Western Asset High Yield Defined Opportunity Fund) Start Date:2010-10-27
HYLN (Hyliion Holdings) Start Date:2020-10-02
HYMC (Hycroft Mining Holding Class A) Start Date:2018-03-12
HYMCL (Hycroft Mining Holding Warrants) Start Date:2021-01-25
HYMCW (Hycroft Mining Holding Warrant) Start Date:2020-06-01
HYMCZ (Hycroft Mining Holding Warrant) Start Date:2017-02-17
HYPR (Hyperfine Class A) Start Date:2021-01-27
HYT (Blackrock Corporate High Yield Fund) Start Date:2007-05-09
HYW (Hywin Holdings) Start Date:2021-03-26
HYZN (Hyzon Motors Class A) Start Date:2021-07-14
HYZNW (Hyzon Motors Warrants) Start Date:2020-12-14
HZNP (Horizon Therapeutics Public Company) Start Date:2011-07-28
HZO (Marinemax) Start Date:2007-05-03
IAC (Iac/Interactivecorp) Start Date:2020-07-01
IAE (Voya Asia Pacific High Dividend Equity Income Fund Ing Asia Pacific High Dividend Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
IAF (Aberdeen Australia Equity Fund Inc) Start Date:2007-05-16
IAG (Iamgold Corporation) Start Date:2007-04-25
IART (Integra Lifesciences Holdings Corporation) Start Date:2007-01-03
IAS (Integral Ad Science Holding) Start Date:2021-06-30
IAUX (I-80 Gold Common Shares) Start Date:2022-05-19
IBCP (Independent Bank) Start Date:2007-05-08
IBEX (Ibex) Start Date:2020-08-07
IBIO (Ibio) Start Date:2008-08-19
IBKR (Interactive Brokers) Start Date:2007-05-04
IBM (International Business Machines) Start Date:2005-01-03
IBN (Icici Bank Limited) Start Date:2007-01-03
IBOC (International Bancshares) Start Date:2007-05-04
IBP (Installed Building Products) Start Date:2014-02-13
IBRX (Immunitybio,) Start Date:2021-03-10
IBTX (Independent Bank  Co) Start Date:2013-04-03
ICAD (Icad) Start Date:2007-05-11
ICCC (Immucell) Start Date:2007-05-16
ICCH (Icc Holdings) Start Date:2017-03-28
ICCM (Icecure Medical Ordinary Shares) Start Date:2021-08-26
ICD (Independence Contract Drilling) Start Date:2014-08-08
ICE (Intercontinental Exchange) Start Date:2005-11-16
ICFI (Icf International) Start Date:2007-05-16
ICG (Intchains Limited) Start Date:2023-03-16
ICHR (Ichor) Start Date:2016-12-09
ICL (Icl Ltd.) Start Date:2014-09-24
ICLK (Iclick Interactive Asia American Depositary Shares) Start Date:2017-12-22
ICLR (Icon Plc) Start Date:2007-05-03
ICMB (Investcorp Credit Management Bdc) Start Date:2014-02-06
ICPT (Intercept Pharmaceuticals) Start Date:2012-10-11
ICU (Seastar Medical Holding) Start Date:2021-03-18
ICUI (Icu Medical) Start Date:2007-04-30
ICVX (Icosavax) Start Date:2021-07-29
IDA (Idacorp) Start Date:2007-01-03
IDAI (T Stamp Class A) Start Date:2021-06-21
IDCC (Interdigital) Start Date:2007-04-27
IDE (Voya Infrastructure Industrials And Materials Fund Common Shares Of Beneficial Interest) Start Date:2010-01-27
IDEX (Ideanomics,) Start Date:2007-05-16
IDICQ (Parts Id Inc) Start Date:2007-05-02
IDN (Intellicheck) Start Date:2007-05-16
IDR (Idaho Strategic Resources) Start Date:2022-03-11
IDT (Idt) Start Date:2011-08-01
IDXX (Idexx Laboratories) Start Date:2005-01-03
IDYA (Ideaya Biosciences) Start Date:2019-05-23
IE (Ivanhoe Electric) Start Date:2022-06-28
IEAWW (Infrastructure And Energy Alternatives Warrant) Start Date:2016-08-30
IEP (Icahn Enterprises L.P) Start Date:2007-09-18
IESC (Ies) Start Date:2007-05-16
IEX (Idex Corporation) Start Date:2005-01-03
IFBD (Infobird) Start Date:2021-04-20
IFF (Intl Flavors & Fragrances) Start Date:2005-01-03
IFN (India Fund) Start Date:2007-04-27
IFRX (Inflarx N.V.) Start Date:2017-11-16
IFS (Intercorp Financial Services) Start Date:2019-07-19
IGA (Voya Global Advantage And Premium Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
IGC (India Globalization Capital) Start Date:2019-02-26
IGD (Voya Global Equity Dividend And Premium Opportunity Fund) Start Date:2007-05-01
IGI (Western Asset Investment Grade Defined Opportunity Trust) Start Date:2009-06-26
IGIC (International General Insurance Holdings Ordinary Share) Start Date:2018-04-10
IGICW (International General Insurance Holdings Warrants Expiring 03/17/2025) Start Date:2018-04-10
IGMS (Igm Biosciences) Start Date:2019-09-18
IGR (Cbre Global Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-26
IGT (International Game Technology) Start Date:2015-04-07
IH (Ihuman) Start Date:2020-10-09
IHD (Voya Emerging Markets High Income Dividend Equity Fund Common Shares) Start Date:2011-04-27
IHG (Intercontinental Hotels Plc) Start Date:2007-01-03
IHIT (Invesco High Income 2023 Target Term Fund Common Shares Of Beneficial Interest) Start Date:2016-11-23
IHRT (Iheartmedia) Start Date:2019-05-07
IHS (Ihs Holding Limited) Start Date:2021-10-14
IHT (Innsuites Hospitality Trust Shares Of Beneficial Interest) Start Date:2007-05-17
IHTA (Invesco High Income 2024 Target Term Fund Common Shares Of Beneficial Interest No Par Value Per Share) Start Date:2017-11-30
IIF (Morgan Stanley India Investment Fund) Start Date:2013-11-19
III (Information Services Grp) Start Date:2007-05-16
IIIN (Insteel Industries) Start Date:2007-05-01
IIIV (I3 Verticals) Start Date:2018-06-21
IIM (Invesco Value Municipal Income Trust) Start Date:2007-05-16
IINN (Inspira Technologies Oxy) Start Date:2021-07-14
IINNW (Inspira Technologies Oxy B.H.N. Warrant) Start Date:2021-07-14
IIPR (Innovative Industrial Properties) Start Date:2016-12-01
IIVIP (Ii-Vi Incorporated 6.00% Series A Mandatory Convertible Preferred Stock) Start Date:2020-08-07
IKNA (Ikena Oncology) Start Date:2021-03-26
IKT (Inhibikase Therapeutics) Start Date:2020-12-23
ILAG (Intelligent Living Application) Start Date:2022-07-13
ILLM (Acuityads Holdings Inc) Start Date:2021-06-10
ILMN (Illumina Inc) Start Date:2005-01-03
ILPT (Industrial Logistics Properties Trust Common Share) Start Date:2018-01-12
IMAB (I-Mab) Start Date:2020-01-17
IMACW (Imac Holdings Warrant) Start Date:2019-02-13
IMAX (Imax) Start Date:2007-04-26
IMBI (Imedia Brands Class A) Start Date:2007-05-01
IMCC (Im Cannabis Common Shares) Start Date:2021-03-01
IMCI (Infinite) Start Date:2022-11-21
IMCR (Immunocore Plc) Start Date:2021-02-05
IMGN (Immunogen) Start Date:2007-04-30
IMKTA (Ingles Markets) Start Date:2007-05-04
IMMP (Immutep American Depositary Shares) Start Date:2013-02-11
IMMR (Immersion) Start Date:2007-05-09
IMMX (Immix Biopharma) Start Date:2021-12-16
IMNM (Immunome) Start Date:2020-10-02
IMNN (Imunon) Start Date:2007-07-06
IMO (Imperial Oil Limited) Start Date:2007-01-03
IMOS (Chipmos Technologies American Depositary Shares) Start Date:2013-02-11
IMPH (Impac Mortgage Holdings Inc) Start Date:2007-04-27
IMPL (Impel Neuropharma) Start Date:2021-04-23
IMPP (Imperial Petroleum) Start Date:2021-12-06
IMRN (Immuron American Depositary Shares) Start Date:2017-03-02
IMRX (Immuneering) Start Date:2021-07-30
IMTE (Integrated Media Technology) Start Date:2017-08-11
IMTX (Immatics N.V. Ordinary Shares) Start Date:2020-07-02
IMTXW (Immatics N.V. Warrants) Start Date:2020-07-02
IMUX (Immunic) Start Date:2019-04-17
IMVT (Immunovant) Start Date:2019-06-21
IMXI (International Money Express) Start Date:2017-03-27
INAB (In8bio) Start Date:2021-07-30
INBK (First Internet Bancorp Common) Start Date:2013-02-22
INBS (Intelligent Bio Solutions) Start Date:2020-12-23
INBX (Inhibrx) Start Date:2020-08-19
INCR (Intercure Ordinary Shares) Start Date:2021-09-01
INCY (Incyte) Start Date:2005-01-03
INDB (Independent Bank) Start Date:2007-05-02
INDI (Indie Semiconductor, Class A) Start Date:2021-06-11
INDIW (Indie Semiconductor Warrant) Start Date:2021-06-11
INDO (Indonesia Energy) Start Date:2019-12-19
INDP (Indaptus Therapeutics) Start Date:2021-08-04
INDT (Indus Realty Trust,) Start Date:2007-05-17
INFA (Informatica) Start Date:2021-10-27
INFI (Infinity Pharmaceuticals) Start Date:2007-05-16
INFN (Infinera) Start Date:2007-06-07
INFU (Infusystems) Start Date:2010-12-23
INFY (Infosys ADR) Start Date:2005-01-03
ING (Ing Groep N.V.) Start Date:2007-01-03
INGN (Inogen) Start Date:2014-02-14
INGR (Ingredion) Start Date:2007-04-30
INHD (Inno Holdings) Start Date:2023-12-14
INKT (Mink Therapeutics) Start Date:2021-10-15
INLX (Intellinetics) Start Date:2012-02-14
INM (Inmed Pharmaceuticals Common Shares) Start Date:2020-06-19
INMB (Inmune Bio) Start Date:2019-02-04
INMD (Inmode Ordinary Shares) Start Date:2019-08-08
INN (Summit Hotel Properties) Start Date:2011-02-09
INNV (Innovage Holding) Start Date:2021-03-04
INO (Inovio Pharmaceuticals) Start Date:2007-01-03
INOD (Innodata) Start Date:2007-05-16
INPX (Inpixon) Start Date:2016-12-12
INSE (Inspired Entertainment) Start Date:2014-12-11
INSG (Inseego) Start Date:2007-05-01
INSI (Insight Select Income Fund) Start Date:2007-05-16
INSM (Insmed Incorporated) Start Date:2007-04-23
INSP (Inspire Medical Systems) Start Date:2018-05-03
INST (Instructure) Start Date:2021-07-22
INSW (International Seaways) Start Date:2016-11-16
INTA (Intapp) Start Date:2021-06-30
INTC (Intel) Start Date:2005-01-03
INTG (Intergroup Corporation) Start Date:2007-05-16
INTR (Inter & Class A) Start Date:2022-06-23
INTS (Intensity Therapeutics) Start Date:2023-06-30
INTT (Intest) Start Date:2007-05-16
INTU (Intuit) Start Date:2005-01-03
INTZ (Intrusion) Start Date:2007-05-16
INUV (Inuvo) Start Date:2009-07-31
INVA (Innoviva) Start Date:2007-05-04
INVE (Identive) Start Date:2010-01-15
INVH (Invitation Homes) Start Date:2017-02-01
INVO (Invo Bioscience) Start Date:2020-11-13
INVZ (Innoviz Technologies Ordinary Shares) Start Date:2021-04-06
INVZW (Innoviz Technologies Warrant) Start Date:2021-04-06
INZY (Inozyme Pharma) Start Date:2020-07-24
IOBT (Io Biotech) Start Date:2021-11-05
IONM (Assure Holdings) Start Date:2021-09-29
IONQ (Ionq,) Start Date:2021-01-04
IONR (Ioneer Ltd) Start Date:2022-06-30
IONS (Ionis Pharmaceuticals) Start Date:2007-05-01
IOR (Income Opportunity Realty Investors) Start Date:2007-05-18
IOSP (Innospec) Start Date:2007-05-07
IOT (Samsara) Start Date:2021-12-15
IOVA (Iovance Biotherapeutics) Start Date:2009-09-01
IP (International Paper) Start Date:2005-01-03
IPA (Immunoprecise Antibodies) Start Date:2017-01-03
IPAR (Inter Parfums) Start Date:2007-05-11
IPDN (Professional Diversity Network) Start Date:2013-03-05
IPG (Interpublic) Start Date:2005-01-03
IPGP (Ipg Photonics) Start Date:2006-12-13
IPHA (Innate Pharma S.A. ADS) Start Date:2019-10-17
IPI (Intrepid Potash) Start Date:2008-04-22
IPOD (Social Capital Hedosophia Holdings Iv Class A Ordinary Shares) Start Date:2020-12-15
IPOF (Social Capital Hedosophia Holdings Vi Class A Ordinary Shares) Start Date:2020-11-30
IPSC (Century Therapeutics) Start Date:2021-06-18
IPVF (Interprivate Iii Financial Partners Class A) Start Date:2021-04-26
IPVIU (Interprivate Iv Infratech Partners Units) Start Date:2021-03-05
IPVIW (Interprivate Iv Infratech Partners Warrant) Start Date:2021-04-30
IPW (Ipower) Start Date:2021-05-12
IPWR (Ideal Power) Start Date:2013-11-22
IPX (Iperionx American Depositary Share) Start Date:2022-06-21
IPXX (Inflection Point Acquisition Ii) Start Date:2023-07-17
IQ (IQiyi) Start Date:2018-03-29
IQI (Invesco Quality Municipal Income Trust) Start Date:2007-05-16
IQV (IQvia Holdings) Start Date:2013-05-09
IR (Ingersoll-Rand Plc) Start Date:2017-05-12
IRBT (Irobot Corporation) Start Date:2007-01-03
IRDM (Iridium Communications) Start Date:2009-09-24
IREN (Iris Energy Ordinary Shares) Start Date:2021-11-17
IRIX (Iridex) Start Date:2007-05-16
IRL (New Ireland Fund Inc) Start Date:2007-05-16
IRM (Iron Mountain Incorporated) Start Date:2005-01-03
IRMD (Iradimed Corp) Start Date:2014-07-16
IRON (Disc Medicine) Start Date:2020-08-12
IROQ (If Bancorp) Start Date:2011-07-08
IRS (Irsa Inversiones Y Representaciones S.A.) Start Date:2007-05-02
IRT (Independence Realty Trust) Start Date:2013-09-18
IRTC (Irhythm Technologies) Start Date:2016-10-20
IRWD (Ironwood Pharmaceuticals) Start Date:2010-02-03
ISD (Pgim High Yield Bond Fund) Start Date:2012-04-26
ISDR (Issuer Direct) Start Date:2008-03-26
ISPC (Ispecimen) Start Date:2021-06-17
ISPO (Inspirat) Start Date:2021-02-09
ISPOW (Inspirato Incorporated Warrant) Start Date:2021-02-09
ISPR (Ispire Technology) Start Date:2023-04-04
ISRG (Intuitive Surgical) Start Date:2006-06-01
ISRL (Israel Acquisitions Corp) Start Date:2023-02-28
ISSC (Innovative Solutions And Support) Start Date:2007-05-04
ISTR (Investar Holding Corp) Start Date:2014-07-01
ISUN (Isun) Start Date:2016-04-26
IT (Gartner Inc) Start Date:2005-01-03
ITCI (Intra-Cellular Therapies) Start Date:2014-01-31
ITCL (Banco Itau Chile) Start Date:2007-05-16
ITGR (Integer Holdings Corporation) Start Date:2007-05-08
ITI (Iteris) Start Date:2007-05-16
ITIC (Investors Title) Start Date:2007-05-16
ITOS (Iteos Therapeutics) Start Date:2020-07-24
ITP (It Tech Packaging) Start Date:2009-12-17
ITRG (Integra Resources Common Shares) Start Date:2020-07-31
ITRI (Itron) Start Date:2007-04-30
ITRM (Iterum Therapeutics Plc Ordinary Share) Start Date:2018-05-25
ITRN (Ituran Location And Control Ltd.) Start Date:2007-05-16
ITT (Itt) Start Date:2007-05-01
ITUB (Itau Unibanco Holding S.A.) Start Date:2009-05-20
ITW (Illinois Tool Works) Start Date:2007-04-30
IVA (Inventiva) Start Date:2020-07-13
IVAC (Intevac) Start Date:2007-04-30
IVCA (Investcorp India Acquisition Corp) Start Date:2022-06-30
IVDA (Iveda Solutions) Start Date:2009-10-12
IVH (Delaware Ivy High Income Opportunities Fund) Start Date:2013-05-29
IVP (Inspire Veterinary Partners) Start Date:2023-08-30
IVR (Invesco Mortgage Capital) Start Date:2009-06-26
IVT (Inventrust Properties) Start Date:2021-10-12
IVVD (Invivyd) Start Date:2021-08-06
IVZ (Invesco Ltd.) Start Date:2007-12-04
IX (Orix ADS) Start Date:2007-05-16
IXHL (Incannex Healthcare American Depositary Shares) Start Date:2022-03-02
IZEA (Izea Worldwide) Start Date:2011-06-07
IZM (Iczoom ,) Start Date:2023-03-15
J (Jacobs Engineering) Start Date:2007-05-02
JACK (Jack In The Box) Start Date:2008-12-15
JAGX (Jaguar Health) Start Date:2015-05-13
JAKK (Jakks Pacific) Start Date:2007-05-01
JAMF (Jamf) Start Date:2020-07-22
JAN (Janone) Start Date:2007-05-16
JANX (Janux Therapeutics) Start Date:2021-06-11
JAZZ (Jazz Pharmaceuticals Plc) Start Date:2012-01-18
JBGS (Jbg Smith Properties) Start Date:2017-07-06
JBHT (J. B. Hunt Transport Services) Start Date:2005-01-03
JBI (Janus International ,) Start Date:2019-12-20
JBL (Jabil) Start Date:2005-01-03
JBLU (Jetblue Airways Corporation) Start Date:2007-01-03
JBSS (John B Sanfilippo) Start Date:2007-05-02
JBT (John Bean Technologies Corporation) Start Date:2008-08-01
JCE (Nuveen Core Equity Alpha Fund Nuveen Core Equity Alpha Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
JCI (Johnson Controls International) Start Date:2005-01-03
JCIC (Jack Creek Investment Class A Ordinary Shares) Start Date:2021-03-17
JCICU (Jack Creek Investment Units) Start Date:2021-01-22
JCICW (Jack Creek Investment Warrants) Start Date:2021-03-15
JCSE (Je Cleantech Holdings Ordinary Shares) Start Date:2022-04-22
JCTCF (Jewett-Cameron Trading Company Common Shares) Start Date:2007-05-16
JD (Jd.com Inc) Start Date:2014-05-22
JEF (Jefferies Financial) Start Date:2007-04-24
JELD (Jeld-Wen Holding) Start Date:2017-01-27
JEMD (Nuveen Emerging Markets Debt 2022 Target Term Fund Common Shares Of Beneficial Interest $0.01 Par Value Per Share) Start Date:2017-09-27
JEQ (Aberdeen Japan Equity Fund) Start Date:2007-05-16
JEWL (Adamas One) Start Date:2022-12-09
JFBR (Jeffs' Brands Ltd) Start Date:2022-08-26
JFIN (Jiayin  American Depositary Shares) Start Date:2019-05-10
JFR (Nuveen Floating Rate Income Fund) Start Date:2007-05-01
JFU (9F American Depositary Shares) Start Date:2019-08-15
JG (Aurora Mobile American Depositary Shares) Start Date:2018-07-26
JGGCR (Jaguar Global Growth I Right) Start Date:2022-04-04
JGGCU (Jaguar Global Growth I Unit) Start Date:2022-02-11
JGGCW (Jaguar Global Growth I Warrant) Start Date:2022-04-04
JGH (Nuveen Global High Income Fund Common Shares Of Beneficial Interest) Start Date:2014-11-24
JHAA (Nuveen Corporate Income 2023 Target Term Fund) Start Date:2018-12-19
JHG (Janus Henderson Plc) Start Date:2017-05-30
JHI (John Hancock Investors Trust) Start Date:2007-05-16
JHS (John Hancock Income Securities Trust) Start Date:2007-05-16
JHX (James Hardie Industries Plc American Depositary Shares) Start Date:2007-05-16
JILL (J. Jill) Start Date:2017-03-09
JJSF (J&J Snack Foods) Start Date:2007-05-04
JKHY (Jack Henry & Associates Inc) Start Date:2005-01-03
JKS (Jinkosolar Holding Company American Depositary Shares) Start Date:2010-05-14
JLL (Jones Lang Lasalle) Start Date:2007-05-01
JLS (Nuveen Mortgage And Income Fund) Start Date:2009-11-25
JMIA (Jumia Technologies Ag American Depositary Shares Each Representing Two Ordinary Shares) Start Date:2019-04-12
JMM (Nuveen Multi-Market Income Fund) Start Date:2007-05-16
JMSB (John Marshall Bancorp) Start Date:2013-11-21
JNJ (Johnson & Johnson) Start Date:2005-01-03
JNPR (Juniper Networks) Start Date:2009-10-29
JNVR (Janover) Start Date:2023-07-25
JOAN (Joann) Start Date:2021-03-12
JOB (Gee) Start Date:2007-05-16
JOBY (Joby Aviation,) Start Date:2021-08-11
JOE (St. Joe) Start Date:2007-05-03
JOF (Japan Smaller Capitalization Fund Inc) Start Date:2007-04-25
JOUT (Johnson Outdoors) Start Date:2007-05-16
JPC (Nuveen Preferred & Income Opportunities Fund) Start Date:2007-05-04
JPI (Nuveen Preferred And Income Term Fund Common Shares Of Beneficial Interest) Start Date:2012-07-27
JPM (JP Morgan Chase & Co.) Start Date:2005-01-03
JPS (Nuveen Preferred & Income Securities Fund) Start Date:2007-05-04
JPT (Nuveen Preferred And Income Fund Common Shares Of Beneficial Interest) Start Date:2017-01-27
JQC (Nuveen Credit Strategies Income Fund Shares Of Beneficial Interest) Start Date:2007-04-30
JRI (Nuveen Real Asset Income And Growth Fund Common Shares Of Beneficial Interest) Start Date:2012-04-26
JRO (Nuveen Floating Rate Income Opportuntiy Fund Shares Of Beneficial Interest) Start Date:2007-05-08
JRS (Nuveen Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-09
JRSH (Jerash Holdings) Start Date:2018-05-04
JRVR (James River  Lt) Start Date:2014-12-12
JSD (Nuveen Short Duration Credit Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2011-05-26
JSPR (Jasper Therapeutics) Start Date:2021-09-20
JSPRW (Japer Therapeutics Warrants) Start Date:2020-01-10
JT (Jianpu Technology American Depositary Shares) Start Date:2017-11-16
JUN (Juniper Ii Class A) Start Date:2021-12-23
JUPWW (Jupiter Wellness Warrant) Start Date:2020-10-30
JVA (Coffee Holding Co.) Start Date:2007-05-16
JWEL (Jowell Global) Start Date:2021-03-17
JWN (Nordstrom) Start Date:2005-01-03
JXJT (Jx Luxventure) Start Date:2013-03-07
JXN (Jackson Financial) Start Date:2021-09-01
JYD (Jayud Global Logistics Limited) Start Date:2023-04-21
JYNT (The Joint) Start Date:2014-11-11
JZ (Jianzhi Education Technology) Start Date:2022-08-26
JZXN (Jiuzi Holdings) Start Date:2021-05-18
K (Kellogg Co.) Start Date:2005-01-03
KA (Kineta) Start Date:2016-02-11
KAI (Kadant) Start Date:2007-05-03
KALA (Kala Pharmaceuticals) Start Date:2017-07-20
KALU (Kaiser Aluminum) Start Date:2007-05-16
KALV (Kalvista Pharmaceuticals) Start Date:2015-04-09
KAMN (Kaman) Start Date:2007-05-07
KAR (Kar Auction Services) Start Date:2009-12-11
KARO (Karooooo) Start Date:2021-04-01
KAVL (Kaival Brands Innovations) Start Date:2021-07-29
KB (Kb Financial Inc) Start Date:2007-05-01
KBH (Kb Home) Start Date:2005-01-03
KBNT (Kubient) Start Date:2020-08-12
KBNTW (Kubient Warrant) Start Date:2020-08-12
KBR (Kbr) Start Date:2007-01-03
KC (Kingsoft Cloud Holdings Limited) Start Date:2020-05-08
KD (Kyndryl Holdings,) Start Date:2021-10-22
KDP (Keurig Dr Pepper) Start Date:2008-05-07
KE (Kimball Electronics Comm) Start Date:2014-11-03
KELYA (Kelly Services) Start Date:2007-05-08
KELYB (Kelly Services) Start Date:2008-01-18
KEN (Kenon Holdings Ltd.) Start Date:2015-01-12
KEP (Korea Electric Power) Start Date:2007-05-01
KEQU (Kewaunee Scientific) Start Date:2007-05-16
KERN (Akerna Corp) Start Date:2018-02-26
KERNW (Akerna Warrant) Start Date:2018-02-27
KEX (Kirby) Start Date:2007-04-27
KEY (Keycorp) Start Date:2005-01-03
KEYS (Keysight Technologies) Start Date:2014-11-03
KF (Korea Fund) Start Date:2007-05-16
KFFB (Kentucky First Federal Bancorp) Start Date:2007-05-16
KFRC (Kforce) Start Date:2007-05-04
KFS (Kingsway Financial Services) Start Date:2007-05-16
KFY (Korn Ferry) Start Date:2007-04-27
KGC (Kinross Gold Corporation) Start Date:2007-01-03
KGS (Kodiak Gas Services) Start Date:2023-06-29
KHC (Kraft Heinz Co) Start Date:2015-07-06
KIDS (Orthopediatrics) Start Date:2017-10-12
KIM (Kimco Realty) Start Date:2005-01-03
KIND (Nextdoor Holdings,) Start Date:2021-11-08
KINS (Kingstone Companies) Start Date:2009-07-02
KINZU (Kins Technology  Unit) Start Date:2020-12-15
KINZW (Kins Technology  Warrant) Start Date:2021-02-04
KIO (Kkr Income Opportunities Fund Common Shares) Start Date:2013-07-26
KIQ (Kelso Technologies Inc Ordinary Shares) Start Date:2014-10-14
KIRK (Kirkland's Commonstock) Start Date:2007-05-16
KITT (Nauticus Robotics) Start Date:2021-08-04
KKR (Kkr & Co.) Start Date:2010-07-15
KLAC (Kla-Tencor) Start Date:2005-01-03
KLDO (Kaleido Biosciences) Start Date:2019-02-28
KLG (Wk Kellogg Co.) Start Date:2023-09-27
KLIC (Kulicke & Soffa Industries Inc) Start Date:2007-04-27
KLR (Kaleyra) Start Date:2017-12-08
KLTR (Kaltura) Start Date:2021-07-21
KLXE (Klx Energy Services) Start Date:2018-08-29
KMB (Kimberly-Clark) Start Date:2005-01-03
KMDA (Kamada Ordinary Shares) Start Date:2013-05-31
KMF (Kayne Anderson Nextgen Energy & Infrastructure) Start Date:2010-11-24
KMI (Kinder Morgan) Start Date:2011-02-11
KMPR (Kemper) Start Date:2007-04-30
KMT (Kennametal) Start Date:2007-01-03
KMX (Carmax Inc) Start Date:2005-01-03
KN (Knowles Corp) Start Date:2014-03-03
KNDI (Kandi Technologies Inc) Start Date:2007-09-24
KNF (Knife River Corp) Start Date:2023-06-01
KNOP (Knot Offshore Partners Lp) Start Date:2013-10-04
KNSA (Kiniksa Pharmaceuticals) Start Date:2018-05-24
KNSL (Kinsale Capital) Start Date:2016-07-28
KNSW (Knightswan Acquisition Corporation) Start Date:2022-03-14
KNTE (Kinnate Biopharma) Start Date:2020-12-03
KNTK (Kinetik) Start Date:2017-05-02
KNW (Know Labs) Start Date:2022-09-16
KNX (Knight-Swift Transportation Holdings) Start Date:2010-12-16
KO (Coca-Cola Company) Start Date:2005-01-03
KOD (Kodiak Sciences) Start Date:2018-10-04
KODK (Eastman Kodak Co.) Start Date:2013-11-01
KOF (Coca Cola Femsa S.A.B. De C.V. American Depositary Shares Each Representing 10 Units) Start Date:2007-04-27
KOP (Koppers) Start Date:2007-05-04
KOPN (Kopin Corp) Start Date:2007-05-01
KORE (Kore Holdings) Start Date:2021-10-01
KOS (Kosmos Energy) Start Date:2011-05-11
KOSS (Koss) Start Date:2007-05-21
KPLT (Katapult Holdings,) Start Date:2019-12-30
KPLTW (Katapult Holdings Warrant) Start Date:2019-12-27
KPRX (Kiora Pharmaceuticals) Start Date:2015-07-27
KPTI (Karyopharm Therapeutics C) Start Date:2013-11-06
KR (Kroger Co.) Start Date:2005-01-03
KRBP (Kiromic Biopharma) Start Date:2020-10-16
KRC (Kilroy Realty Corporation) Start Date:2007-01-03
KREF (Kkr Real Estate Finance Trust) Start Date:2017-05-05
KRG (Kite Realty Trust) Start Date:2007-05-07
KRKR (36Kr Holdings American Depositary Shares) Start Date:2019-11-08
KRMD (Repro Med Systems) Start Date:2007-05-17
KRNL (Kernel Holdings) Start Date:2021-04-01
KRNLU (Kernel Holdings Units) Start Date:2021-02-03
KRNLW (Kernel Holdings Warrants) Start Date:2021-03-26
KRNT (Kornit Digital Ltd.) Start Date:2015-04-02
KRNY (Kearny Financial) Start Date:2007-05-10
KRO (Kronos Worldwide) Start Date:2007-05-16
KRON (Kronos Bio) Start Date:2020-10-09
KROS (Keros Therapeutics) Start Date:2020-04-08
KRP (Kimbell Royalty Partners, Lp Common Units Representing Partner Interests) Start Date:2017-02-03
KRRO (Korro Bio Inc) Start Date:2019-10-03
KRT (Karat Packaging) Start Date:2021-04-15
KRTX (Karuna Therapeutics) Start Date:2019-06-28
KRUS (Kura Sushi Usa) Start Date:2019-08-01
KRYS (Krystal Biotech) Start Date:2017-09-20
KSCP (Knightscope Class A) Start Date:2022-01-27
KSICU (Kadem Sustainable Impact Unit) Start Date:2021-03-17
KSM (Dws Strategic Municipal Income Trust) Start Date:2007-05-16
KSS (Kohl's) Start Date:2005-01-03
KT (Kt Corporation) Start Date:2010-01-04
KTB (Kontoor Brands) Start Date:2019-05-09
KTCC (Key Tronic) Start Date:2007-05-16
KTF (Dws Municipal Income Trust) Start Date:2007-05-16
KTOS (Kratos Defense & Security) Start Date:2007-09-17
KTRA (Kintara Therapeutics) Start Date:2013-02-22
KTTA (Pasithea Therapeutics) Start Date:2021-09-15
KTTAW (Pasithea Therapeutics Warrant) Start Date:2021-09-15
KUKE (Kuke Music Holding) Start Date:2021-01-12
KULR (Kulr Technology) Start Date:2018-07-18
KURA (Kura Oncology) Start Date:2015-11-05
KVAC (Keen Vision Acquisition Corporation) Start Date:2023-09-15
KVHI (Kvh Industries) Start Date:2007-05-07
KVUE (Kenvue) Start Date:2023-05-04
KVYO (Klaviyo) Start Date:2023-09-20
KW (Kennedy-Wilson Holdings) Start Date:2010-03-19
KWE (Kwesst Micro Systems) Start Date:2022-12-07
KWR (Quaker Chemical) Start Date:2007-05-16
KXIN (Kaixin Auto Holdings Ordinary Shares) Start Date:2017-11-06
KYCH (Keyarch Acquisition Corporation) Start Date:2022-03-04
KYMR (Kymera Therapeutics) Start Date:2020-08-21
KYN (Kayne Anderson Energy Infrastructure Fund) Start Date:2007-05-04
KZIA (Kazia Therapeutics American Depositary Shares) Start Date:2013-02-11
KZR (Kezar Life Sciences) Start Date:2018-06-21
L (Loews) Start Date:2007-04-27
LAAC (Lithium Americas) Start Date:2008-10-28
LAB (Standard Biotools) Start Date:2022-04-06
LABP (Landos Biopharma) Start Date:2021-02-04
LAC (Lithium Americas Corp) Start Date:2023-09-21
LAD (Lithia Motors) Start Date:2007-05-01
LADR (Ladder Capital Corp) Start Date:2014-02-06
LAES (Sealsq Corp) Start Date:2023-05-22
LAKE (Lakeland Industries) Start Date:2007-05-16
LAMR (Lamar Advertising Company) Start Date:2007-01-03
LANC (Lancaster Colony) Start Date:2007-04-30
LAND (Gladstone Land Com) Start Date:2013-01-29
LANDM (Gladstone Land 5.00% Series D Cumulative Term Preferred Stock) Start Date:2021-01-25
LANV (Lanvin Holdings) Start Date:2022-12-15
LARK (Landmark Bancorp) Start Date:2007-05-16
LASE (Laser Photonics) Start Date:2022-09-30
LASR (Nlight) Start Date:2018-04-26
LATG (Latamgrowth SPAC Class A) Start Date:2022-03-18
LATGU (Latamgrowth SPAC Unit) Start Date:2022-01-25
LAUR (Laureate Education) Start Date:2017-02-01
LAW (Cs Disco) Start Date:2021-07-21
LAZ (Lazard Ltd) Start Date:2007-01-03
LAZR (Luminar Technologies, Class A) Start Date:2020-12-03
LAZY (Lazydays Holdings) Start Date:2018-03-16
LBAI (Lakeland Bancorp) Start Date:2007-05-08
LBBB (Lakeshore Acquisition Ii) Start Date:2022-04-14
LBC (Luther Burbank) Start Date:2017-12-08
LBPH (Longboard Pharmaceuticals) Start Date:2021-03-12
LBRDA (Liberty Broadband) Start Date:2014-11-04
LBRDK (Liberty Broadband Corporation) Start Date:2014-11-04
LBRDP (Liberty Broadband Series A Cumulative Redeemable Preferred Stock) Start Date:2020-12-22
LBRT (Liberty Oilfield Services) Start Date:2018-01-12
LBTYA (Liberty Global Plc) Start Date:2007-01-03
LBTYB (Liberty Global Plc Class B) Start Date:2007-05-16
LBTYK (Liberty Global Plc Class C) Start Date:2005-09-08
LC (Lendingclub Corp) Start Date:2014-12-11
LCA (Landcadia Holdings Iv Class A) Start Date:2021-05-18
LCAHU (Landcadia Holdings Iv Units) Start Date:2021-03-25
LCAHW (Landcadia Holdings Iv Warrant) Start Date:2021-05-18
LCFY (Locafy Ordinary Share) Start Date:2022-03-25
LCID (Lucid ,) Start Date:2020-09-18
LCII (Lci Industries) Start Date:2017-01-03
LCIN (Lannett Co Inc) Start Date:2013-12-13
LCNB (Lcnb) Start Date:2007-05-16
LCTX (Lineage Cell Therapeutics) Start Date:2007-05-16
LCUT (Lifetime Brands) Start Date:2007-05-04
LCW (Learn Cw Investment Class A Ordinary Shares) Start Date:2021-11-29
LDHAU (Ldh Growth I Units) Start Date:2021-03-19
LDI (Loandepot) Start Date:2021-02-11
LDOS (Leidos Holdings) Start Date:2007-04-27
LDP (Cohen & Steers Duration Preferred And Income Fund) Start Date:2012-07-27
LDTC (Leddartech Holdings Inc) Start Date:2021-03-01
LDWY (Lendway Inc) Start Date:2007-05-16
LE (Lands End) Start Date:2014-03-20
LEA (Lear) Start Date:2009-11-20
LECO (Lincoln Electric Holdings) Start Date:2007-01-03
LEDS (Semileds) Start Date:2010-12-09
LEE (Lee Enterprises Incorporated) Start Date:2007-04-30
LEG (Leggett & Platt) Start Date:2005-01-03
LEGAU (Lead Edge Growth Opportunities Units) Start Date:2021-03-23
LEGAW (Lead Edge Growth Opportunities Warrant) Start Date:2021-05-17
LEGH (Legacy Housing) Start Date:2018-12-14
LEGN (Legend Biotech Corporation) Start Date:2020-06-05
LEJU (Leju Holdings American Depositary Shares Each Representing One Ordinary Share) Start Date:2014-04-17
LEN (Lennar) Start Date:2005-01-03
LEN.B (Lennar) Start Date:2007-05-01
LEO (Bny Mellon Strategic Municipals) Start Date:2007-05-16
LESL (Leslie's) Start Date:2020-11-02
LEU (Centrus Energy) Start Date:2014-09-30
LEV (The Lion Electric Company) Start Date:2021-05-07
LEVI (Levi Strauss & Co.) Start Date:2019-03-21
LEXX (Lexaria Bioscience) Start Date:2021-01-12
LEXXW (Lexaria Bioscience Warrant) Start Date:2021-01-12
LFCR (Lifecore Biomedical) Start Date:2007-05-11
LFLY (Leafly Holdings) Start Date:2019-12-13
LFLYW (Leafly Holdings Warrant) Start Date:2022-02-07
LFMD (Lifemd) Start Date:2021-02-22
LFST (Lifestance Health) Start Date:2021-06-10
LFT (Lument Finance Trust) Start Date:2013-03-22
LFUS (Littelfuse) Start Date:2007-05-02
LFVN (Lifevantage Corp) Start Date:2012-09-12
LGCB (Linkage Global Inc) Start Date:2023-12-19
LGF.A (Lions Gate Entertainment) Start Date:2007-08-01
LGF.B (Lions Gate Entertainment) Start Date:2007-08-01
LGHL (Lion Holding American Depositary Share) Start Date:2020-06-16
LGHLW (Lion Holding Warrant) Start Date:2019-06-21
LGI (Lazard Global Total Return And Income Fund) Start Date:2007-05-16
LGIH (Lgi Homes) Start Date:2013-11-07
LGL (Lgl) Start Date:2007-05-16
LGMK (Logicmark) Start Date:2013-08-23
LGND (Ligand Pharmaceuticals) Start Date:2007-05-02
LGO (Largo Common Shares) Start Date:2021-04-19
LGTOU (Legato Merger Ii Unit) Start Date:2021-11-22
LGTOW (Legato Merger Ii Warrants) Start Date:2021-12-22
LGVC (Lamf Global Ventures I Class A Ordinary Shares) Start Date:2022-01-03
LGVCU (Lamf Global Ventures I Unit) Start Date:2021-11-11
LGVN (Longeveron) Start Date:2021-02-12
LH (Laboratory Of America Holding) Start Date:2005-01-03
LHC (Leo Holdings Ii Class A Ordinary Shares) Start Date:2021-03-01
LHDX (Lucira Health) Start Date:2021-02-05
LHX (L3harris Technologies) Start Date:2007-05-01
LI (Li Auto) Start Date:2020-07-30
LIAN (Lianbio American Depositary Shares) Start Date:2021-11-01
LICN (Lichen China) Start Date:2023-02-06
LICY (Li-Cycle Holdings) Start Date:2021-08-11
LIDR (Aeye Class A) Start Date:2021-01-11
LIDRW (Aeye Warrant) Start Date:2021-01-06
LIFE (Atyr Pharma) Start Date:2015-05-07
LIFW (Msp Recovery Class A) Start Date:2020-10-21
LII (Lennox International) Start Date:2007-01-03
LILA (Liberty Latin America) Start Date:2015-07-10
LILAK (Liberty Latin America Ltd.) Start Date:2015-06-23
LILM (Lilium N.V.) Start Date:2021-09-15
LILMW (Lilium N.V. Warrants) Start Date:2021-09-15
LIN (Linde Plc) Start Date:2018-10-29
LINC (Lincoln Educational Services) Start Date:2007-05-07
LIND (Lindblad Expeditions) Start Date:2013-07-03
LINK (Interlink Electronics) Start Date:2007-05-16
LIONU (Lionheart Iii Unit) Start Date:2021-11-04
LIONW (Lionheart Iii Warrant) Start Date:2021-12-07
LIPO (Lipella Pharmaceuticals) Start Date:2022-12-20
LIQT (Liqtech International) Start Date:2011-08-25
LITB (Lightinthebox Holding Co. American Depositary Shares Each Representing 2 Ordinary Shares) Start Date:2013-06-06
LITE (Lumentum Holdings) Start Date:2015-07-23
LITM (Snow Lake Resources) Start Date:2021-11-19
LITTU (Logistics Innovation Technologies Units) Start Date:2021-06-11
LITTW (Logistics Innovation Technologies Warrant) Start Date:2021-08-11
LIVB (Liv Capital Acquisition Ii) Start Date:2022-03-15
LIVE (Live Ventures Incorporated) Start Date:2015-10-09
LIVN (Livanova Plc) Start Date:2015-10-19
LIXT (Lixte Biotechnology Holdings) Start Date:2020-11-25
LIXTW (Lixte Biotechnology Holdings Warrants) Start Date:2020-11-25
LIZI (Lizhi American Depositary Shares) Start Date:2020-01-17
LKCO (Luokung Technology Ordinary Shares) Start Date:2019-01-08
LKFN (Lakeland Financial) Start Date:2007-05-16
LKQ (Lkq Corporation) Start Date:2007-04-27
LL (Lumber Liquidators) Start Date:2010-01-04
LLAP (Terran Orbital) Start Date:2021-04-26
LLL (Jx Luxventure) Start Date:2017-06-01
LLY (Lilly) Start Date:2005-01-03
LMAT (Lemaitre Vascular) Start Date:2007-05-16
LMB (Limbach Holdings) Start Date:2016-11-16
LMDX (Lumiradx Common Shares) Start Date:2021-09-29
LMDXW (Lumiradx Warrant) Start Date:2021-09-29
LMFA (Lm Funding America) Start Date:2015-12-08
LMND (Lemonade Inc) Start Date:2020-07-02
LMNL (Liminal Biosciences Common Shares) Start Date:2019-11-18
LMNR (Limoneira Co) Start Date:2007-05-22
LMPX (Lmp Automotive Holdings) Start Date:2019-12-05
LMT (Lockheed Martin) Start Date:2005-01-03
LNC (Lincoln National) Start Date:2005-01-03
LND (Brasilagro Brazilian Agric Real Estate Co Sponsored ADR) Start Date:2012-11-08
LNDC (Landec) Start Date:2007-05-11
LNG (Cheniere Energy) Start Date:2007-01-03
LNKB (Linkbancorp) Start Date:2022-09-13
LNN (Lindsay) Start Date:2007-05-01
LNSR (Lensar) Start Date:2020-10-02
LNT (Alliant Energy Corp) Start Date:2005-01-03
LNTH (Lantheus) Start Date:2015-06-25
LNW (Light & Wonder) Start Date:2007-05-02
LNZA (Lanzatech Global) Start Date:2021-09-24
LOAN (Manhattan Bridge Capital Inc) Start Date:2008-07-29
LOB (Live Oak Bancshares) Start Date:2015-07-23
LOCL (Local Bounti) Start Date:2021-11-22
LOCO (El Pollo Loco  C) Start Date:2014-07-25
LODE (Comstock) Start Date:2007-05-16
LOGI (Logitech International Sa) Start Date:2012-09-24
LOMA (Loma Negra Compania Industrial Argentina Sociedad Anonima ADS) Start Date:2017-11-01
LOOP (Loop Industries) Start Date:2015-11-11
LOPE (Grand Canyon Education) Start Date:2008-11-20
LOTZW (Carlotz Warrant) Start Date:2019-04-15
LOVE (The Lovesac Company) Start Date:2018-06-27
LOVLY (Spark Networks Se) Start Date:2017-11-17
LOW (Lowe's Cos.) Start Date:2005-01-03
LPCN (Lipocine) Start Date:2014-03-21
LPG (Dorian Lpg) Start Date:2014-05-08
LPI (Laredo Petroleum,) Start Date:2011-12-15
LPL (Lg Display Co. Ltd.) Start Date:2007-01-03
LPLA (Lpl Financial Holdings) Start Date:2010-11-18
LPRO (Open Lending Class A) Start Date:2020-06-11
LPSN (Liveperson) Start Date:2007-01-03
LPTH (Lightpath Technologies Class A) Start Date:2007-05-16
LPTV (Loop Media) Start Date:2022-09-21
LPTX (Leap Therapeutics) Start Date:2017-01-25
LPX (Louisiana-Pacific Corporation) Start Date:2007-01-03
LQDA (Liquidia Corp) Start Date:2018-07-26
LQDT (Liquidity Service) Start Date:2007-05-02
LQR (Lqr House) Start Date:2023-08-10
LRCX (Lam Research) Start Date:2005-01-03
LRE (Lead Real Estate Co.) Start Date:2023-09-27
LRFC (Logan Ridge Finance) Start Date:2013-09-25
LRHC (La Rosa Holdings) Start Date:2023-10-10
LRMR (Larimar Therapeutics) Start Date:2014-06-19
LRN (Stride) Start Date:2007-12-14
LSAK (Lesaka Technologies) Start Date:2007-04-30
LSBK (Lake Shore Bancorp) Start Date:2007-05-16
LSCC (Lattice Semiconductor Corporation) Start Date:2007-01-03
LSDI (Lucy Scientific Discovery) Start Date:2023-02-09
LSEA (Landsea Homes) Start Date:2018-06-29
LSEAW (Landsea Homes Warrant) Start Date:2018-06-29
LSF (Laird Superfood) Start Date:2020-09-23
LSPD (Lightspeed Commerce) Start Date:2020-09-11
LSTA (Lisata Therapeutics) Start Date:2007-08-09
LSTR (Landstar System) Start Date:2007-01-03
LSXMA (The Liberty Siriusxm) Start Date:2016-04-18
LSXMB (Liberty Media Series B Liberty Siriusxm) Start Date:2016-04-21
LSXMK (The Liberty Siriusxm) Start Date:2016-04-18
LTBR (Lightbridge) Start Date:2009-10-09
LTC (Ltc Properties) Start Date:2007-05-01
LTCHW (Latch Warrant Expiring 6/4/2026) Start Date:2020-12-31
LTH (Life Time Holdings,) Start Date:2021-10-07
LTHM (Livent Corp) Start Date:2018-10-11
LTRN (Lantern Pharma) Start Date:2020-06-11
LTRPA (Liberty Tripadvisor) Start Date:2014-08-27
LTRPB (Liberty Tripadvisor Holdings, Series B) Start Date:2014-08-29
LTRX (Lantronix) Start Date:2007-05-16
LTRY (Lottery.com,) Start Date:2018-06-13
LTRYW (Lottery.com Warrants) Start Date:2021-11-01
LU (Lucent Technology) Start Date:2020-11-02
LUCD (Lucid Diagnostics) Start Date:2021-10-14
LUCY (Innovative Eyewear) Start Date:2022-08-15
LULU (Lululemon Athletica) Start Date:2007-07-30
LUMN (Lumen Technologies) Start Date:2007-04-30
LUMO (Lumos Pharma) Start Date:2011-11-11
LUNA (Luna Innovations) Start Date:2007-05-16
LUNG (Pulmonx) Start Date:2020-10-01
LUV (Southwest Airlines) Start Date:2005-01-03
LUXH (Luxurban Hotels) Start Date:2007-05-11
LVLU (Lulu's Fashion Lounge Holdings,) Start Date:2021-11-11
LVO (Liveone) Start Date:2017-12-14
LVOX (Livevox Holding, Class A) Start Date:2019-04-18
LVOXU (Livevox Holdings Unit) Start Date:2019-03-08
LVRAU (Levere Holdings Unit) Start Date:2021-03-19
LVS (Las Vegas Sands) Start Date:2007-04-27
LVTX (Lava Therapeutics Nv) Start Date:2021-03-25
LVWR (Livewire) Start Date:2020-11-23
LW (Lamb Weston Holdings Inc) Start Date:2016-11-01
LWAY (Lifeway Foods) Start Date:2007-05-16
LWLG (Lightwave Logic,) Start Date:2008-03-10
LX (Lexinfintech Holdings American Depositary Shares) Start Date:2017-12-21
LXEH (Lixiang Education) Start Date:2020-10-01
LXEO (Lexeo Therapeutics) Start Date:2023-11-03
LXFR (Luxfer) Start Date:2012-10-03
LXP (Lexington Realty Trust) Start Date:2007-01-03
LXRX (Lexicon Pharmaceuticals) Start Date:2007-05-16
LXU (Lsb Industries) Start Date:2007-05-16
LYB (Lyondellbasell) Start Date:2010-10-14
LYEL (Lyell Immunopharma,) Start Date:2021-06-17
LYFT (Lyft) Start Date:2019-03-29
LYG (Lloyds Banking Plc) Start Date:2007-01-03
LYL (Dragon Victory International Ordinary Shares) Start Date:2017-10-20
LYLT (Loyalty Ventures) Start Date:2021-11-02
LYRA (Lyra Therapeutics) Start Date:2020-05-01
LYT (Lytus Technologies Holdings Ptv. Common Shares) Start Date:2022-06-15
LYTS (Lsi Industries) Start Date:2007-05-01
LYV (Live Nation Entertainment) Start Date:2006-01-03
LZ (Legalzoom.com) Start Date:2021-06-30
LZB (La-Z-Boy) Start Date:2007-04-25
LZM (Lifezone Metals Ltd.) Start Date:2021-12-13
M (Macy's) Start Date:2007-06-01
MA (Mastercard) Start Date:2006-05-25
MAA (Mid-America Apartments) Start Date:2005-01-03
MAC (Macerich) Start Date:2005-01-03
MACK (Merrimack Pharmaceuticals) Start Date:2012-03-29
MAG (Mag Silver) Start Date:2007-07-09
MAIA (Maia Biotechnology) Start Date:2022-07-28
MAIN (Main Street Capital Corporation) Start Date:2007-10-08
MAMA (Mama's Creations Inc) Start Date:2013-05-22
MAN (Manpowergroup) Start Date:2007-01-03
MANH (Manhattan Associates) Start Date:2007-01-03
MANU (Manchester United Plc) Start Date:2012-08-10
MAPS (Wm Technology, Class A) Start Date:2019-10-01
MAPSW (Wm Technology Warrants) Start Date:2019-10-01
MAR (Marriott Int'l.) Start Date:2005-01-03
MARA (Marathon Digital Holdings,) Start Date:2014-07-28
MARK (Remark Holdings) Start Date:2007-10-03
MARPS (Marine Petroleum Trust Units Of Beneficial Interest) Start Date:2007-05-16
MARX (Mars Acquisition) Start Date:2023-03-14
MAS (Masco) Start Date:2005-01-03
MASI (Masimo Corporation) Start Date:2007-08-08
MASS (908 Devices) Start Date:2020-12-18
MAT (Mattel) Start Date:2005-01-03
MATH (Metalpha Technology Holding) Start Date:2017-10-20
MATV (Mativ Holdings) Start Date:2007-05-02
MATW (Matthews International) Start Date:2007-05-02
MATX (Matson) Start Date:2012-07-02
MAV (Pioneer Municipal High Income Advantage Fund) Start Date:2007-05-16
MAX (Mediaalpha) Start Date:2020-11-02
MAXN (Maxeon Solar) Start Date:2020-12-15
MAYS (J. W. Mays) Start Date:2007-05-18
MBC (Masterbrand) Start Date:2022-12-09
MBCN (Middlefield Banc Cmn) Start Date:2007-05-16
MBI (Mbia) Start Date:2005-01-03
MBIN (Merchants Bancorp) Start Date:2017-10-27
MBINN (Merchants Bancorp Depositary Shares Preferred Series C) Start Date:2021-03-23
MBINO (Merchants Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series B Fixed-To-Floating Rate) Start Date:2019-08-20
MBINP (Merchants Bancorp 7.00% Fixed-To-Floating Rate Series A Non-Cumulative Perpetual Preferred Stock) Start Date:2019-03-29
MBIO (Mustang Bio) Start Date:2017-08-22
MBLY (Mobileye Global) Start Date:2022-10-26
MBNKP (Medallion Bank Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series F) Start Date:2019-12-18
MBOT (Microbot Medical) Start Date:2007-04-27
MBRX (Moleculin Biotech) Start Date:2016-06-02
MBUU (Malibu Boats  Com) Start Date:2014-01-31
MBWM (Mercantile Bank) Start Date:2007-05-16
MC (Moelis & Company) Start Date:2014-04-16
MCAC (Monterey Capital Acquisition Corporation) Start Date:2022-07-01
MCB (Metropolitan Bank Hldg Corp) Start Date:2017-11-08
MCBC (Macatawa Bank) Start Date:2007-05-16
MCBS (Metrocity Bankshares) Start Date:2019-10-03
MCD (Mcdonald's) Start Date:2005-01-03
MCFT (Mastercraft Boat) Start Date:2015-07-17
MCHP (Microchip Technology) Start Date:2005-01-03
MCHX (Marchex Class B) Start Date:2007-05-01
MCI (Barings Corporate Investors) Start Date:2007-05-16
MCK (Mckesson) Start Date:2005-01-03
MCLD (Mcloud Technologies Common Shares) Start Date:2021-11-24
MCN (Madison Covered Call & Equity Strategy Fund) Start Date:2007-05-16
MCO (Moody's Corp) Start Date:2005-01-03
MCOM (Micromobilitycom Inc) Start Date:2019-12-09
MCR (Mfs Charter Income Trust) Start Date:2007-05-16
MCRB (Seres Therapeutics) Start Date:2015-06-26
MCRI (Monarch Casino & Resort) Start Date:2007-04-30
MCS (Marcus) Start Date:2007-05-01
MCVT (Mill City Ventures Iii) Start Date:2009-05-27
MCW (Mister Car Wash) Start Date:2021-06-25
MCY (Mercury General Corporation) Start Date:2007-01-03
MD (Mednax) Start Date:2009-01-02
MDB (Mongodb) Start Date:2017-10-19
MDBH (Mdb Capital Holdings) Start Date:2023-09-21
MDC (M.D.C. Holdings) Start Date:2007-01-03
MDGL (Madrigal Pharmaceuticals) Start Date:2007-05-16
MDGS (Medigus American Depositary Shares) Start Date:2015-08-05
MDGSW (Medigus Series C Warrant) Start Date:2018-07-23
MDIA (Mediaco Holding Class A) Start Date:2020-01-06
MDJH (Mdjm Ordinary Share) Start Date:2019-01-08
MDLZ (Mondelez International) Start Date:2007-04-30
MDNA (Medicenna Therapeutics Common Shares) Start Date:2020-08-24
MDRR (Medalist Diversified Reit) Start Date:2018-11-28
MDRRP (Medalist Diversified Reit Series A Cumulative Redeemable Preferred Stock) Start Date:2020-02-13
MDRX (Allscripts-Misys) Start Date:2007-04-27
MDT (Medtronic Plc) Start Date:2005-01-03
MDU (Mdu Resources) Start Date:2007-01-03
MDV (Modiv Class C) Start Date:2022-02-11
MDVL (Medavail Holdings) Start Date:2011-03-04
MDWD (Mediwound Ordinary Shares) Start Date:2014-03-20
MDWT (Midwest Holding) Start Date:2020-11-04
MDXG (Mimedx , Inc) Start Date:2008-04-02
MDXH (Mdxhealth Sa American Depositary Shares) Start Date:2021-11-04
ME (23Andme Holding Co. Class A) Start Date:2021-06-17
MEC (Mayville Engineering Co) Start Date:2019-05-09
MED (Medifast) Start Date:2007-04-25
MEDP (Medpace) Start Date:2016-08-11
MEDS (Trxade) Start Date:2020-02-13
MEG (Montrose Environmental) Start Date:2020-07-23
MEGI (Mainstay Cbre Global Infrastructure Megatrends Fund Common Shares) Start Date:2021-10-27
MEGL (Magic Empire Global) Start Date:2022-08-05
MEI (Methode Electronics) Start Date:2007-10-17
MEIP (Mei Pharma) Start Date:2007-05-16
MELI (Mercadolibre Inc) Start Date:2007-08-10
MEOH (Methanex Corp) Start Date:2007-05-01
MERC (Mercer International Inc) Start Date:2007-05-04
MESA (Mesa Air) Start Date:2018-08-10
MESO (Mesoblast American Depositary Shares) Start Date:2009-01-05
MET (Metlife) Start Date:2005-01-03
META (Meta Platforms) Start Date:2012-05-18
METC (Ramaco Resources,) Start Date:2017-02-03
METCB (Ramaco Resources Inc) Start Date:2023-06-16
METXW (Meten Holding Warrant) Start Date:2020-05-28
MF (Missfresh) Start Date:2021-06-25
MFA (Mfa Financial) Start Date:2007-04-24
MFC (Manulife Financial Corporation) Start Date:2007-01-03
MFD (Macquarie First Trust Global) Start Date:2007-05-16
MFG (Mizuho Financial) Start Date:2007-01-03
MFH (Mercurity Fintech Holding ADS) Start Date:2015-04-08
MFIC (Midcap Financial Investment) Start Date:2007-04-30
MFIN (Medallion Financial) Start Date:2007-05-11
MFM (Mfs Municipal Income Trust) Start Date:2007-05-16
MFV (Mfs Special Value Trust) Start Date:2007-05-16
MG (Mistras) Start Date:2009-10-08
MGA (Magna International) Start Date:2007-01-03
MGAM (Mobile Global Esports) Start Date:2022-07-29
MGEE (Mge Energy) Start Date:2007-05-04
MGF (Mfs Government Markets Income Trust) Start Date:2007-05-16
MGIC (Magic Software Enterprises Ltd) Start Date:2007-05-16
MGIH (Millennium International Holdings Limited) Start Date:2023-04-04
MGLD (The Marygold Companies) Start Date:2022-03-10
MGM (Mgm Resorts International) Start Date:2005-06-01
MGNI (Magnite,) Start Date:2020-06-30
MGNX (Macrogenics) Start Date:2013-10-10
MGOL (Mgo Global) Start Date:2023-01-13
MGPI (Mgp Ingredients) Start Date:2007-05-03
MGRC (Mcgrath Rentcorp) Start Date:2007-05-04
MGRX (Mangoceuticals,) Start Date:2023-03-21
MGTX (Meiragtx) Start Date:2018-06-08
MGU (Macquarie Global Infrastructure Total Return Fund) Start Date:2007-05-08
MGY (Magnolia Oil & Gas Corp) Start Date:2017-06-29
MGYR (Magyar Bancorp) Start Date:2007-05-16
MHD (Blackrock Muniholdings Fund) Start Date:2007-05-16
MHF (Western Asset Municipal High Income Fund) Start Date:2007-05-16
MHH (Mastech Digital) Start Date:2008-10-01
MHI (Pioneer Municipal High Income Fund) Start Date:2007-05-16
MHK (Mohawk Industries) Start Date:2005-01-03
MHLD (Maiden Holdings Ltd.) Start Date:2008-05-06
MHN (Blackrock Muniholdings New York Quality Fund) Start Date:2007-05-16
MHO (M/I Homes) Start Date:2007-05-02
MHUA (Meihua International Medical Technologies Co. Ordinary Shares) Start Date:2022-02-16
MI (Nft Ltd.) Start Date:2015-11-25
MICS (The Singing Machine Company) Start Date:2022-05-24
MIDD (The Middleby Corporation) Start Date:2007-01-03
MIGI (Mawson Infrastructure) Start Date:2021-06-21
MIMO (Airspan Networks Holdings) Start Date:2020-11-19
MIN (Mfs Intermediate Income Trust) Start Date:2007-05-04
MIND (Mind Technology) Start Date:2007-05-10
MINM (Minim) Start Date:2021-07-07
MIO (Pioneer Municipal High Income Opportunities Fund) Start Date:2021-08-06
MIR (Mirion Technologies,) Start Date:2020-08-20
MIRA (Mira Pharmaceuticals) Start Date:2023-08-03
MIRM (Mirum Pharmaceuticals) Start Date:2019-07-18
MIRO (Miromatrix Medical) Start Date:2021-06-24
MIST (Milestone Pharmaceuticals Common Shares) Start Date:2019-05-09
MITK (Mitek Systems) Start Date:2007-05-16
MITQ (Moving Image Technologies) Start Date:2021-07-08
MITT (Ag Mortgage Investment Trust) Start Date:2011-06-30
MIXT (Mix Telematics American Depositary Shares Each Representing 25 Ordinary Shares) Start Date:2013-08-09
MIY (Blackrock Muniyield Michigan Quality Fund) Start Date:2007-05-16
MKC (Mccormick & Co.) Start Date:2005-01-03
MKFG (Markforged Holding) Start Date:2020-10-08
MKL (Markel) Start Date:2007-05-02
MKSI (Mks Instruments) Start Date:2007-04-26
MKTW (Marketwise, Class A) Start Date:2021-07-22
MKTWW (Marketwise Warrant) Start Date:2021-07-22
MKTX (Marketaxess Holdings) Start Date:2005-01-03
MKUL (Molekule) Start Date:2021-11-24
MKULQ (Molekule Inc) Start Date:2021-11-24
ML (Moneylion) Start Date:2020-08-14
MLAB (Mesa Laboratories) Start Date:2007-05-16
MLCO (Melco Resorts & Entertainment Limited) Start Date:2011-12-07
MLEC (Moolec Science Sa) Start Date:2023-01-03
MLGO (Microalgo) Start Date:2022-12-13
MLI (Mueller Industries) Start Date:2007-04-27
MLKN (Millerknoll,) Start Date:2007-04-30
MLM (Martin Marietta Materials) Start Date:2007-04-30
MLNK (Meridianlink) Start Date:2021-07-28
MLP (Maui Land & Pineapple) Start Date:2007-05-16
MLR (Miller Industries) Start Date:2007-05-07
MLSS (Milestone Scientific) Start Date:2007-05-16
MLTX (Moonlake Immunotherapeutics Class A Ordinary Shares) Start Date:2022-04-06
MLYS (Mineralys Therapeutics) Start Date:2023-02-10
MMAT (Meta Materials) Start Date:2010-11-08
MMC (Marsh & Mclennan) Start Date:2005-01-03
MMD (Mainstay Mackay Definedterm Municipal Opportunities Fund) Start Date:2012-06-27
MMI (Marcus & Millichap) Start Date:2013-10-31
MMLP (Martin Midstream Partners L.P. Partnership) Start Date:2007-05-03
MMM (3M Company) Start Date:2005-01-03
MMP (Magellan Midstream Partners L.P.) Start Date:2007-01-03
MMS (Maximus) Start Date:2007-01-03
MMSI (Merit Medical Systems) Start Date:2007-01-03
MMT (Mfs Multimarket Income Trust) Start Date:2007-05-08
MMU (Western Asset Managed Municipals Fund) Start Date:2007-05-16
MMV (Multimetaverse Holdings Class A) Start Date:2021-06-08
MMYT (Makemytrip Limited) Start Date:2010-08-12
MNDO (Mind C.T.I. Ordinary Shares) Start Date:2007-05-16
MNDY (Monday.com) Start Date:2021-06-10
MNKD (Mannkind) Start Date:2007-04-27
MNKTQ (Mallinckrodt Plc) Start Date:2022-06-17
MNMD (Mind Medicine) Start Date:2021-04-27
MNOV (Medicinova) Start Date:2007-05-16
MNP (Western Asset Municipal Partners Fund) Start Date:2007-05-16
MNPR (Monopar Therapeutics) Start Date:2019-12-19
MNR (Mach Natural Resources Lp) Start Date:2023-10-25
MNRO (Monro) Start Date:2007-01-03
MNSB (Mainstreet Bancshares) Start Date:2007-05-17
MNSBP (Mainstreet Bancshares Depositary Shares) Start Date:2020-09-16
MNSO (Miniso Holding) Start Date:2020-10-15
MNST (Monster Beverage) Start Date:2005-01-03
MNTK (Montauk Renewables) Start Date:2021-01-22
MNTS (Momentus Class A) Start Date:2020-01-02
MNTSW (Momentus Warrant) Start Date:2019-12-30
MNTX (Manitex International) Start Date:2008-05-28
MNY (Moneyhero Ltd.) Start Date:2020-12-07
MO (Altria Inc) Start Date:2005-01-03
MOB (Mobilicom Ltd) Start Date:2022-08-25
MOBQ (Mobiquity Technologies) Start Date:2007-05-17
MOBQW (Mobiquity Technologies Warrant) Start Date:2021-12-09
MOD (Modine Manufacturing) Start Date:2007-05-07
MODD (Modular Medical) Start Date:2020-10-08
MODG (Topgolf Callaway Brands) Start Date:2007-05-01
MODN (Model N) Start Date:2013-03-20
MODV (Modivcare) Start Date:2007-04-25
MOFG (Midwestone Financial) Start Date:2008-03-18
MOG.A (Moog) Start Date:2007-04-30
MOGO (Mogo Common Shares) Start Date:2018-04-18
MOGU (Mogu American Depositary Shares) Start Date:2018-12-06
MOH (Molina Healthcare) Start Date:2007-01-03
MOHO (Ecmoho American Depositary Shares) Start Date:2019-11-08
MOLN (Molecular Partners) Start Date:2021-06-16
MOMO (Momo) Start Date:2014-12-11
MOND (Mondee Holdings Class A) Start Date:2021-03-24
MOR (Morphosys Ag American Depositary Shares) Start Date:2018-04-19
MORF (Morphic Holding) Start Date:2019-06-27
MORN (Morningstar) Start Date:2007-05-03
MOS (The Mosaic Company) Start Date:2011-05-20
MOTS (Motus Gi Holdings) Start Date:2018-02-14
MOV (Movado) Start Date:2007-05-07
MOVE (Movano) Start Date:2021-03-23
MP (Mp Materials) Start Date:2020-11-16
MPA (Blackrock Muniyield Pennsylvania Quality Fund) Start Date:2007-05-16
MPAA (Motorcar Parts Of America) Start Date:2007-05-16
MPB (Mid Penn Bancorp) Start Date:2008-08-01
MPC (Marathon Petroleum) Start Date:2011-06-23
MPLN (Multiplan Corporation) Start Date:2020-04-03
MPLX (Mplx Lp) Start Date:2012-10-26
MPTI (M-Tron Industries) Start Date:2022-10-03
MPU (Mega Matrix) Start Date:2007-05-16
MPV (Barings Participation Investors) Start Date:2007-05-16
MPW (Medical Properties Trust) Start Date:2007-01-03
MPWR (Monolithic Power Systems) Start Date:2007-01-03
MPX (Marine Products) Start Date:2007-05-01
MQ (Marqeta) Start Date:2021-06-09
MQT (Blackrock Muniyield Quality Fund Ii) Start Date:2007-05-16
MQY (Blackrock Muniyield Quality Fund) Start Date:2007-05-16
MRAI (Marpai Class A) Start Date:2021-10-27
MRAM (Everspin Technologies) Start Date:2016-10-07
MRBK (Meridian Bank) Start Date:2017-11-07
MRC (Mrc Global) Start Date:2012-04-12
MRCC (Monroe Capital) Start Date:2012-10-25
MRCY (Mercury Systems) Start Date:2007-01-03
MRDB (Mariadb Plc) Start Date:2022-12-19
MREO (Mereo Biopharma Plc American Depositary Shares) Start Date:2019-04-24
MRIN (Marin Software Incorporated) Start Date:2013-03-22
MRK (Merck & Co.) Start Date:2005-01-03
MRKR (Marker Therapeutics) Start Date:2016-11-08
MRM (Medirom Healthcare) Start Date:2020-12-29
MRNA (Moderna) Start Date:2018-12-07
MRNS (Marinus Pharmaceuticals) Start Date:2014-07-31
MRO (Marathon Oil) Start Date:2005-01-03
MRSN (Mersana Therapeutics) Start Date:2017-06-28
MRTN (Marten Transport) Start Date:2007-04-26
MRTX (Mirati Therapeutics) Start Date:2013-07-15
MRUS (Merus N.V. Common Shares) Start Date:2016-05-19
MRVI (Maravai Lifesciences) Start Date:2020-11-20
MRVL (Marvell Technology Ltd.) Start Date:2005-01-03
MS (Morgan Stanley) Start Date:2006-03-01
MSA (Msa Safety Incorporated) Start Date:2007-01-03
MSB (Mesabi Trust) Start Date:2007-05-03
MSBI (Midland States Bancorp) Start Date:2016-05-24
MSC (Studio City International Holdings American Depositary Shares Each Representing Four Class A Ordinary Shares) Start Date:2018-10-18
MSCI (MSCI Inc) Start Date:2007-11-15
MSD (Morgan Stanley Emerging Markets Debt Fund) Start Date:2007-05-07
MSEX (Middlesex Water) Start Date:2007-05-16
MSFT (Microsoft) Start Date:2005-01-03
MSGE (Madison Square Garden Entertainment Corp) Start Date:2023-04-21
MSGM (Motorsport Games) Start Date:2021-01-13
MSGS (Madison Square Garden Sports Corp) Start Date:2015-10-01
MSI (Motorola Solutions) Start Date:2010-12-17
MSM (Msc Industrial Direct Co.) Start Date:2007-01-03
MSN (Emerson Radio) Start Date:2007-05-16
MSPR (Msp Recovery Class A) Start Date:2022-05-24
MSPRW (Msp Recovery Warrant) Start Date:2022-05-24
MSPRZ (Msp Recovery Warrant) Start Date:2020-10-21
MSS (Maison Solutions) Start Date:2023-10-05
MSSA (Metal Sky Star Acquisition Corporation) Start Date:2022-05-31
MSTR (Microstrategy) Start Date:2007-04-26
MT (Arcelormittal) Start Date:2007-01-03
MTA (Metalla Royalty & Streaming Common Shares) Start Date:2020-01-08
MTB (M&T Bank) Start Date:2005-01-03
MTBC (Carecloud) Start Date:2014-07-23
MTBL (Moatable Inc) Start Date:2011-05-04
MTC (Mmtec Common Shares) Start Date:2019-01-08
MTCH (Match) Start Date:2015-11-19
MTD (Mettler Toledo) Start Date:2005-01-03
MTDR (Matador Resources) Start Date:2012-02-02
MTEK (Maris-Tech Ordinary Shares) Start Date:2022-02-02
MTEKW (Maris-Tech Warrants) Start Date:2022-02-02
MTEM (Molecular Templates) Start Date:2007-05-03
MTEX (Mannatech Incorporated) Start Date:2007-04-30
MTG (Mgic Investment Corporation) Start Date:2007-01-03
MTH (Meritage Homes Corporation) Start Date:2007-01-03
MTLS (Materialise Nv American Depositary Shares) Start Date:2014-06-25
MTMT (Mega Matrix) Start Date:2007-05-16
MTN (Vail Resorts) Start Date:2007-01-03
MTNB (Matinas Biopharma Holdings) Start Date:2014-07-21
MTR (Mesa Royalty Trust) Start Date:2007-05-16
MTRN (Materion) Start Date:2007-05-01
MTRX (Matrix Service) Start Date:2007-05-03
MTSI (Macom Technology Solutions Holdings) Start Date:2012-03-15
MTTR (Matterport, Class A) Start Date:2021-02-02
MTW (Manitowoc Company) Start Date:2005-01-03
MTX (Minerals Technologies) Start Date:2007-05-01
MTZ (Mastec) Start Date:2007-01-03
MU (Micron Technology) Start Date:2005-01-03
MUA (Blackrock Muniassets Fund Inc) Start Date:2007-05-16
MUC (Blackrock Muniholdings California Quality Fund) Start Date:2007-05-16
MUE (Blackrock Muniholdings Quality Fund Ii) Start Date:2007-05-16
MUFG (Mitsubishi Ufj Financial) Start Date:2018-04-02
MUI (Blackrock Municipal Income Fund) Start Date:2007-05-16
MUJ (Blackrock Muniholdings New Jersey Quality Fund) Start Date:2007-05-16
MULN (Mullen Automotive,) Start Date:2008-10-28
MUR (Murphy Oil Corporation) Start Date:2005-01-03
MURA (Mural Oncology Plc) Start Date:2023-11-06
MUSA (Murphy Usa) Start Date:2013-09-03
MUX (Mcewen Mining) Start Date:2007-05-16
MVBF (Mvb Financial) Start Date:2008-02-19
MVF (Blackrock Munivest Fund) Start Date:2007-05-16
MVIS (Microvision Inc) Start Date:2007-04-26
MVO (Mv Oil Trust Units Of Beneficial Interests) Start Date:2007-05-16
MVST (Microvast Holdings,) Start Date:2019-03-27
MVSTW (Microvast Holdings Warrants) Start Date:2019-03-27
MVT (Blackrock Munivest Fund Ii) Start Date:2007-05-16
MWA (Mueller Water Products) Start Date:2007-05-01
MWG (Multi Ways Holdings Limited) Start Date:2023-04-03
MX (Magnachip Semiconductor) Start Date:2011-03-11
MXC (Mexco Energy) Start Date:2007-05-16
MXCT (Maxcyte) Start Date:2021-07-30
MXE (Mexico Equity And Income Fund) Start Date:2007-05-16
MXF (Mexico Fund) Start Date:2007-05-09
MXL (Maxlinear) Start Date:2010-03-24
MYD (Blackrock Muniyield Fund) Start Date:2007-05-16
MYE (Myers Industries) Start Date:2007-05-02
MYFW (First Western Financial) Start Date:2018-07-19
MYGN (Myriad Genetics) Start Date:2007-04-30
MYI (Blackrock Muniyield Quality Fund Iii Inc) Start Date:2007-05-16
MYMD (Mymd Pharmaceuticals) Start Date:2020-01-02
MYN (Blackrock Muniyield New York Quality Fund common Stock) Start Date:2007-05-16
MYNA (Mynaric Ag ADS) Start Date:2021-11-12
MYND (Myndai Inc) Start Date:2022-05-24
MYNZ (Mainz Biomed B.V. Ordinary Shares) Start Date:2021-11-05
MYO (Myomo) Start Date:2017-06-12
MYPS (Playstudios, Class A) Start Date:2020-12-21
MYRG (Myr) Start Date:2008-09-09
MYSZ (My Size) Start Date:2016-07-25
MYTE (Myt Netherlands Parent B.V.) Start Date:2021-01-21
NA (Nano Labs Ltd) Start Date:2022-07-12
NAAS (Naas Technology American Depositary Shares) Start Date:2017-10-20
NABL (N-Able) Start Date:2021-07-20
NAC (Nuveen California Quality Municipal Income Fund) Start Date:2007-05-16
NAD (Nuveen Quality Municipal Income Fund) Start Date:2007-01-03
NAII (Natural Alternatives International) Start Date:2007-05-16
NAK (Northern Dynasty Minerals) Start Date:2007-05-07
NAMS (Newamsterdam Pharma) Start Date:2022-11-23
NAN (Nuveen New York Quality Municipal Income Fund) Start Date:2007-05-16
NAOV (Nanovibronix) Start Date:2015-05-28
NAPA (Duckhorn Portfolio) Start Date:2021-03-18
NARI (Inari Medical) Start Date:2020-05-22
NAT (Nordic American Tankers) Start Date:2007-05-03
NATH (Nathans Famous) Start Date:2007-05-16
NATI (National Instruments Corporation) Start Date:2007-01-03
NATL (Ncr Atleos Corp) Start Date:2023-10-11
NATR (Natures Sunshine Products) Start Date:2009-06-25
NAUT (Nautilus Biotechnolgy,) Start Date:2020-08-07
NAVB (Navidea Biopharmaceuticals) Start Date:2005-10-27
NAVI (Navient Corporation) Start Date:2014-04-17
NAZ (Nuveen Arizona Quality Municipal Income Fund) Start Date:2007-05-16
NBB (Nuveen Taxable Municipal Income Fund Common Shares Of Beneficial Interest) Start Date:2010-04-28
NBH (Neuberger Berman Municipal Fund) Start Date:2007-05-16
NBHC (National Bank) Start Date:2012-09-20
NBIX (Neurocrine Biosciences) Start Date:2007-01-03
NBN (Northeast Bancorp) Start Date:2007-05-16
NBO (Neuberger Berman New York Municipal Fund) Start Date:2007-05-16
NBR (Nabors Industries Ltd.) Start Date:2005-11-03
NBRV (Nabriva Therapeutics Plc Ordinary Shares Ireland) Start Date:2015-09-18
NBSE (Neubase Therapeutics) Start Date:2019-07-15
NBTB (Nbt Bancorp) Start Date:2007-05-07
NBTX (Nanobiotix) Start Date:2020-12-11
NBW (Neuberger Berman California Municipal Fund Inc) Start Date:2007-05-16
NBXG (Neuberger Berman Next Generation Connectivity Fund) Start Date:2021-05-26
NBY (Novabay Pharmaceuticals) Start Date:2007-10-26
NC (Nacco Industries) Start Date:2007-05-08
NCA (Nuveen California Municipal Value Fund) Start Date:2007-05-16
NCL (Northann) Start Date:2023-10-19
NCLH (Norwegian Cruise Line) Start Date:2013-01-18
NCMI (National Cinemedia) Start Date:2007-05-16
NCNA (Nucana Plc American Depositary Share) Start Date:2017-09-28
NCNC (Noco-Noco Inc) Start Date:2022-07-06
NCNO (Ncino) Start Date:2020-07-14
NCPL (Netcapital) Start Date:2007-05-29
NCRA (Nocera) Start Date:2007-05-30
NCSM (Ncs Multistage Holdings) Start Date:2017-04-28
NCTY (The9 ADS) Start Date:2007-04-23
NCV (Virtus Convertible & Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
NCZ (Virtus Convertible & Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-08
NDAQ (Nasdaq) Start Date:2005-02-10
NDLS (Noodles & Co) Start Date:2013-06-28
NDMO (Nuveen Dynamic Municipal Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2020-08-27
NDP (Tortoise Energy Independence Fund) Start Date:2012-07-27
NDRA (Endra Life Sciences) Start Date:2017-06-30
NDSN (Nordson Corporation) Start Date:2007-01-03
NE (Noble Corporation) Start Date:2021-06-09
NEA (Nuveen Amt-Free Quality Municipal Income Fund) Start Date:2007-01-03
NECB (Northeast Community Bancorp) Start Date:2021-07-13
NEE (Nextera Energy) Start Date:2007-04-30
NEGG (Newegg Commerce, Common Shares) Start Date:2010-06-14
NEM (Newmont Mining Corporation) Start Date:2005-01-03
NEN (New England Realty Associates Partnership Class A Depositary Receipts Evidencing Units Of Partnership) Start Date:2007-05-16
NEO (Neogenomics) Start Date:2012-12-10
NEOG (Neogen) Start Date:2007-05-16
NEON (Neonode) Start Date:2007-08-13
NEOV (Neovolta) Start Date:2020-05-20
NEP (Nextera Energy Partners Lp) Start Date:2014-06-27
NEPH (Nephros) Start Date:2009-01-22
NEPT (Neptune Wellness Solutions Ordinary Shares) Start Date:2007-08-13
NERV (Minerva Neurosciences Com) Start Date:2014-07-01
NESRW (National Energy Services Reunited Warrant) Start Date:2017-06-05
NET (Cloudflare) Start Date:2019-09-13
NETD (Nabors Energy Transition Ii) Start Date:2023-09-05
NETI (Eneti) Start Date:2013-12-12
NEU (Newmarket) Start Date:2007-05-01
NEWP (New Pacific Metals Common Shares) Start Date:2021-05-20
NEWR (New Relic) Start Date:2014-12-12
NEWT (Newtek Business Services Corp) Start Date:2007-05-16
NEX (Nextier Oilfield Solutions) Start Date:2019-10-31
NEXA (Nexa Resources S.A. Common Shares) Start Date:2017-10-27
NEXI (Neximmune) Start Date:2021-02-12
NEXT (Nextdecade Corp) Start Date:2015-06-04
NFBK (Northfield Bancorp) Start Date:2007-11-08
NFE (New Fortress Energy Class A) Start Date:2019-01-31
NFG (National Fuel Gas Company) Start Date:2007-01-03
NFGC (New Found Gold Common Shares) Start Date:2021-09-29
NFJ (Virtus Dividend Interest & Premium Strategy Fund Common Shares Of Beneficial Interest) Start Date:2007-04-23
NFLX (Netflix) Start Date:2005-01-03
NFTG (The Nft Gaming) Start Date:2023-02-15
NG (Novagold Resources) Start Date:2007-01-03
NGD (New Gold) Start Date:2007-05-16
NGG (National Grid Plc) Start Date:2007-01-03
NGL (Ngl Energy Partners Lp Common Units Representing Partner Interests) Start Date:2011-05-12
NGM (Ngm Biopharmaceuticals) Start Date:2019-04-04
NGMS (Neogames S.A.) Start Date:2020-11-19
NGNE (Neurogene Inc) Start Date:2014-03-12
NGS (Natural Gas Services) Start Date:2007-04-26
NGVC (Natural Grocers) Start Date:2012-07-25
NGVT (Ingevity Corporation) Start Date:2016-05-02
NHC (National Healthcare) Start Date:2007-05-16
NHI (National Health Investors) Start Date:2007-01-03
NHICU (Newhold Investment Ii Unit) Start Date:2021-10-21
NHICW (Newhold Investment Ii Warrant) Start Date:2021-12-27
NHS (Neuberger Berman High Yield Strategies Fund) Start Date:2008-12-19
NHTC (Natural Health Trends) Start Date:2007-05-16
NHWK (Nighthawk Biosciences) Start Date:2013-07-24
NI (Nisource) Start Date:2005-01-03
NIC (Nicolet Bankshares) Start Date:2013-05-17
NICE (Nice American Depositary Shares) Start Date:2007-05-03
NICK (Nicholas Financial) Start Date:2007-05-16
NID (Nuveen Intermediate Duration Municipal Term Fund Common Shares Of Beneficial Interest) Start Date:2012-12-06
NIE (Virtus Equity & Convertible Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
NILE (Bitnile) Start Date:2007-05-16
NIM (Nuveen Select Maturities Municipal Fund) Start Date:2007-05-16
NIMC (Nisource Inc Series A Corporate Units) Start Date:2021-04-22
NINE (Nine Energy Service) Start Date:2018-01-19
NIO (Nio) Start Date:2018-09-12
NIQ (Nuveenn Intermediate Duration Quality Municipal Term Fund Common Shares Of Beneficial Interest) Start Date:2013-08-02
NISN (Nisun International Enterprise Development Co. Class A Common Shares) Start Date:2016-12-27
NIU (Niu Technologies American Depositary Shares) Start Date:2018-10-19
NJR (New Jersey Resources Corporation) Start Date:2007-01-03
NKE (Nike) Start Date:2005-01-03
NKG (Nuveen Georgia Quality Municipal Income Fund) Start Date:2007-05-16
NKLA (Nikola Corporation) Start Date:2018-06-11
NKSH (National Bankshares) Start Date:2007-05-16
NKTR (Nektar Therapeutics) Start Date:2005-01-03
NKTX (Nkarta) Start Date:2020-07-13
NKX (Nuveen California Amt-Free Quality Municipal Income Fund) Start Date:2007-05-16
NL (Nl Industries) Start Date:2007-04-30
NLOK (Nortonlifelock) Start Date:2007-04-27
NLSP (Nls Pharmaceutics) Start Date:2021-01-29
NLSPW (Nls Pharmaceutics Warrant) Start Date:2021-01-29
NLY (Annaly Capital Management) Start Date:2007-01-03
NM (Navios Maritime Holdings) Start Date:2007-05-14
NMAI (Nuveen Multi-Asset Income Fund Common Shares Of Beneficial Interest) Start Date:2021-11-22
NMCO (Nuveen Municipal Credit Opportunities Fund Common Shares) Start Date:2019-09-17
NMFC (New Mountain Finance Corporation) Start Date:2011-05-20
NMG (Nouveau Monde Graphite Common Shares) Start Date:2021-05-24
NMI (Nuveen Municipal Income Fund) Start Date:2007-05-16
NMIH (Nmi  Comm) Start Date:2013-11-08
NML (Neuberger Berman Mlp And Energy Income Fund) Start Date:2013-03-26
NMM (Navios Maritime Partners L.P.) Start Date:2007-11-13
NMMC (North Mountain Merger Class A) Start Date:2020-11-18
NMMCU (North Mountain Merger Unit) Start Date:2020-09-18
NMMCW (North Mountain Merger Warrant) Start Date:2020-11-13
NMR (Nomura Holdings) Start Date:2007-01-03
NMRA (Neumora Therapeutics) Start Date:2023-09-15
NMRD (Nemaura Medical) Start Date:2014-12-18
NMRK (Newmark) Start Date:2017-12-15
NMS (Nuveen Minnesota Quality Municipal Income Fund) Start Date:2014-10-08
NMT (Nuveen Massachusetts Quality Municipal Income Fund) Start Date:2007-05-16
NMTC (Neuroone Medical Technologies) Start Date:2021-05-26
NMTR (9 Meters Biopharma) Start Date:2016-07-08
NMZ (Nuveen Municipal High Income Opportunity Fund $0.01 Par Value Per Share) Start Date:2007-05-16
NN (Nextnav) Start Date:2021-10-29
NNAG (99 Acquisition) Start Date:2023-10-09
NNAVW (Nextnav Warrant) Start Date:2021-10-29
NNBR (Nn) Start Date:2007-04-26
NNDM (Nano Dimension American Depositary Shares) Start Date:2016-03-07
NNI (Nelnet) Start Date:2007-04-25
NNN (National Retail Properties) Start Date:2007-01-03
NNOX (Nano-X Imaging) Start Date:2020-12-15
NNVC (Nanoviricides) Start Date:2007-05-16
NNY (Nuveen New York Municipal Value Fund) Start Date:2007-05-16
NOA (North American Construction Ltd.) Start Date:2007-05-03
NOAH (Noah Holdings Limited) Start Date:2010-11-10
NOC (Northrop Grumman) Start Date:2005-01-03
NODK (Ni) Start Date:2017-03-16
NOG (Northern Oil And Gas,) Start Date:2008-03-26
NOGN (Nogin) Start Date:2021-09-20
NOK (Nokia Corporation) Start Date:2007-01-03
NOM (Nuveen Missouri Quality Municipal Income Fund) Start Date:2007-05-16
NOMD (Nomad Foods Limited) Start Date:2015-11-27
NOTE (Fiscalnote Holdings Class A) Start Date:2022-08-01
NOTV (Inotiv) Start Date:2007-05-16
NOV (National Oilwell Varco) Start Date:2005-03-15
NOVA (Sunnova Energy International) Start Date:2019-07-25
NOVN (Novan) Start Date:2016-09-21
NOVT (Novanta) Start Date:2011-02-14
NOW (Servicenow) Start Date:2012-06-29
NPCT (Nuveen Core Plus Impact Fund Common Shares Of Beneficial Interest) Start Date:2021-04-28
NPFD (Nuveen Variable Rate Preferred & Income Fund Common Shares) Start Date:2021-12-16
NPK (National Presto) Start Date:2007-05-16
NPO (Enpro Industries) Start Date:2007-05-03
NPV (Nuveen Virginia Quality Municipal Income Fund) Start Date:2007-05-16
NQP (Nuveen Pennsylvania Quality Municipal Income Fund) Start Date:2007-05-16
NR (Newpark Resources) Start Date:2007-04-27
NRBO (Neurobo Pharmaceuticals) Start Date:2016-08-05
NRC (National Research) Start Date:2013-05-23
NRDS (Nerdwallet, Class A) Start Date:2021-11-04
NRDY (Nerdy Class A) Start Date:2020-11-27
NREF (Nexpoint Real Estate Finance) Start Date:2020-02-07
NRG (Nrg Energy) Start Date:2005-01-03
NRGV (Energy Vault) Start Date:2022-02-14
NRGX (Pimco Energy And Tactical Credit Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2019-01-30
NRIM (Northrim Bancorp) Start Date:2007-05-16
NRIX (Nurix Therapeutics) Start Date:2020-07-24
NRK (Nuveen New York Amt-Free Quality Municipal Income Fund) Start Date:2007-05-16
NRO (Neuberger Berman Real Estate Securities Income Fund Neuberger Berman Real Estate Securities Income Fund) Start Date:2007-05-09
NRP (Natural Resource Partners Lp Partnership) Start Date:2007-05-08
NRSN (Neurosense Therapeutics Ordinary Shares) Start Date:2021-12-09
NRSNW (Neurosense Therapeutics Warrant) Start Date:2021-12-09
NRT (North European Oil Royality Trust) Start Date:2007-05-16
NRXP (Nrx Pharmaceuticals) Start Date:2017-12-04
NRXPW (Nrx Pharmaceuticals Warrant) Start Date:2017-12-01
NRXS (Neuraxis) Start Date:2023-08-09
NS (Nustar Energy L.P.) Start Date:2007-05-16
NSA (National Storage Affiliates Trust) Start Date:2015-04-23
NSC (Norfolk Southern) Start Date:2005-01-03
NSIT (Insight Enterprises) Start Date:2007-04-30
NSL (Nuveen Senior Income Fund) Start Date:2007-05-07
NSP (Insperity) Start Date:2007-01-03
NSPR (Inspiremd) Start Date:2016-07-13
NSSC (Napco Security Systems) Start Date:2007-05-07
NSTB (Northern Star Investment Ii Class A) Start Date:2021-02-11
NSTC (Northern Star Investment Iii Class A) Start Date:2021-04-22
NSTD (Northern Star Investment Iv Class A) Start Date:2021-04-22
NSTG (Nanostring Technologies) Start Date:2013-06-26
NSTS (Nsts Bancorp) Start Date:2022-01-19
NSYS (Nortech Systems Incorporated) Start Date:2007-05-16
NTAP (Netapp) Start Date:2005-01-03
NTB (The Bank Of N.T. Butterfield & Son) Start Date:2016-09-16
NTBL (Notable Labs Ltd.) Start Date:2014-10-01
NTCO (Natura &Co Holding S.A.) Start Date:2020-01-07
NTCT (Netscout Systems) Start Date:2007-05-03
NTES (Netease Inc) Start Date:2005-01-03
NTG (Tortoise Midstream Energy Fund) Start Date:2010-07-28
NTGR (Netgear) Start Date:2007-04-30
NTIC (Northern Technologies International) Start Date:2008-06-30
NTIP (Network-1 Technologies) Start Date:2007-05-16
NTLA (Intellia Therapeutics) Start Date:2016-05-06
NTNX (Nutanix) Start Date:2016-09-30
NTR (Nutrien Ltd.) Start Date:2018-01-02
NTRA (Natera) Start Date:2015-07-02
NTRB (Nutriband) Start Date:2017-11-30
NTRBW (Nutriband Warrant) Start Date:2021-10-01
NTRS (Northern Trust) Start Date:2009-04-29
NTRSO (Northern Trust Depositary Shares Each Representing A 1/1000Th Interest In A Share Of Series E Non-Cumulative Perpetual Preferred Stock) Start Date:2019-11-27
NTST (Netstreit) Start Date:2020-08-13
NTWK (Netsol Technologies) Start Date:2007-05-16
NTZ (Natuzzi S.P.A.) Start Date:2007-05-16
NUBI (Nubia Brand International Class A) Start Date:2022-05-02
NUBIU (Nubia Brand International Unit) Start Date:2022-03-11
NUE (Nucor) Start Date:2005-01-03
NUO (Nuveen Ohio Quality Municipal Income Fund) Start Date:2007-05-16
NURO (Neurometrix) Start Date:2007-04-19
NUS (Nu Skin Enterprises) Start Date:2007-01-03
NUTX (Nutex Health) Start Date:2022-04-04
NUV (Nuveen Municipal Value Fund) Start Date:2007-01-03
NUVA (Nuvasive) Start Date:2007-01-03
NUVB (Nuvation Bio) Start Date:2020-08-26
NUVL (Nuvalent) Start Date:2021-07-29
NUW (Nuveen Amt-Free Municipal Value Fund) Start Date:2009-02-25
NUWE (Nuwellis) Start Date:2012-08-10
NUZE (Nuzee) Start Date:2014-04-14
NVAX (Novavax) Start Date:2007-04-25
NVCR (Novocure Limited) Start Date:2015-10-02
NVCT (Nuvectis Pharma) Start Date:2022-02-04
NVDA (Nvidia Corporation) Start Date:2005-01-03
NVEC (Nve) Start Date:2007-04-20
NVEE (Nv5 Global) Start Date:2013-09-30
NVEI (Nuvei Subordinate Voting Shares) Start Date:2021-10-06
NVFY (Nova Lifestyle) Start Date:2014-01-17
NVG (Nuveen Amt-Free Municipal Credit Income Fund) Start Date:2007-01-03
NVGS (Navigator Holdings Ltd.) Start Date:2013-11-21
NVIV (Invivo Therapeutics Holdings) Start Date:2015-04-17
NVMI (Nova Ordinary Shares) Start Date:2007-05-16
NVNO (Envveno Medical) Start Date:2018-05-31
NVNOW (Envveno Medical Warrants) Start Date:2018-05-31
NVO (Novo Nordisk A/S) Start Date:2007-05-04
NVOS (Novo Integrated Sciences) Start Date:2014-04-21
NVR (Nvr) Start Date:2008-01-02
NVRI (Enviri Corp) Start Date:2007-05-03
NVRO (Nevro) Start Date:2014-11-06
NVS (Novartis Ag) Start Date:2007-04-26
NVST (Envista Holdings Corporation) Start Date:2019-09-18
NVT (Nvent Electric Plc) Start Date:2018-04-17
NVTS (Navitas Semiconductor) Start Date:2021-10-20
NVVE (Nuvve Holding) Start Date:2020-05-01
NVVEW (Nuvve Holding Warrant) Start Date:2020-04-30
NVX (Novonix ADS) Start Date:2022-02-02
NWBI (Northwest Bancshares) Start Date:2007-05-03
NWE (Northwestern Corporation) Start Date:2008-05-01
NWFL (Norwood Financial) Start Date:2007-05-18
NWG (Natwest Plc American Depositary Shares) Start Date:2007-10-18
NWGL (Nature Wood Limited) Start Date:2023-09-12
NWL (Newell Brands) Start Date:2005-01-03
NWLI (National Western Life) Start Date:2008-10-03
NWN (Northwest Natural Holding Co) Start Date:2007-04-30
NWPX (Northwest Pipe Co) Start Date:2007-05-16
NWS (News Class B) Start Date:2013-06-19
NWSA (News Class A) Start Date:2013-06-19
NWTN (Nwtn Class B) Start Date:2022-11-14
NX (Quanex Building Products) Start Date:2007-04-26
NXC (Nuveen California Select Tax-Free Income Portfolio) Start Date:2007-05-16
NXDT (Nexpoint Diversified Real Estate Trust) Start Date:2007-05-07
NXE (Nexgen Energy Common Shares) Start Date:2017-05-17
NXG (Nxg Nextgen Infrastructure Income Fund) Start Date:2012-09-26
NXGL (Nexgel Inc) Start Date:2021-12-22
NXGLW (Nexgel Inc Warrant) Start Date:2021-12-22
NXGN (Nextgen Healthcare) Start Date:2007-04-27
NXJ (Nuveen New Jersey Qualified Municipal Fund) Start Date:2007-05-16
NXL (Nexalin Technology) Start Date:2022-09-16
NXN (Nuveen New York Select Tax-Free Income Portfolio) Start Date:2007-05-16
NXP (Nuveen Select Tax Free Income Portfolio) Start Date:2007-05-16
NXPI (Nxp Semiconductors Nv) Start Date:2010-08-06
NXPL (Nextplat) Start Date:2021-05-28
NXPLW (Nextplat Warrants) Start Date:2021-05-28
NXRT (Nexpoint Residential Trust In) Start Date:2015-04-01
NXST (Nexstar Media) Start Date:2007-01-03
NXT (Nextracker) Start Date:2023-02-09
NXTC (Nextcure) Start Date:2019-05-09
NXTP (Nextplay Technologies) Start Date:2018-02-22
NXU (Nxu Inc) Start Date:2022-09-27
NYAX (Nayax) Start Date:2022-09-21
NYCB (New York Community Bancorp) Start Date:2007-04-27
NYMT (New York Mortgage Trust) Start Date:2008-06-05
NYMTN (New York Mortgage Trust 8.00% Series D Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2017-10-13
NYMX (Nymox Pharmaceutical) Start Date:2007-05-16
NYT (New York Times Company) Start Date:2005-01-03
NYXH (Nyxoah) Start Date:2021-07-02
NZF (Nuveen Municipal Credit Income Fund) Start Date:2007-05-16
O (Realty Income Corporation) Start Date:2012-02-10
OABI (Omniab) Start Date:2021-09-30
OB (Outbrain) Start Date:2021-07-23
OBDC (Blue Owl Capital Corp) Start Date:2019-07-18
OBE (Obsidian Energy) Start Date:2022-01-31
OBIO (Orchestra Biomed Holdings) Start Date:2020-08-04
OBK (Origin Bancorp Inc) Start Date:2018-05-09
OBLG (Oblong) Start Date:2007-05-16
OBSV (Obseva Sa Ordinary Shares) Start Date:2018-07-13
OBT (Orange County Bancorp) Start Date:2021-08-05
OC (Owens Corning) Start Date:2007-01-03
OCC (Optical Cable) Start Date:2007-05-16
OCCI (Ofs Credit Company) Start Date:2018-10-05
OCFC (Oceanfirst Financial) Start Date:2007-05-16
OCFCP (Oceanfirst Financial Depositary Shares) Start Date:2020-05-08
OCFT (Oneconnect Financial Technology Co. Ltd.) Start Date:2019-12-13
OCG (Oriental Culture Holding) Start Date:2020-12-15
OCGN (Ocugen,) Start Date:2014-12-03
OCN (Ocwen Financial New) Start Date:2007-04-30
OCSL (Oaktree Specialty Lending Corporation) Start Date:2008-06-12
OCTO (Eightco Holdings Inc) Start Date:2022-05-18
OCUL (Ocular Therapeutix Commo) Start Date:2014-07-25
OCUP (Ocuphire Pharma) Start Date:2019-04-12
OCX (Oncocyte Corp) Start Date:2016-01-04
ODC (Oil-Dri Of America) Start Date:2007-05-16
ODD (Oddity Tech Ltd.) Start Date:2023-07-19
ODFL (Old Dominion Freight Line) Start Date:2005-01-03
ODP (Office Depot) Start Date:2005-01-03
ODV (Osisko Development Common Shares) Start Date:2022-05-27
OEC (Orion Engineered Carbons S.A.) Start Date:2014-07-25
OEPWW (One Equity Partners Open Water I Warrant) Start Date:2021-03-15
OESX (Orion Energy Systems) Start Date:2007-12-19
OFG (Ofg Bancorp) Start Date:2007-05-04
OFIX (Orthofix International) Start Date:2007-05-03
OFLX (Omega Flex) Start Date:2007-05-16
OFS (Ofs Capital) Start Date:2012-11-08
OGCP (Empire State Realty Op, L.P. Series 60) Start Date:2013-10-08
OGE (Oge Energy) Start Date:2007-01-03
OGEN (Oragenics) Start Date:2012-09-24
OGI (Organigram Holdings Common Shares) Start Date:2014-08-27
OGN (Organon) Start Date:2021-05-14
OGS (One Gas) Start Date:2014-01-16
OHI (Omega Healthcare Investors) Start Date:2007-01-03
OI (O-I Glass) Start Date:2005-01-03
OIA (Invesco Municipal Income Opportunities Trust) Start Date:2007-05-16
OIGBQ (Orbital Infrastructure Inc) Start Date:2008-01-07
OII (Oceaneering International) Start Date:2007-04-27
OIS (Oil States International) Start Date:2007-04-27
OKE (Oneok) Start Date:2005-01-03
OKTA (Okta) Start Date:2017-04-07
OKYO (Okyo Pharma American Depositary Shares) Start Date:2022-05-17
OLB (The Olb) Start Date:2020-08-07
OLED (Universal Display Corporation) Start Date:2007-05-04
OLK (Olink Holding Ab) Start Date:2021-03-25
OLLI (Ollie's Bargain Outlet Holdings) Start Date:2015-07-16
OLMA (Olema Pharmaceuticals) Start Date:2020-11-19
OLN (Olin Corporation) Start Date:2007-04-30
OLO (Olo) Start Date:2021-03-17
OLP (One Liberty Properties) Start Date:2007-05-16
OLPX (Olaplex Holdings,) Start Date:2021-09-30
OM (Outset Medical) Start Date:2020-09-15
OMAB (Grupo Aeroportuario Del Centro Norte S.A.B. De C.V. ADS) Start Date:2007-05-09
OMC (Omnicom) Start Date:2005-01-03
OMCL (Omnicell) Start Date:2007-05-03
OMER (Omeros) Start Date:2009-10-08
OMEX (Odyssey Marine Exploration) Start Date:2007-07-10
OMF (Onemain Holdings) Start Date:2013-10-16
OMGA (Omega Therapeutics) Start Date:2021-07-30
OMH (Ohmyhome Limited) Start Date:2023-03-21
OMI (Owens & Minor) Start Date:2007-05-02
OMIC (Singular Genomics Systems) Start Date:2021-05-27
OMQS (Omniq) Start Date:2011-01-14
ON (On Semiconductor Corporation) Start Date:2015-04-06
ONB (Old National Bancorp) Start Date:2007-01-03
ONBPO (Old National Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series C Preferred Stock) Start Date:2022-02-16
ONBPP (Old National Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series A Preferred Stock) Start Date:2022-02-16
ONCO (Onconetix Inc) Start Date:2022-02-18
ONCS (Oncosec Medical Incorporated) Start Date:2015-05-29
ONCT (Oncternal Therapeutics) Start Date:2018-09-17
ONCY (Oncolytics Biotech Common Shares) Start Date:2018-06-01
ONDS (Ondas Holdings) Start Date:2020-12-04
ONEW (Onewater Marine) Start Date:2020-02-07
ONFO (Onfolio Holdings) Start Date:2022-08-26
ONL (Orion Office Reit) Start Date:2021-11-01
ONON (On Holding Ag) Start Date:2021-09-15
ONTF (On24) Start Date:2021-02-03
ONTO (Onto Innovation) Start Date:2007-05-07
ONTX (Onconova Therapeutics) Start Date:2013-07-25
ONVO (Organovo Holdings) Start Date:2013-08-02
OOMA (Ooma) Start Date:2015-07-17
OP (Oceanpal) Start Date:2021-11-30
OPAD (Offerpad Solutions) Start Date:2020-12-11
OPAL (Opal Fuels Class A) Start Date:2021-05-24
OPBK (Op Bancorp) Start Date:2007-05-18
OPCH (Option Care Health) Start Date:2007-04-27
OPEN (Opendoor Technologies Inc) Start Date:2020-12-15
OPFI (Oppfi Class A) Start Date:2021-01-20
OPGN (Opgen) Start Date:2015-05-05
OPHC (Optimumbank Holdings) Start Date:2007-05-16
OPI (Office Properties Ome Trust Common Shares Of Be) Start Date:2009-06-03
OPK (Opko Health) Start Date:2007-06-13
OPOF (Old Point Financial) Start Date:2007-05-16
OPP (Rivernorth/Doubleline Strategic Opportunity Fund) Start Date:2016-09-28
OPRA (Opera American Depositary Shares) Start Date:2018-07-27
OPRT (Oportun Financial) Start Date:2019-09-26
OPRX (Optimizerx) Start Date:2008-04-30
OPT (Opthea) Start Date:2020-10-16
OPTN (Optinose) Start Date:2017-10-13
OPTT (Ocean Power Technologies) Start Date:2007-05-16
OPY (Oppenheimer) Start Date:2007-05-16
OR (Osisko Gold Royalties Ltd) Start Date:2016-07-06
ORA (Ormat Technologies) Start Date:2007-05-04
ORAN (Orange S.A.) Start Date:2007-05-01
ORC (Orchid Island Capital) Start Date:2013-02-14
ORCL (Oracle) Start Date:2005-01-03
ORGN (Origin Materials,) Start Date:2020-09-04
ORGNW (Origin Materials Warrants) Start Date:2020-09-04
ORGO (Organogenesis) Start Date:2017-01-05
ORGS (Orgenesis) Start Date:2012-02-08
ORI (Old Republic International Corporation) Start Date:2007-01-03
ORIAU (Orion Biotech Opportunities Units) Start Date:2021-05-13
ORIAW (Orion Biotech Opportunities Warrant) Start Date:2021-07-07
ORIC (Oric Pharmaceuticals) Start Date:2020-04-24
ORLA (Orla Mining Ltd.) Start Date:2020-12-22
ORLY (O'reilly Automotive) Start Date:2005-01-03
ORMP (Oramed Pharmaceuticals) Start Date:2007-05-16
ORN (Orion Holdings Common) Start Date:2009-05-14
ORRF (Orrstown Financial) Start Date:2007-05-17
ORTX (Orchard Therapeutics Plc American Depositary Shares) Start Date:2018-10-31
OSA (Prosomnus) Start Date:2022-12-07
OSBC (Old Second Bancorp) Start Date:2007-05-08
OSCR (Oscar Health) Start Date:2021-03-03
OSG (Overseas Shipholding) Start Date:2015-12-01
OSIS (Osi Systems) Start Date:2007-04-30
OSK (Oshkosh Corporation) Start Date:2009-08-07
OSPN (Onespan) Start Date:2007-05-03
OSS (One Stop Systems) Start Date:2018-02-01
OST (Ostin Technology Co. Ordinary Shares) Start Date:2022-04-27
OSUR (Orasure Technologies) Start Date:2007-04-26
OSW (Onespaworld) Start Date:2017-11-17
OTEX (Open Text Corporation) Start Date:2007-01-03
OTIS (Otis Worldwide) Start Date:2020-03-19
OTLK (Outlook Therapeutics) Start Date:2016-06-14
OTLY (Oatly) Start Date:2021-05-20
OTMO (Otonomo Technologies Ordinary Shares) Start Date:2021-08-16
OTMOW (Otonomo Technologies Warrant) Start Date:2021-08-16
OTRK (Ontrak) Start Date:2017-04-26
OTTR (Otter Tail) Start Date:2007-05-01
OUST (Ouster,) Start Date:2020-10-09
OUT (Outfront Media) Start Date:2014-03-28
OVBC (Ohio Valley Banc) Start Date:2007-05-16
OVID (Ovid Therapeutics) Start Date:2017-05-05
OVLY (Oak Valley Bancorp) Start Date:2008-08-18
OVV (Ovintiv) Start Date:2007-04-27
OWL (Blue Owl Capital Class A) Start Date:2020-12-14
OWLT (Owlet Class A) Start Date:2020-11-05
OXBR (Oxbridge Re Holdings Ordinary Shares) Start Date:2014-03-27
OXBRW (Oxbridge Re Holdings Warrant Expiring 3/26/2024) Start Date:2014-05-09
OXLC (Oxford Lane Capital) Start Date:2011-01-20
OXM (Oxford Industries) Start Date:2007-05-03
OXSQ (Oxford Square Capital) Start Date:2014-03-05
OXY (Occidental Petroleum) Start Date:2005-01-03
OZ (Belpointe Prep Llc Class A Units) Start Date:2021-10-18
OZK (Bank Ozk) Start Date:2007-05-10
PAA (Plains All American Pipeline L.P.) Start Date:2007-01-03
PAAS (Pan American Silver) Start Date:2007-01-03
PAC (Grupo Aeroportuario Del Pacifico S.A. B. De C.V. Grupo Aeroportuario Del Pacifico S.A. De C.V.) Start Date:2007-05-03
PACB (Pacific Biosciences) Start Date:2010-10-27
PACK (Ranpak Corp) Start Date:2018-03-05
PACW (Pacwest Bancorp) Start Date:2008-05-14
PACX (Pioneer Merger Class A Ordinary Share) Start Date:2021-03-01
PACXU (Pioneer Merger Unit) Start Date:2021-01-08
PACXW (Pioneer Merger Warrant) Start Date:2021-03-01
PAG (Penske Automotive) Start Date:2007-07-02
PAGP (Plains Gp Holdings L.P. Class A Units Representing Partner Interests) Start Date:2013-10-16
PAGS (Pagseguro Digital Ltd.) Start Date:2018-01-24
PAHC (Phibro Animal Health) Start Date:2014-04-11
PAI (Western Asset Investment Grade Income Fund) Start Date:2007-05-16
PALI (Palisade Bio) Start Date:2019-07-18
PALT (Paltalk) Start Date:2018-03-12
PAM (Pampa Energia S.A. Pampa Energia S.A.) Start Date:2009-10-09
PANW (Palo Alto Networks) Start Date:2012-07-20
PAPL (Pineapple Financial) Start Date:2023-11-01
PAR (Par Technology) Start Date:2007-05-16
PARA (Paramount Global) Start Date:2007-04-30
PARAA (Paramount Global Class A) Start Date:2007-05-09
PARR (Par Pacific) Start Date:2012-09-05
PASG (Passage Bio) Start Date:2020-02-28
PATH (Uipath) Start Date:2010-08-06
PATI (Patriot Transportation Holding) Start Date:2015-02-02
PATK (Patrick Industries) Start Date:2007-05-16
PAVM (Pavmed) Start Date:2016-07-28
PAVMZ (Pavmed Series Z Warrant) Start Date:2018-04-10
PAVS (Paranovus Entertainment Technology Ltd.) Start Date:2019-10-25
PAX (Patria Investments) Start Date:2021-01-22
PAXS (Pimco Access Income Fund Common Shares Of Beneficial Interest) Start Date:2022-01-27
PAY (Paymentus Holdings) Start Date:2021-05-26
PAYC (Paycom) Start Date:2014-04-15
PAYO (Payoneer Global) Start Date:2021-06-28
PAYOW (Payoneer Global Warrant) Start Date:2021-06-28
PAYS (Paysign) Start Date:2007-05-18
PAYX (Paychex) Start Date:2005-06-06
PB (Prosperity Bancshares) Start Date:2011-12-28
PBA (Pembina Pipeline Corporation) Start Date:2012-04-02
PBBK (Pb Bankshares) Start Date:2021-07-15
PBF (Pbf Energy) Start Date:2012-12-13
PBFS (Pioneer Bancorp) Start Date:2019-07-18
PBH (Prestige Consumer Healthcare) Start Date:2007-01-03
PBHC (Pathfinder Bancorp) Start Date:2007-05-22
PBI (Pitney Bowes) Start Date:2005-01-03
PBLA (Panbela Therapeutics) Start Date:2020-12-02
PBPB (Potbelly) Start Date:2013-10-04
PBR (Petroleo Brasileiro S.A.- Petrobras) Start Date:2007-04-27
PBR.A (Petroleo Brasileiro ADR Reptg 2 Pref Shares) Start Date:2007-04-26
PBT (Permian Basin Royalty Trust) Start Date:2007-05-02
PBTS (Powerbridge Technologies Co. Ordinary Shares) Start Date:2019-04-02
PBYI (Puma Biotechnology) Start Date:2012-04-20
PCAR (Paccar) Start Date:2005-01-03
PCB (Pcb Bancorp) Start Date:2018-08-10
PCCTU (Perception Capital Ii Units) Start Date:2021-10-28
PCCTW (Perception Capital Ii Warrants) Start Date:2021-12-20
PCF (High Income Securities Fund) Start Date:2007-05-01
PCG (Pacific Gas & Electric Co.) Start Date:2005-01-03
PCH (Potlatchdeltic Corporation) Start Date:2007-01-03
PCK (Pimco California Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PCM (Pcm Fund) Start Date:2007-05-16
PCN (Pimco Corporate & Income Strategy Fund) Start Date:2007-05-03
PCOR (Procore Technologies) Start Date:2021-05-20
PCQ (Pimco California Municipal Income Fund) Start Date:2007-05-16
PCRX (Pacira Biosciences) Start Date:2011-02-03
PCSA (Processa Pharmaceuticals) Start Date:2013-11-21
PCT (Purecycle Technologies,) Start Date:2021-03-18
PCTI (Pctel) Start Date:2007-05-03
PCTTU (Purecycle Technologies Unit) Start Date:2021-03-18
PCTTW (Purecycle Technologies Warrant) Start Date:2021-03-18
PCTY (Paylocity Holding) Start Date:2014-03-19
PCVX (Vaxcyte) Start Date:2020-06-12
PCYO (Pure Cycle) Start Date:2007-05-16
PD (Pagerduty) Start Date:2019-04-11
PDCO (Patterson Companies) Start Date:2005-01-03
PDD (Pinduoduo) Start Date:2018-07-26
PDEX (Pro-Dex) Start Date:2007-05-16
PDFS (Pdf Solutions) Start Date:2007-05-03
PDI (Pimco Dynamic Income Fund) Start Date:2012-05-25
PDLB (Pdl Community Bancorp) Start Date:2017-10-02
PDM (Piedmont Office Realty Trust) Start Date:2010-02-10
PDO (Pimco Dynamic Income Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2021-01-27
PDS (Precision Drilling Corporation) Start Date:2010-06-02
PDSB (Pds Biotechnology) Start Date:2015-10-01
PDT (John Hancock Premium Dividend Fund) Start Date:2007-05-16
PEAK (Healthpeak Properties) Start Date:2007-04-30
PEAR (Pear Therapeutics Class A) Start Date:2021-03-31
PEB (Pebblebrook Hotel Trust) Start Date:2009-12-09
PEBK (Peoples Bancorp Of N) Start Date:2007-05-16
PEBO (Peoples Bancorp) Start Date:2007-05-16
PECO (Phillips Edison & Company) Start Date:2021-07-15
PED (Pedevco) Start Date:2007-05-17
PEG (Public Serv. Enterprise) Start Date:2005-01-03
PEGA (Pegasystems) Start Date:2007-05-03
PEGY (Pineapple Energy) Start Date:2007-05-16
PEI (Pennsylvania Real Estate Investment Trust) Start Date:2007-04-27
PEN (Penumbra) Start Date:2015-09-18
PENN (Penn National Gaming) Start Date:2007-01-03
PEO (Adams Natural Resources Fund) Start Date:2007-04-30
PEP (Pepsico) Start Date:2005-01-03
PEPG (Pepgen) Start Date:2022-05-06
PERF (Perfect Class A) Start Date:2022-10-31
PERI (Perion Network Ltd.) Start Date:2007-05-16
PESI (Perma-Fix Environmental Services) Start Date:2007-05-16
PET (Wag) Start Date:2021-09-27
PETQ (Petiq) Start Date:2017-07-21
PETS (Petmed Express) Start Date:2007-05-01
PETV (Petvivo Holdings) Start Date:2013-05-21
PETVW (Petvivo Holdings Warrant) Start Date:2021-08-11
PETZ (Tdh Holdings, Common Shares) Start Date:2017-09-21
PEV (Phoenix Motor) Start Date:2022-06-08
PFBC (Preferred Bank) Start Date:2007-05-16
PFC (Premier Financial Corp) Start Date:2007-05-16
PFD (Flaherty & Crumrine Preferred And Income Fund Incorporated) Start Date:2007-05-16
PFE (Pfizer) Start Date:2005-01-03
PFG (Principal Financial) Start Date:2005-01-03
PFGC (Performance Food Company) Start Date:2015-10-01
PFHC (Profrac Holding Class A) Start Date:2022-05-13
PFIE (Profire Energy) Start Date:2011-07-06
PFIN (P & F Industries Class A) Start Date:2007-05-16
PFIS (Peoples Financial Services Cor) Start Date:2007-05-21
PFL (Pimco Income Strategy Fund Shares Of Beneficial Interest) Start Date:2007-05-04
PFLT (Pennantpark Floating Rate Capital) Start Date:2011-04-08
PFMT (Performant Financial) Start Date:2012-08-10
PFN (Pimco Income Strategy Fund Ii) Start Date:2007-05-09
PFO (Flaherty & Crumrine Preferred And Income Opportunity Fund Incorporated) Start Date:2007-05-16
PFS (Provident Financial) Start Date:2007-05-02
PFSI (Pennymac Financial Services) Start Date:2013-05-09
PFSW (Pfsweb) Start Date:2007-05-16
PFX (Phenixfin) Start Date:2011-01-20
PG (Procter & Gamble) Start Date:2005-01-03
PGC (Peapack Gladstone) Start Date:2007-05-16
PGEN (Precigen) Start Date:2013-08-08
PGNY (Progyny) Start Date:2019-10-25
PGP (Pimco Global Stocksplus & Income Fund Pimco Global Stocksplus & Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
PGR (Progressive) Start Date:2007-04-26
PGRE (Paramount) Start Date:2014-11-19
PGRU (Propertyguru Ordinary Shares) Start Date:2022-03-18
PGTI (Pgt) Start Date:2007-05-03
PGY (Pagaya Technologies Class A Ordinary Shares) Start Date:2022-06-23
PGYWW (Pagaya Technologies Warrants) Start Date:2022-06-23
PGZ (Principal Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2013-06-26
PH (Parker-Hannifin) Start Date:2005-01-03
PHAR (Pharming N.V. ADS, Each Representing 10 Ordinary Shares) Start Date:2020-12-23
PHAS (Phasebio Pharmaceuticals) Start Date:2018-10-18
PHAT (Phathom Pharmaceuticals) Start Date:2019-10-25
PHCF (Puhui Wealth Investment Management Co. Ordinary Shares) Start Date:2018-12-27
PHD (Pioneer Floating Rate Fund) Start Date:2007-05-08
PHG (Koninklijke Philips N.V.) Start Date:2007-01-03
PHGE (Biomx) Start Date:2019-03-13
PHI (Pldt Sponsored ADR) Start Date:2007-05-01
PHICU (Population Health Investment Co. Unit) Start Date:2020-11-18
PHICW (Population Health Investment Co. Warrant) Start Date:2021-01-12
PHIN (Phinia Inc) Start Date:2023-06-28
PHIO (Phio Pharmaceuticals) Start Date:2012-05-10
PHK (Pimco High Income Fund Pimco High Income Fund) Start Date:2007-04-30
PHM (Pulte Homes) Start Date:2005-01-03
PHR (Phreesia) Start Date:2019-07-18
PHT (Pioneer High Income Fund) Start Date:2007-05-04
PHUN (Phunware) Start Date:2016-10-28
PHUNW (Phunware Warrants) Start Date:2018-12-28
PHVS (Pharvaris N.V.) Start Date:2021-02-05
PHX (Phx Minerals) Start Date:2007-05-16
PHXM (Phaxiam Therapeutics Sa) Start Date:2017-11-10
PI (Impinj) Start Date:2016-07-21
PII (Polaris) Start Date:2007-01-03
PIII (P3 Health Partners Class A) Start Date:2021-04-06
PIIIW (P3 Health Partners Warrant) Start Date:2021-12-03
PIK (Kidpik) Start Date:2021-11-11
PIM (Putnam Master Intermediate Income Trust) Start Date:2007-04-30
PINC (Premier) Start Date:2013-09-26
PINE (Alpine Ome Property Trust) Start Date:2019-11-22
PINS (Pinterest) Start Date:2019-04-18
PIPR (Piper Sandler Companies) Start Date:2020-01-06
PIRS (Pieris Pharmaceuticals) Start Date:2015-06-26
PIXY (Shiftpixy) Start Date:2017-06-30
PJT (Pjt Partners) Start Date:2015-10-01
PK (Park Hotels & Resorts) Start Date:2016-12-13
PKBK (Parke Bancorp) Start Date:2007-05-16
PKE (Park Aerospace Corp) Start Date:2007-05-01
PKG (Packaging Of America) Start Date:2005-01-03
PKOH (Park-Ohio) Start Date:2007-05-08
PKX (Posco Holdings American Depositary Shares) Start Date:2007-04-30
PL (Planet Labs Pbc) Start Date:2021-04-26
PLAB (Photronics) Start Date:2007-04-25
PLAG (Planet Green Holdings) Start Date:2009-09-08
PLAO (Patria Latin American Opportunity Acquisition) Start Date:2022-05-04
PLAY (Dave & Busters Entertainment) Start Date:2014-10-10
PLBC (Plumas Bancorp) Start Date:2007-05-16
PLBY (Plby ,) Start Date:2020-08-31
PLCE (Childrens Place) Start Date:2007-04-27
PLD (Prologis) Start Date:2007-04-27
PLG (Platinum Metals Ordinary Shares) Start Date:2007-06-28
PLL (Piedmont Lithium Limited) Start Date:2018-05-07
PLM (Polymet Mining Ordinary Shares) Start Date:2007-05-10
PLMR (Palomar) Start Date:2019-04-17
PLNT (Planet Fitness) Start Date:2015-08-06
PLOW (Douglas Dynamics) Start Date:2010-05-05
PLPC (Preformed Line Products) Start Date:2007-05-16
PLRX (Pliant Therapeutics) Start Date:2020-06-03
PLSE (Pulse Biosciences) Start Date:2016-05-18
PLTK (Playtika Holding) Start Date:2021-01-15
PLTN (Plutonian Acquisition) Start Date:2023-01-11
PLTR (Palantir Technologies) Start Date:2020-09-30
PLUG (Plug Power) Start Date:2007-04-27
PLUR (Pluri) Start Date:2007-01-03
PLUS (Eplus) Start Date:2007-05-16
PLX (Protalix Biotherapeutics) Start Date:2010-09-07
PLXP (Plx Pharma) Start Date:2014-03-13
PLXS (Plexus) Start Date:2007-04-27
PLYA (Playa Hotels & Resorts N.V. Ordinary Shares) Start Date:2017-03-13
PLYM (Plymouth Industrial Reit) Start Date:2017-06-09
PM (Philip Morris International) Start Date:2008-03-31
PMCB (Pharmacyte Biotech) Start Date:2009-03-18
PMD (Psychemedics Corporation) Start Date:2007-05-16
PMEC (Primech Holdings Ltd.) Start Date:2023-10-10
PMF (Pimco Municipal Income Fund) Start Date:2007-05-16
PML (Pimco Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PMM (Putnam Managed Municipal Income Trust) Start Date:2007-05-16
PMN (Promis Neurosciences) Start Date:2022-07-08
PMO (Putnam Municipal Opportunities Trust) Start Date:2007-05-16
PMT (Pennymac Mortgage) Start Date:2009-07-30
PMTS (Cpi Card) Start Date:2015-10-09
PMVP (Pmv Pharmaceuticals) Start Date:2020-09-25
PMX (Pimco Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PNBK (Patriot National Bancorp) Start Date:2007-05-16
PNC (Pnc Financial Services) Start Date:2005-01-03
PNF (Pimco New York Municipal Income Fund) Start Date:2007-05-16
PNFP (Pinnacle Financial Partners) Start Date:2007-01-03
PNI (Pimco New York Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PNM (Pnm Resources) Start Date:2007-01-03
PNNT (Pennantpark Investment) Start Date:2007-05-16
PNR (Pentair Plc) Start Date:2012-09-17
PNRG (Primeenergy Resources Corp) Start Date:2007-05-16
PNT (Point Biopharma Global) Start Date:2020-07-08
PNTG (Pennant) Start Date:2019-10-01
PNW (Pinnacle West Capital) Start Date:2005-01-03
POAI (Predictive Oncology) Start Date:2010-04-09
POCI (Precision Optics) Start Date:2022-11-16
PODC (Courtside Inc) Start Date:2023-09-08
PODD (Insulet Corporation) Start Date:2007-05-15
POET (Poet Technologies Common Shares) Start Date:2022-03-14
POL (Polished) Start Date:2020-07-31
POLA (Polar Power) Start Date:2016-12-07
POND (Angel Pond Holdings) Start Date:2021-07-09
PONO (Pono Capital Class A) Start Date:2021-10-12
PONOU (Pono Capital Unit) Start Date:2021-08-11
POOL (Pool Corporation) Start Date:2005-01-03
POR (Portland General Electric Company) Start Date:2007-01-03
POST (Post) Start Date:2012-01-27
POWI (Power Integrations) Start Date:2007-03-15
POWL (Powell Industries) Start Date:2007-05-16
POWRU (Powered Brands Units) Start Date:2021-01-08
POWRW (Powered Brands Warrants) Start Date:2021-03-03
POWW (Ammo,) Start Date:2007-05-17
PPBI (Pacific Premier Bancorp) Start Date:2007-05-16
PPBT (Purple Biotech American Depositary Shares) Start Date:2015-11-20
PPC (Pilgrim's Pride Corporation) Start Date:2009-12-29
PPG (Ppg Industries) Start Date:2005-01-03
PPIH (Perma-Pipe International Holdings) Start Date:2007-05-16
PPL (Ppl) Start Date:2005-01-03
PPSI (Pioneer Power Solutions) Start Date:2013-09-19
PPT (Putnam Premier Income Trust) Start Date:2007-04-30
PPTA (Perpetua Resources Common Shares) Start Date:2021-02-18
PPYA (Papaya Growth Opportunity I Class A) Start Date:2022-03-04
PPYAU (Papaya Growth Opportunity I Unit) Start Date:2022-01-14
PPYAW (Papaya Growth Opportunity I Warrant) Start Date:2022-03-04
PR (Permian Resources Class A) Start Date:2016-04-15
PRA (Proassurance) Start Date:2007-05-02
PRAA (Pra) Start Date:2007-05-02
PRAX (Praxis Precision Medicines) Start Date:2020-10-16
PRCH (Porch ,) Start Date:2020-01-13
PRCT (Procept Biorobotics) Start Date:2021-09-15
PRDO (Perdoceo Education) Start Date:2007-05-01
PRDS (Pardes Biosciences) Start Date:2021-02-17
PRE (Prenetics Global Class A Ordinary Share) Start Date:2022-05-18
PRFT (Perficient) Start Date:2007-04-25
PRFX (Painreform) Start Date:2020-09-01
PRG (Prog Holdings) Start Date:2020-12-01
PRGO (Perrigo) Start Date:2005-01-03
PRGS (Progress Software) Start Date:2007-05-01
PRI (Primerica) Start Date:2010-04-01
PRIM (Primoris Services) Start Date:2008-08-04
PRK (Park National) Start Date:2007-05-16
PRLB (Proto Labs) Start Date:2012-02-24
PRLD (Prelude Therapeutics) Start Date:2020-09-25
PRM (Perimeter Solutions Sa Ordinary Shares) Start Date:2021-11-09
PRME (Prime Medicine) Start Date:2022-10-20
PRO (Pros) Start Date:2007-06-28
PROC (Procaps S.A. Ordinary Shares) Start Date:2021-09-30
PROCW (Procaps S.A. Warrants) Start Date:2021-09-30
PROF (Profound Medical) Start Date:2016-06-09
PROK (Prokidney Class A) Start Date:2021-06-30
PROV (Provident Financial) Start Date:2007-05-16
PRPC (Cc Neuberger Principal Holdings Iii Class A Ordinary Shares) Start Date:2021-03-30
PRPH (Prophase Labs) Start Date:2007-05-16
PRPL (Purple Innovation) Start Date:2015-10-29
PRPO (Precipio) Start Date:2017-06-30
PRQR (Proqr Therapeutics N.V. Ordinary Shares) Start Date:2014-09-18
PRSO (Peraso) Start Date:2019-08-28
PRSRU (Prospector Capital Unit) Start Date:2021-01-08
PRSRW (Prospector Capital Warrants) Start Date:2021-03-01
PRST (Presto Automation) Start Date:2021-02-05
PRT (Permrock Royalty Trust Trust Units) Start Date:2018-05-02
PRTA (Prothena  Ordin) Start Date:2012-12-21
PRTC (Puretech Health Plc American Depositary Shares) Start Date:2020-11-16
PRTG (Portage Biotech) Start Date:2021-02-25
PRTH (Priority Technology) Start Date:2016-12-06
PRTK (Paratek Pharmaceuticals) Start Date:2009-02-02
PRTS (Carparts) Start Date:2007-05-16
PRTY (Party City Holdco) Start Date:2015-04-16
PRU (Prudential Financial) Start Date:2005-01-03
PRVA (Privia Health) Start Date:2021-04-29
PRZO (Parazero Technologies Ltd.) Start Date:2023-07-27
PSA (Public Storage) Start Date:2005-01-03
PSF (Cohen & Steers Select Preferred And Income Fund) Start Date:2010-11-24
PSFE (Paysafe Limited) Start Date:2020-10-09
PSHG (Performance Shipping Common Shares) Start Date:2011-01-03
PSMT (Pricesmart) Start Date:2007-05-11
PSN (Parsons Corporation) Start Date:2019-05-08
PSNL (Personalis) Start Date:2019-06-20
PSNY (Polestar Automotive Holding Uk Plc Class A ADS) Start Date:2022-06-24
PSNYW (Polestar Automotive Holding Uk Plc Class C-1 ADS) Start Date:2022-06-24
PSO (Pearson Plc) Start Date:2013-02-11
PSTG (Pure Storage) Start Date:2015-10-07
PSTV (Plus Therapeutics) Start Date:2007-05-16
PSTX (Poseida Therapeutics) Start Date:2020-07-10
PSX (Phillips 66) Start Date:2012-05-01
PT (Pintec Technology Holdings American Depositary Shares) Start Date:2018-10-25
PTA (Cohen & Steers Tax-Advantaged Preferred Securities And Income Fund Common Shares Of Beneficial Interest) Start Date:2020-11-02
PTC (Ptc) Start Date:2007-04-27
PTCT (Ptc Therapeutics) Start Date:2013-06-20
PTEN (Patterson-Uti Energy) Start Date:2007-04-27
PTGX (Protagonist Therapeutics) Start Date:2016-08-11
PTHRU (Pono Capital Three Unit) Start Date:2023-02-10
PTICU (Proptech Investment Ii Unit) Start Date:2020-12-04
PTICW (Proptech Investment Ii Warrant) Start Date:2021-01-25
PTIX (Protagenic Therapeutics) Start Date:2017-01-11
PTIXW (Protagenic Therapeutics Warrant) Start Date:2021-04-27
PTLO (Portillo's Class A) Start Date:2021-10-21
PTMN (Portman Ridge Finance) Start Date:2007-05-16
PTN (Palatin Technologies) Start Date:2007-04-25
PTNR (Partner Communications Company American Depositary Shares) Start Date:2013-02-11
PTON (Peloton Interactive) Start Date:2019-09-26
PTPI (Petros Pharmaceuticals) Start Date:2020-12-02
PTRA (Proterra) Start Date:2020-11-25
PTRS (Partners Bancorp) Start Date:2007-05-16
PTSI (P.A.M. Transportation) Start Date:2007-05-10
PTVE (Pactiv Evergreen) Start Date:2020-09-17
PTWO (Pono Capital Two) Start Date:2022-09-26
PTWOU (Pono Capital Two Unit) Start Date:2022-08-05
PTY (Pimco Corporate & Income Opportunity Fund) Start Date:2007-04-30
PUBM (Pubmatic) Start Date:2020-12-09
PUK (Prudential Plc) Start Date:2013-02-11
PULM (Pulmatrix) Start Date:2014-03-21
PUMP (Propetro Holding Corp) Start Date:2017-03-17
PUYI (Puyi ADS) Start Date:2019-03-29
PVBC (Provident Bancorp) Start Date:2015-07-16
PVH (Pvh) Start Date:2005-01-03
PVL (Permianville Royalty Trust Trust Units) Start Date:2011-11-03
PW (Power Reit) Start Date:2007-05-16
PWFL (Powerfleet) Start Date:2007-05-07
PWM (Prestige Wealth) Start Date:2023-07-06
PWOD (Penns Woods Bancorp) Start Date:2007-05-16
PWP (Perella Weinberg Partners Class A) Start Date:2020-11-24
PWR (Quanta Services) Start Date:2005-01-03
PWSC (Powerschool Holdings) Start Date:2021-07-28
PWUP (Powerup Acquisition) Start Date:2022-04-11
PX (P10) Start Date:2021-10-21
PXD (Pioneer Natural Resources) Start Date:2005-01-03
PXDT (Pixie Dust Technologies) Start Date:2023-08-01
PXLW (Pixelworks) Start Date:2007-04-30
PXMD (Paxmedica) Start Date:2022-08-26
PXS (Pyxis Tankers) Start Date:2015-11-03
PYCR (Paycor) Start Date:2021-07-21
PYN (Pimco New York Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PYPD (Polypid) Start Date:2020-06-26
PYPL (Paypal) Start Date:2015-07-06
PYR (Pyrogenesis Canada Common Shares) Start Date:2021-03-11
PYS (Merrill Lynch Depositor Inc Pplus Tr Ser Rrd-1 Tr Ctf Cl A) Start Date:2007-05-16
PYT (Pplus Tr Gsc-2 Tr Ctf Fltg Rate) Start Date:2007-05-17
PYXS (Pyxis Oncology) Start Date:2021-10-08
PZC (Pimco California Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PZG (Paramount Gold Nevada) Start Date:2015-04-10
PZZA (Papa John's International) Start Date:2007-01-03
QBTS (D-Wave Quantum) Start Date:2022-08-08
QCOM (Qualcomm) Start Date:2005-01-03
QCRH (Qcr) Start Date:2007-05-16
QD (Qudian American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2017-10-18
QDEL (Quidel Corporation) Start Date:2007-01-03
QETA (Quetta Acquisition Corporation) Start Date:2023-11-30
QFIN (360 Digitech American Depositary Shares) Start Date:2018-12-14
QGEN (Qiagen Nv) Start Date:2005-02-15
QH (Quhuo) Start Date:2020-07-13
QIPT (Quipt Home Medical Common Shares) Start Date:2021-05-27
QLGN (Qualigen Therapeutics) Start Date:2015-06-24
QLI (Qilian International Holding Ordinary Shares) Start Date:2021-01-12
QLYS (Qualys) Start Date:2012-09-28
QMCO (Quantum) Start Date:2019-01-15
QNCX (Quince Therapeutics) Start Date:2019-05-09
QNGY (Quanergy Systems) Start Date:2022-02-09
QNRX (Quoin Pharmaceuticals American Depositary Shares) Start Date:2021-10-28
QNST (Quinstreet) Start Date:2010-02-11
QOMO (Qomolangma Acquisition) Start Date:2022-11-25
QRHC (Quest Resource Holding) Start Date:2009-07-16
QRTEA (Qurate Retail) Start Date:2018-03-12
QRTEB (Qurate Retail, Series B) Start Date:2018-03-16
QRVO (Qorvo) Start Date:2015-01-02
QS (Quantumscape Corporation) Start Date:2020-11-23
QSG (Quantasing) Start Date:2023-01-25
QSI (Quantum-Si Orporated) Start Date:2020-11-13
QSIAW (Quantum-Si Incorporated Warrant) Start Date:2020-11-04
QSR (Restaurant Brands International) Start Date:2014-12-15
QTEK (Qualtek Services Class A) Start Date:2022-02-15
QTEWQ (Qualtek Services Inc) Start Date:2021-03-26
QTNT (Quotient R) Start Date:2014-05-27
QTRX (Quanterix) Start Date:2017-12-07
QTWO (Q2 Holdings) Start Date:2014-03-20
QUAD (Quad/Graphics) Start Date:2010-07-06
QUBT (Quantum Computing) Start Date:2018-07-11
QUIK (Quicklogic) Start Date:2007-05-03
QUOT (Quotient Technology) Start Date:2014-03-07
QURE (Uniqure N.V.) Start Date:2014-02-05
R (Ryder System) Start Date:2005-01-03
RA (Brookfield Real Assets Income Fund) Start Date:2016-12-05
RAAS (Cloopen Holding) Start Date:2021-02-09
RACE (Ferrari N.V.) Start Date:2016-01-04
RACY (Relativity Acquisition) Start Date:2022-04-04
RADCQ (Rite Aid Corp) Start Date:2007-04-27
RADI (Radius Global Infrastructure, Class A) Start Date:2018-02-22
RAIL (Freightcar America) Start Date:2007-05-01
RAIN (Rain Therapeutics) Start Date:2021-04-23
RAMP (Liveramp Holdings) Start Date:2018-10-01
RAND (Rand Capital) Start Date:2007-05-16
RANI (Rani Therapeutics) Start Date:2021-07-30
RAPT (Rapt Therapeutics) Start Date:2019-10-31
RARE (Ultragenyx Pharmaceutical) Start Date:2014-01-31
RAVE (Rave Restaurant) Start Date:2007-05-16
RAYA (Erayak Power Solution) Start Date:2022-12-14
RBA (Ritchie Bros. Auctioneers Incorporated) Start Date:2007-05-04
RBB (Rbb Bancorp) Start Date:2017-07-26
RBBN (Ribbon Communication) Start Date:2007-04-30
RBC (Rbc Bearings Incorporated) Start Date:2007-05-04
RBCAA (Republic Bancorp) Start Date:2007-05-16
RBKB (Rhinebeck Bancorp) Start Date:2019-01-17
RBLX (Roblox) Start Date:2021-03-10
RBOT (Vicarious Surgical) Start Date:2020-09-04
RBT (Rubicon Technologies Class A) Start Date:2022-08-16
RC (Ready Capital Corp) Start Date:2013-02-08
RCAT (Red Cat Holdings) Start Date:2007-12-28
RCEL (Avita Medical) Start Date:2012-03-29
RCG (Renn Fund Inc) Start Date:2007-05-22
RCI (Rogers Communications) Start Date:2007-06-15
RCKT (Rocket Pharmaceuticals) Start Date:2015-02-18
RCKY (Rocky Brands) Start Date:2007-05-08
RCL (Royal Caribbean Cruises Ltd) Start Date:2005-01-03
RCM (R1 Rcm) Start Date:2017-03-15
RCMT (Rcm Technologies) Start Date:2007-05-16
RCON (Recon Technology Class A Ordinary Shares) Start Date:2009-07-30
RCRT (Recruiter.com) Start Date:2021-06-30
RCRTW (Recruiter.com  Warrant) Start Date:2021-06-30
RCS (Pimco Strategic Income Fund) Start Date:2007-05-04
RCUS (Arcus Biosciences) Start Date:2018-03-15
RDCM (Radcom Ordinary Shares) Start Date:2008-07-15
RDFN (Redfin Corporation) Start Date:2017-07-28
RDHL (Redhill Biopharma American Depositary Shares) Start Date:2012-12-27
RDI (Reading International Inc Class A) Start Date:2007-05-16
RDIB (Reading International) Start Date:2019-12-16
RDN (Radian) Start Date:2007-01-03
RDNT (Radnet) Start Date:2007-05-16
RDUS (Radius Recycling) Start Date:2007-04-30
RDVT (Red Violet) Start Date:2018-03-26
RDW (Redwire) Start Date:2021-09-03
RDWR (Radware Ltd.) Start Date:2007-04-25
RDY (Dr. Reddy's Laboratories) Start Date:2007-04-23
REAL (The Realreal) Start Date:2019-06-28
REAX (The Real Brokerage Common Shares) Start Date:2021-06-15
REBN (Reborn Coffee) Start Date:2022-08-12
REE (Ree Automotive) Start Date:2021-07-23
REEAW (Ree Automotive Warrant) Start Date:2021-07-23
REFI (Chicago Atlantic Real Estate Finance) Start Date:2021-12-08
REFR (Research Frontiers) Start Date:2007-05-16
REG (Regency Centers Corporation) Start Date:2005-01-03
REGN (Regeneron) Start Date:2005-01-03
REI (Ring Energy) Start Date:2008-06-04
REKR (Rekor Systems) Start Date:2017-08-29
RELI (Reliance Global) Start Date:2021-02-09
RELIW (Reliance Global  Series A Warrants) Start Date:2021-02-09
RELL (Richardson Electronics) Start Date:2007-05-03
RELX (Relx Plc Plc American Depositary Shares) Start Date:2007-05-07
RELY (Remitly Global,) Start Date:2021-09-23
RENB (Renovaro Biosciences Inc) Start Date:2015-02-02
RENE (Cartesian Growth Ii) Start Date:2022-07-08
RENEU (Cartesian Growth Ii Unit) Start Date:2022-05-06
RENT (Rent The Runway, Class A) Start Date:2021-10-27
REPL (Replimune) Start Date:2018-07-20
REPX (Riley Exploration Permian,) Start Date:2007-05-16
RERE (Atrenew American Depositary Shares) Start Date:2021-06-18
RES (Rpc) Start Date:2007-04-26
RETA (Reata Pharmaceuticals) Start Date:2016-05-26
RETO (Reto Eco-Solutions Common Shares) Start Date:2017-11-29
REVB (Revelation Biosciences) Start Date:2020-11-17
REVBU (Revelation Biosciences Unit) Start Date:2020-10-08
REVBW (Revelation Biosciences Warrant) Start Date:2020-11-16
REVG (Rev) Start Date:2017-01-27
REX (Rex American Resources) Start Date:2007-05-16
REXR (Rexford Industrial Realty) Start Date:2013-07-19
REYN (Reynolds Consumer Products) Start Date:2020-01-31
REZI (Resideo Technologies) Start Date:2018-10-29
RF (Regions Financial) Start Date:2005-01-03
RFAC (Rf Acquisition) Start Date:2022-04-20
RFI (Cohen & Steers Total Return Realty Fund) Start Date:2007-05-16
RFIL (Rf Industries) Start Date:2007-05-16
RFL (Rafael) Start Date:2018-03-27
RFM (Rivernorth Flexible Municipal Income Fund) Start Date:2020-03-27
RFMZ (Rivernorth Flexible Municipal Income Fund Ii) Start Date:2021-02-24
RGA (Reinsurance) Start Date:2007-04-25
RGC (Regencell Bioscience) Start Date:2007-05-01
RGCO (Rgc Resources) Start Date:2007-05-17
RGEN (Repligen Corporation) Start Date:2007-01-03
RGF (The Real Good Food Company Class A) Start Date:2021-11-05
RGLD (Royal Gold) Start Date:2010-04-19
RGLS (Regulus Therapeutics) Start Date:2012-10-04
RGNX (Regenxbio) Start Date:2015-09-17
RGP (Resources Connection) Start Date:2007-05-02
RGR (Sturm Ruger) Start Date:2007-04-27
RGS (Regis) Start Date:2007-05-01
RGT (Royce Global Value Trust) Start Date:2013-10-18
RGTI (Rigetti Computing) Start Date:2022-03-02
RGTIW (Rigetti Computing Warrants) Start Date:2022-03-02
RH (Rh) Start Date:2012-11-02
RHE (Regional Health Properties) Start Date:2017-10-02
RHI (Robert Half International) Start Date:2005-01-03
RIBT (Ricebran Technologies) Start Date:2007-05-09
RICK (Rci Hospitality) Start Date:2007-05-08
RIDE (Lordstown Motors Class A) Start Date:2019-04-17
RIG (Transocean Ltd.) Start Date:2008-12-19
RIGL (Rigel Pharmaceuticals) Start Date:2007-05-01
RILY (B. Riley Financial) Start Date:2009-08-04
RILYP (B. Riley Financial Depositary Shares Each Representing A 1/1000Th Fractional Interest In A Share Of Series A Cumulative Perpetual Preferred Stock) Start Date:2019-10-08
RIO (Rio Tinto Plc) Start Date:2013-02-11
RIOT (Riot Blockchain,) Start Date:2007-08-28
RITM (Rithm Capital) Start Date:2013-05-02
RIV (Rivernorth Opportunities Fund) Start Date:2015-12-24
RIVN (Rivian Automotive, Class A) Start Date:2021-11-10
RJF (Raymond James Financial) Start Date:2005-01-03
RKDA (Arcadia Biosciences) Start Date:2015-05-15
RKLB (Rocket Lab Usa,) Start Date:2021-08-19
RKLY (Rockley Photonics Holdings Ordinary Shares) Start Date:2021-08-12
RKT (Rocket Cos) Start Date:2020-08-06
RL (Polo Ralph Lauren) Start Date:2005-01-03
RLAY (Relay Therapeutics) Start Date:2020-07-16
RLGT (Radiant Logistics) Start Date:2007-05-18
RLI (Rli) Start Date:2016-01-04
RLJ (Rlj Lodging) Start Date:2011-05-11
RLMD (Relmada Therapeutics) Start Date:2015-09-08
RLTY (Cohen & Steers Real Estate Opportunities And Income Fund Common Shares Of Beneficial Interest) Start Date:2022-02-24
RLX (Rlx Technology) Start Date:2021-01-22
RLYB (Rallybio) Start Date:2021-07-29
RM (Regional Management) Start Date:2012-03-28
RMAX (Re/Max) Start Date:2013-10-02
RMBI (Richmond Mutual Bancorporation) Start Date:2019-07-02
RMBL (Rumbleon Class B) Start Date:2017-01-09
RMBS (Rambus) Start Date:2007-04-25
RMCF (Rocky Mountain Chocolate Factory) Start Date:2007-05-16
RMD (Resmed) Start Date:2005-01-03
RMI (Rivernorth Opportunistic Municipal Income Fund) Start Date:2018-10-26
RMMZ (Rivernorth Managed Duration Municipal Income Fund Ii) Start Date:2022-02-11
RMNI (Rimini Street) Start Date:2015-08-28
RMR (The Rmr) Start Date:2015-12-14
RMT (Royce Micro-Cap Trust) Start Date:2007-05-16
RMTI (Rockwell Medical) Start Date:2007-05-16
RNA (Avidity Biosciences) Start Date:2020-06-12
RNAC (Cartesian Therapeutics Inc) Start Date:2016-06-22
RNAZ (Transcode Therapeutics) Start Date:2021-07-09
RNG (Ringcentral) Start Date:2013-09-27
RNGR (Ranger Energy Services Class A) Start Date:2017-08-11
RNLX (Renalytix Ai) Start Date:2020-07-17
RNP (Cohen & Steers Reit And Preferred And Income Fund Common Shares) Start Date:2007-05-09
RNR (Renaissancere Holdings Ltd.) Start Date:2007-01-03
RNST (Renasant) Start Date:2007-05-10
RNW (Renew Energy Global) Start Date:2021-08-24
RNWWW (Renew Energy Global Plc Warrant) Start Date:2021-08-24
RNXT (Renovorx) Start Date:2021-08-26
ROAD (Construction Partners) Start Date:2018-05-04
ROCK (Gibraltar Industries) Start Date:2007-04-30
ROG (Rogers) Start Date:2007-05-01
ROI (Riskon International Inc) Start Date:2010-02-12
ROIC (Retail Opportunity) Start Date:2014-03-06
ROIV (Roivant Sciences Common Shares) Start Date:2021-10-01
ROIVW (Roivant Sciences Warrant) Start Date:2021-10-01
ROK (Rockwell Automation) Start Date:2005-01-03
ROKU (Roku) Start Date:2017-09-28
ROL (Rollins) Start Date:2005-01-03
ROOT (Root Insurance) Start Date:2020-11-02
ROP (Roper Technologies) Start Date:2007-04-30
ROST (Ross Stores) Start Date:2005-01-03
ROVR (Rover , Class A) Start Date:2021-02-01
RPAY (Repay Corp) Start Date:2018-07-17
RPD (Rapid7) Start Date:2015-07-17
RPHM (Reneo Pharmaceuticals) Start Date:2021-04-09
RPID (Rapid Micro Biosystems) Start Date:2021-07-15
RPM (Rpm International) Start Date:2007-01-03
RPRX (Royalty Pharma) Start Date:2020-06-16
RPT (Rpt Realty) Start Date:2007-05-01
RPTX (Repare Therapeutics) Start Date:2020-06-19
RQI (Cohen & Steers Quality Income Realty Fund Inc Common Shares) Start Date:2007-05-08
RR (Richtech Robotics) Start Date:2023-11-17
RRBI (Red River Bancshares) Start Date:2019-05-03
RRC (Range Resources Corporation) Start Date:2005-01-03
RRGB (Red Robin Gourmet Burgers) Start Date:2007-04-24
RRR (Red Rock Resorts) Start Date:2016-04-27
RRX (Regal Rexnord Corporation) Start Date:2007-05-01
RS (Reliance Steel) Start Date:2007-04-30
RSF (Rivernorth Specialty Finance Corporation) Start Date:2019-06-12
RSG (Republic Services Inc) Start Date:2005-01-03
RSI (Rush Street Interactive,) Start Date:2020-04-23
RSKD (Riskified) Start Date:2021-07-29
RSLS (Reshape Lifesciences) Start Date:2017-01-12
RSSS (Research Solutions Inc) Start Date:2009-05-15
RSVR (Reservoir Media) Start Date:2021-01-05
RSVRW (Reservoir Media Warrant) Start Date:2021-01-07
RTC (Baijiayun Class A) Start Date:2007-05-16
RTO (Rentokil Initial Plc) Start Date:2008-10-27
RTX (Raytheon Co.) Start Date:2007-04-27
RUM (Rumble Class A) Start Date:2021-04-14
RUN (Sunrun) Start Date:2015-08-05
RUSHA (Rush Enterprises) Start Date:2007-05-04
RUSHB (Rush Enterprises) Start Date:2007-05-16
RVLP (Rvl Pharmaceuticals Plc Ordinary Shares) Start Date:2018-10-19
RVLV (Revolve ,) Start Date:2019-06-07
RVMD (Revolution Medicines) Start Date:2020-02-13
RVNC (Revance Therapeutics Com) Start Date:2014-02-06
RVP (Retractable Technologies) Start Date:2007-05-16
RVPH (Reviva Pharmaceuticals Holdings) Start Date:2018-10-18
RVPHW (Reviva Pharmaceuticals Holdings Warrants) Start Date:2018-10-18
RVSB (Riverview Bancorp) Start Date:2007-05-16
RVSN (Rail Vision Ordinary Share) Start Date:2022-03-31
RVSNW (Rail Vision Warrant) Start Date:2022-03-31
RVT (Royce Value Trust) Start Date:2007-05-10
RVTY (Revvity Inc) Start Date:2005-01-03
RVYL (Ryvyl) Start Date:2021-02-17
RWAY (Runway Growth Finance) Start Date:2021-10-21
RWLK (Rewalk Robotics Ordinary Shares) Start Date:2014-09-12
RWOD (Redwoods Acquisition) Start Date:2022-04-29
RWT (Redwood Trust) Start Date:2007-04-27
RXO (Rxo) Start Date:2022-10-27
RXRX (Recursion Pharmaceuticals) Start Date:2021-04-16
RXST (Rxsight) Start Date:2021-07-30
RXT (Rackspace Technologies) Start Date:2020-08-05
RY (Royal Bank Of Canada) Start Date:2007-04-30
RYAAY (Ryanair Holdings Plc) Start Date:2013-02-11
RYAM (Rayonier Advanced Materials In) Start Date:2014-06-30
RYAN (Ryan Specialty) Start Date:2021-07-22
RYI (Ryerson Holding) Start Date:2014-08-08
RYN (Rayonier) Start Date:2007-01-03
RYTM (Rhythm Pharmaceuticals) Start Date:2017-10-05
RYZB (Rayzebio) Start Date:2023-09-15
RZB (Reinsurance Of America Incorporated 5.75% Fixed-To-Floating Rate Subordinated Debentures Due 2056) Start Date:2016-06-13
RZLT (Rezolute) Start Date:2017-12-19
S (Sprint Corporation) Start Date:2021-06-30
SA (Seabridge Gold,) Start Date:2007-05-02
SABR (Sabre Corporation) Start Date:2014-04-17
SABS (Sab Biotherapeutics) Start Date:2021-02-09
SABSW (Sab Biotherapeutics Warrant) Start Date:2021-10-25
SACH (Sachem Capital Common Shares) Start Date:2017-02-10
SAFE (Safehold) Start Date:2017-06-22
SAFT (Safety Insurance) Start Date:2007-05-09
SAGE (Sage Therapeutics) Start Date:2014-07-18
SAH (Sonic Automotive) Start Date:2007-04-30
SAIA (Saia) Start Date:2007-05-02
SAIC (Science Applications International Corporation) Start Date:2013-09-16
SAITW (Sai.Tech Global Warrant) Start Date:2021-06-28
SALM (Salem Media  Class A) Start Date:2007-05-16
SAM (Boston Beer Company) Start Date:2007-05-09
SAMG (Silvercrest Asset Management G) Start Date:2013-06-27
SAN (Banco Santander S.A.) Start Date:2007-04-27
SANA (Sana Biotechnology) Start Date:2021-02-04
SAND (Sandstorm Gold Ltd) Start Date:2009-06-01
SANG (Sangoma Technologies Common Shares) Start Date:2021-12-16
SANM (Sanmina) Start Date:2007-04-30
SANW (S&W Seed Company) Start Date:2010-06-14
SAP (Sap Se ADS) Start Date:2013-02-11
SAR (Saratoga Investment New) Start Date:2010-08-13
SASI (Sigma Labs) Start Date:2010-10-14
SASR (Sandy Spring Bancorp) Start Date:2007-05-16
SATL (Satellogic Class A Ordinary Shares) Start Date:2022-01-26
SATLW (Satellogic Warrant) Start Date:2022-01-26
SATS (Echostar) Start Date:2008-01-02
SATX (Satixfy Communications) Start Date:2021-11-08
SAVA (Cassava Sciences) Start Date:2007-04-30
SAVE (Spirit Airlines) Start Date:2011-05-26
SB (Safe Bulkers) Start Date:2008-05-29
SBAC (Sba Communications) Start Date:2005-01-03
SBCF (Seacoast Banking O) Start Date:2007-05-08
SBET (Sharplink Gaming Ordinary Shares) Start Date:2007-05-16
SBEV (Splash Beverage) Start Date:2020-12-24
SBFG (Sb Financial  Commo) Start Date:2007-05-16
SBFM (Sunshine Biopharma) Start Date:2022-02-15
SBFMW (Sunshine Biopharma Warrant) Start Date:2022-02-15
SBGI (Sinclair Broadcast) Start Date:2007-05-02
SBH (Sally Beauty) Start Date:2007-04-27
SBI (Western Asset Intermediate Muni Fund Inc) Start Date:2007-05-16
SBIG (Springbig Holdings) Start Date:2021-04-06
SBIGW (Springbig Holdings Warrant) Start Date:2021-04-05
SBLK (Star Bulk Carriers) Start Date:2007-12-03
SBOW (Silverbow Resorces) Start Date:2017-05-05
SBR (Sabine Royalty Trust) Start Date:2007-05-04
SBRA (Sabra Health Care Reit) Start Date:2010-11-08
SBS (Companhia De Saneamento Basico Do Estado De Sao Paulo - Sabesp) Start Date:2013-02-11
SBSI (Southside Bancshares) Start Date:2007-05-16
SBSW (Sibanye Stillwater Limited) Start Date:2013-02-21
SBT (Sterling Bancorp) Start Date:2017-11-17
SBTX (Silverback Therapeutics) Start Date:2020-12-04
SBUX (Starbucks) Start Date:2005-01-03
SCCO (Southern Copper Corporation) Start Date:2010-02-17
SCD (Lmp Capital And Income Fund) Start Date:2007-05-08
SCHL (Scholastic) Start Date:2007-05-03
SCHW (Charles Schwab Corporation) Start Date:2010-03-05
SCI (Service International) Start Date:2007-01-03
SCKT (Socket Mobile) Start Date:2007-05-16
SCL (Stepan) Start Date:2007-05-16
SCLX (Scilex Holding Company) Start Date:2021-03-05
SCM (Stellus Capital Investment) Start Date:2012-11-08
SCNI (Scinai Immunotherapeutics Ltd.) Start Date:2015-05-12
SCOAU (Scion Tech Growth I Unit) Start Date:2020-12-17
SCOAW (Scion Tech Growth I Warrant) Start Date:2021-02-08
SCOBU (Scion Tech Growth Ii Units) Start Date:2021-02-10
SCOBW (Scion Tech Growth Ii Warrants) Start Date:2021-04-08
SCOR (Comscore) Start Date:2007-06-27
SCPH (Scpharmaceuticals) Start Date:2017-11-17
SCPL (Sciplay Class A) Start Date:2019-05-03
SCS (Steelcase) Start Date:2007-05-03
SCSC (Scansource) Start Date:2007-05-02
SCTL (Societal Cdmo) Start Date:2014-03-07
SCU (Sculptor Capital Management) Start Date:2019-10-01
SCVL (Shoe Carnival) Start Date:2007-04-18
SCWO (374Water) Start Date:2008-10-03
SCWX (Secureworks) Start Date:2016-04-22
SCX (L.S. Starrett Company) Start Date:2007-05-16
SCYX (Scynexis) Start Date:2014-05-02
SD (Sandridge Energy,) Start Date:2016-10-04
SDCCQ (Smiledirectclub Inc) Start Date:2019-09-12
SDGR (Schrodinger) Start Date:2020-02-06
SDHY (Pgim Short Duration High Yield Opportunities Fund Common Shares) Start Date:2020-11-25
SDIG (Stronghold Digital Mining) Start Date:2021-10-20
SDOT (Sadot Inc) Start Date:2020-02-13
SDPI (Superior Drilling Products) Start Date:2014-05-23
SDRL (Seadrill) Start Date:2022-06-01
SE (Sea Limited) Start Date:2017-10-20
SEAC (Seachange International) Start Date:2007-04-26
SEAS (Seaworld Entertainment) Start Date:2013-04-19
SEAT (Vivid Seats Class A) Start Date:2021-10-19
SEATW (Vivid Seats Warrant) Start Date:2021-10-19
SEB (Seaboard) Start Date:2007-05-02
SECO (Secoo Holding ADS) Start Date:2017-09-22
SEDG (Solaredge Technologies) Start Date:2015-03-26
SEE (Sealed Air) Start Date:2005-01-03
SEED (Origin Agritech) Start Date:2007-04-13
SEEL (Seelos Therapeutics) Start Date:2007-05-16
SEER (Seer, Class A) Start Date:2020-12-04
SEIC (Sei Investments Company) Start Date:2007-01-03
SELF (Global Self Storage) Start Date:2008-04-07
SEM (Select Medical Holdings Corporation) Start Date:2009-09-25
SEMR (Semrush) Start Date:2021-03-25
SENEA (Seneca Foods) Start Date:2007-05-16
SENEB (Seneca Foods Class B) Start Date:2007-05-16
SENS (Senseonics Holdings,) Start Date:2016-03-18
SEQL (Seqll Inc) Start Date:2021-08-27
SERA (Sera Prognostics) Start Date:2021-07-15
SES (Ses Ai) Start Date:2022-02-04
SEVN (Seven Hills Realty Trust) Start Date:2014-10-31
SF (Stifel Financial) Start Date:2012-02-08
SFBC (Sound Financial Bancorp) Start Date:2012-08-23
SFBS (Servisfirst Bancshares) Start Date:2014-05-14
SFE (Safeguard Scientifics) Start Date:2007-05-02
SFET (Safe-T American Depositary Share) Start Date:2018-09-11
SFIX (Stitch Fix) Start Date:2017-11-17
SFL (Sfl Corp) Start Date:2007-04-25
SFM (Sprouts Farmers Market) Start Date:2013-08-01
SFNC (Simmons First National) Start Date:2007-05-08
SFRT (Appreciate Holdings Inc) Start Date:2021-01-25
SFRT (Appreciate Holdings Inc) Start Date:2021-01-25
SFST (Southern First Bancshares) Start Date:2007-07-06
SFTGQ (Shift Technologies Inc) Start Date:2019-06-04
SFWL (Shengfeng Development Limited) Start Date:2023-03-31
SG (Sweetgreen) Start Date:2021-11-18
SGA (Saga Communications) Start Date:2007-05-16
SGBX (Sg Blocks) Start Date:2017-06-22
SGC (Superior Uniform) Start Date:2007-05-16
SGD (Safe &Amp; Green Development Corp) Start Date:2023-09-19
SGE (Strong Global Entertainment) Start Date:2023-05-16
SGEN (Seattle Genetics) Start Date:2007-01-03
SGH (Smart Global) Start Date:2017-05-24
SGHC (Super) Start Date:2022-01-28
SGHL (Signal Hill Acquisition) Start Date:2022-03-28
SGHT (Sight Sciences) Start Date:2021-07-15
SGLY (Singularity Future Technology) Start Date:2022-01-07
SGMA (Sigmatron International) Start Date:2007-05-16
SGML (Sigma Lithium Common Shares) Start Date:2021-09-13
SGMO (Sangamo Therapeutics) Start Date:2007-04-27
SGMT (Sagimet Biosciences) Start Date:2023-07-14
SGN (Signing Day Sports) Start Date:2023-11-14
SGRP (Spar) Start Date:2007-05-16
SGRY (Surgery Partners) Start Date:2015-10-01
SGU (Star L.P.) Start Date:2007-05-11
SHAK (Shake Shack) Start Date:2015-01-30
SHBI (Shore Bancshares) Start Date:2007-05-16
SHC (Sotera Health Co) Start Date:2020-11-20
SHCO (Soho House &Amp; Co Inc) Start Date:2021-07-15
SHCR (Sharecare, Class A) Start Date:2020-11-23
SHCRW (Sharecare Warrant) Start Date:2020-11-25
SHEL (Royal Dutch Shell Plc American Depositary Shares) Start Date:2007-04-26
SHEN (Shenandoah Telecommunicat) Start Date:2007-05-16
SHFS (Shf Holdings Class A) Start Date:2021-08-20
SHG (Shinhan Financial Co American Depositary Shares) Start Date:2013-02-11
SHIM (Shimmick Corporation) Start Date:2023-11-14
SHIP (Seanergy Maritime Holdings) Start Date:2008-10-15
SHLS (Shoals Technologies) Start Date:2021-01-27
SHOO (Steven Madden Ltd.) Start Date:2007-01-03
SHOP (Shopify Class A Subordinate Voting Shares) Start Date:2015-05-21
SHOT (Safety Shot Inc) Start Date:2020-10-30
SHPH (Shuttle Pharmaceuticals Holdings) Start Date:2022-08-31
SHPW (Shapeways Holdings) Start Date:2019-11-14
SHUA (Shuaa Partners Acquisition I) Start Date:2022-04-26
SHW (Sherwin-Williams) Start Date:2005-01-03
SHYF (Shyft) Start Date:2007-05-04
SIBN (Si-Bone) Start Date:2018-10-17
SID (Companhia Siderurgica Nacional) Start Date:2013-02-11
SIDU (Sidus Space Class A) Start Date:2021-12-14
SIEB (Siebert Financial) Start Date:2007-05-16
SIEN (Sientra) Start Date:2014-10-29
SIF (Sifco Industries) Start Date:2007-05-16
SIFY (Sify Technologies American Depositary Shares) Start Date:2007-04-25
SIG (Signet Jewelers Limited) Start Date:2005-01-03
SIGA (Siga Technologies) Start Date:2015-03-20
SIGI (Selective Insurance) Start Date:2007-01-03
SII (Sprott Common Shares) Start Date:2007-04-30
SILC (Silicom Ordinary Shares) Start Date:2007-05-16
SILK (Silk Road Medical) Start Date:2019-04-04
SILO (Silo Pharma) Start Date:2022-09-27
SILV (Silvercrest Metals Common Shares) Start Date:2018-08-21
SIM (Grupo Simec S.A.B. De C.V. American Depositary Shares) Start Date:2013-02-11
SIMO (Silicon Motion Technology American Depositary Shares) Start Date:2007-05-04
SINT (Sintx Technologies) Start Date:2014-02-13
SIRI (Sirius Xm Holdings Inc) Start Date:2005-01-03
SISI (Shineco) Start Date:2016-09-28
SITC (Site Centers) Start Date:2007-05-01
SITE (Siteone Landscape Supply) Start Date:2016-05-12
SITM (Sitime) Start Date:2019-11-21
SIX (Six Flags Entertainment Corporation) Start Date:2010-06-21
SJ (Scienjoy Holding Class A Ordinary Shares) Start Date:2019-02-06
SJM (Jm Smucker) Start Date:2005-01-03
SJT (San Juan Basin Royalty Trust) Start Date:2007-04-27
SJW (Sjw) Start Date:2007-05-14
SKE (Skeena Resources Common Shares) Start Date:2008-03-25
SKGR (Sk Growth Opportunities Class A) Start Date:2022-08-18
SKGRU (Sk Growth Opportunities Unit) Start Date:2022-06-24
SKIL (Skillsoft Class A) Start Date:2019-07-26
SKIN (The Beauty Health Company Class A) Start Date:2020-11-24
SKLZ (Skillz) Start Date:2020-12-15
SKM (Sk Telecom Co.Ltd) Start Date:2013-02-11
SKT (Tanger Factory Outlet) Start Date:2007-05-01
SKWD (Skyward Specialty Insurance) Start Date:2023-01-13
SKX (Skechers U.S.A.) Start Date:2007-01-03
SKY (Skyline) Start Date:2007-05-10
SKYH (Sky Harbour) Start Date:2022-01-26
SKYT (Skywater Technology) Start Date:2021-04-21
SKYW (Skywest) Start Date:2007-04-27
SKYX (Skyx Platforms) Start Date:2022-02-10
SLAB (Silicon Laboratories) Start Date:2007-01-03
SLAM (Slam) Start Date:2021-04-16
SLAMU (Slam Unit) Start Date:2021-02-23
SLAMW (Slam Warrant) Start Date:2021-04-16
SLB (Schlumberger Ltd.) Start Date:2005-01-03
SLCA (Us Silica) Start Date:2012-02-01
SLDB (Solid Biosciences) Start Date:2018-01-26
SLDP (Solid Power) Start Date:2021-05-18
SLDPW (Solid Power Warrant) Start Date:2021-12-09
SLE (Super League Enterprise Inc) Start Date:2019-02-26
SLF (Sun Life Financial) Start Date:2007-01-03
SLG (Sl Green Realty) Start Date:2005-01-03
SLGC (Somalogic) Start Date:2021-04-23
SLGCW (Somalogic Warrant) Start Date:2021-04-16
SLGL (Sol-Gel Technologies Ordinary Shares) Start Date:2018-02-01
SLGN (Silgan Holdings) Start Date:2007-01-03
SLI (Standard Lithium Ltd.) Start Date:2021-07-13
SLM (Slm Corporation) Start Date:2011-12-12
SLMBP (Slm Floating Rate Non-Cumulative Preferred Stock Series B) Start Date:2007-05-16
SLN (Silence Therapeutics Plc American Depository Share) Start Date:2020-09-08
SLNA (Selina Hospitality Plc) Start Date:2022-10-27
SLND (Southland Holdings Inc) Start Date:2021-12-23
SLNG (Stabilis Solutions) Start Date:2007-05-16
SLNH (Soluna Holdings) Start Date:2009-04-23
SLNO (Soleno Therapeutics) Start Date:2014-11-13
SLP (Simulations Plus) Start Date:2007-05-16
SLQT (Selectquote) Start Date:2020-05-21
SLRC (Slr Investment) Start Date:2010-02-09
SLRN (Acelyrin) Start Date:2023-05-05
SLRX (Salarius Pharmaceuticals) Start Date:2015-01-29
SLS (Sellas Life Sciences) Start Date:2008-03-13
SLVM (Sylvamo Corporation) Start Date:2021-10-01
SLVR (Silverspac Class A) Start Date:2021-11-01
SM (Sm Energy) Start Date:2007-04-30
SMAR (Smartsheet) Start Date:2018-04-27
SMBC (Southern Missouri Bancorp) Start Date:2007-05-16
SMBK (Smartfinancial) Start Date:2007-05-16
SMCI (Super Micro Computer) Start Date:2007-05-16
SMFG (Sumitomo Mitsui Financial) Start Date:2013-02-11
SMFL (Smart For Life) Start Date:2022-02-16
SMFR (Sema4 Holdings Class A) Start Date:2020-11-04
SMFRW (Sema4 Holdings Warrant) Start Date:2020-11-02
SMG (The Scotts Miracle-Gro Company) Start Date:2007-01-03
SMHI (Seacor Marine) Start Date:2017-06-02
SMID (Smith-Midland) Start Date:2007-05-16
SMLP (Summit Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2012-09-28
SMLR (Semler Scientific,) Start Date:2014-02-21
SMMF (Summit Financial) Start Date:2007-05-16
SMMT (Summit Therapeutics) Start Date:2015-03-05
SMP (Standard Motor Products) Start Date:2007-05-09
SMPL (The Simply Good Foods Company) Start Date:2017-07-10
SMR (Nuscale Power Class A) Start Date:2022-05-03
SMRT (Smartrent) Start Date:2021-08-25
SMSI (Smith Micro Software) Start Date:2007-04-30
SMTC (Semtech Corporation) Start Date:2007-01-03
SMTI (Sanara Medtech) Start Date:2008-06-12
SMTS (Sierra Metals) Start Date:2017-07-11
SMWB (Similarweb) Start Date:2021-05-12
SMX (Smx) Start Date:2021-12-09
SNA (Snap-On) Start Date:2005-01-03
SNAL (Snail) Start Date:2022-11-10
SNAP (Snap) Start Date:2017-03-02
SNAX (Stryve Foods Class A) Start Date:2019-03-06
SNAXW (Stryve Foods Warrant) Start Date:2019-03-06
SNBR (Sleep Number Corp) Start Date:2007-04-27
SNCE (Science 37 Holdings) Start Date:2020-11-23
SNCR (Synchronoss) Start Date:2007-05-04
SNCY (Sun Country Airlines) Start Date:2021-03-17
SND (Smart Sand) Start Date:2016-11-04
SNDA (Sonida Senior Living) Start Date:2007-05-01
SNDL (Sundial Growers Common Shares) Start Date:2019-08-01
SNDR (Schneider National) Start Date:2017-04-06
SNDX (Syndax Pharmaceuticals) Start Date:2016-03-03
SNES (Senestech) Start Date:2016-12-08
SNEX (Stonex) Start Date:2007-04-16
SNFCA (Security Natl Financial) Start Date:2007-05-16
SNGX (Soligenix) Start Date:2009-09-30
SNMP (Evolve Transition Infrastructure Lp) Start Date:2007-04-10
SNN (Smith & Nephew Plc) Start Date:2013-02-11
SNOA (Sonoma Pharmaceuticals) Start Date:2007-05-16
SNOW (Snowflake) Start Date:2020-09-16
SNPO (Snap One Holdings) Start Date:2021-07-28
SNPS (Synopsys) Start Date:2005-01-03
SNPX (Synaptogenix) Start Date:2021-06-07
SNSE (Sensei Biotherapeutics) Start Date:2021-02-04
SNT (Senstar Technologies Ordinary Shares) Start Date:2007-05-16
SNTG (Sentage Holdings) Start Date:2021-07-09
SNTI (Senti Biosciences) Start Date:2021-05-26
SNV (Synovus Financial) Start Date:2007-01-03
SNX (Synnex Corporation) Start Date:2007-01-03
SNY (Sanofi ADS) Start Date:2013-02-11
SO (Southern Co.) Start Date:2005-01-03
SOBR (Sobr Safe) Start Date:2022-05-16
SOFI (Sofi Technologies,) Start Date:2021-06-01
SOFO (Sonic Foundry) Start Date:2007-05-02
SOHO (Sotherly Hotels) Start Date:2007-05-16
SOHU (Sohu.com American Depositary Shares) Start Date:2007-04-30
SOI (Solaris Oilfield Infrastructure) Start Date:2017-05-12
SOL (Renesola American Depsitary Shares) Start Date:2008-01-29
SOLO (Electrameccanica Vehicles) Start Date:2018-08-09
SOLOW (Electrameccanica Vehicles Warrants) Start Date:2018-08-09
SON (Sonoco Products Company) Start Date:2007-01-03
SOND (Sonder Holdings Class A) Start Date:2021-03-15
SONDW (Sonder Holdings Warrants) Start Date:2021-03-15
SONM (Sonim Technologies) Start Date:2019-05-10
SONN (Sonnet Biotherapeutics Holdings) Start Date:2012-06-21
SONO (Sonos) Start Date:2018-08-02
SONX (Sonendo) Start Date:2021-10-29
SONY (Sony American Depositary Shares) Start Date:2013-02-11
SOPA (Society Pass Incorporated) Start Date:2021-11-09
SOPH (Sophia Genetics) Start Date:2021-07-23
SOR (Source Capital) Start Date:2007-05-16
SOS (Sos American Depositary Shares) Start Date:2017-04-28
SOTK (Sono-Tek) Start Date:2007-05-16
SOUN (Soundhound AI Inc Class A) Start Date:2022-04-28
SOUNW (Soundhound AI Warrant) Start Date:2021-04-26
SOVO (Sovos Brands) Start Date:2021-09-23
SP (Sp Plus O) Start Date:2007-05-16
SPB (Spectrum Brands Holdings) Start Date:2010-03-18
SPCB (Supercom Ordinary Shares) Start Date:2008-12-22
SPCE (Virgin Galactic Holdings) Start Date:2017-09-29
SPCM (Sound Point Acquisition I, Ltd) Start Date:2022-04-25
SPE (Special Opportunities Fund Inc) Start Date:2007-05-16
SPEC (Spectaire Holdings Inc) Start Date:2021-12-27
SPFI (South Plains Financial) Start Date:2019-05-09
SPG (Simon Property Inc) Start Date:2005-01-03
SPGC (Sacks Parente Golf) Start Date:2023-08-15
SPGI (S&P Global) Start Date:2007-04-27
SPH (Suburban Propane Partners L P) Start Date:2007-05-09
SPHR (Sphere Entertainment Co.) Start Date:2020-04-09
SPI (Spi Energy Co., Ordinary Shares) Start Date:2016-01-19
SPIR (Spire Global Class A) Start Date:2020-11-03
SPKL (Spark I Acquisition Corporation) Start Date:2023-11-27
SPLK (Splunk) Start Date:2012-04-19
SPLP (Steel Partners Holdings L.P.) Start Date:2012-04-10
SPNS (Sapiens International) Start Date:2007-05-16
SPNT (Siriuspoint Ltd.) Start Date:2013-08-15
SPOK (Spok  O) Start Date:2007-05-04
SPOT (Spotify Technology S.A.) Start Date:2018-04-03
SPPL (Simpple Ltd.) Start Date:2023-09-13
SPR (Spirit Aerosystems Holdings) Start Date:2007-01-03
SPRB (Spruce Biosciences) Start Date:2020-10-09
SPRC (Scisparc Ordinary Shares) Start Date:2021-12-22
SPRO (Spero Therapeutics) Start Date:2017-11-02
SPRU (Spruce Power Holding Class A) Start Date:2022-11-14
SPRY (Ars Pharmaceuticals) Start Date:2020-12-04
SPSC (Sps Commerce) Start Date:2010-04-23
SPT (Sprout Social) Start Date:2019-12-13
SPTN (Spartannash Company O) Start Date:2007-05-03
SPWH (Sportsmans Warehouse) Start Date:2014-04-17
SPWR (Sunpower) Start Date:2007-05-02
SPXC (Spx Corp) Start Date:2007-04-30
SPXX (Nuveen S&P 500 Dynamic Overwrite Fund) Start Date:2007-04-24
SQ (Square) Start Date:2015-11-19
SQFT (Presidio Property Trust) Start Date:2020-10-07
SQFTW (Presidio Property Trust Series A Purchase Warrants) Start Date:2022-01-24
SQLLW (Seqll Warrant) Start Date:2021-08-27
SQM (Sociedad Quimica Y Minera De Chile S.A.) Start Date:2013-02-11
SQNS (Sequans Communications S.A. American Depositary Shares) Start Date:2011-04-15
SQSP (Squarespace) Start Date:2021-05-19
SR (Spire) Start Date:2007-05-07
SRAD (Sportradar) Start Date:2021-09-14
SRC (Spirit Realty Capital) Start Date:2012-09-20
SRCE (1St Source) Start Date:2007-05-16
SRCL (Stericycle) Start Date:2005-01-03
SRDX (Surmodics) Start Date:2007-04-30
SRE (Sempra Energy) Start Date:2005-01-03
SRFM (Surf Air Mobility) Start Date:2023-07-27
SRG (Seritage Growth Properties) Start Date:2015-07-06
SRGA (Surgalign Holdings) Start Date:2007-05-14
SRI (Stoneridge) Start Date:2007-05-16
SRL (Scully Royalty Ltd.) Start Date:2019-06-04
SRM (Srm Entertainment) Start Date:2023-08-15
SRNE (Sorrento Therapeutics  C) Start Date:2009-12-31
SRPT (Sarepta Therapeutics) Start Date:2007-05-02
SRRK (Scholar Rock Holding) Start Date:2018-05-24
SRT (Startek) Start Date:2007-05-08
SRTS (Sensus Healthcare) Start Date:2016-07-26
SRV (Cushing Mlp & Infrastructure Total Return Fund) Start Date:2007-08-27
SRZN (Surrozen) Start Date:2021-08-12
SRZNW (Surrozen Warrant) Start Date:2021-08-12
SSB (South State Corp) Start Date:2007-05-16
SSBI (Summit State Bank) Start Date:2007-05-16
SSBK (Southern States Bancshares) Start Date:2021-08-12
SSD (Simpson Manufacturing Co.) Start Date:2007-01-03
SSIC (Silver Spike Investment) Start Date:2022-02-04
SSKN (Strata Skin Sciences) Start Date:2007-05-16
SSL (Sasol Limited) Start Date:2013-02-11
SSNC (Ss&C Technologies Holdings) Start Date:2010-03-31
SSNT (Silversun Technologies) Start Date:2007-05-16
SSP (E. W. Scripps Co) Start Date:2005-01-03
SSRM (Ssr Mining) Start Date:2007-04-27
SSSS (Suro Capital) Start Date:2011-04-28
SST (System1) Start Date:2022-01-28
SSTI (Shotspotter) Start Date:2017-06-07
SSTK (Shutterstock) Start Date:2012-11-12
SSU (Signa Sports United N.V. Ordinary Share) Start Date:2021-12-15
SSY (Sunlink Health Systems) Start Date:2007-05-17
SSYS (Stratasys Inc) Start Date:2012-12-03
ST (Sensata Technologies Holding Plc) Start Date:2010-03-11
STAA (Staar Surgical Company) Start Date:2007-01-03
STAF (Staffing 360 Solutions) Start Date:2015-09-29
STAG (Stag Industrial) Start Date:2011-04-15
STAR (Istar Corp) Start Date:2006-11-30
STBA (S&T Bancorp) Start Date:2007-05-03
STBX (Starbox Holdings) Start Date:2022-08-23
STC (Stewart Information Svcs) Start Date:2007-05-01
STCN (Steel Connect) Start Date:2008-09-30
STE (Steris Plc) Start Date:2015-11-03
STEL (Stellar Bancorp) Start Date:2017-11-08
STEM (Stem,) Start Date:2020-10-08
STEP (Stepstone) Start Date:2020-09-16
STER (Sterling Check) Start Date:2021-09-23
STEW (Srh Total Return Fund) Start Date:2022-04-04
STG (Sunlands Technology American Depositary Shares Representing Class A Ordinary Shares) Start Date:2018-03-23
STGW (Stagwell) Start Date:2007-05-16
STHO (Star Holdings) Start Date:2023-04-03
STIM (Neuronetics) Start Date:2018-06-28
STIX (Semantix Class A) Start Date:2022-08-04
STK (Columbia Seligman Premium Technology Growth Fund Inc) Start Date:2009-11-25
STKH (Steakholder Foods) Start Date:2021-03-12
STKL (Sunopta,) Start Date:2007-05-01
STKS (The One Hospitality) Start Date:2015-05-08
STLA (Stellantis N.V.) Start Date:2008-10-27
STLD (Steel Dynamics) Start Date:2007-01-03
STM (Stmicroelectronics N.V.) Start Date:2013-02-11
STN (Stantec Inc) Start Date:2008-07-31
STNE (Stoneco Ltd.) Start Date:2018-10-25
STNG (Scorpio Tankers) Start Date:2010-03-31
STOK (Stoke Therapeutics) Start Date:2019-06-19
STR (Sitio Royalties Class A) Start Date:2022-06-14
STRA (Strayer Education) Start Date:2007-04-30
STRC (Sarcos Technology And Robotics) Start Date:2021-03-08
STRCW (Sarcos Technology And Robotics Warrants) Start Date:2021-09-27
STRL (Sterling Construction Co) Start Date:2007-05-03
STRM (Streamline Health Solutions) Start Date:2007-05-16
STRN (86260J102 Nasdaq Pillar Stran & Company,) Start Date:2021-11-09
STRNW (Stran & Company Warrant) Start Date:2021-11-09
STRO (Sutro Biopharma) Start Date:2018-09-27
STRR (Star Equity Holdings) Start Date:2007-04-19
STRRP (Star Equity Holdings Series A Cumulative Perpetual Preferred Stock) Start Date:2019-09-13
STRS (Stratus Properties) Start Date:2007-05-16
STRT (Strattec Security) Start Date:2007-05-16
STRY (Starry Holdings Class A) Start Date:2022-03-29
STSS (Sharps Technology) Start Date:2022-04-14
STSSW (Sharps Technology Warrant) Start Date:2022-04-14
STT (State Street) Start Date:2005-01-03
STTK (Shattuck Labs) Start Date:2020-10-09
STVN (Stevanato) Start Date:2021-07-16
STWD (Starwood Property Trust) Start Date:2009-08-12
STX (Seagate Technology) Start Date:2005-01-03
STXS (Stereotaxis) Start Date:2007-05-01
STZ (Constellation Brands) Start Date:2005-01-03
SU (Suncor Energy) Start Date:2007-01-03
SUI (Sun Communities) Start Date:2007-01-03
SUM (Summit Materials) Start Date:2015-03-12
SUN (Sunoco Lp) Start Date:2012-09-20
SUNL (Sunlight Financial) Start Date:2021-01-15
SUNW (Sunworks) Start Date:2015-03-04
SUP (Superior Industries International) Start Date:2009-07-21
SUPN (Supernus Pharmaceuticals) Start Date:2012-05-01
SUPV (Grupo Supervielle S.A.) Start Date:2016-05-19
SURF (Surface Oncology) Start Date:2018-04-19
SURG (Surgepays) Start Date:2015-06-01
SURGW (Surgepays Warrant) Start Date:2021-11-02
SUZ (Suzano S.A.) Start Date:2018-12-10
SVC (Service Properties Trust) Start Date:2019-09-25
SVFAU (Svf Investment Unit) Start Date:2021-01-08
SVFAW (Svf Investment Warrant) Start Date:2021-01-27
SVFD (Save Foods) Start Date:2021-05-14
SVII (Spring Valley Acquisition Ii) Start Date:2022-10-28
SVM (Silvercorp Metals Common Shares) Start Date:2017-05-15
SVMH (Srivaru Holding Ltd.) Start Date:2022-09-26
SVRA (Savara) Start Date:2017-04-28
SVRE (Saverone 2014 American Depositary Shares) Start Date:2022-06-03
SVREW (Saverone 2014 Warrant) Start Date:2022-06-03
SVT (Servotronics) Start Date:2007-05-17
SVV (Savers Value Village) Start Date:2023-06-29
SVVC (Firsthand Technology Value Fund) Start Date:2011-04-19
SWAG (Stran & Company) Start Date:2021-11-09
SWAV (Shockwave Medical) Start Date:2019-03-07
SWBI (Smith & Wesson Brands) Start Date:2007-05-01
SWI (Solar Winds Corp) Start Date:2018-10-19
SWIM (Latham) Start Date:2021-04-23
SWIN (Solowin Holdings) Start Date:2023-09-07
SWK (Stanley Black & Decker) Start Date:2005-01-03
SWKH (Swk) Start Date:2010-02-04
SWKS (Skyworks Solutions) Start Date:2005-01-03
SWN (Southwestern Energy Company) Start Date:2005-01-03
SWSS (Springwater Special Situations) Start Date:2021-09-23
SWSSU (Springwater Special Situations Unit) Start Date:2021-08-26
SWSSW (Springwater Special Situations Warrant) Start Date:2021-09-23
SWTX (Springworks Therapeutics) Start Date:2019-09-13
SWVL (Swvl Holdings Class A Common Shares) Start Date:2022-04-01
SWVLW (Swvl Holdings Warrant) Start Date:2022-04-01
SWX (Southwest Gas Holdings) Start Date:2007-01-03
SWZ (Swiss Helvetia Fund) Start Date:2007-05-16
SXC (Suncoke Energy) Start Date:2011-07-21
SXI (Standex International) Start Date:2007-05-10
SXT (Sensient Technologies Corporation) Start Date:2007-01-03
SXTC (China Sxt Pharmaceuticals) Start Date:2019-01-04
SXTP (60 Degrees Pharmaceuticals) Start Date:2023-07-12
SY (So-Young International ADS) Start Date:2019-05-02
SYBT (Stock Yards Bancorp Comm) Start Date:2007-05-16
SYBX (Synlogic) Start Date:2015-10-01
SYF (Synchrony Financial) Start Date:2014-07-31
SYK (Stryker) Start Date:2005-01-03
SYM (Symbotic Class A) Start Date:2021-03-09
SYN (Synthetic Biologics) Start Date:2007-05-16
SYNA (Synaptics Incorporated) Start Date:2007-01-03
SYNH (Syneos Health) Start Date:2014-11-07
SYPR (Sypris Solutions) Start Date:2007-05-16
SYRA (Syra Health) Start Date:2023-09-29
SYRE (Spyre Therapeutics Inc) Start Date:2016-04-07
SYRS (Syros Pharmaceuticals) Start Date:2016-06-30
SYT (Syla Technologies Co.) Start Date:2023-03-31
SYTA (Siyata Mobile) Start Date:2020-09-25
SYTAW (Siyata Mobile Warrant) Start Date:2020-09-25
SYY (Sysco) Start Date:2005-01-03
SZC (Cushing Nextgen Infrastructure Income Fund Common Shares Of Beneficial Interest) Start Date:2012-09-26
T (At&T) Start Date:2006-01-03
TAC (Transalta Corporation) Start Date:2007-05-16
TACT (Transact Technologies Incorporated) Start Date:2007-05-16
TAIT (Taitron Components Incorporated Class A) Start Date:2007-05-16
TAK (Takeda Pharmaceutical Company American Depositary Shares) Start Date:2018-12-24
TAL (Tal Education) Start Date:2010-10-20
TALK (Talkspace) Start Date:2020-07-30
TALKW (Talkspace Warrant) Start Date:2020-07-30
TALO (Talos Energy) Start Date:2018-05-10
TANH (Tantech Holdings Common Shares) Start Date:2015-03-24
TAOP (Taoping Ordinary Shares) Start Date:2007-05-16
TAP (Molson Coors Brewing Company) Start Date:2005-03-01
TARA (Protara Therapeutics) Start Date:2020-02-03
TARO (Taro Pharmaceutical Industries Ltd.) Start Date:2012-03-22
TARS (Tarsus Pharmaceuticals) Start Date:2020-10-16
TASK (Taskus) Start Date:2021-06-11
TAST (Carrols Restaurant) Start Date:2007-05-16
TATT (Tat Technologies Ordinary Shares) Start Date:2010-01-08
TAYD (Taylor Devices) Start Date:2007-05-16
TBBK (Bancorp) Start Date:2007-05-16
TBCP (Thunder Bridge Capital Partners Iii Class A) Start Date:2021-04-01
TBCPU (Thunder Bridge Capital Partners Iii Units) Start Date:2021-02-05
TBCPW (Thunder Bridge Capital Partners Iii Warrant) Start Date:2021-03-31
TBI (Trueblue) Start Date:2007-12-18
TBIO (Telesis Bio) Start Date:2021-06-18
TBK (Triumph Bancorp) Start Date:2014-11-07
TBKCP (Triumph Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of 7.125% Series C Fixed-Rate Non-Cumulative Perpetual Preferred Stock) Start Date:2020-06-24
TBLA (Taboola.com Ordinary Shares) Start Date:2021-06-30
TBLAW (Taboola.com Warrant) Start Date:2021-06-30
TBLD (Thornburg Income Builder Opportunities Trust) Start Date:2021-07-28
TBLT (Toughbuilt Industries) Start Date:2018-11-09
TBLTW (Toughbuilt Industries Warrant) Start Date:2018-12-03
TBNK (Territorial Bancorp) Start Date:2009-07-14
TBPH (Theravance Biopharma) Start Date:2014-05-16
TC (Tuanche American Depositary Shares) Start Date:2018-11-20
TCBC (Tc Bancshares) Start Date:2021-07-21
TCBI (Texas Capital Bancshares) Start Date:2007-05-09
TCBK (Trico Bancshares) Start Date:2007-05-08
TCBP (Tc Biopharm) Start Date:2022-02-11
TCBPW (Tc Biopharm) Start Date:2022-02-11
TCBS (Texas Community Bancshares) Start Date:2021-07-16
TCBX (Third Coast Bancshares) Start Date:2021-11-09
TCDA (Tricida) Start Date:2018-06-28
TCI (Transcontinental Realty) Start Date:2007-05-16
TCJH (Top Kingwin Ltd) Start Date:2023-04-18
TCMD (Tactile Systems Technology) Start Date:2016-07-28
TCN (Tricon Residential Common Shares) Start Date:2021-10-07
TCOM (Trip.com Limited) Start Date:2007-04-26
TCON (Tracon Pharmaceuticals) Start Date:2015-01-30
TCPC (Blackrock Tcp Capital) Start Date:2012-04-04
TCRT (Alaunos Therapeutics) Start Date:2007-05-16
TCRX (Tscan Therapeutics) Start Date:2021-07-16
TCS (The Container Store) Start Date:2013-11-01
TCX (Tucows  O) Start Date:2007-05-16
TD (Toronto Dominion Bank) Start Date:2007-05-01
TDC (Teradata Corporation) Start Date:2007-10-01
TDCX (Tdcx American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2021-10-01
TDF (Templeton Dragon Fund) Start Date:2007-05-10
TDG (Transdigm) Start Date:2006-03-15
TDOC (Teladoc Health) Start Date:2015-07-01
TDS (Telephone And Data Systems) Start Date:2012-01-25
TDUP (Thredup) Start Date:2021-03-26
TDW (Tidewater) Start Date:2007-04-30
TDY (Teledyne Technologies Incorporated) Start Date:2007-01-03
TEAF (Ecofin Sustainable And Social Impact Term Fund) Start Date:2019-03-27
TEAM (Atlassian) Start Date:2015-12-10
TECH (Bio-Techne Corporation) Start Date:2007-01-03
TECK (Teck Resources Limited) Start Date:2016-12-05
TEDU (Tarena International American Depositary Shares) Start Date:2014-04-03
TEF (Telefonica S.A.) Start Date:2013-02-11
TEI (Templeton Emerging Markets Income Fund) Start Date:2007-05-08
TEL (Te Connectivity Ltd.) Start Date:2009-06-26
TELA (Tela Bio) Start Date:2019-11-08
TELL (Tellurian) Start Date:2007-05-16
TENB (Tenable Holdings) Start Date:2018-07-26
TENK (Tenx Keane Acquisition Ordinary Share) Start Date:2022-12-08
TENX (Tenax Therapeutics) Start Date:2009-11-09
TEO (Telecom Argentina Sa) Start Date:2013-02-11
TER (Teradyne) Start Date:2005-01-03
TERN (Terns Pharmaceuticals) Start Date:2021-02-05
TETCU (Tech And Energy Transition Unit) Start Date:2021-03-17
TETCW (Tech And Energy Transition Warrant) Start Date:2021-05-14
TEVA (Teva Pharmaceutical Industries Ltd) Start Date:2013-02-11
TEX (Terex) Start Date:2005-01-03
TFC (Truist Financial Corporation) Start Date:2007-04-30
TFFP (Tff Pharmaceuticals) Start Date:2019-10-25
TFII (Tfi International) Start Date:2020-02-13
TFIN (Triumph Financial) Start Date:2014-11-07
TFPM (Triple Flag Precious Metals) Start Date:2022-08-30
TFSL (Tfs Financial) Start Date:2007-05-16
TFX (Teleflex Inc) Start Date:2005-01-03
TG (Tredegar) Start Date:2007-04-27
TGAN (Transphorm) Start Date:2020-12-24
TGB (Taseko Mines Limited) Start Date:2007-05-03
TGH (Textainer) Start Date:2007-10-10
TGI (Triumph) Start Date:2007-05-01
TGL (Treasure Global) Start Date:2022-08-11
TGLS (Tecnoglass) Start Date:2012-05-10
TGNA (Tegna) Start Date:2007-04-30
TGR (Kimbell Tiger Acquisition Corporation) Start Date:2022-03-28
TGS (Transportadora De Gas Del Sur Sa Tgs) Start Date:2013-02-11
TGT (Target) Start Date:2005-01-03
TGTX (Tg Therapeutics) Start Date:2013-07-18
TH (Target Hospitality) Start Date:2018-03-08
THAR (Tharimmune Inc) Start Date:2022-01-12
THC (Tenet Healthcare Corporation) Start Date:2005-01-03
THCAW (Tuscan Holdings Ii Warrant) Start Date:2019-08-13
THCH (Th International) Start Date:2022-09-29
THCP (Thunder Bridge Capital Partners Iv Class A) Start Date:2021-09-09
THCPU (Thunder Bridge Capital Partners Iv Unit) Start Date:2021-06-30
THCPW (Thunder Bridge Capital Partners Iv Warrant) Start Date:2021-09-01
THFF (First Financial) Start Date:2007-05-16
THG (The Hanover Insurance) Start Date:2007-01-03
THM (International Tower Hill Mines Ordinary Shares) Start Date:2007-08-03
THMO (Thermogenesis Holdings) Start Date:2007-05-04
THNPY (Partial Technip Energies) Start Date:2021-06-17
THO (Thor Industries) Start Date:2007-01-03
THQ (Tekla Healthcare Opportunies Fund Shares Of Beneficial Interest) Start Date:2014-07-29
THR (Thermon) Start Date:2011-05-05
THRD (Third Harmonic Bio) Start Date:2022-09-15
THRM (Gentherm) Start Date:2007-05-16
THRN (Thorne Healthtech) Start Date:2021-09-23
THRX (Theseus Pharmaceuticals) Start Date:2021-10-07
THRY (Thryv Holdings) Start Date:2020-10-01
THS (Treehouse Foods) Start Date:2007-01-03
THTX (Theratechnologies Common Shares) Start Date:2013-02-05
THW (Tekla World Healthcare Fund Shares Of Beneficial Interest) Start Date:2015-06-26
THWWW (Target Hospitality Warrant Expiring 3/15/2024) Start Date:2019-03-18
TIGO (Millicom International Cellular S.A.) Start Date:2019-01-09
TIGR (Up Fintech Holding American Depositary Share Representing Fifteen Class A Ordinary Shares) Start Date:2019-03-20
TIL (Instil Bio) Start Date:2021-03-19
TILE (Interface) Start Date:2013-01-18
TIMB (Tim S.A. American Depositary Shares) Start Date:2020-10-12
TIO (Tingo Inc) Start Date:2013-04-09
TIOAU (Tio Tech A Units) Start Date:2021-04-08
TIOAW (Tio Tech A Warrants) Start Date:2021-06-09
TIPT (Tiptree) Start Date:2010-09-03
TIRX (Tian Ruixiang Holdings) Start Date:2021-01-27
TISI (Team) Start Date:2012-01-03
TITN (Titan Machinery) Start Date:2007-12-07
TIVC (Tivic Health Systems,) Start Date:2021-11-11
TIXT (Telus International) Start Date:2021-02-03
TJX (Tjx Companies) Start Date:2005-01-03
TK (Teekay) Start Date:2007-05-01
TKC (Turkcell Iletisim Hizmetleri As) Start Date:2013-02-11
TKLF (Yoshitsu Co. American Depositary Shares) Start Date:2022-01-18
TKNO (Alpha Teknova) Start Date:2021-06-25
TKR (The Timken Company) Start Date:2007-01-03
TLF (Tandy Leather Factory) Start Date:2022-09-07
TLIS (Talis Biomedical) Start Date:2021-02-12
TLK (Perusahaan Perseroan) Start Date:2007-01-03
TLRY (Tilray, Class 2) Start Date:2018-07-19
TLS (Telos Corp) Start Date:2020-11-20
TLSA (Tiziana Life Sciences Common Shares) Start Date:2018-11-20
TLYS (Tilly's) Start Date:2012-05-04
TM (Toyota Motor) Start Date:2013-02-11
TMBR (Timber Pharmaceuticals) Start Date:2015-06-11
TMC (Tmc The Metals Company) Start Date:2021-09-10
TMCI (Treace Medical Concepts) Start Date:2021-04-23
TMCWW (Tmc The Metals Company Warrants) Start Date:2021-09-10
TMDI (Titan Medical Ordinary Shares) Start Date:2018-06-27
TMDX (Transmedics) Start Date:2019-05-02
TME (Tencent Music Entertainment) Start Date:2018-12-12
TMHC (Taylor Morrison Home Corporation) Start Date:2013-04-10
TMO (Thermo Fisher Scientific) Start Date:2005-01-03
TMP (Tompkins Financial) Start Date:2007-05-16
TMPO (Tempo Automation Holdings) Start Date:2020-09-21
TMQ (Trilogy Metals) Start Date:2012-05-01
TMST (Timkensteel Corp) Start Date:2014-06-19
TMUS (T-Mobile Us) Start Date:2007-05-16
TNC (Tennant) Start Date:2007-05-08
TNDM (Tandem Diabetes Care) Start Date:2013-11-14
TNET (Trinet) Start Date:2014-03-27
TNGX (Tango Therapeutics,) Start Date:2021-08-09
TNK (Teekay Tankers Ltd.) Start Date:2007-12-13
TNL (Travel + Leisure Co.) Start Date:2018-05-21
TNON (Tenon Medical) Start Date:2022-04-27
TNP (Tsakos Energy Navigation Common Shares) Start Date:2007-05-02
TNXP (Tonix Pharmaceuticals Holding) Start Date:2013-08-09
TNYA (Tenaya Therapeutics) Start Date:2021-07-30
TOI (The Oncology Institute) Start Date:2021-11-15
TOIIW (The Oncology Institute Warrant) Start Date:2020-06-04
TOL (Toll Brothers) Start Date:2007-01-03
TOMZ (Tomi Environmental Solutions) Start Date:2020-10-01
TOON (Kartoon Studios Inc) Start Date:2016-11-21
TOP (Zhong Yang Financial Ordinary Shares) Start Date:2022-06-01
TOPS (Top Ships) Start Date:2017-11-03
TORO (Toro Corp) Start Date:2023-04-03
TOST (Toast,) Start Date:2021-09-22
TOUR (Tuniu American Depositary Shares) Start Date:2014-05-09
TOVX (Theriva Biologics) Start Date:2007-05-16
TOWN (Towne Bank) Start Date:2007-05-16
TPB (Turning Point Brands) Start Date:2016-05-11
TPC (Tutor Perini) Start Date:2009-06-01
TPET (Trio Petroleum) Start Date:2023-04-18
TPG (Tpg) Start Date:2022-01-13
TPH (Tri Pointe Homes) Start Date:2013-01-31
TPHS (Trinity Place Holdings) Start Date:2012-09-26
TPIC (Tpi Composites) Start Date:2016-07-22
TPL (Texas Pacific Land Corporation) Start Date:2007-05-16
TPR (Tapestry) Start Date:2007-04-27
TPST (Tempest Therapeutics) Start Date:2021-06-24
TPVG (Triplepoint Venture Growth Bdc) Start Date:2014-03-06
TPX (Tempur Sealy International) Start Date:2007-01-03
TPZ (Tortoise Power And Energy Infrastructure Fund Inc) Start Date:2009-07-29
TR (Tootsie Roll Industries) Start Date:2007-01-03
TRAK (Park City Inc) Start Date:2007-05-16
TRC (Tejon Ranch) Start Date:2007-05-10
TRDA (Entrada Therapeutics) Start Date:2021-10-29
TREE (Lendingtree) Start Date:2008-08-21
TREX (Trex Company) Start Date:2009-11-23
TRGP (Targa Resources) Start Date:2010-12-07
TRHC (Tabula Rasa Healthcare) Start Date:2016-09-29
TRI (Thomson Reuters Corporation) Start Date:2008-04-17
TRIB (Trinity Biotech Plc American Depositary Shares) Start Date:2007-05-16
TRIN (Trinity Capital) Start Date:2021-01-29
TRIP (Tripadvisor) Start Date:2011-12-21
TRKA (Troika Media) Start Date:2021-04-20
TRKWQ (Troika Media Inc) Start Date:2021-04-20
TRMB (Trimble) Start Date:2007-01-03
TRMD (Torm Plc Class A) Start Date:2018-02-23
TRMK (Trustmark) Start Date:2007-05-01
TRML (Tourmaline Bio Inc) Start Date:2021-05-07
TRMR (Tremor International ADS) Start Date:2021-06-18
TRN (Trinity Industries) Start Date:2007-01-03
TRNO (Terreno Realty Corporation) Start Date:2010-02-10
TRNR (Interactive Strength) Start Date:2023-04-28
TRNS (Transcat) Start Date:2007-05-16
TROO (Troops Ordinary Shares) Start Date:2010-12-20
TROW (T. Rowe Price) Start Date:2005-01-03
TROX (Tronox) Start Date:2012-06-18
TRP (Tc Energy Corporation) Start Date:2007-01-03
TRS (Trimas) Start Date:2007-05-18
TRST (Trustco Bank N) Start Date:2007-05-02
TRT (Trio-Tech International) Start Date:2007-04-27
TRTN (Triton International Limited) Start Date:2007-05-10
TRTX (Tpg Re Finance Trust) Start Date:2017-07-20
TRU (Transunion) Start Date:2015-06-25
TRUE (Truecar) Start Date:2014-05-16
TRUP (Trupanion) Start Date:2014-07-18
TRV (The Travelers Companies) Start Date:2007-02-27
TRVG (Trivago N.V. American Depositary Shares) Start Date:2016-12-16
TRVI (Trevi Therapeutics) Start Date:2019-05-07
TRVN (Trevena) Start Date:2014-01-31
TRX (Trx Gold) Start Date:2007-04-20
TS (Tenaris S.A.) Start Date:2013-02-11
TSAT (Telesat Class A Common Shares And Class B Variable Voting Shares) Start Date:2021-11-19
TSBK (Timberland Bancorp) Start Date:2007-05-16
TSBX (Turnstone Biologics) Start Date:2023-07-21
TSCO (Tractor Supply Company) Start Date:2005-01-03
TSE (Trinseo Sa) Start Date:2014-06-12
TSEM (Tower Semiconductor Ltd.) Start Date:2007-01-03
TSHA (Taysha Gene Therapies) Start Date:2020-09-24
TSI (TCWStrategic Income Fund) Start Date:2007-05-16
TSIBU (Tishman Speyer Innovation Ii Unit) Start Date:2021-02-12
TSIBW (Tishman Speyer Innovation Ii Warrant) Start Date:2021-04-05
TSLA (Tesla Inc) Start Date:2010-06-29
TSLX (Sixth Street Specialty Lending,) Start Date:2014-03-21
TSM (Taiwan Semiconductor Manufacturing Company Ltd.) Start Date:2007-04-27
TSN (Tyson Foods) Start Date:2005-01-03
TSP (Tusimple) Start Date:2021-04-15
TSQ (Townsquare Media Class A) Start Date:2014-07-24
TSRI (Tsr) Start Date:2007-05-16
TSVT (2Seventy Bio,) Start Date:2021-11-05
TT (Trane Technologies Plc) Start Date:2007-04-30
TTC (The Toro Company) Start Date:2007-01-03
TTCF (Tattooed Chef, Inc Class A) Start Date:2018-09-12
TTD (The Trade Desk) Start Date:2016-09-21
TTE (Totalenergies Se) Start Date:2007-04-30
TTEC (Teletech) Start Date:2007-05-01
TTEK (Tetra Tech) Start Date:2007-01-03
TTGT (Techtarget) Start Date:2007-05-17
TTI (Tetra Technologies) Start Date:2007-04-30
TTMI (Ttm Technologies) Start Date:2007-05-01
TTNP (Titan Pharmaceuticals) Start Date:2015-10-12
TTOO (T2 Biosystems) Start Date:2014-08-07
TTP (Tortoise Pipeline & Energy Fund) Start Date:2011-10-27
TTSH (Tile Shop Holdings) Start Date:2021-06-17
TTWO (Take-Two Interactive) Start Date:2005-01-03
TU (Telus Corporation) Start Date:2007-01-03
TUEM (Tuesday Morning) Start Date:2021-05-25
TUP (Tupperware Brands) Start Date:2005-01-03
TURB (Turbo Energy) Start Date:2023-09-22
TURN (180 Degree Capital) Start Date:2007-05-03
TUSK (Mammoth Energy Services) Start Date:2016-10-14
TUYA (Tuya) Start Date:2021-03-18
TV (Grupo Televisa S.A.B.) Start Date:2013-02-11
TVC (Tennessee Valley Authority) Start Date:2013-02-11
TVE (Tennessee Valley Authority) Start Date:2013-11-11
TVTX (Travere Therapeutics,) Start Date:2012-11-02
TW (Tradeweb Markets) Start Date:2019-04-04
TWI (Titan International) Start Date:2007-05-02
TWIN (Twin Disc Incorporated) Start Date:2007-05-16
TWKS (Thoughtworks Holding,) Start Date:2021-09-15
TWLO (Twilio) Start Date:2016-06-23
TWLV (Twelve Seas Investment Company Ii Class A) Start Date:2021-04-29
TWLVU (Twelve Seas Investment Company Ii Unit) Start Date:2021-02-26
TWLVW (Twelve Seas Investment Company Ii Warrant) Start Date:2021-04-26
TWN (Taiwan Fund) Start Date:2007-05-16
TWNK (Hostess Brands) Start Date:2015-11-30
TWO (Two Harbors Investment) Start Date:2009-10-29
TWOA (Two) Start Date:2021-03-30
TWST (Twist Bioscience) Start Date:2018-10-31
TX (Ternium S.A.) Start Date:2007-01-03
TXG (10X Genomics) Start Date:2019-09-12
TXMD (Therapeuticsmd) Start Date:2017-10-10
TXN (Texas Instruments) Start Date:2005-01-03
TXO (Txo Energy Partners Lp) Start Date:2023-01-27
TXRH (Texas Roadhouse) Start Date:2007-01-03
TXT (Textron) Start Date:2005-01-03
TY (Tri Continental) Start Date:2007-05-11
TYG (Tortoise Energy Infrastructure) Start Date:2007-05-04
TYL (Tyler Technologies) Start Date:2007-01-03
TYRA (Tyra Biosciences,) Start Date:2021-09-15
TZOO (Travelzoo) Start Date:2007-05-02
U (Unity Software) Start Date:2020-09-18
UA (Under Armour Class C) Start Date:2016-03-23
UAA (Under Armour Class A) Start Date:2007-05-14
UAL (United Continental Holdings) Start Date:2010-10-01
UAMY (United States Antimony) Start Date:2007-05-16
UAN (Cvr Partners, Lp) Start Date:2011-04-08
UAVS (Ageagle Aerial Systems) Start Date:2014-06-17
UBCP (United Bancorp) Start Date:2007-05-16
UBER (Uber Technologies) Start Date:2019-05-10
UBFO (United Security) Start Date:2007-05-16
UBOH (United Bancshares) Start Date:2007-05-16
UBS (Ubs Ag) Start Date:2014-11-28
UBSI (United Bankshares) Start Date:2007-01-03
UBX (Unity Biotechnology) Start Date:2018-05-03
UCAR (U Power Limited) Start Date:2023-04-20
UCBI (United Community Banks) Start Date:2007-05-07
UCBIO (United Community Banks Depositary Shares Each Representing 1/1000Th Interest In A Share Of Series I Non-Cumulativepreferred Stock) Start Date:2020-06-11
UCL (Unocal Co) Start Date:2020-06-10
UCTT (Ultra Clean) Start Date:2007-05-03
UDMY (Udemy,) Start Date:2021-10-29
UDR (Udr Inc) Start Date:2005-01-03
UE (Urban Edge Properties) Start Date:2015-01-16
UEC (Uranium Energy) Start Date:2015-01-16
UEIC (Universal Electronics) Start Date:2007-05-09
UFAB (Unique Fabricating) Start Date:2015-07-01
UFCS (United Fire) Start Date:2007-05-01
UFI (Unifi) Start Date:2007-05-02
UFPI (Ufp Industries) Start Date:2007-01-03
UFPT (Ufp Technologies) Start Date:2007-05-16
UG (United-Guardian) Start Date:2007-05-16
UGI (Ugi Corporation) Start Date:2007-01-03
UGIC (Ugi Corporate Units) Start Date:2021-05-28
UGP (Ultrapar Participacoes S.A.) Start Date:2013-02-11
UGRO (Urban-Gro) Start Date:2021-02-02
UHAL (Amerco) Start Date:2007-05-01
UHG (United Homes Inc) Start Date:2021-03-29
UHS (Universal Health Services) Start Date:2005-01-03
UHT (Universal Health Realty) Start Date:2007-05-10
UI (Ubiquiti Networks) Start Date:2011-10-14
UIS (Unisys) Start Date:2004-01-02
UK (Ucommune International Ordinary Shares) Start Date:2019-11-07
UKOMW (Ucommune International Warrant Expiring 11/17/2025) Start Date:2019-11-07
UL (Unilever Plc) Start Date:2013-02-11
ULBI (Ultralife Batteries) Start Date:2007-05-08
ULCC (Frontier Holdings) Start Date:2021-04-01
ULH (Universal Logistics) Start Date:2007-05-16
ULTA (Ulta Beauty) Start Date:2007-10-25
UMBF (Umb Financial Corporation) Start Date:2007-01-03
UMC (United Microelectronics Corporation) Start Date:2013-02-11
UMH (Umh Properties) Start Date:2007-05-16
UNAM (Unico American) Start Date:2007-05-16
UNB (Union Bankshares) Start Date:2007-05-16
UNCY (Unicycive Therapeutics) Start Date:2021-07-13
UNF (Unifirst) Start Date:2007-05-10
UNFI (United Natural Foods) Start Date:2007-04-25
UNH (United Health) Start Date:2005-01-03
UNIT (Unit) Start Date:2015-04-20
UNM (Unum) Start Date:2005-01-03
UNP (Union Pacific) Start Date:2005-01-03
UNTY (Unity Bancorp) Start Date:2007-05-16
UONE (Urban One Class A) Start Date:2007-05-16
UONEK (Urban One Class D) Start Date:2007-05-01
UP (Wheels Up Experience) Start Date:2021-07-14
UPBD (Upbound Inc) Start Date:2007-04-27
UPC (Union Planters) Start Date:2021-03-23
UPHL (Uphealth Inc) Start Date:2019-07-01
UPLD (Upland Software) Start Date:2014-11-06
UPS (United Parcel Service) Start Date:2005-01-03
UPST (Upstart Holdings) Start Date:2020-12-16
UPWK (Upwork) Start Date:2018-10-03
UPXI (Upexi) Start Date:2021-06-24
URBN (Urban Outfitters) Start Date:2005-01-03
URG (Ur Energy Inc Common Shares) Start Date:2008-07-24
URGN (Urogen Pharma) Start Date:2017-05-04
URI (United Rentals) Start Date:2005-01-03
UROY (Uranium Royalty) Start Date:2021-04-28
USA (Liberty All-Star Equity Fund) Start Date:2007-05-08
USAC (Usa Compression Partners Lp) Start Date:2013-01-15
USAP (Universal Stainless & Alloy Products) Start Date:2007-05-04
USAS (Americas Gold And Silver Common Shares No Par Value) Start Date:2017-01-19
USAU (U.S. Gold) Start Date:2007-05-16
USB (U.S. Bancorp) Start Date:2005-01-03
USCB (Uscb Financial Holdings Class A) Start Date:2021-07-23
USCT (Tkb Critical Technologies 1 Class A Ordinary Shares) Start Date:2021-12-27
USDP (Usd Partners Lp Common Units Representing Partner Interest) Start Date:2014-10-09
USEA (United Maritime) Start Date:2022-07-06
USEG (U.S. Energy) Start Date:2007-05-08
USFD (Us Foods Holding) Start Date:2016-05-26
USGO (U.S. Goldmining) Start Date:2023-04-20
USIO (Usio) Start Date:2015-08-11
USLM (United States Lime) Start Date:2007-05-16
USM (United States Cellular) Start Date:2007-05-02
USNA (Usana Health Sciences) Start Date:2007-05-04
USPH (U.S. Physical Therapy) Start Date:2007-05-16
USWSW (U.S. Well Services Warrants) Start Date:2018-11-07
UTF (Cohen & Steers Infrastructure Fund) Start Date:2007-01-03
UTG (Reaves Utility Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-08
UTHR (United Therapeutics Corporation) Start Date:2007-01-03
UTI (Universal Technical Inst) Start Date:2007-05-02
UTL (Unitil) Start Date:2007-05-16
UTMD (Utah Medical Products) Start Date:2007-05-16
UTRS (Minerva Surgical) Start Date:2021-10-22
UTSI (Utstarcom Holdings Ordinary Shares) Start Date:2007-05-01
UTZ (Utz Brands,) Start Date:2020-03-02
UUU (Universal Security Instruments) Start Date:2007-04-23
UUUU (Energy Fuels) Start Date:2008-10-27
UVE (Universal Insurance) Start Date:2007-05-16
UVSP (Univest Of Pa) Start Date:2007-05-16
UVV (Universal) Start Date:2007-04-27
UWMC (Uwm Holdings Corporation) Start Date:2020-12-28
UXIN (Uxin ADS) Start Date:2018-06-27
V (Visa) Start Date:2008-03-19
VABK (Virginia National Bankshares) Start Date:2007-05-16
VAC (Marriott Vacations Worldwide Corporation) Start Date:2011-11-08
VAL (Ensco Plc) Start Date:2021-05-03
VALE (Vale S.A. American Depositary Shares Each Representing One Common Share) Start Date:2013-02-11
VALN (Valneva) Start Date:2021-05-06
VALU (Value Line) Start Date:2007-05-16
VANI (Vivani Medical) Start Date:2014-11-19
VAPO (Vapotherm) Start Date:2018-11-14
VATE (Innovate) Start Date:2021-09-20
VAXX (Vaxxinity, Class A) Start Date:2021-11-11
VBF (Invesco Bond Fund) Start Date:2007-05-16
VBFC (Village Bank And Trust Financial) Start Date:2007-05-16
VBIV (Vbi Vaccines) Start Date:2014-07-29
VBNK (Versabank Common Shares) Start Date:2021-09-22
VBTX (Veritex  Common) Start Date:2014-10-09
VC (Visteon Corporation) Start Date:2011-01-10
VCEL (Aastrom Biosciences Comm) Start Date:2007-04-26
VCIF (Vertical Capital Income Fund Common Shares Of Beneficial Interest) Start Date:2019-05-30
VCIG (Vci Global Limited) Start Date:2023-04-13
VCKA (Vickers Vantage I Ordinary Shares) Start Date:2021-03-05
VCKAU (Vickers Vantage I Unit) Start Date:2021-01-07
VCKAW (Vickers Vantage I Warrant) Start Date:2021-03-08
VCNX (Vaccinex) Start Date:2018-08-09
VCSA (Vacasa Class A) Start Date:2021-12-07
VCTR (Victory Capital Holdings Class A) Start Date:2018-02-08
VCV (Invesco California Value Municipal Income Trust) Start Date:2007-05-16
VCYT (Veracyte) Start Date:2013-10-30
VECO (Veeco Instruments) Start Date:2007-05-02
VEEE (Twin Vee Powercats Co.) Start Date:2021-07-21
VEEV (Veeva Systems) Start Date:2013-10-16
VEL (Velocity Financial) Start Date:2020-01-17
VEON (Veon Ltd.) Start Date:2013-02-11
VERA (Vera Therapeutics) Start Date:2021-05-14
VERB (Verb Technology Company) Start Date:2019-04-05
VERBW (Verb Technology Company Warrant) Start Date:2019-04-05
VERI (Veritone) Start Date:2017-05-12
VERO (Venus Concept) Start Date:2017-10-12
VERU (Veru) Start Date:2009-06-09
VERV (Verve Therapeutics) Start Date:2021-06-17
VERX (Vertex) Start Date:2020-07-29
VERY (Vericity) Start Date:2019-08-15
VET (Vermilion Energy) Start Date:2013-03-12
VEV (Vicinity Motor) Start Date:2021-07-07
VFC (V.F.) Start Date:2005-01-03
VFF (Village Farms International, Common Shares) Start Date:2019-02-21
VFL (Delaware Investments National Municipal Income Fund) Start Date:2007-05-16
VFS (Vinfast Auto) Start Date:2023-08-15
VGFC (The Very Good Food Company Common Shares) Start Date:2021-10-13
VGI (Virtus Global Multi-Sector Income Fund Common Shares Of Beneficial Interest) Start Date:2012-02-24
VGM (Invesco Trust For Investment Grade Municipals) Start Date:2016-12-23
VGR (Vector) Start Date:2007-04-30
VGZ (Vista Gold) Start Date:2007-04-24
VHC (Virnetx Holding) Start Date:2007-12-26
VHI (Valhi,) Start Date:2007-05-16
VIA (Via Renewables Class A) Start Date:2021-08-09
VIAO (Via Optronics Ag) Start Date:2020-09-25
VIAV (Viavi Solutions) Start Date:2007-04-27
VICI (Vici Properties) Start Date:2017-10-17
VICR (Vicor Corporation) Start Date:2007-01-03
VIEW (View Class A) Start Date:2020-10-19
VIEWW (View Warrant) Start Date:2020-10-21
VIGL (Vigil Neuroscience) Start Date:2022-01-07
VIIAW (7Gc & Co. Holdings Warrant) Start Date:2021-02-12
VINC (Vincerx Pharma) Start Date:2020-05-27
VINE (Fresh Vine Wine) Start Date:2021-12-14
VINO (Gaucho Holdings) Start Date:2021-02-17
VINP (Vinci Partners Investments) Start Date:2021-01-28
VIOT (Viomi Technology Co. American Depositary Shares) Start Date:2018-09-25
VIPS (Vipshop Holdings Limited) Start Date:2012-03-23
VIR (Vir Biotechnology) Start Date:2019-10-11
VIRC (Virco Manufacturing) Start Date:2007-06-20
VIRI (Virios Therapeutics) Start Date:2020-12-17
VIRT (Virtu Financial) Start Date:2015-04-16
VIRX (Viracta Therapeutics) Start Date:2011-03-16
VISL (Vislink Technologies) Start Date:2011-11-22
VIST (Vista Energy S.A.B. De C.V. American Depositary Shares Each Representing One Series A Share With No Par Value) Start Date:2019-07-26
VITL (Vital Farms) Start Date:2020-07-31
VIV (Telefonica Brasil S.A.) Start Date:2007-05-01
VIVK (Vivakor) Start Date:2022-02-14
VJET (Voxeljet Ag American Depositary Shares) Start Date:2013-10-18
VKI (Invesco Advantage Municipal Income Trust Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
VKQ (Invesco Municipal Trust) Start Date:2007-05-16
VKTX (Viking Therapeutics) Start Date:2015-04-29
VLCN (Volcon) Start Date:2021-10-06
VLD (Velo3d,) Start Date:2021-09-24
VLDRW (Velodyne Lidar Warrants) Start Date:2020-09-30
VLGEA (Village Super Market) Start Date:2007-05-16
VLN (Valens Semiconductor Ordinary Shares) Start Date:2021-09-30
VLO (Valero Energy) Start Date:2005-01-03
VLRS (Controladora Vuela Compania De Aviacion S.A.B. De C.V. American Depositary Shares Each Representing Ten) Start Date:2013-09-18
VLT (Invesco High Income Trust Ii) Start Date:2007-05-16
VLTO (Veralto Corp) Start Date:2023-09-27
VLY (Valley National Bancorp) Start Date:2007-01-03
VLYPO (Valley National Bancorp 5.50% Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series B) Start Date:2018-10-10
VLYPP (Valley National Bancorp 6.25% Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2018-10-10
VMAR (Vision Marine Technologies) Start Date:2020-11-24
VMC (Vulcan Materials) Start Date:2007-11-19
VMCA (Valuence Merger I Class A Ordinary Shares) Start Date:2022-04-25
VMCAU (Valuence Merger I Unit) Start Date:2022-03-01
VMD (Viemed Healthcare) Start Date:2019-08-09
VMEO (Vimeo) Start Date:2021-05-19
VMI (Valmont Industries) Start Date:2007-05-04
VMO (Invesco Municipal Opportunity Trust) Start Date:2007-05-16
VMW (Vmware) Start Date:2007-08-14
VNCE (Vince Holding) Start Date:2013-11-22
VNDA (Vanda Pharmaceuticals) Start Date:2007-05-02
VNET (Vnet  American Depositary Shares) Start Date:2011-04-21
VNO (Vornado Realty Trust) Start Date:2005-01-03
VNOM (Viper Energy Partners Lp) Start Date:2015-01-16
VNRX (Volitionrx Limited) Start Date:2015-02-06
VNT (Vontier) Start Date:2020-10-05
VNTR (Venator Materials Plc) Start Date:2017-08-03
VOC (Voc Energy Trust Units Of Beneficial Interest) Start Date:2011-05-05
VOD (Vodafone Plc) Start Date:2005-01-03
VOR (Vor Biopharma) Start Date:2021-02-05
VORB (Virgin Orbit Holdings) Start Date:2021-12-27
VORBW (Virgin Orbit Holdings Warrant) Start Date:2021-05-21
VOXR (Vox Royalty) Start Date:2022-10-10
VOXX (Voxx International) Start Date:2007-05-09
VOYA (Voya Financial) Start Date:2013-05-02
VPG (Vishay Precision) Start Date:2010-07-07
VPV (Invesco Pennsylvania Value Municipal Income Trust) Start Date:2007-05-16
VQS (Viq Solutions Common Shares) Start Date:2008-10-29
VRA (Vera Bradley) Start Date:2010-10-21
VRAR (Glimpse) Start Date:2021-07-01
VRAX (Virax Biolabs) Start Date:2022-07-21
VRAY (Viewray) Start Date:2015-08-10
VRCA (Verrica Pharmaceuticals) Start Date:2018-06-15
VRDN (Viridian Therapeutics) Start Date:2021-01-20
VRE (Veris Residential) Start Date:2012-11-08
VREX (Varex Imaging) Start Date:2017-01-20
VRM (Vroom) Start Date:2020-06-09
VRME (Verifyme) Start Date:2007-05-23
VRMEW (Verifyme Warrant) Start Date:2020-06-18
VRNA (Verona Pharma Plc American Depositary Share) Start Date:2017-04-27
VRNS (Varonis Systems) Start Date:2014-02-28
VRNT (Verint Systems) Start Date:2007-01-03
VRPX (Virpax Pharmaceuticals) Start Date:2021-02-17
VRRM (Verra Mobility Corp) Start Date:2017-03-24
VRSK (Verisk Analytics) Start Date:2009-10-09
VRSN (Verisign) Start Date:2005-01-03
VRT (Vertiv Holdings Co.) Start Date:2018-07-30
VRTS (Veritas Software) Start Date:2009-01-02
VRTV (Veritiv Corp) Start Date:2014-07-02
VRTX (Vertex Pharmaceuticals Inc) Start Date:2005-01-03
VS (Versus Systems Common Shares) Start Date:2020-12-29
VSAT (Viasat) Start Date:2007-01-03
VSCO (Victoria's Secret) Start Date:2021-07-21
VSEC (Vse) Start Date:2007-05-16
VSH (Vishay Intertechnology) Start Date:2007-01-03
VSME (Vs Media Holdings Limited) Start Date:2023-09-28
VST (Vistra Energy) Start Date:2017-05-10
VSTA (Vasta Platform) Start Date:2020-07-31
VSTE (Vast Renewables Ltd.) Start Date:2022-01-10
VSTM (Verastem) Start Date:2012-01-27
VSTO (Vista Outdoor) Start Date:2015-02-09
VSTS (Vestis Corp) Start Date:2023-09-27
VTAK (Ra Medical Systems Inc) Start Date:2018-09-27
VTEX (Vtex) Start Date:2021-07-22
VTGN (Vistagen Therapeutics,) Start Date:2016-05-11
VTLE (Vital Energy) Start Date:2011-12-15
VTMX (Vesta Real Estate Corporation) Start Date:2023-06-30
VTN (Invesco Trust For Investment Grade New York Municipals) Start Date:2007-05-16
VTNR (Vertex Energy Inc) Start Date:2013-02-13
VTOL (Bristow) Start Date:2013-01-22
VTR (Ventas Inc) Start Date:2005-01-03
VTRS (Viatris) Start Date:2020-11-12
VTRU (Vitru) Start Date:2020-09-18
VTS (Vitesse Energy) Start Date:2023-01-17
VTSI (Virtra) Start Date:2018-03-29
VTVT (Vtv Therapeutics) Start Date:2015-07-30
VTYX (Ventyx Biosciences) Start Date:2021-10-21
VUZI (Vuzix Corporation) Start Date:2010-04-01
VVI (Viad) Start Date:2007-04-27
VVOS (Vivos Therapeutics) Start Date:2020-12-11
VVPR (Vivopower International Plc Ordinary Shares) Start Date:2016-12-29
VVR (Invesco Senior Income Trust) Start Date:2007-05-04
VVV (Valvoline) Start Date:2016-09-23
VVX (V2x) Start Date:2014-09-29
VWE (Vintage Wine Estates) Start Date:2021-02-08
VWEWW (Vintage Wine Estates Warrants) Start Date:2022-01-19
VXRT (Vaxart) Start Date:2012-11-09
VYGR (Voyager Therapeutics) Start Date:2015-11-11
VYNE (Vyne Therapeutics) Start Date:2018-01-25
VYX (Ncr Voyix Corp) Start Date:2007-01-03
VZ (Verizon Communications) Start Date:2005-01-03
VZIO (Vizio Holding) Start Date:2021-03-25
VZLA (Vizsla Silver Common Shares) Start Date:2022-01-21
W (Wayfair) Start Date:2014-10-02
WAB (Wabtec Corporation) Start Date:2005-01-03
WABC (Westamerica Bancorp) Start Date:2009-07-21
WAFD (Washington Federal) Start Date:2007-05-01
WAFDP (Washington Federal Depositary Shares) Start Date:2021-02-11
WAFU (Wah Fu Education Ordinary Shares) Start Date:2019-04-30
WAL (Western Alliance Bancorporation) Start Date:2007-01-03
WALD (Waldencast Plc Class A) Start Date:2021-05-12
WASH (Washington Trust) Start Date:2007-05-04
WAT (Waters Corporation) Start Date:2005-01-03
WATT (Energous) Start Date:2014-03-28
WAVD (Wavedancer) Start Date:2007-05-17
WAVE (Eco Wave Power Global) Start Date:2021-07-01
WB (Weibo Corporation) Start Date:2014-04-17
WBA (Walgreens Boots Alliance) Start Date:2014-12-31
WBD (Warner Bros Discovery) Start Date:2022-04-04
WBEV (Winc,) Start Date:2021-11-11
WBS (Webster Financial Corporation) Start Date:2007-01-03
WBUY (Webuy Global Ltd) Start Date:2023-10-19
WBX (Wallbox N.V. Class A Ordinary Shares) Start Date:2021-04-19
WCC (Wesco International) Start Date:2007-05-01
WCN (Waste Connections) Start Date:2007-01-03
WD (Walker & Dunlop) Start Date:2010-12-15
WDAY (Workday) Start Date:2012-12-10
WDC (Western Digital) Start Date:2005-01-03
WDFC (Wd-40) Start Date:2007-05-09
WDH (Waterdrop) Start Date:2021-05-07
WDI (Western Asset Diversified Income Fund Common Shares Of Beneficial Interest) Start Date:2021-06-25
WDS (Woodside Energy American Depositary Shares Each Representing One Ordinary Share) Start Date:2022-06-02
WEA (Western Asset Bond Fund Share Of Beneficial Interest) Start Date:2007-05-16
WEAV (Weave Communications,) Start Date:2021-11-11
WEC (Wec Energy Inc) Start Date:2005-01-03
WEJO (Wejo Common Shares) Start Date:2021-11-19
WELL (Welltower) Start Date:2007-04-30
WEN (The Wendy's Company) Start Date:2007-01-03
WERN (Werner Enterprises) Start Date:2007-01-03
WES (Western Midstream Partners Lp) Start Date:2012-12-07
WEST (Westrock Coffee Company) Start Date:2022-08-29
WETF (WisdomTree Investments) Start Date:2007-05-16
WETG (Wetrade) Start Date:2020-07-23
WEWKQ (Wework Inc) Start Date:2021-10-21
WEX (Wex) Start Date:2007-04-30
WEYS (Weyco) Start Date:2007-05-16
WF (Woori Financial  American Depositary Shares) Start Date:2007-05-16
WFC (Wells Fargo) Start Date:2005-01-03
WFCF (Where Food Comes From) Start Date:2021-01-05
WFG (West Fraser Timber Co. Ltd) Start Date:2021-02-01
WFRD (Weatherford International Plc Ordinary Shares) Start Date:2021-06-02
WGO (Winnebago Industries) Start Date:2007-01-03
WGS (Genedx Holdings Class A) Start Date:2020-11-04
WH (Wyndham Hotels & Resorts) Start Date:2018-05-18
WHD (Cactus) Start Date:2018-02-08
WHF (Whitehorse Finance) Start Date:2012-12-05
WHG (Westwood) Start Date:2007-05-16
WHLM (Wilhelmina International) Start Date:2009-02-19
WHLR (Wheeler Real Estate Investment Trust) Start Date:2012-11-19
WHLRD (Wheeler Real Estate Investment Trust Series D Cumulative Preferred Stock) Start Date:2016-09-16
WHLRP (Wheeler Real Estate Investment Trust Class B Preferred Stock) Start Date:2014-04-30
WHR (Whirlpool) Start Date:2005-01-03
WIA (Western Asset Inflation-Linked Income Fund) Start Date:2007-05-07
WILC (G Willi-Food International Ltd) Start Date:2016-04-07
WIMI (Wimi Hologram Cloud) Start Date:2020-04-01
WINA (Winmark) Start Date:2007-05-18
WING (Wingstop) Start Date:2015-06-12
WINT (Windtree Therapeutics) Start Date:2020-05-20
WIRE (Encore Wire) Start Date:2007-04-26
WISA (Wisa Technologies) Start Date:2018-07-27
WISH (Contextlogic) Start Date:2020-12-16
WIT (Wipro Limited) Start Date:2013-02-11
WIW (Western Asset Inflation-Linked Opportunities & Income Fund) Start Date:2007-05-02
WIX (Wix.com Ltd.) Start Date:2013-11-06
WK (Workiva) Start Date:2014-12-12
WKC (World Kinect Corp) Start Date:2007-04-30
WKEY (Wisekey International Holding Ag American Depositary Shares) Start Date:2019-12-27
WKHS (Workhorse) Start Date:2016-01-07
WKME (Walkme) Start Date:2021-06-16
WKSP (Worksport) Start Date:2021-08-04
WKSPW (Worksport Warrant) Start Date:2021-08-04
WLDN (Willdan) Start Date:2007-05-16
WLDS (Wearable Devices) Start Date:2022-09-13
WLFC (Willis Lease Finance) Start Date:2007-05-16
WLGS (Wang &Amp; Lee) Start Date:2023-04-20
WLK (Westlake Chemical) Start Date:2007-05-01
WLKP (Westlake Chemical Partners Lp) Start Date:2014-07-30
WLMS (Williams Industrial Services) Start Date:2008-02-13
WLY (John Wiley & Sons) Start Date:2022-04-01
WLYB (John Wiley & Sons) Start Date:2007-05-16
WM (Waste Management) Start Date:2007-04-30
WMB (Williams Cos.) Start Date:2005-01-03
WMC (Western Asset Mortgage) Start Date:2012-05-10
WMG (Warner Music) Start Date:2020-06-03
WMK (Weis Markets) Start Date:2007-05-10
WMPN (William Penn Bancorporation) Start Date:2021-03-25
WMS (Advanced Drainage Systems) Start Date:2014-07-25
WMT (Walmart) Start Date:2005-01-03
WNC (Wabash National) Start Date:2007-05-01
WNEB (Western New England Bancorp) Start Date:2007-05-16
WNS (Wns) Start Date:2007-01-03
WNW (Wunong Net Technology) Start Date:2020-12-15
WOLF (Wolfspeed,) Start Date:2007-04-30
WOOF (Petco Health & Wellness Company) Start Date:2021-01-14
WOR (Worthington Industries) Start Date:2005-01-03
WORX (Scworx) Start Date:2016-10-06
WOW (Wideopenwest) Start Date:2017-05-25
WPC (W. P. Carey) Start Date:2007-01-03
WPM (Wheaton Precious Metals) Start Date:2007-05-01
WPP (Wpp Plc) Start Date:2017-11-28
WPRT (Westport Fuel Systems Inc Common Shares) Start Date:2008-08-15
WRAP (Wrap Technologies) Start Date:2018-05-29
WRB (W. R. Berkley Corporation) Start Date:2007-04-27
WRBY (Warby Parker) Start Date:2021-09-29
WRE (Washington Real Estate Investment Trust) Start Date:2007-01-03
WRK (Westrock) Start Date:2015-06-24
WRLD (World Acceptance) Start Date:2007-05-01
WRN (Western Copper And Gold) Start Date:2008-10-27
WRNT (Warrantee) Start Date:2023-07-25
WS (Worthington Steel Inc) Start Date:2023-11-28
WSBC (Wesbanco) Start Date:2007-05-10
WSBF (Waterstone Financial Com) Start Date:2008-08-04
WSC (Willscot Mobile Mini Corp) Start Date:2015-11-05
WSFS (Wsfs Financial) Start Date:2007-05-07
WSM (Williams-Sonoma) Start Date:2007-01-03
WSO (Watsco) Start Date:2007-05-02
WSO.B (Watsco) Start Date:2007-05-16
WSR (Whitestone Reit) Start Date:2010-08-26
WST (West Pharmaceutical Services) Start Date:2007-01-03
WSTG (Wayside Technology) Start Date:2007-05-16
WT (WisdomTree) Start Date:2007-05-16
WTBA (West Bancorporation) Start Date:2007-05-16
WTER (The Alkaline Water Company) Start Date:2013-07-09
WTFC (Wintrust Financial Corporation) Start Date:2007-01-03
WTFCM (Wintrust Financial Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D) Start Date:2015-07-09
WTFCP (Wintrust Financial Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 6.875% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E) Start Date:2020-05-29
WTI (W&T Offshore) Start Date:2007-04-30
WTM (White Mountains Insurance) Start Date:2007-05-16
WTO (Utime Ltd.) Start Date:2021-04-06
WTRG (Essential Utilities) Start Date:2007-04-27
WTS (Watts Water Technologies) Start Date:2007-04-27
WTTR (Select Energy Services) Start Date:2017-04-21
WTW (Willis Towers Watson) Start Date:2016-01-05
WU (Western Union Co) Start Date:2006-10-02
WULF (Terawulf) Start Date:2007-05-18
WVE (Wave Life Sciences) Start Date:2015-11-11
WVVI (Willamette Valley Vineyards) Start Date:2007-05-16
WVVIP (Willamette Valley Vineyards Series A Redeemable Preferred Stock) Start Date:2016-06-29
WW (Ww International) Start Date:2007-05-02
WWD (Woodward) Start Date:2007-05-03
WWE (World Wrestling Entertainment) Start Date:2007-01-03
WWR (Westwater Resources) Start Date:2007-05-08
WWW (Wolverine World Wide) Start Date:2007-01-03
WY (Weyerhaeuser) Start Date:2005-01-03
WYNN (Wynn Resorts Ltd) Start Date:2005-01-03
WYY (Widepoint) Start Date:2007-04-26
X (United States Steel Corporation) Start Date:2005-01-03
XAIR (Beyond Air) Start Date:2019-05-07
XBIO (Xenetic Biosciences) Start Date:2016-11-07
XBIOW (Xenetic Biosciences Warrants) Start Date:2019-07-23
XBIT (Xbiotech) Start Date:2015-04-15
XCUR (Exicure) Start Date:2018-05-22
XEL (Xcel Energy Inc) Start Date:2005-01-03
XELA (Exela Technologies) Start Date:2015-03-27
XELB (Xcel Brands) Start Date:2007-05-23
XENE (Xenon Pharmaceuticals Inc) Start Date:2014-11-05
XERS (Xeris Pharmaceuticals) Start Date:2018-06-21
XFLT (Xai Octagon Floating Rate & Alternative Income Term Trust Common Shares Of Beneficial Interest) Start Date:2017-09-27
XFOR (X4 Pharmaceuticals) Start Date:2019-04-16
XGN (Exagen) Start Date:2019-09-19
XHR (Xenia Hotels & Resorts) Start Date:2015-02-04
XIN (Xinyuan Real Estate Co American Depositary Shares) Start Date:2007-12-12
XL (Xl Fleet) Start Date:2019-09-03
XLO (Xilio Therapeutics) Start Date:2021-10-22
XMTR (Xometry) Start Date:2021-06-30
XNCR (Xencor) Start Date:2013-12-03
XNET (Xunlei American Depositary Shares) Start Date:2014-06-24
XOM (Exxon Mobil) Start Date:2005-01-03
XOMA (Xoma) Start Date:2007-05-04
XOS (Xos,) Start Date:2020-12-08
XOSWW (Xos Warrants) Start Date:2020-12-07
XP (Xp) Start Date:2019-12-11
XPEL (Xpel) Start Date:2019-07-22
XPER (Xperi Holding Corp) Start Date:2020-05-29
XPEV (Xpeng) Start Date:2020-08-27
XPL (Solitario Zinc) Start Date:2007-05-16
XPO (Xpo Logistics) Start Date:2007-01-03
XPOF (Xponential Fitness) Start Date:2021-07-23
XPON (Expion360) Start Date:2022-04-01
XPRO (Expro Holdings N.V.) Start Date:2013-08-09
XRAY (Dentsply Sirona) Start Date:2005-01-03
XRTX (Xortx Therapeutics) Start Date:2021-10-13
XRX (Xerox) Start Date:2005-01-03
XSPA (Xpresspa) Start Date:2010-07-27
XTLB (Xtl Biopharmaceuticals American Depositary Shares) Start Date:2014-02-18
XTNT (Xtant Medical Holdings) Start Date:2015-10-19
XWEL (Xwell) Start Date:2010-07-27
XXII (22Nd Century) Start Date:2011-01-26
XYF (X Financial American Depositary Shares Each Representing Six Class A Ordinary Shares) Start Date:2018-09-19
XYL (Xylem) Start Date:2011-10-13
YALA (Yalla) Start Date:2020-09-30
YCBD (Cbdmd) Start Date:2017-11-17
YELL (Yellow) Start Date:2007-05-01
YELP (Yelp) Start Date:2012-03-02
YETI (Yeti Holdings) Start Date:2018-10-25
YEXT (Yext) Start Date:2017-04-13
YGF (Yangufang International Co., Ltd.) Start Date:2023-03-28
YGMZ (Mingzhu Logistics) Start Date:2020-11-02
YHGJ (Yunhong Green Cti Ltd.) Start Date:2007-05-16
YI (111 American Depositary Shares) Start Date:2018-09-12
YJ (Yunji ADS) Start Date:2019-05-03
YMAB (Y-Mabs Therapeutics) Start Date:2018-09-21
YMM (Full Truck Alliance Co.) Start Date:2021-06-22
YMTX (Yumanity Therapeutics) Start Date:2016-02-11
YORW (York Water) Start Date:2007-05-16
YOSH (Yoshiharu Global Co.) Start Date:2022-09-09
YOTA (Yotta Acquisition Corporation) Start Date:2022-06-27
YOU (Clear Secure) Start Date:2021-06-30
YPF (Ypf Sociedad Anonima) Start Date:2013-02-11
YQ (17 Education & Technology) Start Date:2020-12-04
YRD (Yiren Digital American Depositary Shares Each Representing Two Ordinary Shares) Start Date:2015-12-18
YSG (Yatsen Holding) Start Date:2020-11-19
YTEN (Yield10 Bioscience) Start Date:2007-05-10
YTRA (Yatra Online, Ordinary Shares) Start Date:2016-12-19
YUM (Yum! Brands Inc) Start Date:2005-01-03
YUMC (Yum China Holdings) Start Date:2016-10-31
YVR (Liquid Media Common Shares) Start Date:2018-08-13
YY (Joyy) Start Date:2012-11-21
Z (Zillow) Start Date:2015-08-03
ZAPP (Zapp Electric Vehicles Ltd.) Start Date:2021-11-05
ZBH (Zimmer Biomet Holdings) Start Date:2007-04-30
ZBRA (Zebra Technologies) Start Date:2005-01-03
ZCMD (Zhongchao) Start Date:2020-02-24
ZD (Ziff Davis,) Start Date:2007-04-30
ZDGE (Zedge Class B) Start Date:2016-05-26
ZENV (Zenvia) Start Date:2021-07-22
ZEPP (Zepp Health American Depositary Shares) Start Date:2018-02-08
ZETA (Zeta Global Holdings) Start Date:2021-06-10
ZEUS (Olympic Steel) Start Date:2007-04-26
ZEVY (Lightning Emotors Inc) Start Date:2020-07-02
ZFOX (Zerofox Holdings) Start Date:2022-08-04
ZG (Zillow) Start Date:2011-07-20
ZGN (Ermenegildo Zegna N.V. Ordinary Shares) Start Date:2021-12-20
ZH (Zhihu) Start Date:2021-03-26
ZI (Zoominfo Technologies) Start Date:2020-06-04
ZIM (Zim Integrated Shipping Services) Start Date:2021-01-28
ZIMV (Zimvie) Start Date:2022-02-24
ZION (Zions Bancorp) Start Date:2005-01-03
ZIONO (Zions Bancorporation N.A. Dep Shs Repstg 1/40Th Perp Pfd Ser G) Start Date:2020-01-02
ZIONP (Zions Bancorporation N.A. Depositary Shares) Start Date:2020-01-02
ZIP (Ziprecruiter) Start Date:2021-05-26
ZIVO (Zivo Bioscience) Start Date:2021-05-28
ZIVOW (Zivo Bioscience Warrants) Start Date:2021-05-28
ZJYL (Jin Medical International Ltd.) Start Date:2023-03-28
ZKH (Zkh Limited) Start Date:2023-12-15
ZKIN (Zk International Co. Ordinary Share) Start Date:2017-09-01
ZLAB (Zai Lab Limited) Start Date:2017-09-20
ZM (Zoom) Start Date:2019-04-18
ZNTL (Zentalis Pharmaceuticals) Start Date:2020-04-03
ZOM (Zomedica) Start Date:2016-07-29
ZS (Zscaler) Start Date:2018-03-16
ZTEK (Zentek) Start Date:2022-03-22
ZTO (Zto Express) Start Date:2016-10-27
ZTR (Virtus Total Return Fund) Start Date:2007-05-08
ZTS (Zoetis) Start Date:2013-02-01
ZUMZ (Zumiez) Start Date:2007-04-27
ZUO (Zuora) Start Date:2018-04-12
ZVIA (Zevia) Start Date:2021-07-22
ZVRA (Zevra Therapeutics Inc) Start Date:2021-01-08
ZVSA (Zyversa Therapeutics) Start Date:2022-02-10
ZWS (Zurn Water Solutions Corporation) Start Date:2012-03-29
ZYME (Zymeworks) Start Date:2017-04-28
ZYNE (Zynerba Pharmaceuticals) Start Date:2015-08-05
ZYXI (Zynex) Start Date:2008-07-08
AABA-DELISTED () Start Date:2007-04-27
AATC-DELISTED (Autoscope Technologies) Start Date:2021-07-21
AAWW-DELISTED (Atlas Air Worldwide) Start Date:2007-04-25
ABI-DELISTED (Safety First Trust Series 2009-) Start Date:2007-04-30
ABK-DELISTED (Ambac Financial Inc) Start Date:2004-01-02
ABMD-DELISTED (Abiomed Inc) Start Date:2005-01-03
ABS-DELISTED (Albertsons) Start Date:2004-01-02
ABST-DELISTED (Absolute Software) Start Date:2020-11-02
ABTX-DELISTED (Allegiance Bancshares) Start Date:2015-10-08
ACAS-DELISTED (American Capital) Start Date:2004-01-02
ACBI-DELISTED (Atlantic Capital Bancshares) Start Date:2015-11-02
ACC-DELISTED (American Campus Communities) Start Date:2007-01-03
ACGN-DELISTED (Aceragen) Start Date:2007-12-10
ACII-DELISTED (Atlas Crest Investment Ii Class A) Start Date:2021-03-29
ACQR-DELISTED (Independence Holdings) Start Date:2021-05-19
ACTD-DELISTED (Arclight Clean Transition Ii Class A Ordinary Share) Start Date:2021-05-24
ACTDU-DELISTED (Arclight Clean Transition Ii Unit) Start Date:2021-03-23
ACTDW-DELISTED (Arclight Clean Transition Ii Warrant) Start Date:2021-05-21
ACXM-DELISTED (Acxiom Holdings) Start Date:2004-01-02
ADF-DELISTED (Aldel Financial) Start Date:2007-06-04
ADGI-DELISTED (Adagio Therapeutics) Start Date:2021-08-06
ADS-DELISTED (Alliance Data Systems) Start Date:2005-01-03
AERI-DELISTED (Aerie Pharmaceuticals Co) Start Date:2013-10-25
AET-DELISTED (Aetna) Start Date:2004-01-02
AFIN-DELISTED (American Finance Trust) Start Date:2018-07-19
AGCB-DELISTED (Altimeter Growth 2) Start Date:2021-01-07
AGFS-DELISTED (Agrofresh Solutions) Start Date:2014-04-24
AGGR-DELISTED (Agile Growth Class A Ordinary Share) Start Date:2021-05-19
AGTC-DELISTED (Applied Genetic Technologies C) Start Date:2014-03-27
AIMAU-DELISTED (Aimfinity Investment I Unit) Start Date:2022-04-26
AIMC-DELISTED (Altra Industrial Motion) Start Date:2007-01-03
AINV-DELISTED (Apollo Investment Corp) Start Date:2005-01-03
AJRD-DELISTED (Aerojet Rocketdyne Holdings) Start Date:2007-04-26
AKUS-DELISTED (Akouos) Start Date:2020-06-26
ALBO-DELISTED (Albireo Pharma) Start Date:2007-05-16
ALFIQ-DELISTED (Alfi Inc) Start Date:2021-05-04
ALJJ-DELISTED (Alj Regional Holdings) Start Date:2007-05-16
ALNA-DELISTED (Allena Pharmaceuticals) Start Date:2017-11-02
ALR-DELISTED (Alerislife) Start Date:2017-07-03
ALSK-DELISTED (Alaska Comm Sys) Start Date:2007-05-01
ALXN-DELISTED (Alexion Pharmaceuticals) Start Date:2005-01-03
AMLN-DELISTED (Amylin Pharmaceuticals) Start Date:2004-01-02
AMOV-DELISTED (America Movil S.A.B. De C.V. Class A American Depositary Shares) Start Date:2007-05-16
AMPI-DELISTED (Advanced Merger Partners Class A) Start Date:2021-04-22
AMTBB-DELISTED (Amerant Bancorp Class B) Start Date:2018-08-29
AMYT-DELISTED (Amryt Pharma Plc American Depositary Shares) Start Date:2020-07-08
ANAT-DELISTED (American National) Start Date:2007-05-16
ANDV-DELISTED (Andeavor) Start Date:2007-04-30
ANR-DELISTED (Alpha Natural Resources C) Start Date:2005-02-15
ANTM-DELISTED (Anthem) Start Date:2007-04-30
APC-DELISTED (Anadarko Petroleum Corp) Start Date:2004-01-02
APEN-DELISTED (Apollo Endosurgery) Start Date:2007-05-16
APGN-DELISTED (Apexigen) Start Date:2021-02-22
APNC-DELISTED (Apeiron Capital Investment Corp) Start Date:2021-12-30
APOL-DELISTED (Apollo Education) Start Date:2004-01-02
APR-DELISTED (Apria) Start Date:2021-02-11
APTS-DELISTED (Preferred Apartment) Start Date:2011-04-01
APTX-DELISTED (Aptinyx) Start Date:2018-06-21
AQUA-DELISTED (Evoqua Water Technologies) Start Date:2017-11-02
ARCK-DELISTED (Arbor Rapha Capital Bioholdings I Class A) Start Date:2021-12-20
ARCP-DELISTED (Vereit) Start Date:2011-09-07
ARD-DELISTED (Ardagh S.A.) Start Date:2017-03-15
ARDS-DELISTED (Aridis Pharmaceuticals) Start Date:2018-08-14
ARG-DELISTED (Airgas) Start Date:2004-01-02
ARGU-DELISTED (Argus Capital Class A) Start Date:2021-11-15
ARNA-DELISTED (Arena Pharmaceuticals) Start Date:2007-01-03
ARNC-DELISTED (Arconic) Start Date:2020-04-01
ASAP-DELISTED (Waitr Holdings Inc) Start Date:2016-05-26
ASBC-DELISTED (Associated Banc-Corp) Start Date:2004-01-02
ASPL-DELISTED (Aspirational Consumer Lifestyle) Start Date:2020-11-13
ASPU-DELISTED (Aspen) Start Date:2011-06-30
ATC-DELISTED (Atotech) Start Date:2021-02-04
ATCO-DELISTED (Atlas) Start Date:2007-05-07
ATCX-DELISTED (Atlas Technical Consultants Class A) Start Date:2018-11-16
ATH-DELISTED (Athene Holding Ltd.) Start Date:2016-12-09
ATRS-DELISTED (Antares Pharma) Start Date:2007-05-16
ATVC-DELISTED (Tribe Capital Growth I Class A) Start Date:2021-05-26
ATVCU-DELISTED (Tribe Capital Growth I Units) Start Date:2021-03-05
ATVCW-DELISTED (Tribe Capital Growth I Warrant) Start Date:2021-05-19
AUDA-DELISTED (Audacy Inc) Start Date:2007-04-27
AUTO-DELISTED (Autoweb) Start Date:2007-05-08
AUY-DELISTED (Yamana Gold) Start Date:2007-06-12
AV-DELISTED (Aviva Plc Unsponsored ADR) Start Date:2009-10-20
AVEO-DELISTED (Aveo Pharmaceuticals) Start Date:2010-03-12
AVLR-DELISTED (Avalara) Start Date:2018-06-15
AVP-DELISTED (Avon Products) Start Date:2004-01-02
AXHI-DELISTED (Industrial Human Capital Inc) Start Date:2021-12-10
AXU-DELISTED (Alexco Resource Common Shares) Start Date:2007-09-20
AYLA-DELISTED (Ayala Pharmaceuticals) Start Date:2020-05-08
AZRE-DELISTED (Azure Power Global Limited) Start Date:2016-10-12
BBI-DELISTED (Brickell Biotech) Start Date:2007-05-01
BBIG-DELISTED (Vinco Ventures) Start Date:2018-05-03
BBQ-DELISTED (Bbq Holdings) Start Date:2007-05-16
BBT-DELISTED (Bb&T Corporation) Start Date:2004-01-02
BCEI-DELISTED (Bonanza Creek Energy) Start Date:2011-12-15
BCR-DELISTED (C.R. Bard) Start Date:2004-01-02
BDSI-DELISTED (Biodelivery Sciences) Start Date:2007-05-16
BDXB-DELISTED (Becton Dickinson And Company Depositary Shares Each Representing A 1/20Th Interest In A Share Of 6.00% Mandatory Convertible Preferred Stock Series B) Start Date:2020-06-03
BEAM-DELISTED () Start Date:2007-05-01
BGRY-DELISTED (Berkshire Grey) Start Date:2021-02-11
BHGE-DELISTED (Baker Hughes) Start Date:2017-07-05
BHI-DELISTED (Baker Hughes Incorporated Commo) Start Date:2004-01-02
BKEP-DELISTED (Blueknight Energy Partners L.P. Common Units) Start Date:2010-11-01
BKEPP-DELISTED (Blueknight Energy Partners L.P. Series A Preferred Units) Start Date:2011-11-10
BLCM-DELISTED (Bellicum Pharmaceuticals) Start Date:2014-12-18
BLCT-DELISTED (Bluecity Holdings) Start Date:2020-07-08
BLU-DELISTED (Bellus Health) Start Date:2007-05-16
BMC-DELISTED (Bmc Software) Start Date:2004-01-02
BMS-DELISTED (Bemis Company Common Stoc) Start Date:2004-01-02
BMTC-DELISTED (Bryn Mawr Bank) Start Date:2007-05-16
BNFT-DELISTED (Benefitfocus) Start Date:2013-09-18
BOCH-DELISTED (Bank Of Commerce) Start Date:2007-05-16
BOMN-DELISTED (Boston Omaha) Start Date:2016-09-06
BPFH-DELISTED (Boston Private Financial) Start Date:2007-05-08
BPMP-DELISTED (Bp Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2017-10-26
BPY-DELISTED (Brookfield Property Partners L.P.) Start Date:2013-03-22
BPYU-DELISTED (Brookfield Property Reit) Start Date:2018-08-28
BRCM-DELISTED (Broadcom) Start Date:2004-01-02
BRCN-DELISTED (Burcon Nutrascience) Start Date:2021-05-25
BRG-DELISTED (Bluerock Residential Growth) Start Date:2014-03-28
BRKS-DELISTED (Brooks Automation) Start Date:2007-01-03
BRMK-DELISTED (Broadmark Realty Capital) Start Date:2019-11-15
BRPM-DELISTED (B. Riley Principal 150 Merger Class A) Start Date:2021-04-13
BRPMU-DELISTED (B. Riley Principal 150 Merger Unit) Start Date:2021-02-19
BRPMW-DELISTED (B. Riley Principal 150 Merger Warrant) Start Date:2021-04-13
BSKY-DELISTED (Big Sky Growth Partners Class A) Start Date:2021-07-01
BSMX-DELISTED (Banco Santander Mexico S.A. Institucion De Banca Multiple Grupo Financiero Santander Mexico) Start Date:2012-09-26
BTRS-DELISTED (Btrs Holdings Class 1) Start Date:2019-08-06
BWC-DELISTED (Bwx Technologies) Start Date:2005-11-01
BXLT-DELISTED () Start Date:2015-06-15
BXS-DELISTED (Bancorpsouth Bank) Start Date:2017-11-07
CA-DELISTED (Ca Technologies) Start Date:2004-01-02
CAI-DELISTED (Cai International) Start Date:2007-05-16
CAJPY-DELISTED (Canon Inc) Start Date:2007-01-03
CAM-DELISTED (Cameron International Corporati) Start Date:2004-01-02
CATB-DELISTED (Catabasis Pharmaceuticals) Start Date:2015-06-25
CBB-DELISTED (Cincinnati Bell) Start Date:2012-12-20
CBE-DELISTED (Cooper Industries Plc) Start Date:2004-01-02
CBG-DELISTED (Cbre Inc Cla) Start Date:2004-07-01
CBRGU-DELISTED (Chain Bridge I Units) Start Date:2021-11-10
CCE-DELISTED (Coca-Cola Enterprises Com) Start Date:2004-01-02
CCIV-DELISTED (Churchill Capital Iv) Start Date:2020-09-18
CCMP-DELISTED (Cmc Materials) Start Date:2007-04-26
CCXI-DELISTED (Chemocentryx) Start Date:2012-02-08
CDEV-DELISTED (Centennial Resource Development, Class A Business Combination) Start Date:2016-04-15
CDK-DELISTED (Cdk Global) Start Date:2014-09-22
CDR-DELISTED (Cedar Realty Trust) Start Date:2007-04-26
CEAYY-DELISTED (China Eastern Airlines Ltd.) Start Date:2007-05-16
CEG-DELISTED (Constellation Energy Inc) Start Date:2004-01-02
CELG-DELISTED (Celgene) Start Date:2004-01-02
CEMI-DELISTED (Chembio Diagnostics) Start Date:2007-05-16
CERC-DELISTED (Cerecor) Start Date:2015-11-13
CERN-DELISTED (Cerner) Start Date:2005-01-03
CFN-DELISTED (Carefusion Common S) Start Date:2009-09-01
CFX-DELISTED (Colfax Corporation) Start Date:2008-05-08
CHMA-DELISTED (Chiasma) Start Date:2015-07-16
CHNG-DELISTED (Change Healthcare) Start Date:2019-06-27
CHNGU-DELISTED (Change Healthcare Tangible Equity Units) Start Date:2019-06-27
CHRA-DELISTED (Charah Solutions) Start Date:2018-06-14
CIH-DELISTED (China Index Holdings ADS) Start Date:2019-06-12
CINC-DELISTED (Cincor Pharma) Start Date:2022-01-07
CIT-DELISTED (Cit Inc) Start Date:2009-12-10
CLAS-DELISTED (Class Acceleration) Start Date:2021-03-08
CLBS-DELISTED (Caladrius Biosciences) Start Date:2007-08-09
CLDR-DELISTED (Cloudera) Start Date:2017-04-28
CLI-DELISTED (Mack-Cali Realty) Start Date:2007-04-27
CLOEU-DELISTED (Clover Leaf Capital Unit) Start Date:2021-07-20
CLR-DELISTED (Continental Resources) Start Date:2007-05-15
CLSN-DELISTED (Celsion) Start Date:2008-06-30
CMCSK-DELISTED (Comcast Corporation) Start Date:2004-01-02
CMO-DELISTED (Capstead Mortgage) Start Date:2007-05-07
CMPI-DELISTED (Checkmate Pharmaceuticals) Start Date:2020-08-07
CNBKA-DELISTED (Century Bancorp) Start Date:2007-05-16
CNCE-DELISTED (Concert Pharmaceuticals) Start Date:2014-02-13
CNNB-DELISTED (Cincinnati Bancorp) Start Date:2015-10-15
CNR-DELISTED (Cornerstone Building Brands) Start Date:2007-04-27
CNST-DELISTED (Constellation Pharmaceuticals) Start Date:2018-07-19
CNVY-DELISTED (Convey Holding Parent) Start Date:2021-06-16
CO-DELISTED (Global Cord Blood) Start Date:2009-11-19
COG-DELISTED (Cabot Oil & Gas) Start Date:2004-01-02
COH-DELISTED (Coach) Start Date:2004-01-02
COHR-DELISTED (Coherent) Start Date:2007-04-27
COL-DELISTED (Rockwell Collins Common S) Start Date:2004-01-02
COLI-DELISTED (Colicity) Start Date:2021-04-16
CONE-DELISTED (Cyrusone) Start Date:2013-01-18
COR-DELISTED (Coresite Realty Corporation) Start Date:2007-05-02
CORE-DELISTED (Core Mark Holding Co) Start Date:2017-01-26
CORS-DELISTED (Corsair Partnering) Start Date:2021-08-24
COUP-DELISTED (Coupa Software Incorporated) Start Date:2016-10-06
COV-DELISTED (Covidien Plc. Ordinary Shares) Start Date:2007-07-02
COWN-DELISTED (Cowen) Start Date:2007-05-03
CPGX-DELISTED () Start Date:2015-06-17
CPL-DELISTED (Carolina Power & Light) Start Date:2004-10-01
CPLG-DELISTED (Corepoint Lodging) Start Date:2018-05-31
CREE-DELISTED (Cree) Start Date:2007-01-03
CRTD-DELISTED (Creatd) Start Date:2020-09-11
CRTX-DELISTED (Cortexyme) Start Date:2019-05-09
CRXT-DELISTED (Clarus Therapeutics Holdings) Start Date:2021-09-07
CRY-DELISTED (Cryolife) Start Date:2007-05-10
CRZN-DELISTED (Corazon Capital V838 Monoceros Class A Ordinary Shares) Start Date:2021-06-11
CRZWQ-DELISTED (Core Scientific Inc) Start Date:2021-04-08
CSC-DELISTED (Computer Sciences C) Start Date:2004-01-02
CS-DELISTED (Credit Suisse Ag) Start Date:2007-01-03
CSII-DELISTED (Cardiovascular Systems) Start Date:2009-02-26
CSOD-DELISTED (Cornerstone Ondemand) Start Date:2011-03-17
CSPR-DELISTED (Casper) Start Date:2020-02-06
CSRA-DELISTED () Start Date:2015-11-16
CTEK-DELISTED (Cynergistek) Start Date:2017-02-14
CTIC-DELISTED (Cti Biopharma) Start Date:2007-05-14
CTRP-DELISTED (Ctrip.com International Ltd.) Start Date:2004-01-02
CTRX-DELISTED (Catamaran Corporation) Start Date:2006-06-23
CTT-DELISTED (Catchmark Timber Trust) Start Date:2013-12-12
CTX-DELISTED (Centex Corp) Start Date:2007-04-30
CTXRW-DELISTED (Citius Pharmaceuticals Warrant) Start Date:2017-08-03
CTXS-DELISTED (Citrix Systems) Start Date:2004-01-02
CU-DELISTED (Cuc International) Start Date:2004-01-02
CVA-DELISTED (Covanta Holding) Start Date:2007-05-02
CVC-DELISTED (Cablevision Systems Corporation) Start Date:2004-01-02
CVET-DELISTED (Covetrus) Start Date:2019-02-05
CVG-DELISTED (Convergys Common St) Start Date:2004-01-02
CVH-DELISTED (Coventry Health Care Comm) Start Date:2004-01-02
CVT-DELISTED (Cvent Holding) Start Date:2020-11-17
CXP-DELISTED (Columbia Property Trust) Start Date:2007-05-16
CYBE-DELISTED (Cyberoptics) Start Date:2007-05-16
DBDQQ-DELISTED (Diebold Nixdorf Inc) Start Date:2007-04-30
DCGOW-DELISTED (Docgo Warrants) Start Date:2020-12-17
DCP-DELISTED (Dcp Midstream Lp) Start Date:2007-05-09
DCT-DELISTED (Duck Creek Technologies) Start Date:2020-08-14
DCUE-DELISTED (Dominion Energy 2019 Series A Corporate Units) Start Date:2019-06-19
DDR-DELISTED (Ddr) Start Date:2004-01-02
DEH-DELISTED (D8 Holdings) Start Date:2020-09-04
DF-DELISTED (Dean Foods Company) Start Date:2004-01-02
DGNU-DELISTED (Dragoneer Growth Opportunities Iii Class A Ordinary Shares) Start Date:2021-03-23
DHBC-DELISTED (Dhb Capital Class A) Start Date:2021-04-23
DICE-DELISTED (Dice Therapeutics) Start Date:2021-09-15
DIDI-DELISTED (Xiaoju Kuaizhi) Start Date:2021-06-30
DISCA-DELISTED (Discovery Class A) Start Date:2007-05-02
DISCB-DELISTED (Discovery, Series B) Start Date:2007-05-16
DISCK-DELISTED (Discovery Class C) Start Date:2008-09-18
DMYQ-DELISTED (Dmy Technology , Iv) Start Date:2021-04-26
DMYS-DELISTED (Dmy Technology  Vi Class A) Start Date:2021-11-22
DNAA-DELISTED (Social Capital Suvretta Holdings I Class A Ordinary Share) Start Date:2021-06-30
DNAC-DELISTED (Social Capital Suvretta Holdings Iii Class A Ordinary Shares) Start Date:2021-06-30
DPS-DELISTED (Dr Pepper Snapple Inc Dr) Start Date:2008-05-07
DRE-DELISTED (Duke Realty Corp) Start Date:2005-01-03
DRNA-DELISTED (Dicerna Pharmaceuticals) Start Date:2014-01-30
DSEY-DELISTED (Diversey) Start Date:2021-03-25
DSPG-DELISTED (Dsp) Start Date:2007-05-02
DSSI-DELISTED (Diamond S Shipping) Start Date:2019-03-28
DV-DELISTED (Devry) Start Date:2004-01-02
DWDP-DELISTED (Dowdupont) Start Date:2007-04-27
DYFN-DELISTED (Angel Oak Dynamic Financial Strategies Income Term Trust Common Shares Of Beneficial Interest) Start Date:2020-06-26
DYN-DELISTED () Start Date:2012-10-03
DYNS-DELISTED (Dynamics Special Purpose) Start Date:2021-05-26
EBSB-DELISTED (Meridian Bancorp Common) Start Date:2008-01-23
ECHO-DELISTED (Echo Global Logistics) Start Date:2009-10-02
ECOL-DELISTED (Us Ecology) Start Date:2011-04-19
ECOM-DELISTED (Channeladvisor) Start Date:2013-05-23
EDS-DELISTED (Exceed Company Ltd.) Start Date:2007-04-30
ELMS-DELISTED (Electric Last Mile Solutions, Class A) Start Date:2020-09-21
ELVT-DELISTED (Elevate Credit) Start Date:2017-04-06
ELY-DELISTED (Callaway Golf) Start Date:2007-05-01
EMBK-DELISTED (Embark Technology) Start Date:2021-11-11
EMC-DELISTED (Emc) Start Date:2004-01-02
EMCF-DELISTED (Emclaire Financial) Start Date:2007-05-21
EMWP-DELISTED (Eros Media World Plc A Ordinary Shares Gbp 0.30 Par Value) Start Date:2013-11-13
ENBL-DELISTED (Enable Midstream Partners Lp) Start Date:2014-04-11
ENDP-DELISTED (Endo International Plc) Start Date:2014-03-03
ENFA-DELISTED (890 5Th Avenue Partners) Start Date:2021-03-05
ENIA-DELISTED (Enel Americas S.A.) Start Date:2007-05-01
ENJY-DELISTED (Enjoy Technology) Start Date:2021-10-13
ENJYW-DELISTED (Enjoy Technology Warrant) Start Date:2021-02-04
EOCW-DELISTED (Elliott Opportunity Ii Class A Ordinary Shares) Start Date:2021-08-19
EPAY-DELISTED (Bottomline Technologies) Start Date:2007-05-09
EP-DELISTED (El Paso Common Stoc) Start Date:2004-01-02
EPWR-DELISTED (Empowerment & Inclusion Capital I Class A) Start Date:2021-03-01
EPZM-DELISTED (Epizyme) Start Date:2013-05-31
ESRX-DELISTED (Express Scripts Holding Company) Start Date:2004-01-02
ESV-DELISTED (Ensco Plc American Depositary S) Start Date:2004-01-02
ESXB-DELISTED (Community Bankers Trust Corpor) Start Date:2007-05-16
ETH-DELISTED (Ethan Allen Interiors) Start Date:2007-04-26
ETTX-DELISTED (Entasis Therapeutics Holdings) Start Date:2018-09-26
EVHC-DELISTED () Start Date:2013-08-14
EVKG-DELISTED (Ever-Glory International Inc) Start Date:2008-07-16
EVOP-DELISTED (Evo Payments) Start Date:2018-05-23
EXTN-DELISTED (Exterran Corp) Start Date:2015-11-04
EYES-DELISTED (Second Sight Medical Products) Start Date:2014-11-19
EYESW-DELISTED (Second Sight Medical Products Warrants Expiring 03/14/2024) Start Date:2017-03-29
FBC-DELISTED (Flagstar Bancorp) Start Date:2007-05-02
FCBP-DELISTED (First Choice Bancorp) Start Date:2007-05-02
FCCY-DELISTED (1St Constitution) Start Date:2007-05-16
FCRD-DELISTED (First Eagle Alternative Capital Bdc) Start Date:2010-04-22
FDC-DELISTED (First Data Corp) Start Date:2004-01-02
FDO-DELISTED (Family Dollar Stores Comm) Start Date:2004-01-02
FEXDU-DELISTED (Fintech Ecosystem Development Units) Start Date:2021-10-19
FEYE-DELISTED (Fireeye) Start Date:2013-09-20
FFBW-DELISTED (Ffbw) Start Date:2017-10-11
FHSEY-DELISTED (First High-School Education Co Ltd.) Start Date:2021-03-11
FI-DELISTED (Franks International) Start Date:2013-08-09
FII-DELISTED (Federated Investors) Start Date:2004-01-02
FINM-DELISTED (Marlin Technology) Start Date:2021-03-09
FLDM-DELISTED (Fluidigm) Start Date:2011-02-10
FLMN-DELISTED (Falcon Minerals) Start Date:2017-09-08
FLOW-DELISTED (Spx Flow) Start Date:2015-09-28
FLXN-DELISTED (Flexion Therapeutics Com) Start Date:2014-02-12
FMBI-DELISTED (First Midwest Bancorp) Start Date:2007-05-04
FMIV-DELISTED (Forum Merger Iv Class A) Start Date:2021-06-07
FMTX-DELISTED (Forma Therapeutics) Start Date:2020-06-19
FNHC-DELISTED (Federated National) Start Date:2007-05-10
FOE-DELISTED (Ferro) Start Date:2007-05-03
FORG-DELISTED (Forgerock,) Start Date:2021-09-16
FRBK-DELISTED (Republic First Bancorp) Start Date:2007-05-16
FRG-DELISTED (Franchise) Start Date:2018-08-02
FRSG-DELISTED (First Reserve Sustainable Growth Class A) Start Date:2021-04-29
FRTA-DELISTED (Forterra) Start Date:2016-10-20
FRX-DELISTED (Forest Laboratories Class) Start Date:2004-01-02
FSSI-DELISTED (Fortistar Sustainable Solutions) Start Date:2021-03-22
FSTX-DELISTED (F-Star Therapeutics) Start Date:2016-05-06
FTRP-DELISTED (Field Trip Health Common Shares) Start Date:2021-07-29
FVE-DELISTED (Five Star Quality Care) Start Date:2007-05-03
FWLT-DELISTED (Foster Wheeler Ag) Start Date:2005-06-03
FWPAY-DELISTED (Forward Pharma A) Start Date:2014-10-15
GAMCU-DELISTED (Golden Arrow Merger Unit) Start Date:2021-03-17
GAMI-DELISTED (Gamco Investors Inc Et Al) Start Date:2007-05-16
GAS-DELISTED (Agl Resources Common Stoc) Start Date:2004-01-02
GBT-DELISTED (Global Blood Therapeutics) Start Date:2015-08-12
GCP-DELISTED (Gcp Applied Technologies) Start Date:2016-01-26
GDP-DELISTED (Goodrich Petroleum Corp) Start Date:2017-04-11
GET-DELISTED (Getnet Adquirencia E Servicos Para Meios De Pagamento S.A. American Depositary Shares) Start Date:2021-10-18
GFLU-DELISTED (Gfl Environmental Tangible Equity Units) Start Date:2020-03-03
GGMCW-DELISTED (Glenfarne Merger Warrant) Start Date:2021-05-18
GGP-DELISTED (General Growth Properties) Start Date:2004-01-02
GGPI-DELISTED (Gores Guggenheim) Start Date:2021-05-18
GIIX-DELISTED (Gores Holdings Viii Class A) Start Date:2021-04-26
GIW-DELISTED (Giginternational1) Start Date:2021-07-12
GLBLU-DELISTED (Cartesian Growth Unit) Start Date:2021-02-24
GLK-DELISTED (Great Lakes Chemical) Start Date:2006-06-01
GLOP-DELISTED (Gaslog Partners Lp Common Units Representing Partnership Interests) Start Date:2014-05-07
GLSH-DELISTED (Gelesis Holdings Inc) Start Date:2022-01-14
GMCR-DELISTED (Keurig Green Mountain) Start Date:2004-01-02
GNCMA-DELISTED (Gci Liberty) Start Date:2004-01-02
GNOG-DELISTED (Golden Nugget Online Gaming, Class A) Start Date:2020-12-15
GOED-DELISTED (1847 Goedeker) Start Date:2020-07-31
GPL-DELISTED (Great Panther Mining Ordinary Shares) Start Date:2008-10-27
GPX-DELISTED (Gp Strategies) Start Date:2007-05-16
GRA-DELISTED (W.R. Grace & Co.) Start Date:2005-01-03
GR-DELISTED (Goodrich Corporation) Start Date:2004-01-02
GRNA-DELISTED (Greenlight Biosciences Holdings Pbc) Start Date:2022-02-02
GRUB-DELISTED (Grubhub) Start Date:2021-06-15
GRVI-DELISTED (Grove) Start Date:2021-06-24
GSEV-DELISTED (Gores Holdings Vii, Class A) Start Date:2021-04-15
GSKY-DELISTED (Greensky) Start Date:2018-05-24
GSQB-DELISTED (G Squared Ascend Ii Class A Ordinary Shares) Start Date:2021-08-05
GSQD-DELISTED (G Squared Ascend I Class A Ordinary Shares) Start Date:2021-03-26
GSV-DELISTED (Gold Standard Ventures) Start Date:2010-02-03
GTPA-DELISTED (Gores Technology Partners) Start Date:2021-05-06
GTPB-DELISTED (Gores Technology Partners Ii Class A) Start Date:2021-05-05
GTS-DELISTED (Triple-S Management) Start Date:2007-12-07
GTT-DELISTED (Gtt Communications) Start Date:2013-06-17
GTYH-DELISTED (Gty Technology) Start Date:2016-11-18
GWB-DELISTED (Great Western Bancorp) Start Date:2014-10-15
GWGH-DELISTED (Gwg) Start Date:2014-09-25
HAR-DELISTED (Harman International Industries) Start Date:2004-01-02
HBHC-DELISTED (Hancock Holding) Start Date:2004-01-02
HBMD-DELISTED (Howard Bancorp Md) Start Date:2007-05-23
HCBK-DELISTED (Hudson City Bancorp) Start Date:2004-01-02
HCHC-DELISTED (Hc2) Start Date:2011-06-23
HCIC-DELISTED (Hennessy Capital Investment V Class A) Start Date:2021-03-08
HCII-DELISTED (Hudson Executive Investment Ii Class A) Start Date:2021-03-29
HCN-DELISTED (Health Care Reit Common S) Start Date:2004-01-02
HCP-DELISTED (Hcp) Start Date:2004-01-02
HEXO-DELISTED (Hexo Common Shares) Start Date:2019-01-22
HFC-DELISTED (Hollyfrontier Corp) Start Date:2007-04-27
HGEN-DELISTED (Humanigen,) Start Date:2016-01-13
HGH-DELISTED (Hartford Financial Services) Start Date:2012-04-25
HIII-DELISTED (Hudson Executive Investment Iii Class A) Start Date:2021-04-20
HIL-DELISTED (Hill International) Start Date:2008-02-22
HLAH-DELISTED (Hamilton Lane Alliance Holdings I Class A) Start Date:2021-03-18
HLG-DELISTED (Hailiang Education  American Depositary Shares) Start Date:2015-07-07
HLS-DELISTED (Hls Therapeutics) Start Date:2006-11-01
HMHC-DELISTED (Houghton Mifflin Harcourt Comp) Start Date:2013-11-14
HMLP-DELISTED (Hoegh Lng Partners Lp) Start Date:2014-08-07
HMPT-DELISTED (Home Point Capital Inc) Start Date:2021-01-29
HMT-DELISTED (Host Marriott Corp) Start Date:2004-01-02
HMTV-DELISTED (Hemisphere Media  C) Start Date:2013-04-05
HNGR-DELISTED (Hanger) Start Date:2007-05-11
HNZ-DELISTED (H.J. Heinz Company) Start Date:2004-01-02
HOME-DELISTED (At Home) Start Date:2007-06-04
HORI-DELISTED (Emerging Markets Horizon Class A Ordinary Shares) Start Date:2022-02-07
HOT-DELISTED (Starwood Hotels & Resorts World) Start Date:2004-01-02
HRC-DELISTED (Hill-Rom) Start Date:2008-04-01
HRS-DELISTED (Harris Corporation) Start Date:2004-01-02
HSH-DELISTED (Hillshire Brands Company) Start Date:2012-06-12
HSKA-DELISTED (Heska) Start Date:2007-05-16
HSP-DELISTED (Hospira Inc) Start Date:2004-05-03
HTA-DELISTED (Healthcare Trust Of America) Start Date:2012-06-06
HTPA-DELISTED (Highland Transcend Partners I Class A Ordinary Shares) Start Date:2021-01-25
HVBC-DELISTED (Hv Bancorp) Start Date:2017-01-12
HYRE-DELISTED (Hyrecar) Start Date:2018-06-27
HZN-DELISTED (Horizon Global Common Shares) Start Date:2015-06-23
IAA-DELISTED (Iaa) Start Date:2019-06-17
IBAAY-DELISTED (Industrias Bachoco Sab De Cv) Start Date:2007-05-16
IBER-DELISTED (Ibere Pharmaceuticals) Start Date:2021-04-20
ICBK-DELISTED (County Bancorp) Start Date:2015-01-16
IDBA-DELISTED (Idex Biometrics Asa American Depositary Shares) Start Date:2021-03-01
IDWM-DELISTED (Idw Media Holdings Inc) Start Date:2021-08-04
IEA-DELISTED (Infrastructure And Energy Alternatives) Start Date:2016-10-06
IHC-DELISTED (Independence Holding) Start Date:2007-05-16
IIN-DELISTED (Intricon) Start Date:2007-05-16
IIVI-DELISTED (Ii-Vi Incorporated) Start Date:2007-01-03
IMAC-DELISTED (Imac Holdings) Start Date:2019-02-13
IMGO-DELISTED (Imago Biosciences) Start Date:2021-07-16
IMPX-DELISTED (Aea-Bridges Impact Class A Ordinary Shares) Start Date:2020-12-15
IMVIQ-DELISTED (Imv Inc) Start Date:2018-06-01
INFO-DELISTED (Ihs Markit Ltd.) Start Date:2014-06-19
INOV-DELISTED (Inovalon Holdings) Start Date:2015-02-12
INS-DELISTED (Intelligent Systems) Start Date:2007-05-18
IPVI-DELISTED (Interprivate Iv Infratech Partners Class A) Start Date:2021-04-30
IRCP-DELISTED (Irsa Propiedades Comerciales S.A. American Depositary Shares) Start Date:2020-11-23
IRNT-DELISTED (Ironnet) Start Date:2020-03-23
ISAA-DELISTED (Iron Spark I Class A) Start Date:2021-06-09
ISBC-DELISTED (Investors Bancorp) Start Date:2007-01-03
IS-DELISTED (Ironsource Ltd.) Start Date:2021-06-29
ISEE-DELISTED (Iveric Bio) Start Date:2013-09-25
ISO-DELISTED (Isoplexis) Start Date:2021-10-08
IVCRQ-DELISTED (Invacare Corp) Start Date:2007-05-03
JCOM-DELISTED (J2 Global) Start Date:2007-01-03
JEC-DELISTED (Jacobs Engineering) Start Date:2004-01-02
JNCE-DELISTED (Jounce Therapeutics) Start Date:2017-01-27
JNS-DELISTED (Janus Capital Cmn S) Start Date:2004-01-02
JNY-DELISTED (Jones) Start Date:2004-01-02
JOBS-DELISTED (51Job American Depositary Shares) Start Date:2007-04-18
JOY-DELISTED (Joy Global) Start Date:2007-04-30
JOYG-DELISTED () Start Date:2004-01-02
JP-DELISTED (Jefferson-Pilot) Start Date:2015-07-16
JW.A-DELISTED (John Wiley & Sons) Start Date:2007-05-01
KALRQ-DELISTED (Kalera Public Co.) Start Date:2022-06-29
KBAL-DELISTED (Kimball International Cl) Start Date:2007-04-25
KDMN-DELISTED (Kadmon) Start Date:2016-07-27
KDNY-DELISTED (Chinook Therapeutics,) Start Date:2015-04-15
KFT-DELISTED (Kraft Foods) Start Date:2004-01-02
KIN-DELISTED (Kindred Biosciences Comm) Start Date:2013-12-12
KL-DELISTED (Kirkland Lake Gold Ltd.) Start Date:2017-08-16
KNL-DELISTED (Knoll) Start Date:2007-05-04
KOR-DELISTED (Corvus Gold Common Shares) Start Date:2010-09-02
KORS-DELISTED (Michael Kors Holdings O) Start Date:2011-12-15
KRA-DELISTED (Kraton Corp) Start Date:2009-12-17
KRFT-DELISTED (Kraft Foods) Start Date:2012-09-17
KSICW-DELISTED (Kadem Sustainable Impact Warrant) Start Date:2021-05-17
KSI-DELISTED (Kadem Sustainable Impact Class A) Start Date:2021-05-18
KSPN-DELISTED (Kaspien Holdings) Start Date:2007-05-04
KSU-DELISTED (Kansas City Southern) Start Date:2005-01-03
LAWS-DELISTED (Lawson Products) Start Date:2007-05-16
LB-DELISTED (L Brands) Start Date:2007-04-27
LBPSW-DELISTED (4D Pharma Plc Warrant) Start Date:2021-03-23
LDHA-DELISTED (Ldh Growth I Class A Ordinary Shares) Start Date:2021-05-13
LDL-DELISTED (Lydall) Start Date:2007-05-11
LEAP-DELISTED (Ribbit Leap) Start Date:2020-11-02
LEGA-DELISTED (Lead Edge Growth Opportunities Class A Ordinary Shares) Start Date:2021-05-26
LEH-DELISTED (Lehman Brothers) Start Date:2004-01-02
LEVL-DELISTED (Level One Bancorp) Start Date:2018-04-20
LFG-DELISTED (Archaea Energy) Start Date:2020-12-14
LHCG-DELISTED (Lhc) Start Date:2007-01-03
LITT-DELISTED (Logistics Innovation Technologies Class A) Start Date:2021-08-12
LIVX-DELISTED (Livexlive Media) Start Date:2017-12-14
LIZ-DELISTED (Liz Claiborne) Start Date:2004-01-02
LJPC-DELISTED (La Jolla Pharmaceutical Compan) Start Date:2007-05-14
LLL-DELISTED (L-3 Communications Holdings) Start Date:2007-04-30
LLNW-DELISTED (Limelight Networks) Start Date:2007-06-08
LLTC-DELISTED (Linear Technology Corporation) Start Date:2004-01-02
LMCA-DELISTED (Liberty Media Corporation) Start Date:2013-02-01
LMCK-DELISTED () Start Date:2014-08-08
LMNX-DELISTED (Luminex) Start Date:2007-04-25
LMST-DELISTED (Limestone Bancorp) Start Date:2007-05-16
LO-DELISTED (Lorillard Inc) Start Date:2008-06-10
LOGC-DELISTED (Logicbio Therapeutics) Start Date:2018-10-19
LORL-DELISTED (Loral Space) Start Date:2007-05-07
LOTZ-DELISTED (Carlotz Class A) Start Date:2019-05-09
LSI-DELISTED (Life Storage) Start Date:2016-08-15
LTCH-DELISTED (Latch,) Start Date:2020-12-31
LUK-DELISTED (Leucadia National C) Start Date:2004-01-02
LVLT-DELISTED (Level 3 Communications Co) Start Date:2004-01-02
LVNTA-DELISTED (Liberty Ventures) Start Date:2012-08-10
LVRA-DELISTED (Levere Holdings) Start Date:2021-05-14
LXK-DELISTED (Lexmark International Com) Start Date:2004-01-02
MACC-DELISTED (Mission Advancement) Start Date:2021-04-28
MANT-DELISTED (Mantech International) Start Date:2007-05-01
MBII-DELISTED (Marrone Bio Innovations) Start Date:2013-08-02
MBT-DELISTED (Mobile Telesystems Public Joint Stock Company) Start Date:2007-01-03
MCF-DELISTED (Contango Oil & Gas) Start Date:2007-05-11
MCFE-DELISTED (Mcafee) Start Date:2020-11-02
MDLA-DELISTED (Medallia) Start Date:2019-07-19
MDP-DELISTED (Meredith Corporation) Start Date:2005-01-03
MEKA-DELISTED (Meli Kaszek Pioneer Class A Ordinary Shares) Start Date:2021-09-29
MFCB-DELISTED () Start Date:2007-05-01
MFGP-DELISTED (Softwareinto Micro Focus) Start Date:2017-09-01
MFNC-DELISTED (Mackinac Financial) Start Date:2007-05-16
MGHL-DELISTED (Morgan Holding) Start Date:2007-05-16
MGI-DELISTED (Moneygram International) Start Date:2007-04-26
MGLN-DELISTED (Magellan Health) Start Date:2007-05-02
MGP-DELISTED (Mgm Growth Properties Llc) Start Date:2016-04-20
MHS-DELISTED (Medcohealth Solutions Inc Commo) Start Date:2004-01-02
MIC-DELISTED (Macquarie Infrastructure Corporation) Start Date:2007-01-03
MILE-DELISTED (Metromile,) Start Date:2020-11-09
MILEW-DELISTED (Metromile Warrant) Start Date:2020-11-20
MIME-DELISTED (Mimecast Limited) Start Date:2015-11-19
MITC-DELISTED (Meatech 3D American Depositary Shares) Start Date:2021-03-12
MIT-DELISTED (Mason Industrial Technology,) Start Date:2021-03-22
MITO-DELISTED (Stealth Biotherapeutics ADS) Start Date:2019-02-15
MJN-DELISTED (Mead Johnson Nutrition Company) Start Date:2009-02-11
MLHR-DELISTED (Herman Miller) Start Date:2007-04-30
MLVF-DELISTED (Malvern Bancorp) Start Date:2008-05-20
MMAC-DELISTED (Mma Capital Management Co) Start Date:2008-02-06
MMX-DELISTED (Maverix Metals Common Shares) Start Date:2019-06-25
MN-DELISTED (Manning & Napier Class A) Start Date:2011-11-18
MNDT-DELISTED (Mandiant,) Start Date:2013-09-20
MNR-DELISTED (Monmouth Real Estate) Start Date:2007-05-16
MNRL-DELISTED (Brigham Minerals) Start Date:2019-04-18
MNTV-DELISTED (Momentive Global) Start Date:2018-09-26
MOLX-DELISTED (Molex Incorporated) Start Date:2005-03-24
MON-DELISTED (Monsanto Company) Start Date:2004-01-02
MRLN-DELISTED (Marlin Business Services) Start Date:2007-05-11
MSGN-DELISTED (The Madison Square Garden Company) Start Date:2010-02-10
MSON-DELISTED (Misonix) Start Date:2007-05-16
MSP-DELISTED (Datto Holding) Start Date:2020-11-02
MSVB-DELISTED (Mid-Southern Bancorp) Start Date:2018-07-12
MTCR-DELISTED (Metacrine) Start Date:2020-09-16
MTOR-DELISTED (Meritor) Start Date:2007-04-30
MTVC-DELISTED (Motive Capital Ii Class A Ordinary Shares) Start Date:2022-01-27
MWV-DELISTED (Meadwestvaco Common) Start Date:2004-01-02
MWW-DELISTED (Monster Worldwide Common) Start Date:2007-04-27
MXIM-DELISTED (Maxim Integrated Products Inc) Start Date:2007-04-27
MYOV-DELISTED (Myovant Sciences Ltd.) Start Date:2016-10-27
NAKD-DELISTED (Naked Brand Ordinary Shares) Start Date:2018-06-20
NAV-DELISTED (Navistar International Corporation) Start Date:2008-06-30
NCBS-DELISTED (Nicolet Bankshares) Start Date:2013-05-17
NCR-DELISTED (Ncr Corporation) Start Date:2007-01-03
NESR-DELISTED (National Energy Services Reunited Ordinary S) Start Date:2017-06-05
NFH-DELISTED (New Frontier Health Ordinary Shares) Start Date:2018-06-28
NFX-DELISTED (Newfield Exploration Company Co) Start Date:2004-01-02
NHIC-DELISTED (Newhold Investment Ii Class A) Start Date:2021-12-28
NHIQ-DELISTED (Nanthealth Inc) Start Date:2016-06-02
NIHD-DELISTED (Nii Holdings) Start Date:2007-04-26
NLSN-DELISTED (Nielsen Holdings) Start Date:2015-08-31
NP-DELISTED (Neenah) Start Date:2007-04-25
NPTN-DELISTED (Neophotonics) Start Date:2011-02-02
NRZ-DELISTED (New Residential Investment) Start Date:2013-05-02
NSEC-DELISTED (National Security) Start Date:2007-05-16
NSM-DELISTED (National Semiconductor Corp) Start Date:2007-04-25
NSR-DELISTED (Nomad Royalty Company Common Shares) Start Date:2021-08-31
NTP-DELISTED (Nam Tai Property) Start Date:2007-05-04
NTUS-DELISTED (Natus Medical) Start Date:2007-05-09
NU (Northeast Utilities Common Stoc) Start Date:2021-12-09
NUAN-DELISTED (Nuance Communications) Start Date:2007-01-03
NUBIW-DELISTED (Nubia Brand International Warrant) Start Date:2022-05-02
NVCN-DELISTED (Neovasc Common Shares) Start Date:2008-12-22
NYX-DELISTED (Nyse Euronext) Start Date:2006-03-08
OAS-DELISTED (Oasis Petroleum) Start Date:2020-11-20
OBCI-DELISTED (Ocean Bio-Chem) Start Date:2007-04-13
OCDX-DELISTED (Ortho Clinical Diagnostics Plc) Start Date:2021-01-28
ODT-DELISTED (Odonate Therapeutics) Start Date:2017-12-07
OEG-DELISTED (Orbital Energy) Start Date:2008-01-07
OEPW-DELISTED (One Equity Partners Open Water I Class A) Start Date:2021-03-18
OFED-DELISTED (Oconee Federal Financial) Start Date:2011-01-14
OGBLY-DELISTED (Onion Global Ltd.) Start Date:2021-05-07
OIIM-DELISTED (O2micro International American Depositary Shares) Start Date:2007-05-03
OMP-DELISTED (Oasis Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2017-09-21
ONCR-DELISTED (Oncorus) Start Date:2020-10-02
ONE-DELISTED (Bank One) Start Date:2018-03-28
ONEM-DELISTED (1Life Healthcare) Start Date:2020-01-31
ONNN-DELISTED (On Semiconductor) Start Date:2004-01-02
OPNT-DELISTED (Opiant Pharmaceuticals) Start Date:2009-12-02
ORBC-DELISTED (Orbcomm) Start Date:2007-05-07
ORIA-DELISTED (Orion Biotech Opportunities Class A Ordinary Share) Start Date:2021-07-13
ORPH-DELISTED (Orphazyme A/S) Start Date:2020-09-29
OSH-DELISTED (Oak Street Health) Start Date:2020-08-06
OSMT-DELISTED (Osmotica Pharmaceuticals) Start Date:2018-10-18
OTIC-DELISTED (Otonomy) Start Date:2014-08-13
OYST-DELISTED (Oyster Point Pharma) Start Date:2019-10-31
OZON-DELISTED (Ozon Plc) Start Date:2020-11-24
OZRK-DELISTED (Bank Ozk) Start Date:2004-01-02
PAE-DELISTED (Pae) Start Date:2018-09-07
PAYA-DELISTED (Paya Holdings Class A) Start Date:2020-10-19
PBCT-DELISTED (People's United Financial) Start Date:2007-03-29
PBCTP-DELISTED (People's United Financial Perpetual Preferred Series A Fixed-To-Floating Rate) Start Date:2016-11-29
PBFX-DELISTED (Pbf Logistics Lp) Start Date:2014-05-09
PBIP-DELISTED (Prudential Bancorp Commo) Start Date:2007-05-16
PCGU-DELISTED (Pacific Gas & Electric Co. Equity Unit) Start Date:2020-07-07
PCI-DELISTED (Pimco Dynamic Credit And Mortgage Income Fund) Start Date:2013-01-29
PCL-DELISTED (Plum Creek Timber Company) Start Date:2004-01-02
PCLN-DELISTED (The Priceline) Start Date:2004-01-02
PCOM-DELISTED (Points.com Common Shares) Start Date:2007-05-16
PCPC-DELISTED (Periphas Capital Partnering Class A) Start Date:2021-02-02
PCP-DELISTED (Precision Castparts Corporation) Start Date:2004-01-02
PCSB-DELISTED (Pcsb Financial) Start Date:2017-04-21
PDCE-DELISTED (Pdc Energy) Start Date:2007-04-27
PETM-DELISTED (Petsmart Inc) Start Date:2004-01-02
PFBI-DELISTED (Premier Financial) Start Date:2007-05-17
PFHD-DELISTED (Professional Hldg Corp) Start Date:2017-03-15
PFPT-DELISTED (Proofpoint) Start Date:2012-04-20
PGN-DELISTED (Progress Energy Common St) Start Date:2014-09-02
PHIC-DELISTED (Population Health Investment Co. Class A Ordinary Share) Start Date:2021-01-12
PICC-DELISTED (Pivotal Investment Iii Class A) Start Date:2021-04-01
PING-DELISTED (Ping Identity Holding) Start Date:2019-09-19
PLAN-DELISTED (Anaplan) Start Date:2018-10-12
PME-DELISTED (Pingtan Marine Enterprise Ltd.) Start Date:2013-02-26
PMTC-DELISTED (Parametric Technology) Start Date:2006-05-01
PNTM-DELISTED (Pontem) Start Date:2021-03-05
POLY-DELISTED (Plantronics,) Start Date:2021-05-24
POM-DELISTED (Pepco Holdings Inc) Start Date:2004-01-02
POSH-DELISTED (Poshmark) Start Date:2021-01-14
POW-DELISTED (Powered Brands) Start Date:2021-03-04
PPD-DELISTED (Ppd) Start Date:2020-02-06
PPDI-DELISTED (Pharmaceutical Product Development Inc) Start Date:2004-01-02
PPGH-DELISTED (Poema Global) Start Date:2021-03-01
PQG-DELISTED (Pq) Start Date:2017-09-29
PRAH-DELISTED (Pra Health Sciences Comm) Start Date:2014-11-13
PROG-DELISTED (Progenity) Start Date:2020-06-19
PROS-DELISTED (Prosight Global) Start Date:2019-07-25
PRPB-DELISTED (Cc Neuberger Principal Holdings Ii Class A Ordinary Shares) Start Date:2020-09-21
PRVB-DELISTED (Provention Bio) Start Date:2018-07-24
PSB-DELISTED (Ps Business Parks) Start Date:2007-05-03
PSFT-DELISTED (People Soft) Start Date:2008-10-07
PSPC-DELISTED (Post Holdings Partnering) Start Date:2021-07-16
PSTH-DELISTED (Pershing Square Tontine Holdings, Ltd.) Start Date:2020-09-11
PSTI-DELISTED (Pluristem Therapeutics) Start Date:2007-12-10
PSXP-DELISTED (Phillips 66 Partners Lp) Start Date:2013-07-23
PTEIQ-DELISTED (Polarityte Inc) Start Date:2007-05-16
PVAC-DELISTED (Penn Virginia) Start Date:2016-11-15
PVG-DELISTED (Pretium Resources) Start Date:2010-12-16
PWPPW-DELISTED (Perella Weinberg Partners Warrant) Start Date:2020-11-20
PX-DELISTED (Praxair) Start Date:2004-01-02
PZN-DELISTED (Pzena Investment) Start Date:2007-10-25
QADA-DELISTED (Qad) Start Date:2010-12-16
Q-DELISTED (Qwest Communications International Inc) Start Date:2013-06-03
QK-DELISTED (Q&K International American Depositary Shares) Start Date:2019-11-05
QLGC-DELISTED (Qlogic Corporation) Start Date:2004-01-02
QTS-DELISTED (Qts Realty Trust) Start Date:2013-10-09
QTT-DELISTED (Qutoutiao American Depositary Shares) Start Date:2018-09-14
QUMU-DELISTED (Qumu) Start Date:2007-05-16
QVCA-DELISTED (Liberty Interactive Corporation) Start Date:2007-04-26
RACB-DELISTED (Research Alliance Ii Class A) Start Date:2021-03-18
RADA-DELISTED (Rada Electronic Industries) Start Date:2007-05-16
RAI-DELISTED (Reynolds American Inc Common St) Start Date:2004-08-02
RAVN-DELISTED (Raven Industries) Start Date:2007-04-30
RBC-DELISTED (Regal Beloit Corporation) Start Date:2007-01-03
RBCN-DELISTED (Rubicon Technology) Start Date:2007-11-16
RBNC-DELISTED (Reliant Bancorp) Start Date:2009-10-30
RCOR-DELISTED (Renovacor) Start Date:2021-09-03
RDBX-DELISTED (Redbox Entertainment Class A) Start Date:2020-12-10
RDBXW-DELISTED (Redbox Entertainment Warrant) Start Date:2021-10-25
RDC-DELISTED (Rowan Companies Common St) Start Date:2004-01-02
RDUS-DELISTED (Radius Health O) Start Date:2014-06-06
REED-DELISTED (Reeds) Start Date:2007-05-16
REGI-DELISTED (Renewable Energy) Start Date:2012-01-19
REPH-DELISTED (Recro Pharma) Start Date:2014-03-07
RESN-DELISTED (Resonant) Start Date:2014-05-29
REUN-DELISTED (Reunion Neuroscience) Start Date:2021-07-29
REVRQ-DELISTED (Revlon Inc) Start Date:2008-09-16
RFP-DELISTED (Resolute Forest Products) Start Date:2008-03-03
RHT-DELISTED (Red Hat) Start Date:2007-05-14
RKTA-DELISTED (Rocket Internet Growth Opportunities Class A Ordinary Shares) Start Date:2021-05-13
RLGY-DELISTED (Realogy Holdings) Start Date:2012-10-11
RMO-DELISTED (Romeo Power,) Start Date:2019-04-01
RNDB-DELISTED (Randolph Bancorp) Start Date:2016-07-01
RNWK-DELISTED (Realnetworks) Start Date:2007-04-26
ROCC-DELISTED (Ranger Oil Class A) Start Date:2021-01-05
ROLL-DELISTED (Rbc Bearings) Start Date:2007-05-04
RPAI-DELISTED (Retail Properties) Start Date:2012-04-05
RRD-DELISTED (R.R. Donnelley & Sons Company) Start Date:2005-01-03
RSH-DELISTED (Radioshack Common S) Start Date:2004-01-02
RTLR-DELISTED (Rattler Midstream Lp Common Units) Start Date:2019-05-23
RTP-DELISTED (Reinvent Technology Partners) Start Date:2020-11-09
RTPY-DELISTED (Reinvent Technology Partners Y) Start Date:2021-05-10
RUBY-DELISTED (Rubius Therapeutics) Start Date:2018-07-18
RUTH-DELISTED (Ruth's Hospitality) Start Date:2007-05-02
RVI-DELISTED (Retail Value) Start Date:2018-06-26
RXDX-DELISTED (Prometheus Biosciences) Start Date:2021-03-12
RXN-DELISTED (Rexnord Corporation) Start Date:2012-03-29
RZA-DELISTED (Reinsurance Of America Incorporated 6.20% Fixed-To-Floating Rate Subordinated Debentures Due 2042) Start Date:2013-02-11
SAF-DELISTED (Safeco) Start Date:2008-03-03
SAFM-DELISTED (Sanderson Farms) Start Date:2007-05-01
SAL-DELISTED (Salisbury Bancorp Common) Start Date:2007-05-16
SBBP-DELISTED (Strongbridge Biopharma) Start Date:2015-10-16
SBII-DELISTED (Sandbridge X2) Start Date:2021-04-30
SBNY-DELISTED (Signature Bank) Start Date:2007-05-04
SC-DELISTED (Santander Consumer Usa Holding) Start Date:2014-01-23
SCG-DELISTED (Scana) Start Date:2004-01-02
SCOA-DELISTED (Scion Tech Growth I) Start Date:2021-02-08
SCOB-DELISTED (Scion Tech Growth Ii Class A Ordinary Shares) Start Date:2021-04-06
SCPS-DELISTED (Scopus Biopharma) Start Date:2020-12-16
SCR-DELISTED (Score Media & Gaming) Start Date:2014-01-10
SCVX-DELISTED (Scvx) Start Date:2020-03-20
SDH-DELISTED (Global Internet Of People Ordinary Shares) Start Date:2021-02-09
SEVCQ-DELISTED (Sono Nv) Start Date:2021-11-17
SGFY-DELISTED (Signify Health) Start Date:2021-02-11
SGMS-DELISTED (Scientific Games) Start Date:2007-05-02
SGP-DELISTED (Merck & Co/Inc) Start Date:2004-01-02
SGTX-DELISTED (Sigilon Therapeutics) Start Date:2020-12-04
SHLX-DELISTED (Shell Midstream Partners L.P.) Start Date:2014-10-29
SIAL-DELISTED (Sigma-Aldrich Corporation) Start Date:2004-01-02
SICP-DELISTED (Silvergate Capital Corp) Start Date:2019-11-07
SIOX-DELISTED (Sio Gene Therapies) Start Date:2015-06-11
SIRE-DELISTED (Sisecam Resources Lp Common Units Representing Partner Interests) Start Date:2022-03-01
SIVB-DELISTED (Svb Financial) Start Date:2006-03-01
SJI-DELISTED (South Jersey Industries) Start Date:2007-01-03
SJIV-DELISTED (South Jersey Industries Corporate Units) Start Date:2021-03-25
SJR-DELISTED (Shaw Communications) Start Date:2007-01-03
SLCT-DELISTED (Select Bancorp) Start Date:2007-05-16
SLHG-DELISTED (Skylight Health  Ordinary Shares) Start Date:2021-06-07
SLR-DELISTED (Solectron) Start Date:2004-01-02
SMED-DELISTED (Sharps Compliance) Start Date:2009-05-06
SMIT-DELISTED (Schmitt Industries) Start Date:2007-05-16
SMM-DELISTED (Salient Midstream Common Shares Of Beneficial Interest) Start Date:2012-05-25
SNDK-DELISTED (Sandisk) Start Date:2004-01-02
SNI-DELISTED (Scripps Networks Interactive I) Start Date:2008-07-01
SNR-DELISTED (New Senior Investment  I) Start Date:2014-11-07
SOLN-DELISTED (The Southern Company) Start Date:2019-08-21
SOLY-DELISTED (Soliton) Start Date:2019-02-19
SPKE-DELISTED (Spark Energy  Com) Start Date:2014-07-29
SPNE-DELISTED (Seaspine) Start Date:2015-06-17
SPPI-DELISTED (Spectrum Pharmaceuticals) Start Date:2007-05-07
SQZB-DELISTED (Sqz Biotechnologies Co.) Start Date:2020-11-02
SRAX-DELISTED (Srax Class A) Start Date:2016-10-13
SREV-DELISTED (Servicesource) Start Date:2011-03-25
SRLP-DELISTED (Sprague Resources Lp Common Units Representing Partner Interests) Start Date:2013-10-25
SRRA-DELISTED (Sierra Oncology) Start Date:2015-07-16
SSS-DELISTED (Sovran Self Storage) Start Date:2004-01-02
STAB-DELISTED (Statera Biopharma) Start Date:2007-05-16
STET-DELISTED (St Energy Transition I Class A Ordinary Shares) Start Date:2022-01-24
STFC-DELISTED (State Auto Financial) Start Date:2007-05-02
STI-DELISTED (Suntrust Banks) Start Date:2004-01-02
STJ-DELISTED (St. Jude Medical Common S) Start Date:2004-01-02
STL-DELISTED (Sterling Bancorp) Start Date:2007-01-03
STMP-DELISTED (Stamps.com) Start Date:2007-01-03
STON-DELISTED (Stonemor) Start Date:2007-05-16
STOR-DELISTED (Store Capital Corporation) Start Date:2014-11-18
STR-DELISTED (Questar Common Stoc) Start Date:2004-01-02
STSA-DELISTED (Satsuma Pharmaceuticals) Start Date:2019-09-13
STXB-DELISTED (Spirit Of Texas Bancshares) Start Date:2018-05-04
STZ.B-DELISTED (Constellation Brands Inc) Start Date:2007-05-16
SUMO-DELISTED (Sumo Logic) Start Date:2020-09-17
SUNE-DELISTED () Start Date:2013-06-03
SVA-DELISTED (Sinovac Biotech, Ltd) Start Date:2007-04-26
SVFA-DELISTED (Svf Investment Class A Ordinary Shares) Start Date:2021-01-27
SVFB-DELISTED (Svf Investment 2 Class A Ordinary Shares) Start Date:2021-03-09
SVU-DELISTED (Supervalu) Start Date:2004-01-02
SWCH-DELISTED (Switch) Start Date:2017-10-06
SWIR-DELISTED (Sierra Wireless) Start Date:2007-05-09
SWM-DELISTED (Schweitzer-Mauduit Intl) Start Date:2007-05-02
SWT-DELISTED (Stanley Black & Decker Corporate Unit) Start Date:2019-11-14
SWY-DELISTED (Safeway) Start Date:2004-01-02
SYKE-DELISTED (Sykes Enterprises) Start Date:2007-04-30
SYMC-DELISTED (Symantec) Start Date:2018-01-02
SYNL-DELISTED (Synalloy) Start Date:2007-05-16
TACO-DELISTED (Levy Acquisition) Start Date:2014-01-08
TA-DELISTED (Travelcenters Of America Llc) Start Date:2007-05-16
TBIO-DELISTED (Translate Bio) Start Date:2018-06-28
TCFC-DELISTED (The Community Financial Corpor) Start Date:2007-06-04
TCRR-DELISTED (Tcr2 Therapeutics) Start Date:2019-02-14
TE-DELISTED (Teco Energy) Start Date:2004-01-02
TEG-DELISTED (Integrys Energy Com) Start Date:2007-02-22
TEN-DELISTED (Tenneco) Start Date:2007-05-01
TESS-DELISTED (Tessco Technologies Incorporated) Start Date:2007-05-16
TETC-DELISTED (Tech & Energy Transition) Start Date:2021-05-20
TGA-DELISTED (Transglobe Energy Ordinary Shares) Start Date:2007-04-27
TGP-DELISTED (Teekay Lng Partners L.P.) Start Date:2007-05-16
THCA-DELISTED (Tuscan Holdings Ii) Start Date:2019-07-30
THCAU-DELISTED (Tuscan Holdings Ii Unit) Start Date:2019-07-12
TIE-DELISTED (Titanium Metals Com) Start Date:2004-01-02
TIG-DELISTED (Trean Insurance ,) Start Date:2020-07-16
TIOA-DELISTED (Tio Tech A) Start Date:2021-06-10
TLAB-DELISTED (Tellabs) Start Date:2004-01-02
TLMD-DELISTED (Soc Telemed, Class A) Start Date:2020-01-28
TMK-DELISTED (Torchmark) Start Date:2004-01-02
TMX-DELISTED (Terminix Global Holdings,) Start Date:2014-06-26
TPGS-DELISTED (Tpg Pace Solutions) Start Date:2021-04-09
TPGY-DELISTED (Tpg Pace Beneficial Finance) Start Date:2020-12-15
TPTX-DELISTED (Turning Point Therapeutics) Start Date:2019-04-17
TREC-DELISTED (Trecora Resources) Start Date:2007-05-16
TRIL-DELISTED (Trillium Therapeutics) Start Date:2014-12-19
TRQ-DELISTED (Turquoise Hill Resources Ltd) Start Date:2007-05-02
TSC-DELISTED (Tristate Capital) Start Date:2013-05-09
TSG-DELISTED (Sabre Holdings) Start Date:2004-01-02
TSIB-DELISTED (Tishman Speyer Innovation Ii Class A) Start Date:2021-04-05
TSO-DELISTED (Tesoro) Start Date:2004-01-02
TSS-DELISTED (Total System Services) Start Date:2004-01-02
TTM-DELISTED (Tata Motors Limited) Start Date:2013-02-11
TUFN-DELISTED (Tufin Software Technologies Ordinary Shares) Start Date:2019-04-11
TUGC-DELISTED (Tradeup Global) Start Date:2021-06-28
TVTY-DELISTED (Tivity Health) Start Date:2007-04-30
TWC-DELISTED (Time Warner Cable Inc Common St) Start Date:2007-03-01
TWTR-DELISTED (Twitter) Start Date:2013-11-07
TWX-DELISTED (Time Warner New Common Sto) Start Date:2004-01-02
TYME-DELISTED (Tyme Technologies) Start Date:2015-03-12
UBA-DELISTED (Urstadt Biddle Properties) Start Date:2007-05-07
UBP-DELISTED (Urstadt Biddle Properties) Start Date:2013-02-11
UFS-DELISTED (Domtar) Start Date:2007-05-16
UMPQ-DELISTED (Umpqua Holdings Corporation) Start Date:2007-01-03
UNVR-DELISTED (Univar Solutions) Start Date:2015-06-18
USAK-DELISTED (Usa Truck) Start Date:2007-04-30
USCR-DELISTED (Us Concrete) Start Date:2010-10-15
USER-DELISTED (Usertesting) Start Date:2021-11-17
USWS-DELISTED (U.S. Well Services Class A) Start Date:2017-05-05
USX-DELISTED (Us Xpress Enterprises) Start Date:2018-06-14
VCRA-DELISTED (Vocera Communications) Start Date:2012-03-28
VEC-DELISTED (Vectrus) Start Date:2014-09-29
VECT-DELISTED (Vectivbio Holding) Start Date:2021-04-09
VEDL-DELISTED (Vedanta Limited) Start Date:2013-09-09
VEI-DELISTED (Vine Energy) Start Date:2021-03-18
VER-DELISTED (Vereit) Start Date:2011-09-07
VG-DELISTED (Vonage Holdings) Start Date:2007-01-03
VIAB-DELISTED (Viacom) Start Date:2007-04-30
VIACA-DELISTED (Viacomcbs) Start Date:2019-12-05
VIAC-DELISTED (Viacomcbs) Start Date:2007-04-30
VIA-DELISTED (Viacom Inc) Start Date:2004-01-02
VIP-DELISTED (Vimpelcom Ltd.) Start Date:2004-01-02
VIVE-DELISTED (Viveve Medical) Start Date:2016-06-14
VIVO-DELISTED (Meridian Bioscience) Start Date:2007-05-04
VLDR-DELISTED (Velodyne Lidar,) Start Date:2018-10-26
VLNS-DELISTED (The Valens Company Common Shares) Start Date:2021-12-09
VLTA-DELISTED (Volta) Start Date:2020-11-02
VMED-DELISTED (Virgin Media) Start Date:2007-02-08
VNE-DELISTED (Veoneer) Start Date:2018-06-11
VRS-DELISTED (Verso Corp) Start Date:2016-07-19
VVNT-DELISTED (Vivint Smart Home) Start Date:2017-10-19
VYGG-DELISTED (Vy Global Growth) Start Date:2020-12-15
VYNT-DELISTED (Vyant Bio) Start Date:2013-04-10
WBT-DELISTED (Welbilt) Start Date:2016-02-18
WCG-DELISTED (Wellcare) Start Date:2004-07-01
WCRX-DELISTED (Warner Chilcott Plc) Start Date:2006-09-21
WEBR-DELISTED (Weber) Start Date:2021-08-05
WEJWQ-DELISTED (Wejo Ltd.) Start Date:2021-11-19
WFM-DELISTED (Whole Foods Market) Start Date:2007-04-27
WIN-DELISTED (Windstream Corporation) Start Date:2006-07-18
WLL-DELISTED (Whiting Petroleum) Start Date:2020-09-02
WLTW-DELISTED (Willis Towers Watson) Start Date:2016-01-05
WORK-DELISTED (Slack Technologies) Start Date:2019-06-20
WPCA-DELISTED (Warburg Pincus Capital Ia Class A Ordinary Shares) Start Date:2021-04-26
WPCB-DELISTED (Warburg Pincus Capital Ib Class A Ordinary Shares) Start Date:2021-04-26
WRI-DELISTED (Weingarten Realty Investors) Start Date:2007-01-03
WSH-DELISTED (Willis Holdings) Start Date:2004-01-02
WSO.B-DELISTED (Watsco) Start Date:2007-05-16
WTRE-DELISTED (Watford  Common Shares) Start Date:2019-03-28
WTT-DELISTED (Wireless Telecom) Start Date:2007-05-16
WXS-DELISTED (Wex) Start Date:2005-03-01
WYN-DELISTED (Wyndham Worldwide Common) Start Date:2006-08-01
XEC-DELISTED (Cimarex Energy) Start Date:2005-01-03
XENT-DELISTED (Intersect Ent O) Start Date:2014-07-24
XL-DELISTED (Xl Plc) Start Date:2004-01-02
XLNX-DELISTED (Xilinx) Start Date:2005-01-03
XLRN-DELISTED (Acceleron Pharma) Start Date:2013-09-19
XM-DELISTED (Qualtrics International) Start Date:2021-01-28
XONE-DELISTED (The Exone Company) Start Date:2013-02-07
XPOA-DELISTED (Dpcm Capital Class A) Start Date:2020-12-15
Y-DELISTED (Yte) Start Date:2019-01-02
YHOO-DELISTED (Yahoo!) Start Date:2004-01-02
YNDX-DELISTED (Yandex N.V.) Start Date:2011-05-24
YTPG-DELISTED (Tpg Pace Beneficial Ii Class A Ordinary Shares) Start Date:2021-04-14
ZEAL-DELISTED (Zealand Pharma A/S American Depositary Shares) Start Date:2017-08-09
ZEN-DELISTED (Zendesk) Start Date:2014-05-15
ZGNX-DELISTED (Zogenix) Start Date:2010-11-23
ZIOP-DELISTED (Ziopharm Oncology) Start Date:2007-05-16
ZIXI-DELISTED (Zix) Start Date:2007-05-09
ZME-DELISTED (Zhangmen Education) Start Date:2021-06-08
ZNGA-DELISTED (Zynga) Start Date:2011-12-16
ZNHYY-DELISTED (China Southern Airlines Co Ltd.) Start Date:2013-02-11
ZVOI-DELISTED (Zovio Inc) Start Date:2009-04-15







ETF Tickers
---------------
A (Agilent Technologies Inc) Start Date:2005-01-03
AA (Alcoa Corporation) Start Date:2016-10-18
AACG (Ata Creativity Global American Depositary Shares) Start Date:2008-01-29
AACT (Ares Acquisition Ii) Start Date:2023-06-12
AADI (Aadi Bioscience) Start Date:2017-08-08
AAIC (Arlington Asset Investment Class A) Start Date:2009-06-10
AAL (American Airlines) Start Date:2013-12-09
AAMC (Altisource Asset Management Com) Start Date:2012-12-13
AAME (Atlantic American) Start Date:2007-05-16
AAN (Aaron's) Start Date:2020-12-01
AAOI (Applied Optoelectronics) Start Date:2013-09-26
AAON (Aaon) Start Date:2007-05-16
AAP (Advance Auto Parts) Start Date:2005-01-03
AAPL (Apple) Start Date:2005-01-03
AAT (American Assets Trust) Start Date:2011-01-13
AAU (Almaden Minerals Common Shares) Start Date:2007-05-16
AB (Alliancebernstein Holding L.P.) Start Date:2007-01-03
ABBNY (Abb Ltd.) Start Date:2007-05-01
ABBV (Abbvie) Start Date:2013-01-02
ABCB (Ameris Bancorp) Start Date:2007-05-16
ABCL (Abcellera Biologics) Start Date:2020-12-11
ABCM (Abcam Plc) Start Date:2020-11-02
ABEO (Abeona Therapeutics) Start Date:2007-05-16
ABEV (Ambev S.A. American Depositary Shares) Start Date:2013-11-11
ABG (Asbury Automotive) Start Date:2007-05-01
ABIO (Arca Biopharma) Start Date:2009-01-28
ABLV (Able View Global Inc) Start Date:2022-09-12
ABM (Abm Industries Incorporated) Start Date:2007-01-03
ABNB (Airbnb) Start Date:2020-12-10
ABOS (Acumen Pharmaceuticals) Start Date:2021-07-01
ABR (Arbor Realty Trust) Start Date:2007-05-02
ABSI (Absci) Start Date:2021-07-22
ABT (Abbott Laboratories) Start Date:2005-01-03
ABTS (Abits Inc) Start Date:2014-04-10
ABUS (Arbutus Biopharma) Start Date:2010-11-15
ABVC (Abvc Biopharma) Start Date:2021-08-03
AC (Associated Capital) Start Date:2015-11-09
ACA (Arcosa) Start Date:2018-10-30
ACAC (Acri Capital Acquisition Corporation) Start Date:2022-08-08
ACAD (Acadia Pharmaceuticals) Start Date:2007-01-03
ACAX (Alset Capital Acquisition) Start Date:2022-03-24
ACB (Aurora Cannabis Common Shares) Start Date:2018-10-23
ACCD (Accolade) Start Date:2020-07-02
ACCO (Acco Brands) Start Date:2007-05-02
ACDC (Profrac Holding) Start Date:2022-05-13
ACEL (Accel Entertainment) Start Date:2017-08-24
ACER (Acer Therapeutics) Start Date:2007-05-16
ACET (Adicet Bio) Start Date:2018-01-26
ACGL (Arch Capital Ltd.) Start Date:2007-01-03
ACGN (Aceragen Inc) Start Date:2007-12-10
ACHC (Acadia Healthcare Company) Start Date:2012-01-11
ACHL (Achilles Therapeutics Plc) Start Date:2021-03-31
ACHR (Archer Aviation) Start Date:2020-12-18
ACHV (Achieve Life Sciences Common Shares) Start Date:2008-08-22
ACI (Albertsons Companies) Start Date:2020-06-26
ACIC (American Coastal Insurance Corp) Start Date:2008-10-28
ACIU (Ac Immune Sa) Start Date:2016-09-23
ACIW (Aci Worldwide) Start Date:2007-07-25
ACLS (Axcelis Technologies) Start Date:2007-05-01
ACLX (Arcellx) Start Date:2022-02-04
ACM (Aecom) Start Date:2007-05-10
ACMR (Acm Research, Class A) Start Date:2017-11-03
ACN (Accenture Plc) Start Date:2009-09-01
ACNB (Acnb) Start Date:2007-05-16
ACNT (Ascent Industries) Start Date:2007-05-16
ACON (Aclarion) Start Date:2022-04-22
ACONW (Aclarion Warrant) Start Date:2022-04-22
ACOR (Acorda Therapeutics) Start Date:2007-04-25
ACP (Aberdeen Income Credit Strategies Fund Common Shares) Start Date:2011-01-27
ACQRU (Independence Holdings Units) Start Date:2021-03-09
ACQRW (Independence Holdings Warrant) Start Date:2021-05-17
ACR (Acres Commercial Realty) Start Date:2021-02-17
ACRE (Ares Commercial Real) Start Date:2012-04-26
ACRS (Aclaris Therapeutics,) Start Date:2015-10-07
ACRV (Acrivon Therapeutics) Start Date:2022-11-15
ACRX (Acelrx Pharmaceuticals) Start Date:2011-02-11
ACST (Acasti Pharma Class A) Start Date:2013-01-07
ACTG (Acacia Research) Start Date:2007-05-03
ACU (Acme United Corporation.) Start Date:2007-05-16
ACV (Alberto-Culver Co.) Start Date:2015-05-22
ACVA (Acv Auctions) Start Date:2021-03-24
ACXP (Acurx Pharmaceuticals) Start Date:2021-06-25
ADAG (Adagene) Start Date:2021-02-09
ADAP (Adaptimmune Therapeutics Plc American Depositary Shares) Start Date:2015-05-06
ADBE (Adobe Systems Inc) Start Date:2005-01-03
ADC (Agree Realty Corporation) Start Date:2007-01-03
ADD (Color Star Technology) Start Date:2008-06-16
ADEA (Adeia) Start Date:2007-04-26
ADES (Advanced Emissions Solutions) Start Date:2007-05-16
ADI (Analog Devices) Start Date:2005-01-03
ADIL (Adial Pharmaceuticals Inc) Start Date:2018-07-27
ADILW (Adial Pharmaceuticals Inc Warrant) Start Date:2018-07-27
ADM (Archer-Daniels-Midland Co) Start Date:2005-01-03
ADMA (Adma Biologics Cmn) Start Date:2013-10-17
ADN (Advent Technologies Holdings Class A) Start Date:2018-11-16
ADNT (Adient) Start Date:2016-10-17
ADNWW (Advent Technologies Holdings Warrant) Start Date:2019-01-24
ADP (Automatic Data Processing) Start Date:2005-01-03
ADPT (Adaptive Biotechnologies Corporation) Start Date:2019-06-27
ADRT (Ault Disruptive Technologies) Start Date:2022-02-09
ADSE (ADS-Tec Energy Plc Ordinary Shares) Start Date:2021-12-23
ADSEW (ADS-Tec Energy Plc Warrant) Start Date:2021-12-23
ADSK (Autodesk) Start Date:2005-01-03
ADT (Adt) Start Date:2018-01-19
ADTH (Adtheorent Holding Company) Start Date:2021-12-23
ADTHW (Adtheorent Holding Company Warrants) Start Date:2021-04-20
ADTN (Adtran) Start Date:2007-04-30
ADTX (Aditx Therapeutics) Start Date:2020-06-30
ADUS (Addus Homecare) Start Date:2009-10-28
ADV (Advantage Solutions Class A) Start Date:2019-09-09
ADVM (Adverum Biotechnologies) Start Date:2014-07-31
ADVWW (Advantage Solutions Warrant) Start Date:2016-09-15
ADX (Adams Diversified Equity Fund) Start Date:2007-05-08
ADXN (Addex Therapeutics American Depositary Shares) Start Date:2020-01-29
AE (Adams Resources) Start Date:2007-05-16
AEE (Ameren Corp) Start Date:2005-01-03
AEF (Aberdeen Emerging Markets Equity Income Fund) Start Date:2007-10-02
AEG (Aegon N.V.) Start Date:2007-01-03
AEHL (Antelope Enterprise Holdings) Start Date:2010-01-25
AEHR (Aehr Test Systems) Start Date:2007-05-16
AEI (Alset Ehome International) Start Date:2020-11-24
AEIS (Advanced Energy Inds) Start Date:2007-04-30
AEL (American Equity Investment Life Holding Company) Start Date:2007-01-03
AEM (Agnico Eagle Mines Limited) Start Date:2007-01-03
AEMD (Aethlon Medical) Start Date:2007-05-16
AENT (Bldrs Asia 50 ADR Index Fund) Start Date:2021-03-24
AENZ (Aenza S.A.A. American Depositary Shares) Start Date:2018-07-06
AEO (American Eagle Outfitters) Start Date:2007-03-08
AEP (American Electric Power) Start Date:2005-01-03
AEPPZ (American Electric Power Company Corporate Units) Start Date:2020-10-01
AER (Aercap Holdings N.V.) Start Date:2007-01-03
AES (Aes Corp) Start Date:2005-01-03
AESC (The Aes Corporate Units) Start Date:2021-03-15
AESE (Allied Esports Entertainment) Start Date:2017-10-25
AESI (Atlas Energy Solutions) Start Date:2023-03-09
AEVA (Aeva Technologies,) Start Date:2020-02-27
AEY (Addvantage Technologies) Start Date:2007-05-16
AEYE (Audioeye) Start Date:2018-09-04
AEZS (Aeterna Zentaris) Start Date:2007-05-17
AFAR (Aura Fat Projects Acquisition Corp) Start Date:2022-06-03
AFB (Alliancebernstein National Municipal Income Fund Inc) Start Date:2007-05-16
AFBI (Affinity Bancshares) Start Date:2020-07-23
AFCG (Afc Gamma) Start Date:2021-03-19
AFG (American Financial) Start Date:2007-01-03
AFGE (American Financial  4.500% Subordinated Debentures Due 2060) Start Date:2020-09-18
AFIB (Acutus Medical) Start Date:2020-08-06
AFL (Aflac Inc) Start Date:2005-01-03
AFMD (Affimed N.V.) Start Date:2014-09-12
AFRI (Forafric Global Plc Ordinary Shares) Start Date:2022-06-10
AFRIW (Forafric Global Plc Warrants) Start Date:2022-06-10
AFRM (Affirm) Start Date:2021-01-13
AFT (Apollo Senior Floating Rate Fund) Start Date:2011-02-24
AFYA (Afya Limited) Start Date:2019-07-19
AG (First Majestic Silver) Start Date:2010-12-15
AGAE (Allied Gaming & Entertainment) Start Date:2017-10-25
AGBA (Agba Holding) Start Date:2019-07-30
AGCO (Agco Corporation) Start Date:2009-05-04
AGD (Aberdeen Global Dynamic Dividend Fund) Start Date:2007-05-02
AGE (Agex Therapeutics) Start Date:2018-11-29
AGEN (Agenus) Start Date:2007-05-09
AGFY (Agrify) Start Date:2021-01-28
AGGRU (Agile Growth Units) Start Date:2021-03-10
AGGRW (Agile Growth Warrant.) Start Date:2021-05-05
AGI (Alamos Gold) Start Date:2015-07-06
AGIL (Agilethought Class A) Start Date:2020-01-14
AGILW (Agilethought Warrant) Start Date:2020-01-14
AGIO (Agios Pharmaceuticals) Start Date:2013-07-24
AGL (Agilon Health) Start Date:2021-04-15
AGM (Federal Agricultural Mortgage) Start Date:2007-05-04
AGMH (Agm Holdings Class A Ordinary Shares) Start Date:2018-04-18
AGNC (Agnc Investment) Start Date:2008-05-15
AGNCN (Agnc Investment Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 7.00% Series C Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2017-08-28
AGNCP (Agnc Investment Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 6.125% Series F Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2020-02-04
AGO (Assured Guaranty Ltd.) Start Date:2007-01-03
AGR (Avangrid) Start Date:2015-12-17
AGRI (Agriforce Growing Systems) Start Date:2021-07-08
AGRIW (Agriforce Growing Systems Warrant) Start Date:2021-07-08
AGRO (Adecoagro S.A.) Start Date:2011-01-28
AGRX (Agile Therapeutics Commo) Start Date:2014-05-23
AGS (Playags) Start Date:2018-01-26
AGTI (Agiliti) Start Date:2021-04-23
AGX (Argan) Start Date:2007-08-22
AGYS (Agilysys) Start Date:2007-05-03
AHCO (Adapthealth Corp) Start Date:2018-05-24
AHG (Akso Health ADS) Start Date:2017-11-03
AHH (Armada Hoffler Properties) Start Date:2013-08-05
AHI (Advanced Human Imaging Limited. American Depositary Shares) Start Date:2021-11-19
AHPI (Allied Healthcare Products) Start Date:2007-05-16
AHT (Ashford Hospitality Trust Inc) Start Date:2007-05-04
AI (C3 Ai) Start Date:2020-12-09
AIF (Apollo Tactical Income Fund) Start Date:2013-02-26
AIG (American International) Start Date:2005-01-03
AIH (Aesthetic Medical International Holdings American Depositary Shares) Start Date:2019-10-25
AIHS (Senmiao Technology) Start Date:2018-03-16
AIKI (Aikido Pharma) Start Date:2009-11-16
AIM (Aim Immunotech) Start Date:2007-05-07
AIMAU (Aimfinity Investment I) Start Date:2022-04-26
AIMAW (Aimfinity Investment I Warrant) Start Date:2022-06-17
AIMD (Ainos) Start Date:2007-05-16
AIN (Albany International) Start Date:2007-01-03
AINC (Ashford) Start Date:2014-11-07
AIO (Virtus Artificial Intelligence & Technology Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2019-10-29
AIP (Arteris) Start Date:2007-05-17
AIR (Aar) Start Date:2007-05-02
AIRC (Taxable Apartment Income Reit) Start Date:2020-12-15
AIRG (Airgain) Start Date:2016-08-12
AIRI (Air Industries) Start Date:2007-07-16
AIRS (Airsculpt Technologies) Start Date:2021-10-29
AIRT (Air T) Start Date:2007-05-16
AIRTP (Air T Air T Funding Alpha Income Trust Preferred Securities) Start Date:2019-06-11
AIT (Applied Industrial Technologies) Start Date:2007-01-03
AIU (Meta Data ADS) Start Date:2022-05-02
AIV (Apartment Investment & Management) Start Date:2009-07-21
AIXI (Xiao-I Corporation) Start Date:2023-03-09
AIZ (Assurant) Start Date:2005-01-03
AJG (Arthur J. Gallagher & Co.) Start Date:2005-01-03
AJX (Great Ajax Corp) Start Date:2015-02-13
AKA (A.K.A. Brands Holding) Start Date:2021-09-22
AKAM (Akamai Technologies Inc) Start Date:2005-01-03
AKAN (Akanda Common Shares) Start Date:2022-03-15
AKBA (Akebia Therapeutics Comm) Start Date:2014-03-20
AKLI (Akili) Start Date:2021-06-30
AKO.A (Embotelladora Andina S.A.) Start Date:2007-05-16
AKO.B (Embotelladora Andina S.A.) Start Date:2007-05-16
AKR (Acadia Realty Trust) Start Date:2007-05-01
AKRO (Akero Therapeutics) Start Date:2019-06-20
AKTS (Akoustis Technologies) Start Date:2017-03-13
AKTX (Akari Therapeutics Plc ADS) Start Date:2014-01-31
AKUMQ (Akumin Inc) Start Date:2020-09-03
AKYA (Akoya Biosciences) Start Date:2021-04-16
AL (Air Lease Corporation) Start Date:2011-04-19
ALAR (Alarum Technologies) Start Date:2018-09-11
ALB (Albemarle Corp) Start Date:2005-01-03
ALBT (Avalon Globocare) Start Date:2018-03-26
ALC (Alcon) Start Date:2019-04-09
ALCE (Alternus Clean Energy Inc) Start Date:2022-04-20
ALCO (Alico) Start Date:2007-05-16
ALCY (Alchemy Investments Acquisition 1) Start Date:2023-06-26
ALDX (Aldeyra Therapeutics,) Start Date:2014-05-02
ALE (Allete) Start Date:2007-01-03
ALEC (Alector) Start Date:2019-02-07
ALEX (Alexander & Baldwin) Start Date:2012-07-02
ALFIW (Alfi Warrant) Start Date:2021-05-04
ALG (Alamo) Start Date:2007-05-16
ALGM (Allegro Microsystems) Start Date:2020-11-02
ALGN (Align Technology) Start Date:2007-05-01
ALGS (Aligos Therapeutics) Start Date:2020-10-16
ALGT (Allegiant Travel) Start Date:2007-05-16
ALHC (Alignment Healthcare) Start Date:2021-03-26
ALIM (Alimera Sciences) Start Date:2010-04-22
ALIT (Alight,) Start Date:2020-07-17
ALK (Alaska Air Inc) Start Date:2005-01-03
ALKS (Alkermes Plc) Start Date:2007-01-03
ALKT (Alkami Technology) Start Date:2021-04-14
ALL (Allstate Corp) Start Date:2005-01-03
ALLE (Allegion) Start Date:2013-11-18
ALLG (Allego N.V.) Start Date:2022-03-17
ALLK (Allakos) Start Date:2018-07-19
ALLO (Allogene Therapeutics) Start Date:2018-10-11
ALLR (Allarity Therapeutics) Start Date:2021-12-21
ALLT (Allot Ordinary Shares) Start Date:2007-04-27
ALLY (Ally Financial) Start Date:2014-04-10
ALNT (Allient Inc) Start Date:2007-05-16
ALNY (Alnylam Pharmaceuticals) Start Date:2007-01-03
ALOT (Astronova) Start Date:2007-05-16
ALPN (Alpine Immune Sciences) Start Date:2015-06-17
ALPP (Alpine 4 Holdings Class A) Start Date:2017-01-13
ALPS (Alpine Summit Energy Partners Class A Subordinate) Start Date:2022-09-28
ALRM (Alarm.com Holdings) Start Date:2015-06-26
ALRN (Aileron Therapeutics) Start Date:2017-06-29
ALRS (Alerus Finl Corp) Start Date:2007-05-17
ALSN (Allison Transmission Holdings) Start Date:2012-03-15
ALTG (Alta Equipment) Start Date:2019-04-25
ALTI (Alvarium Tiedemann Holdings Class A) Start Date:2021-04-27
ALTO (Alto Ingredients,) Start Date:2007-04-25
ALTR (Altair Engineering) Start Date:2017-11-01
ALV (Autoliv) Start Date:2007-01-03
ALVO (Alvotech Ordinary Shares) Start Date:2022-06-16
ALVOW (Alvotech Warrant) Start Date:2022-06-16
ALVR (Allovir) Start Date:2020-07-30
ALX (Alexander's) Start Date:2007-05-16
ALXO (Alx Oncology Holdings) Start Date:2020-07-17
ALYA (Alithya  Class A Subordinate Voting Shares) Start Date:2018-11-01
ALZN (Alzamend Neuro) Start Date:2021-06-15
AM (Antero Midstream Corporation) Start Date:2017-05-04
AMAL (Amalgamated Bank) Start Date:2018-08-09
AMAM (Ambrx Biopharma) Start Date:2021-06-18
AMAT (Applied Materials) Start Date:2005-01-03
AMBA (Ambarella) Start Date:2012-10-10
AMBC (Ambac Financial) Start Date:2013-05-01
AMBI (Ambipar Emergency Response) Start Date:2020-09-09
AMBO (Ambow Education Holding ADS Each Representing Two Class A Ordinary Shares) Start Date:2018-06-01
AMBP (Ardagh Metal Packaging S.A. Ordinary Shares) Start Date:2020-09-29
AMC (Amc Entertainment) Start Date:2013-12-18
AMCR (Amcor Plc) Start Date:2019-06-11
AMCX (Amc Networks) Start Date:2011-06-16
AMD (Advanced Micro Devices Inc) Start Date:2005-01-03
AME (Ametek) Start Date:2005-01-03
AMED (Amedisys) Start Date:2007-01-03
AMEH (Apollo Medical) Start Date:2015-06-03
AMG (Affiliated Managers Inc) Start Date:2005-01-03
AMGN (Amgen) Start Date:2005-01-03
AMH (American Homes 4 Rent) Start Date:2013-08-01
AMK (Assetmark Financial) Start Date:2019-07-18
AMKR (Amkor Technology) Start Date:2007-01-03
AMLI (American Lithium) Start Date:2023-01-10
AMLX (Amylyx Pharmaceuticals,) Start Date:2022-01-07
AMN (Amn Healthcare Services) Start Date:2007-06-04
AMNB (American National) Start Date:2007-05-16
AMP (Ameriprise Financial) Start Date:2005-10-03
AMPE (Ampio Pharmaceuticals) Start Date:2011-05-19
AMPG (Amplitech) Start Date:2021-02-17
AMPH (Amphastar Pharmaceuticals) Start Date:2014-06-25
AMPL (Amplitude, Class A) Start Date:2021-09-28
AMPS (Altus Power Class A) Start Date:2021-02-01
AMPX (Amprius Technologies) Start Date:2022-09-15
AMPY (Amplify Energy) Start Date:2017-05-19
AMR (Alpha Metallurgical Resources,) Start Date:2016-08-18
AMRC (Ameresco) Start Date:2010-07-22
AMRK (A-Mark Precious Metals C) Start Date:2014-03-17
AMRN (Amarin Plc) Start Date:2008-02-19
AMRS (Amyris) Start Date:2010-09-28
AMRX (Amneal Pharmaceuticals) Start Date:2018-05-07
AMS (American Shared Hospital Services) Start Date:2007-05-16
AMSC (American Superconductor Corpor) Start Date:2007-04-30
AMSF (Amerisafe) Start Date:2007-05-08
AMST (Amesite) Start Date:2020-09-25
AMSWA (American Software) Start Date:2007-05-09
AMT (American Tower) Start Date:2012-01-03
AMTB (Amerant Bancorp) Start Date:2018-08-29
AMTD (Amtd Idea American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2022-01-31
AMTI (Applied Molecular Transport) Start Date:2020-06-05
AMTX (Aemetis) Start Date:2007-12-11
AMWD (American Woodmark) Start Date:2007-04-20
AMWL (Amwell Health) Start Date:2020-09-17
AMX (America Movil S.A.B. De C.V. American Depository Receipt Series L) Start Date:2007-04-30
AMZN (Amazon.com) Start Date:2005-01-03
AN (Autonation) Start Date:2005-01-03
ANAB (Anaptysbio) Start Date:2017-01-26
ANDE (Andersons) Start Date:2007-05-02
ANEB (Anebulo Pharmaceuticals) Start Date:2021-05-07
ANET (Arista Networks) Start Date:2014-06-06
ANF (Abercrombie & Fitch Company) Start Date:2005-01-03
ANGH (Anghami Ordinary Shares) Start Date:2022-02-04
ANGHW (Anghami Warrants) Start Date:2022-02-04
ANGI (Angi Homeservices) Start Date:2017-10-02
ANGO (Angiodynamics) Start Date:2007-05-07
ANIK (Anika Therapeutics) Start Date:2007-04-27
ANIP (Ani Pharmaceuticals) Start Date:2007-11-05
ANIX (Anixa Biosciences) Start Date:2007-05-16
ANL (Adlai Nortye Ltd.) Start Date:2023-09-29
ANNX (Annexon Biosciences) Start Date:2020-07-24
ANSS (Ansys) Start Date:2005-01-03
ANTE (Airnet Technology American Depositary Shares) Start Date:2007-11-07
ANTX (An2 Therapeutics) Start Date:2022-03-25
ANVS (Annovis Bio) Start Date:2020-01-29
ANY (Sphere 3D Common Shares) Start Date:2014-07-07
AOD (Aberdeen Total Dynamic Dividend Fund) Start Date:2007-05-16
AOMR (Angel Oak Mortgage) Start Date:2021-06-17
AON (Aon Plc) Start Date:2007-04-30
AONC (American Oncology Network Inc) Start Date:2021-05-05
AORT (Artivion) Start Date:2007-05-10
AOS (A.O. Smith Corp) Start Date:2007-04-02
AOSL (Alpha & Omega) Start Date:2010-04-29
AOUT (American Outdoor Brands) Start Date:2020-08-21
AP (Ampco-Pittsburgh) Start Date:2007-05-09
APA (Apache Corporation) Start Date:2005-01-03
APAM (Artisan Partners Asset Management) Start Date:2013-03-07
APCX (Apptech Payments) Start Date:2017-05-08
APCXW (Apptech Payments Warrant) Start Date:2022-01-05
APD (Air Products & Chemicals Inc) Start Date:2005-01-03
APDN (Applied Dna Sciences) Start Date:2007-05-16
APE (Amc Entertainment Holdings Amc Preferred Equity Units) Start Date:2022-08-22
APEI (American Public Education) Start Date:2007-11-09
APGB (Apollo Strategic Growth Capital Ii Class A Ordinary Shares) Start Date:2021-04-05
APGE (Apogee Therapeutics) Start Date:2023-07-14
APH (Amphenol Corp) Start Date:2005-01-03
API (Agora) Start Date:2020-06-26
APLD (Applied Blockchain) Start Date:2009-12-10
APLE (Apple Hospitality Reit) Start Date:2015-05-18
APLS (Apellis Pharmaceuticals) Start Date:2017-11-09
APLT (Applied Therapeutics) Start Date:2019-05-14
APM (Aptorum Class A Ordinary Shares) Start Date:2018-12-18
APO (Apollo Global Management) Start Date:2011-03-30
APOG (Apogee Enterprises) Start Date:2007-05-08
APP (Applovin) Start Date:2021-04-15
APPF (Appfolio) Start Date:2015-06-26
APPH (Appharvest,) Start Date:2020-06-12
APPHW (Appharvest Warrants) Start Date:2020-06-16
APPN (Appian Corporation) Start Date:2017-05-25
APPS (Digital Turbine) Start Date:2007-11-26
APRE (Aprea Therapeutics) Start Date:2019-10-03
APRN (Blue Apron Holdings Class A) Start Date:2017-06-29
APT (Alpha Pro Tech) Start Date:2007-05-16
APTM (Alpha Partners Technology Merger Class A Ordinary Shares) Start Date:2021-09-23
APTMU (Alpha Partners Technology Merger Unit) Start Date:2021-07-28
APTMW (Alpha Partners Technology Merger Warrant) Start Date:2021-09-27
APTO (Aptose Biosciences Common Shares) Start Date:2008-10-31
APTV (Aptiv Plc) Start Date:2011-11-17
APVO (Aptevo Therapeutics) Start Date:2016-07-20
APWC (Asia Pacific Wire & Cable Ordinary Shares) Start Date:2011-04-29
APYX (Apyx Medical Corp) Start Date:2007-05-16
AQB (Aquabounty Technologies) Start Date:2017-01-11
AQMS (Aqua Metals) Start Date:2015-07-31
AQN (Algonquin Power & Utilities) Start Date:2016-11-29
AQNU (Algonquin Power & Utilities Corporate Units) Start Date:2021-06-29
AQST (Aquestive Therapeutics) Start Date:2018-07-25
AQU (Aquaron Acquisition) Start Date:2022-10-19
AR (Antero Resources Corp) Start Date:2013-10-10
ARAV (Aravive) Start Date:2014-03-21
ARAY (Accuray) Start Date:2007-05-16
ARBB (Arb Iot Limited) Start Date:2023-04-05
ARBE (Arbe Robotics Ordinary Shares) Start Date:2021-10-08
ARBEW (Arbe Robotics Warrant) Start Date:2021-10-08
ARBK (Argo Blockchain Plc American Depositary Shares) Start Date:2021-09-23
ARC (Arc Document Solutions) Start Date:2007-05-03
ARCB (Arcbest O) Start Date:2007-04-27
ARCC (Ares Capital Corporation) Start Date:2012-10-08
ARCE (Arco Platform Limited) Start Date:2018-09-26
ARCH (Arch Resources) Start Date:2016-10-05
ARCKU (Arbor Rapha Capital Bioholdings I Units) Start Date:2021-10-29
ARCKW (Arbor Rapha Capital Bioholdings I Warrants) Start Date:2021-12-20
ARCO (Arcos Dorados Holdings) Start Date:2011-04-14
ARCT (Arcturus Therapeutics) Start Date:2013-05-22
ARDC (Ares Dynamic Credit Allocation Fund Common Shares) Start Date:2012-11-28
ARDX (Ardelyx) Start Date:2014-06-19
ARE (Alexandria Real Estate Equities) Start Date:2005-01-03
AREB (American Rebel Holdings) Start Date:2018-01-23
AREBW (American Rebel Holdings Warrants) Start Date:2022-02-07
AREC (American Resources Class A) Start Date:2015-11-25
AREN (The Arena Holdings) Start Date:2022-02-09
ARES (Ares Management Corporation) Start Date:2014-05-02
ARGO (Argo International) Start Date:2018-03-14
ARGUW (Argus Capital Warrant) Start Date:2021-11-12
ARGX (Argenx Se) Start Date:2017-05-18
ARHS (Arhaus) Start Date:2021-11-04
ARI (Apollo Commercial) Start Date:2009-09-24
ARIS (Aris Water Solutions Class A) Start Date:2021-10-22
ARKO (Arko) Start Date:2020-12-23
ARKOW (Arko Warrant) Start Date:2020-12-23
ARKR (ARKRestaurants) Start Date:2007-05-16
ARL (American Realty Investors) Start Date:2007-05-16
ARLO (Arlo Technologies) Start Date:2018-08-03
ARLP (Alliance Resource Partners Lp) Start Date:2007-04-26
ARM (Arm Holdings Limited) Start Date:2023-09-14
ARMK (Aramark) Start Date:2013-12-12
ARMP (Armata Pharmaceuticals) Start Date:2015-08-21
AROC (Archrock) Start Date:2007-08-21
AROW (Arrow Financial) Start Date:2007-05-02
ARQQ (Arqit Quantum Ordinary Shares) Start Date:2021-09-07
ARQQW (Arqit Quantum Warrants) Start Date:2021-09-07
ARQT (Arcutis Biotherapeutics) Start Date:2020-01-31
ARR (Armour Residential Reit) Start Date:2009-11-10
ARRY (Array Technologies) Start Date:2020-10-15
ARTE (Artemis Strategic Investment Class A) Start Date:2021-11-23
ARTEU (Artemis Strategic Investment Unit) Start Date:2021-09-30
ARTEW (Artemis Strategic Investment Warrant) Start Date:2021-11-22
ARTL (Artelo Biosciences) Start Date:2017-11-14
ARTLW (Artelo Biosciences Warrant) Start Date:2019-06-21
ARTNA (Artesian Resource) Start Date:2007-05-16
ARTW (Art's-Way Manufacturing Co.) Start Date:2007-05-16
ARVL (Arrival Ordinary Shares) Start Date:2021-03-25
ARVN (Arvinas) Start Date:2018-09-27
ARW (Arrow Electronics) Start Date:2007-01-03
ARWR (Arrowhead Pharmaceuticals) Start Date:2007-05-16
ASA (Asa Gold And Precious Metals Limited) Start Date:2007-05-01
ASAI (Sendas Distribuidora S A ADS) Start Date:2021-03-08
ASAN (Asana) Start Date:2020-09-30
ASB (Associated Banc-Corp) Start Date:2014-12-23
ASC (Ardmore Shipping Corp) Start Date:2013-08-01
ASCA (A SPAC I Acquisition) Start Date:2022-03-18
ASCB (A SPAC Ii Acquisition Corporation) Start Date:2022-05-31
ASG (Liberty All-Star Growth Fund) Start Date:2007-05-16
ASGI (Aberdeen Standard Global Infrastructure Income Fund Common Shares Of Beneficial Interest) Start Date:2020-07-29
ASGN (Asgn Incorporated) Start Date:2012-08-31
ASH (Ashland Global Holdings) Start Date:2005-01-03
ASIX (Advansix) Start Date:2016-09-15
ASLE (Aersale) Start Date:2020-12-15
ASLN (Aslan Pharmaceuticals American Depositary Shares) Start Date:2018-05-04
ASM (Avino Silver & Gold Mines Common Shares) Start Date:2018-01-08
ASMB (Assembly Biosciences Com) Start Date:2010-12-17
ASML (Asml Holding) Start Date:2007-04-30
ASND (Ascendis Pharma A/S American Depositary Shares) Start Date:2015-01-28
ASNS (Actelis Networks) Start Date:2022-05-13
ASO (Amsouth Ban) Start Date:2020-10-02
ASPI (Asp Isotopes) Start Date:2022-11-10
ASPN (Aspen Aerogels) Start Date:2014-06-13
ASPS (Altisource Portfolio) Start Date:2009-08-10
ASR (Grupo Aeroportuario Del Sureste S.A. De C.V.) Start Date:2007-05-02
ASRT (Assertio Holdings) Start Date:2007-04-26
ASRV (Ameriserv Financial) Start Date:2007-05-16
ASST (Asset Entities) Start Date:2023-02-03
ASTC (Astrotech Corporation) Start Date:2009-05-04
ASTE (Astec Industries) Start Date:2007-05-03
ASTI (Ascent Solar Technologies) Start Date:2007-05-16
ASTL (Algoma Steel  Common Shares) Start Date:2021-10-20
ASTLW (Algoma Steel  Warrant) Start Date:2021-10-20
ASTR (Astra Space, Class A) Start Date:2021-06-28
ASTS (Ast Spacemobile, Class A) Start Date:2019-11-01
ASTSW (Ast Spacemobile Warrant) Start Date:2019-11-01
ASUR (Asure Software) Start Date:2010-01-21
ASX (Ase Technology Holding Co. Ltd.) Start Date:2018-05-01
ASXC (Asensus Surgical) Start Date:2021-03-05
ASYS (Amtech Systems) Start Date:2007-05-16
ATAI (Atai Life Sciences) Start Date:2021-06-18
ATAK (Aurora Technology Acquisition) Start Date:2022-03-21
ATAT (Atour Lifestyle Holdings) Start Date:2022-11-11
ATAX (America First Multifamily Investors L.P. Beneficial Unit Certificates) Start Date:2008-07-01
ATEC (Alphatec) Start Date:2007-05-16
ATEN (A10 Networks) Start Date:2014-03-21
ATER (Aterian) Start Date:2019-06-12
ATEX (Anterix) Start Date:2015-02-03
ATGE (Devry) Start Date:2007-05-01
ATGL (Alpha Technology Limited) Start Date:2023-10-31
ATHA (Athira Pharma) Start Date:2020-09-18
ATHE (Alterity Therapeutics American Depositary Shares) Start Date:2019-04-09
ATHM (Autohome) Start Date:2013-12-11
ATHX (Athersys) Start Date:2007-12-12
ATI (Allegheny Technologies Incorporated) Start Date:2005-01-03
ATIF (Atif Holdings Ordinary Shares) Start Date:2019-05-03
ATIP (Ati Physical Therapy,) Start Date:2020-10-02
ATKR (Atkore Intl) Start Date:2016-06-10
ATLC (Atlanticus) Start Date:2007-04-27
ATLO (Ames National) Start Date:2007-05-16
ATLX (Atlas Lithium) Start Date:2023-01-10
ATMC (Alphatime Acquisition Corp) Start Date:2023-01-19
ATMU (Atmus Filtration Technologies) Start Date:2023-05-26
ATMV (Alphavest Acquisition Corp) Start Date:2023-01-25
ATNF (180 Life Sciences) Start Date:2020-06-08
ATNFW (180 Life Sciences Warrant) Start Date:2017-06-27
ATNI (Atn International) Start Date:2007-05-04
ATNM (Actinium Pharmaceuticals) Start Date:2014-03-26
ATNX (Athenex) Start Date:2017-06-14
ATO (Atmos Energy Corp) Start Date:2005-01-03
ATOM (Atomera) Start Date:2016-08-05
ATOS (Atossa Therapeutics,) Start Date:2012-11-08
ATR (Aptargroup) Start Date:2007-05-02
ATRA (Atara Biotherapeutics) Start Date:2014-10-16
ATRC (Atricure) Start Date:2007-05-16
ATRI (Atrion) Start Date:2007-05-16
ATRO (Astronics) Start Date:2007-05-16
ATS (Ats Corporation) Start Date:2023-05-25
ATSG (Air Transport Srvcs) Start Date:2008-05-16
ATTO (Atento S.A. Ordinary Shares) Start Date:2014-10-02
ATUS (Altice Usa) Start Date:2017-06-22
ATVI (Activision Blizzard) Start Date:2007-04-30
ATXG (Addentax) Start Date:2016-12-12
ATXI (Avenue Therapeutics) Start Date:2017-06-27
ATXS (Astria Therapeutics) Start Date:2015-06-25
AU (Anglogold Ashanti Limited) Start Date:2007-01-03
AUB (Atlantic Union Bankshares Corp) Start Date:2014-11-28
AUBN (Auburn National Bancorp) Start Date:2007-05-16
AUDC (Audiocodes Ltd) Start Date:2007-05-01
AUGX (Augmedix) Start Date:2021-03-31
AUID (Ipsidy) Start Date:2021-07-19
AULT (Ault Alliance) Start Date:2008-03-12
AUMN (Golden Minerals Company) Start Date:2007-07-16
AUPH (Aurinia Pharmaceuticals Inc) Start Date:2013-11-08
AUR (Aurora Innovation, Class A) Start Date:2021-05-10
AURA (Aura Biosciences) Start Date:2021-10-29
AUROW (Aurora Innovation Warrant) Start Date:2021-11-04
AUST (Austin Gold Common Shares) Start Date:2022-05-04
AUTL (Autolus Therapeutics Plc American Depositary Share) Start Date:2018-06-22
AUUD (Auddia) Start Date:2021-02-17
AUUDW (Auddia Warrants) Start Date:2021-02-17
AUVI (Applied Uv) Start Date:2020-08-31
AVA (Avista Corporation) Start Date:2007-01-03
AVAH (Aveanna Healthcare Holdings) Start Date:2021-04-29
AVAL (Grupo Aval Acciones Y Valores S.A.) Start Date:2014-09-23
AVAV (Aerovironment) Start Date:2007-05-16
AVB (Avalonbay Communities) Start Date:2005-01-03
AVCO (Avalon Globocare) Start Date:2016-12-06
AVCT (American Virtual Cloud Technologies) Start Date:2017-08-08
AVCTW (American Virtual Cloud Technologies Warrant Expiring 4/7/2025) Start Date:2017-08-08
AVD (American Vanguard) Start Date:2007-05-02
AVDL (Avadel Pharmaceuticals Plc American Depositary Shares) Start Date:2007-05-04
AVDX (Avidxchange Holdings,) Start Date:2021-10-13
AVGO (Broadcom) Start Date:2016-02-01
AVGOP (Broadcom 8.00% Mandatory Convertible Preferred Stock Series A) Start Date:2019-09-25
AVGR (Avinger) Start Date:2015-01-30
AVHI (Achari Ventures Holdings I) Start Date:2021-11-17
AVID (Avid Technology) Start Date:2007-04-27
AVIR (Atea Pharmaceuticals) Start Date:2020-11-02
AVK (Advent Convertible And Income Fund) Start Date:2007-04-25
AVNS (Avanos Medical) Start Date:2014-11-03
AVNT (Avient Corporation) Start Date:2007-05-01
AVNW (Aviat Networks) Start Date:2010-01-29
AVO (Mission Produce) Start Date:2020-10-01
AVPT (Avepoint, Class A) Start Date:2021-06-28
AVPTW (Avepoint Warrant) Start Date:2019-11-05
AVRO (Avrobio) Start Date:2018-06-21
AVT (Avnet) Start Date:2007-01-03
AVTA (Avantax) Start Date:2007-04-30
AVTE (Aerovate Therapeutics) Start Date:2021-06-30
AVTR (Avantor) Start Date:2019-05-17
AVTX (Avalo Therapeutics) Start Date:2015-11-13
AVXL (Anavex Life Sciences) Start Date:2015-10-28
AVY (Avery Dennison Corp) Start Date:2005-01-03
AVYA (Avaya Corp) Start Date:2017-12-19
AWF (Alliancebernstein Global High Income Fund) Start Date:2007-05-03
AWH (Aspira Women's Health) Start Date:2010-01-27
AWI (Armstrong World Industries) Start Date:2007-01-03
AWIN (Aerwins Technologies) Start Date:2021-10-12
AWK (American Water Works Company Inc) Start Date:2008-04-23
AWP (Aberdeen Global Premier Properties Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
AWR (American States Water) Start Date:2007-05-02
AWRE (Aware) Start Date:2007-05-16
AWX (Avalon Holdings) Start Date:2007-05-16
AX (Axos Financial) Start Date:2007-05-16
AXAC (Axios Sustainable Growth Acquisition Corporation) Start Date:2022-03-25
AXDX (Accelerate Diagnostics C) Start Date:2007-05-16
AXGN (Axogen) Start Date:2007-05-16
AXL (American Axle & Mfg) Start Date:2007-05-02
AXLA (Axcella Health) Start Date:2019-05-09
AXNX (Axonics Modulation Technologies) Start Date:2018-10-31
AXON (Axon Enterprise,) Start Date:2007-05-01
AXP (American Express Co) Start Date:2005-01-03
AXR (Amrep) Start Date:2007-04-27
AXS (Axis Capital Holdings Limited) Start Date:2007-01-03
AXSM (Axsome Therapeutics) Start Date:2015-11-19
AXTA (Axalta Coating Systems Ltd.) Start Date:2014-11-12
AXTI (Axt) Start Date:2007-05-03
AY (Atlantica Sustainable Infrastructure Plc) Start Date:2014-06-13
AYI (Acuity Brands) Start Date:2005-01-03
AYRO (Ayro) Start Date:2007-05-16
AYTU (Aytu Bioscience) Start Date:2017-10-20
AYX (Alteryx) Start Date:2017-03-24
AZ (A2z Smart Technologies Common Shares) Start Date:2022-01-05
AZEK (Azek Company) Start Date:2020-06-12
AZN (Astrazeneca Plc American Depositary Shares) Start Date:2007-04-27
AZO (Autozone Inc) Start Date:2005-01-03
AZPN (Aspen Technology) Start Date:2007-05-02
AZTA (Azenta) Start Date:2007-05-02
AZTR (Azitra) Start Date:2023-06-16
AZUL (Azul S.A. American Depositary Shares) Start Date:2017-04-11
AZZ (Azz) Start Date:2007-05-09
B (Barnes) Start Date:2007-06-04
BA (Boeing Company) Start Date:2005-01-03
BABA (Alibaba Holding American Depositary Shares Each Representing Eight Ordinary Share) Start Date:2014-09-19
BAC (Bank Of America Corp) Start Date:2005-01-03
BACK (Imac Holdings) Start Date:2019-02-13
BAER (Bridger Aerospace Holdings) Start Date:2023-01-25
BAFN (Bayfirst Financial) Start Date:2021-11-30
BAH (Booz Allen Hamilton Holding Corporation) Start Date:2010-11-17
BAK (Braskem Sa ADR) Start Date:2019-10-24
BALL (Ball Corp) Start Date:2005-01-03
BALY (Bally's Corporation) Start Date:2019-03-29
BAM (Brookfield Asset Management Inc) Start Date:2007-05-01
BAMR (Bam Reinsurance) Start Date:2021-06-28
BANC (Banc Of California Commo) Start Date:2007-05-17
BAND (Bandwidth) Start Date:2017-11-10
BANF (Bancfirst) Start Date:2007-05-16
BANFP (Bancfirst - Bfc Capital Trust Ii Cumulative Trust Preferred Securities) Start Date:2007-05-16
BANL (Cbl International Limited) Start Date:2023-03-23
BANR (Banner) Start Date:2007-05-07
BANX (Arrowmark Financial) Start Date:2013-11-07
BAOS (Baosheng Media) Start Date:2021-02-08
BAP (Credicorp Ltd.) Start Date:2007-01-03
BARK (The Original Bark Company) Start Date:2020-12-18
BASE (Couchbase) Start Date:2021-07-22
BATL (Battalion Oil) Start Date:2020-02-20
BATRA (Liberty Media Series A Lbty Braves) Start Date:2016-04-18
BATRK (Liberty Media Series C Lbty Braves) Start Date:2016-04-18
BAX (Baxter International) Start Date:2005-01-03
BAYA (Bayview Acquisition Corp) Start Date:2023-12-29
BB (Blackberry Limited) Start Date:2007-04-25
BBAI (Bigbear.AI) Start Date:2021-12-08
BBAR (Banco Bbva Argentina S.A. ADS) Start Date:2007-05-16
BBBY (Bed Bath & Beyond) Start Date:2005-01-03
BBCP (Concrete Pumping) Start Date:2017-08-21
BBD (Banco Bradesco S.A.) Start Date:2007-01-03
BBDC (Barings Bdc,) Start Date:2007-05-16
BBDO (Banco Bradesco Sa American Depositary Shares) Start Date:2012-03-13
BBGI (Beasley Broadcast  Class A) Start Date:2007-05-16
BBIO (Bridgebio Pharma) Start Date:2019-06-27
BBLG (Bone Biologics) Start Date:2021-10-13
BBLGW (Bone Biologics Warrants) Start Date:2021-10-13
BBLN (Babylon Holdings Class A Ordinary Shares) Start Date:2021-10-22
BBN (Blackrock Taxable Municipal Bond Trust Common Shares Of Beneficial Interest) Start Date:2010-08-27
BBSI (Barrett Business Services) Start Date:2007-05-16
BBU (Brookfield Business Partners) Start Date:2016-06-01
BBUC (Brookfield Business Class A Exchangeable Subordinate Voting Shares) Start Date:2022-03-15
BBVA (Banco Bilbao Vizcaya Argentaria S.A.) Start Date:2009-12-14
BBW (Build-A-Bear Workshop) Start Date:2007-04-27
BBWI (Bath & Body Works,) Start Date:2007-04-27
BBY (Best Buy Co.) Start Date:2005-01-03
BC (Brunswick Corporation) Start Date:2005-01-03
BCAB (Bioatla) Start Date:2020-12-16
BCAN (Bynd Cannasoft Enterprises) Start Date:2022-05-31
BCAT (Blackrock Capital Allocation Trust) Start Date:2020-09-25
BCBP (Bcb Bancorp) Start Date:2007-05-16
BCC (Boise Cascade) Start Date:2013-02-06
BCDA (Biocardia) Start Date:2008-11-28
BCDAW (Biocardia Warrant) Start Date:2019-08-02
BCE (Bce) Start Date:2007-01-03
BCEL (Atreca) Start Date:2019-06-20
BCH (Banco De Chile Banco De Chile ADS) Start Date:2007-05-16
BCLI (Brainstorm Cell Therapeutics I) Start Date:2007-05-16
BCML (Baycom Corp) Start Date:2007-05-16
BCO (The Brink's Company) Start Date:2007-01-03
BCOR (Blucora) Start Date:2007-04-30
BCOV (Brightcove) Start Date:2012-02-17
BCOW (1895 Bancorp Of Wisconsin) Start Date:2019-01-09
BCPC (Balchem) Start Date:2007-05-16
BCRX (Biocryst Pharmaceuticals) Start Date:2007-04-30
BCS (Barclays Plc) Start Date:2007-01-03
BCSF (Bain Capital Specialty Finance) Start Date:2018-11-15
BCTX (Briacell Therapeutics Common Shares) Start Date:2021-02-24
BCTXW (Briacell Therapeutics Warrant) Start Date:2021-02-24
BCV (Bancroft Fund Ltd.) Start Date:2007-05-16
BCX (Blackrock Resources Common Shares Of Beneficial Interest) Start Date:2011-03-29
BCYC (Bicycle Therapeutics Plc American Depositary Shares) Start Date:2019-05-23
BDC (Belden) Start Date:2007-05-02
BDJ (Blackrock Enhanced Equity Dividend Trust) Start Date:2007-05-02
BDL (Flanigan's Enterprises) Start Date:2007-05-16
BDN (Brandywine Realty Trust) Start Date:2007-05-01
BDRX (Biodexa Pharmaceuticals Plc) Start Date:2015-12-07
BDSX (Biodesix Inc) Start Date:2020-11-02
BDTX (Black Diamond Therapeutics) Start Date:2020-01-30
BDX (Becton Dickinson) Start Date:2005-01-03
BE (Bloom Energy Corp) Start Date:2018-07-25
BEAM (Beam Therapeutics) Start Date:2020-02-06
BEAT (Heartbeam,) Start Date:2021-11-11
BECN (Beacon Roofing Supply) Start Date:2007-04-30
BEDU (Bright Scholar Education Holdings American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2017-05-18
BEEM (Beam Global) Start Date:2020-12-15
BEEMW (Beam Global Warrant) Start Date:2019-04-16
BEKE (Ke) Start Date:2020-08-13
BELFA (Bel Fuse Class A) Start Date:2007-05-16
BELFB (Bel Fuse) Start Date:2007-05-09
BEN (Franklin Resources) Start Date:2005-01-03
BEP (Brookfield Renewable Partners L.P.) Start Date:2007-05-16
BEPC (Brookfield Renewable Class A Subordinate Voting Shares) Start Date:2020-07-24
BERY (Berry Global) Start Date:2012-10-04
BEST (Best) Start Date:2019-02-19
BETS (Bit Brother Ltd.) Start Date:2019-02-20
BF.A (Brown-Forman) Start Date:2007-05-16
BF.B (Brown-Forman) Start Date:2005-01-03
BFAM (Bright Horizons Family Solutions) Start Date:2013-01-25
BFC (Bank First Corp) Start Date:2007-05-17
BFH (Bread Financial) Start Date:2007-04-30
BFI (Burgerfi International) Start Date:2018-03-26
BFIIW (Burgerfi International Warrant) Start Date:2018-03-26
BFIN (Bankfinancial) Start Date:2007-05-10
BFK (Blackrock Municipal Income Trust) Start Date:2007-05-16
BFLY (Butterfly Network) Start Date:2020-07-13
BFRG (Bullfrog AI Holdings) Start Date:2023-02-14
BFRI (Biofrontera) Start Date:2021-10-29
BFRIW (Biofrontera Warrants) Start Date:2021-10-29
BFS (Saul Centers) Start Date:2007-05-08
BFST (Business First Bancshares) Start Date:2018-04-11
BFX (Nautilus Inc) Start Date:2007-04-30
BFZ (Blackrock California Municipal Income Trust) Start Date:2007-05-16
BG (Bunge Limited) Start Date:2007-01-03
BGB (Blackstone Strategic Credit Fund Common Shares) Start Date:2012-09-26
BGC (Bgc Inc) Start Date:2008-04-02
BGFV (Big 5 Sporting Goods Corp) Start Date:2007-05-04
BGH (Barings Global Short Duration High Yield Fund Common Shares Of Beneficial Interests) Start Date:2012-10-26
BGI (Birks) Start Date:2007-05-16
BGNE (Beigene American Depositary Shares) Start Date:2016-02-03
BGR (Blackrock Energy And Resources Trust) Start Date:2007-05-07
BGRYW (Berkshire Grey Warrant) Start Date:2021-02-12
BGS (B&G Foods) Start Date:2007-05-23
BGSF (Bg Staffing) Start Date:2014-04-29
BGT (Blackrock Floating Rate Income Trust) Start Date:2007-05-16
BGX (Blackstone Long Short Credit Income Fund Common Shares) Start Date:2011-01-27
BGXX (Bright Green) Start Date:2022-05-17
BGY (Blackrock Enhanced International Dividend Trust) Start Date:2007-05-25
BH (Biglari) Start Date:2018-05-01
BH.A (Biglari) Start Date:2018-05-01
BHAT (Blue Hat Interactive Entertainment Technology Ordinary Shares) Start Date:2019-07-26
BHB (Bar Harbor Bankshares) Start Date:2007-05-16
BHC (Bausch Health Companies) Start Date:2007-04-27
BHE (Benchmark Electronics) Start Date:2007-04-26
BHF (Brighthouse Financial) Start Date:2017-07-17
BHFAL (Brighthouse Financial 6.25% Junior Subordinated Debentures Due 2058) Start Date:2018-09-14
BHFAP (Brighthouse Financial Depositary Shares 6.6% Non-Cumulative Preferred Stock Series A) Start Date:2019-03-26
BHG (Bright Health) Start Date:2021-06-24
BHIL (Benson Hill) Start Date:2021-09-27
BHK (Blackrock Core Bond Trust Blackrock Core Bond Trust) Start Date:2007-05-07
BHLB (Berkshire Hills Bancorp) Start Date:2007-04-25
BHM (Bluerock Homes Trust Class A) Start Date:2022-09-28
BHP (Bhp American Depositary Shares) Start Date:2007-04-30
BHR (Braemar Hotels & Resorts) Start Date:2013-11-20
BHSE (Bull Horn Holdings) Start Date:2020-12-17
BHSEW (Bull Horn Holdings Warrants) Start Date:2020-12-17
BHV (Blackrock Virginia Municipal Bond Trust) Start Date:2007-05-16
BHVN (Biohaven Pharmaceutical Holding Company Ltd.) Start Date:2017-05-04
BIAF (Bioaffinity Technologies) Start Date:2022-09-01
BIDU (Bidu) Start Date:2005-08-05
BIG (Big Lots) Start Date:2006-09-01
BIGC (Bigcommerce) Start Date:2020-08-05
BIGZ (Blackrock Innovation And Growth Trust Common Shares Of Beneficial Interest) Start Date:2021-03-26
BIIB (Biogen) Start Date:2005-01-03
BILI (Bilibili) Start Date:2018-03-28
BILL (Bill.com Holdings) Start Date:2019-12-12
BIMI (Bimi International Medical) Start Date:2010-10-04
BIO (Bio-Rad Laboratories) Start Date:2007-05-08
BIO.B (Bio-Rad Laboratories) Start Date:2007-05-16
BIOC (Biocept) Start Date:2014-02-05
BIOL (Biolase) Start Date:2007-05-07
BIOR (Biora Therapeutics) Start Date:2020-06-19
BIOX (Bioceres Crop Solutions Ordinary Shares) Start Date:2019-03-15
BIP (Brookfield Infrastructure Partners L.P.) Start Date:2008-01-31
BIPC (Brookfield Infrastructure Corporation) Start Date:2020-04-20
BIRD (Allbirds, Class A) Start Date:2021-11-03
BIRK (Birkenstock Holding Limited) Start Date:2023-10-11
BIT (Blackrock Multi-Sector Income Trust Common Shares Of Beneficial Interest) Start Date:2013-02-26
BITF (Bitfarms) Start Date:2021-06-21
BIVI (Biovie Class A) Start Date:2019-08-15
BJ (Bj's Wholesale Club Holdings) Start Date:2018-06-28
BJDX (Bluejay Diagnostics,) Start Date:2021-11-10
BJRI (Bj's Restaurants) Start Date:2007-05-08
BK (The Bank Of New York Mellon) Start Date:2007-07-02
BKCC (Blackrock Capital Investment) Start Date:2007-06-27
BKD (Brookdale Senior Living) Start Date:2007-05-04
BKE (Buckle) Start Date:2007-04-30
BKH (Black Hills Corporation) Start Date:2007-01-03
BKI (Black Knight) Start Date:2017-10-02
BKKT (Bakkt Holdings,) Start Date:2021-10-18
BKN (Blackrock Investment Quality Municipal Trust) Start Date:2007-05-16
BKNG (Booking Holdings Inc) Start Date:2007-04-30
BKR (Baker Hughes Company) Start Date:2017-07-05
BKSC (Bank Of South Carolina) Start Date:2007-05-16
BKSY (Blacksky Technology) Start Date:2019-12-20
BKT (Blackrock Income Trust) Start Date:2007-05-16
BKTI (Bk Technologies) Start Date:2007-04-26
BKU (Bankunited) Start Date:2011-01-28
BKYI (Bio-Key International) Start Date:2006-12-11
BL (Blackline) Start Date:2016-10-28
BLAC (Bellevue Life Sciences Acquisition) Start Date:2023-03-17
BLBD (Perseon Corp) Start Date:2014-03-20
BLBX (Blackboxstocks) Start Date:2016-01-22
BLCO (Bausch + Lomb Common Shares) Start Date:2022-05-06
BLD (Topbuild) Start Date:2015-06-29
BLDE (Blade Air Mobility, Class A) Start Date:2019-11-05
BLDEW (Blade Air Mobility Warrants) Start Date:2020-01-03
BLDP (Ballard Power Systems) Start Date:2007-04-30
BLDR (Builders Firstsource) Start Date:2007-01-03
BLE (Blackrock Municipal Income Trust Ii) Start Date:2007-05-16
BLEU (Bleuacacia Class A Ordinary Shares) Start Date:2022-01-10
BLEUR (Bleuacacia Rights) Start Date:2022-01-10
BLEUU (Bleuacacia Unit) Start Date:2021-11-18
BLEUW (Bleuacacia Warrants) Start Date:2022-01-10
BLFS (Biolife Solutions) Start Date:2007-05-16
BLFY (Blue Foundry Bancorp) Start Date:2021-07-16
BLIN (Bridgeline Digital) Start Date:2007-06-29
BLK (Blackrock) Start Date:2005-01-03
BLKB (Blackbaud) Start Date:2007-01-03
BLMN (Bloomin Brands) Start Date:2012-08-08
BLND (Blend Labs) Start Date:2021-07-16
BLNK (Blink Charging Co.) Start Date:2018-02-14
BLNKW (Blink Charging Co. Warrant) Start Date:2018-02-14
BLPH (Bellerophon Therapeutics) Start Date:2015-02-13
BLRX (Biolinerx American Depositary Shares) Start Date:2011-07-25
BLTE (Belite Bio Inc American Depositary Shares) Start Date:2022-04-29
BLUE (Bluebird Bio) Start Date:2013-06-19
BLW (Blackrock Duration Income Trust) Start Date:2007-05-07
BLX (Banco Latinoamericano) Start Date:2007-05-10
BLZE (Backblaze, Class A) Start Date:2021-11-11
BMA (Banco Macro S.A. ADR) Start Date:2007-05-11
BMBL (Bumble) Start Date:2021-02-11
BME (Blackrock Health Sciences Trust) Start Date:2007-05-16
BMEA (Biomea Fusion) Start Date:2021-04-16
BMEZ (Blackrock Health Sciences Trust Ii Common Shares Of Beneficial Interest) Start Date:2020-01-29
BMI (Badger Meter) Start Date:2007-05-09
BMN (Blackrock 2037 Municipal Target Term Trust Of Beneficial Interest) Start Date:2022-10-27
BMO (Bank Of Montreal) Start Date:2007-01-03
BMR (Beamr Imaging) Start Date:2023-02-28
BMRA (Biomerica) Start Date:2007-05-17
BMRC (Bank Of Marin) Start Date:2007-05-16
BMRN (Biomarin Pharmaceutical) Start Date:2009-07-21
BMTX (Bm Technologies) Start Date:2018-09-21
BMY (Bristol-Myers Squibb) Start Date:2005-01-03
BN (Brookfield Class A) Start Date:2007-05-01
BNED (Barnes & Noble Education Inc) Start Date:2015-07-23
BNGO (Bionano Genomics,) Start Date:2018-09-21
BNGOW (Bionano Genomics Warrant) Start Date:2018-09-21
BNL (Broadstone Net Lease) Start Date:2020-09-17
BNOX (Bionomics ADS) Start Date:2021-12-16
BNR (Burning Rock Biotech) Start Date:2020-06-12
BNRE (Brookfield Reinsurance Class A Exchangeable) Start Date:2022-12-14
BNRG (Brenmiller Energy Ordinary Shares) Start Date:2022-05-25
BNS (Bank Of Nova Scotia) Start Date:2007-05-08
BNSO (Bonso Electronics International) Start Date:2007-05-16
BNTC (Benitec Biopharma) Start Date:2015-08-18
BNTX (Biontech Se) Start Date:2019-10-10
BNY (Blackrock New York Municipal Income Trust) Start Date:2007-05-16
BNZI (Banzai International Inc) Start Date:2021-02-12
BOC (Boston Omaha Class A) Start Date:2017-06-16
BODY (The Beachbody Company,) Start Date:2021-06-28
BOE (Blackrock Enhanced Global Dividend Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BOF (Branchout Food) Start Date:2023-06-16
BOH (Bank Of Hawaii Corporation) Start Date:2007-01-03
BOKF (Bok Financial) Start Date:2007-05-16
BOLT (Bolt Biotherapeutics) Start Date:2021-02-05
BON (Bon Natural Life) Start Date:2009-06-16
BOOM (Dmc Global) Start Date:2007-05-01
BOOT (Boot Barn) Start Date:2014-10-30
BORR (Borr Drilling Common Shares) Start Date:2019-07-31
BOSC (B.O.S. Better Online Solutions) Start Date:2007-05-16
BOTJ (Bank Of The James Financial) Start Date:2012-01-25
BOWL (Bowlero Class A) Start Date:2021-04-23
BOWN (Bowen Acquisition Corp) Start Date:2023-08-17
BOX (Box) Start Date:2015-01-23
BOXD (Boxed) Start Date:2021-12-09
BOXL (Boxlight Class A) Start Date:2017-11-30
BP (Bp P.L.C.) Start Date:2007-04-30
BPMC (Blueprint Medicines Corporation) Start Date:2015-04-30
BPOP (Popular) Start Date:2007-01-03
BPRN (The Bank Of Princeton) Start Date:2016-07-12
BPT (Bp Prudhoe Bay Royalty Trust) Start Date:2007-04-30
BPTH (Bio-Path Holdings) Start Date:2008-03-04
BPTS (Biophytis) Start Date:2021-02-10
BPYPP (Brookfield Property Partners L.P. 6.50% Class A Cumulative Redeemable Perpetual Preferred Units) Start Date:2019-03-22
BQ (Boqii Holding) Start Date:2020-09-30
BR (Broadridge Financial Solutions) Start Date:2007-05-01
BRAG (Bragg Gaming  Common Shares) Start Date:2021-08-27
BRBR (Bellring Brands) Start Date:2019-10-17
BRBS (Blue Ridge Bankshares) Start Date:2010-08-24
BRC (Brady) Start Date:2007-04-26
BRCC (Brc) Start Date:2022-02-09
BRDG (Bridge Investment) Start Date:2021-07-16
BRDS (Bird Global Class A) Start Date:2021-03-01
BREA (Brera Holdings Plc) Start Date:2023-01-27
BRFH (Barfresh Food) Start Date:2022-01-20
BRFS (Brf S.A.) Start Date:2009-12-10
BRID (Bridgford Foods) Start Date:2007-05-16
BRIV (B. Riley Principal 250 Merger Class A) Start Date:2021-07-06
BRIVU (B. Riley Principal 250 Merger Units) Start Date:2021-05-07
BRIVW (B. Riley Principal 250 Merger Warrant) Start Date:2021-06-29
BRK.A (Berkshire Hathaway) Start Date:2007-05-16
BRK.B (Berkshire Hathaway) Start Date:2007-05-02
BRKL (Brookline Bancorp) Start Date:2007-05-01
BRKR (Bruker) Start Date:2007-05-04
BRLT (Brilliant Earth  Class A) Start Date:2021-09-23
BRN (Barnwell Industries) Start Date:2007-05-16
BRNS (Barinthus Biotherapeutics Plc) Start Date:2021-04-30
BRO (Brown & Brown) Start Date:2007-01-03
BROG (Brooge Energy Ordinary Shares) Start Date:2018-07-13
BROGW (Brooge Holdings Warrant Expiring 12/20/2024) Start Date:2018-07-13
BROS (Dutch Bros) Start Date:2021-09-15
BRP (Brp) Start Date:2019-10-24
BRQS (Borqs Technologies) Start Date:2015-11-05
BRSH (Bruush Oral Care) Start Date:2022-08-03
BRSP (Brightspire Capital Class A) Start Date:2018-02-01
BRT (Brt Apartments Corp) Start Date:2007-05-16
BRTX (Biorestorative Therapies) Start Date:2021-11-05
BRW (Saba Capital Income & Opportunities Fund Sbi) Start Date:2007-05-03
BRX (Brixmor Property) Start Date:2013-10-30
BRY (Berry Corp) Start Date:2018-07-20
BRZE (Braze) Start Date:2021-11-17
BSAC (Banco Santander-Chile) Start Date:2007-04-27
BSBK (Bogota Financial Corp) Start Date:2020-01-16
BSBR (Banco Santander) Start Date:2009-10-07
BSET (Bassett Furniture Industries Incorporated) Start Date:2007-05-16
BSFC (Blue Star Foods) Start Date:2020-04-28
BSGM (Biosig Technologies) Start Date:2018-09-21
BSIG (Brightsphere Investment) Start Date:2014-10-09
BSKYU (Big Sky Growth Partners Unit) Start Date:2021-04-29
BSKYW (Big Sky Growth Partners Warrant) Start Date:2021-06-21
BSL (Blackstone Senior Floating Rate Term Fund Common Shares Of Beneficial Interest) Start Date:2010-05-26
BSM (Black Stone Minerals, L.P.) Start Date:2015-05-01
BSQR (Bsquare) Start Date:2007-05-10
BSRR (Sierra) Start Date:2007-05-16
BST (Blackrock Science And Technology Trust Common Shares Of Beneficial Interest) Start Date:2014-10-29
BSTZ (Blackrock Science And Technology Trust Ii Common Shares Of Beneficial Interest) Start Date:2019-06-26
BSVN (Bank7) Start Date:2018-09-20
BSX (Boston Scientific) Start Date:2005-01-03
BSY (Bentley Systems Inc) Start Date:2020-09-23
BTA (Blackrock Long-Term Municipal Advantage Trust Blackrock Long-Term Municipal Advantage Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BTAI (Bioxcel Therapeutics) Start Date:2018-03-08
BTBD (Bt Brands) Start Date:2021-11-12
BTBDW (Bt Brands Warrant) Start Date:2021-11-12
BTBT (Bit Digital Ordinary Shares) Start Date:2018-03-20
BTCM (Bit Mining ADS) Start Date:2013-11-22
BTCS (Btcs) Start Date:2021-09-14
BTCT (Btc Digital Ltd.) Start Date:2018-10-17
BTCY (Biotricity) Start Date:2016-02-18
BTG (B2gold) Start Date:2008-10-29
BTI (British American Tobacco Industries P.L.C. ADR) Start Date:2007-05-11
BTM (Bitcoin Depot Inc) Start Date:2022-04-19
BTMD (Biote Class A) Start Date:2021-04-28
BTMDW (Biote Warrant) Start Date:2021-04-29
BTN (Ballantyne Strong) Start Date:2007-05-16
BTO (John Hancock Financial Opportunities Fund) Start Date:2007-05-16
BTOG (Bit Origin Ordinary Shares) Start Date:2019-08-14
BTT (Blackrock Municipal 2030 Target Term Trust) Start Date:2012-08-29
BTTR (Better Choice Company) Start Date:2021-06-29
BTTX (Better Therapeutics) Start Date:2021-10-29
BTU (Peabody Energy Corporation) Start Date:2017-04-03
BTWNU (Bridgetown Holdings Units) Start Date:2020-10-16
BTWNW (Bridgetown Holdings Warrants) Start Date:2020-12-07
BTX (Brooklyn Immunotherapeutics,) Start Date:2021-03-26
BTZ (Blackrock Credit Allocation Income Trust) Start Date:2007-05-16
BUD (Anheuser-Busch Inbev Sa) Start Date:2009-09-16
BUI (Blackrock Utility Infrastructure & Power Opportunities Trust) Start Date:2011-11-23
BUJA (Bukit Jalil Global Acquisition 1 Ltd.) Start Date:2023-08-21
BUR (Burford Capital Ordinary Shares) Start Date:2016-04-06
BURL (Burlington Stores) Start Date:2013-10-02
BURU (Nuburu) Start Date:2023-02-01
BUSE (First Busey) Start Date:2007-05-16
BV (Brightview) Start Date:2018-06-28
BVH (Bluegreen Vacations Holding Corporation) Start Date:2017-07-13
BVN (Compania De Minas Buenaventura S.A.A.) Start Date:2007-01-03
BVS (Bioventus) Start Date:2021-02-11
BW (Babcock & Wilcox Enterprises,) Start Date:2015-07-01
BWA (Borgwarner) Start Date:2005-01-03
BWAQ (Blue World Acquisition Corporation) Start Date:2022-03-16
BWAY (Brainsway American Depositary Shares) Start Date:2019-04-17
BWB (Bridgewater Bancshares) Start Date:2018-03-14
BWEN (Broadwind) Start Date:2008-03-04
BWFG (Bankwell Financial) Start Date:2014-05-15
BWG (Brandywineglobal Global Income Opportunities Fund) Start Date:2012-03-28
BWMN (Bowman Consulting) Start Date:2021-05-07
BWMX (Betterware De Mexico, S.A.B. De C.V.) Start Date:2020-03-16
BWXT (Bwx Technologies) Start Date:2010-08-02
BX (Blackstone) Start Date:2007-06-22
BXC (Bluelinx) Start Date:2007-05-03
BXMT (Blackstone Mortgage Trust) Start Date:2007-05-02
BXMX (Nuveen S&P 500 Buy-Write Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
BXP (Boston Properties) Start Date:2005-01-03
BXRX (Baudax Bio) Start Date:2019-11-14
BXSL (Blackstone Secured Lending Fund Common Shares Of Beneficial Interest) Start Date:2021-10-28
BY (Byline Bancorp) Start Date:2017-06-30
BYD (Boyd Gaming Corporation) Start Date:2007-01-03
BYFC (Broadway Financial) Start Date:2007-05-17
BYM (Blackrock Municipal Income Quality Trust Common Shares Of Beneficial Interest) Start Date:2007-05-16
BYND (Beyond Meat) Start Date:2019-05-02
BYNO (Bynordic Acquisition Corporation) Start Date:2022-04-05
BYON (Beyond Inc) Start Date:2007-04-26
BYRN (Byrna Technologies) Start Date:2021-05-05
BYSI (Beyondspring) Start Date:2017-03-09
BYU (Baiyu Holdings Inc) Start Date:2015-04-22
BZ (Kanzhun) Start Date:2021-06-11
BZFD (Buzzfeed Class A) Start Date:2021-12-06
BZFDW (Buzzfeed Warrant) Start Date:2021-03-05
BZH (Beazer Homes Usa) Start Date:2007-04-27
BZUN (Baozun) Start Date:2015-05-21
C (Citigroup) Start Date:2011-05-09
C.K (Citigroup Dep Shs Repstg 1/1000Th Pfd Ser K) Start Date:2007-04-26
CAAP (Corporacion America Airports S.A.) Start Date:2018-02-01
CAAS (China Automotive Systems) Start Date:2007-04-11
CABA (Cabaletta Bio) Start Date:2019-10-25
CABO (Cable One) Start Date:2015-06-11
CAC (Camden National) Start Date:2007-05-16
CACC (Credit Acceptance) Start Date:2007-05-08
CACI (Caci International) Start Date:2009-05-04
CACO (Caravelle International) Start Date:2022-12-19
CADE (Cadence Bancorporation) Start Date:2017-04-13
CADL (Candel Therapeutics) Start Date:2021-07-27
CAE (Cae) Start Date:2009-07-02
CAF (Morgan Stanley China A Share Fund) Start Date:2007-05-08
CAG (Conagra Brands) Start Date:2005-01-03
CAH (Cardinal Health) Start Date:2005-01-03
CAKE (Cheesecake Factory) Start Date:2007-04-27
CAL (Caleres) Start Date:2007-04-30
CALA (Calithera Biosciences Co) Start Date:2014-10-02
CALB (California Bancorp) Start Date:2017-07-03
CALC (Calcimedica Inc) Start Date:2020-09-25
CALM (Cal-Maine Foods) Start Date:2007-05-10
CALT (Calliditas Therapeutics) Start Date:2020-06-05
CALX (Calix) Start Date:2010-03-24
CAMP (Calamp) Start Date:2007-04-30
CAMT (Camtek) Start Date:2007-04-24
CAN (Canaan American Depositary Shares) Start Date:2019-11-21
CANB (Can B) Start Date:2011-04-29
CANF (Can-Fite Biopharma Sponsored ADR) Start Date:2012-11-01
CANG (Cango American Depositary Shares Each Representing Two) Start Date:2018-07-26
CANO (Cano Health,) Start Date:2020-07-06
CAPD (iPath Shiller Cape ETN) Start Date:2012-10-11
CAPL (Crossamerica Partners Lp Common Units Representing Partner Interests) Start Date:2012-10-25
CAPR (Capricor Therapeutics) Start Date:2008-05-13
CAPT (Captivision Inc) Start Date:2022-04-04
CAR (Avis Budget) Start Date:2006-09-05
CARA (Cara Therapeutics Common) Start Date:2014-01-31
CARE (Carter Bankshares) Start Date:2007-05-16
CARG (Cargurus) Start Date:2017-10-12
CARM (Carisma Therapeutics Inc) Start Date:2014-02-06
CARR (Carrier Global) Start Date:2020-03-19
CARS (Cars Com) Start Date:2017-05-18
CART (Instacart) Start Date:2023-09-19
CARV (Carver Bancorp) Start Date:2007-07-10
CASA (Casa Systems) Start Date:2017-12-15
CASH (Meta Financial) Start Date:2007-05-16
CASI (Casi Pharmaceuticals) Start Date:2007-04-24
CASS (Cass Information Systems) Start Date:2007-05-16
CASY (Casey's General Stores) Start Date:2007-01-03
CAT (Caterpillar) Start Date:2005-01-03
CATC (Cambridge Bancorp) Start Date:2007-05-18
CATO (Cato) Start Date:2009-10-16
CATX (Perspective Therapeutics Inc) Start Date:2007-05-16
CATY (Cathay General Bancorp) Start Date:2007-01-03
CAUD (Collective Audience Inc) Start Date:2021-09-03
CAVA (Cava) Start Date:2023-06-15
CB (Chubb Limited) Start Date:2008-07-18
CBAN (Colony Bankcorp) Start Date:2007-05-16
CBAT (Cbak Energy Technology) Start Date:2007-05-03
CBAY (Cymabay Therapeutics Comm) Start Date:2014-01-27
CBD (Companhia Brasileira De Distribuicao) Start Date:2007-01-03
CBFV (Cb Financial Svc Cmn) Start Date:2007-05-22
CBH (Allianzgi Convertible & Income 2024 Target Term Fund) Start Date:2017-06-28
CBL (Cbl & Associates Properties) Start Date:2021-11-02
CBNK (Capital Bancorp) Start Date:2018-09-26
CBOE (Cboe Global Markets) Start Date:2010-06-15
CBRE (Cbre) Start Date:2017-01-03
CBRG (Chain Bridge I Class A Ordinary Shares) Start Date:2022-01-04
CBRGU (Chain Bridge I Units) Start Date:2021-11-10
CBRGW (Chain Bridge I Warrants) Start Date:2021-12-31
CBRL (Cracker Barrel Old Country Store) Start Date:2007-01-03
CBSH (Commerce Bancshares) Start Date:2007-05-02
CBT (Cabot Corporation) Start Date:2007-01-03
CBTX (Cbtx) Start Date:2017-11-08
CBU (Community Bank System) Start Date:2007-01-03
CBUS (Cibus Inc) Start Date:2017-07-20
CBZ (Cbiz) Start Date:2007-05-03
CC (Chemours Company) Start Date:2015-06-19
CCAP (Crescent Capital Bdc) Start Date:2020-02-03
CCB (Coastal Financial) Start Date:2018-07-18
CCBG (Capital City Bank) Start Date:2007-05-09
CCCC (C4 Therapeutics) Start Date:2020-10-02
CCCS (Ccc Intelligent Solutions Holdings) Start Date:2021-08-02
CCEL (Cryo-Cell International) Start Date:2007-05-16
CCEP (Coca-Cola European Partners Plc) Start Date:2018-11-07
CCF (Chase) Start Date:2007-05-16
CCI (Crown Castle International) Start Date:2005-01-03
CCJ (Cameco Corporation) Start Date:2007-01-03
CCK (Crown Holdings) Start Date:2005-01-03
CCL (Carnival) Start Date:2005-01-03
CCLD (Carecloud) Start Date:2014-07-23
CCLP (CSI Compressco Lp Common Units) Start Date:2011-06-15
CCM (Concord Medical Services Holdings ADS) Start Date:2009-12-11
CCNC (Code Chain New Continent) Start Date:2015-12-29
CCNE (Cnb Financial) Start Date:2007-05-16
CCO (Clear Channel Outdoor Holdings,) Start Date:2007-05-08
CCOI (Cogent Communications Holdings) Start Date:2007-01-03
CCRD (Corecard) Start Date:2007-05-18
CCRN (Cross Country Healthcare) Start Date:2007-04-27
CCS (Century Communities) Start Date:2014-06-18
CCSI (Consensus Cloud Solutions,) Start Date:2021-09-30
CCU (Compania Cervecerias Unidas S.A.) Start Date:2007-04-30
CCV (Churchill Capital V Class A) Start Date:2021-02-05
CCVI (Churchill Capital Vi Class A) Start Date:2021-04-05
CCZ (Comcast Holdings Zones) Start Date:2018-09-25
CD (Chindata) Start Date:2020-09-30
CDAK (Codiak Biosciences) Start Date:2020-10-14
CDAY (Ceridian Hcm Holding) Start Date:2018-04-26
CDE (Couer Mining) Start Date:2007-04-30
CDIO (Cardio Diagnostics Holdings) Start Date:2022-01-14
CDLX (Cardlytics) Start Date:2018-02-09
CDMO (Avid Bioservices) Start Date:2007-04-25
CDNA (Caredx) Start Date:2014-07-17
CDNS (Cadence Design Systems) Start Date:2005-10-31
CDP (Copt Defense Properties) Start Date:2007-01-03
CDRE (Cadre Holdings) Start Date:2021-11-04
CDRO (Codere Online Luxembourg S.A. Ordinary Shares) Start Date:2021-12-01
CDROW (Codere Online Luxembourg S.A. Warrants) Start Date:2021-12-01
CDT (Conduit Pharmaceuticals Inc) Start Date:2022-03-28
CDTX (Cidara Therapeutics) Start Date:2015-04-15
CDW (Cdw Corporation) Start Date:2013-06-27
CDXC (Chromadex) Start Date:2008-07-15
CDXS (Codexis) Start Date:2010-04-22
CDZI (Cadiz) Start Date:2007-05-16
CDZIP (Cadiz Depositary Shares) Start Date:2021-07-08
CE (Celanese) Start Date:2005-03-01
CEAD (Cea Industries) Start Date:2022-02-11
CEADW (Cea Industries Warrant) Start Date:2022-02-11
CECE (Ceco Environmental) Start Date:2007-05-16
CECO (Ceco Environmental) Start Date:2007-05-16
CEE (The Central And Eastern Europe Fund) Start Date:2007-05-10
CEG (Constellation Energy) Start Date:2022-01-19
CEI (Camber Energy) Start Date:2016-11-30
CEIX (Consol Energy) Start Date:2017-11-14
CELC (Celcuity) Start Date:2017-09-20
CELH (Celsius) Start Date:2010-02-10
CELL (Phenomex Inc) Start Date:2020-07-17
CELU (Celularity Class A) Start Date:2019-08-08
CELUW (Celularity Warrant) Start Date:2021-07-19
CELZ (Creative Medical Technology Holdings) Start Date:2021-12-03
CEM (Clearbridge Mlp And Midstream Fund) Start Date:2010-06-25
CEN (Center Coast Brookfield Mlp & Energy Infrastructure Fund) Start Date:2013-09-26
CENN (Cenntro Electric) Start Date:2013-02-15
CENQW (Cenaq Energy Warrant) Start Date:2021-10-04
CENT (Central Garden & Pet) Start Date:2007-04-30
CENTA (Central Garden & Pet) Start Date:2007-05-16
CENX (Century Aluminum) Start Date:2007-04-27
CEPU (Central Puerto S.A. ADS) Start Date:2018-02-02
CEQP (Crestwood Equity Partners Lp) Start Date:2010-03-24
CERE (Cerevel Therapeutics Holdings,) Start Date:2020-07-30
CERS (Cerus) Start Date:2007-05-02
CERT (Certara) Start Date:2020-12-11
CET (Central Securities) Start Date:2007-05-16
CETU (Cetus Capital Acquisition) Start Date:2023-03-24
CETX (Cemtrex) Start Date:2015-06-25
CETXP (Cemtrex Series 1 Preferred Stock) Start Date:2017-02-17
CEV (Eaton Vance California Municipal Income Trust Shares Of Beneficial Interest) Start Date:2007-05-16
CEVA (Ceva) Start Date:2007-05-16
CF (Cf Industries Holdings Inc) Start Date:2005-10-03
CFB (Crossfirst Bankshares) Start Date:2019-08-15
CFBK (Cf Bankshares) Start Date:2007-05-16
CFFI (C&F Financial) Start Date:2007-05-16
CFFN (Capitol Federal Financial) Start Date:2007-05-02
CFG (Citizens Financial) Start Date:2014-09-24
CFLT (Confluent) Start Date:2021-06-24
CFMS (Conformis) Start Date:2015-07-01
CFR (Cullen/Frost Bankers) Start Date:2007-01-03
CFRX (Contrafect Common) Start Date:2014-09-12
CFSB (Cfsb Bancorp) Start Date:2022-01-13
CG (The Carlyle) Start Date:2012-05-03
CGA (China Green Agriculture) Start Date:2009-03-09
CGAU (Centerra Gold Common Shares) Start Date:2021-04-15
CGBD (Tcg Bdc,) Start Date:2017-06-14
CGC (Canopy Growth Corporation) Start Date:2018-05-24
CGEM (Cullinan Oncology) Start Date:2021-01-08
CGEN (Compugen Ltd) Start Date:2007-05-16
CGNT (Cognyte Software) Start Date:2021-02-02
CGNX (Cognex Corporation) Start Date:2007-01-03
CGRN (Capstone Green Energy) Start Date:2007-05-02
CGTX (Cognition Therapeutics) Start Date:2021-10-08
CHAA (Catcha Investment Class A Ordinary Shares) Start Date:2021-04-05
CHCI (Comstock Holding Companies Class A) Start Date:2007-05-02
CHCO (City Holding) Start Date:2007-05-10
CHCT (Community Healthcare Trust) Start Date:2015-05-21
CHD (Church & Dwight) Start Date:2004-01-02
CHDN (Churchill Downs Incorporated) Start Date:2007-01-03
CHE (Chemed) Start Date:2007-05-08
CHEA (Chenghe Acquisition Co.) Start Date:2022-06-27
CHEF (Chefs Warehouse) Start Date:2011-07-28
CHEK (Check-Cap Ordinary Share) Start Date:2015-03-18
CHEKZ (Check-Cap Series C Warrant) Start Date:2018-05-04
CHGG (Chegg) Start Date:2013-11-13
CHH (Choice Hotels International) Start Date:2007-01-03
CHK (Chesapeake Energy Corporation) Start Date:2021-02-10
CHKEL (Chesapeake Energy Class C Warrants) Start Date:2021-02-10
CHKEW (Chesapeake Energy Class A Warrants) Start Date:2021-02-10
CHKEZ (Chesapeake Energy Class B Warrants) Start Date:2021-02-10
CHKP (Check Point Software Technologies Ltd) Start Date:2004-01-02
CHMG (Chemung Financial) Start Date:2007-05-18
CHMI (Cherry Hill Mortgage Investmen) Start Date:2013-10-04
CHN (China Fund) Start Date:2007-05-11
CHNR (China Natural Resources) Start Date:2007-05-16
CHPT (Chargepoint Holdings,) Start Date:2019-09-16
CHR (Cheer Holding Inc) Start Date:2018-09-12
CHRD (Chord Energy) Start Date:2020-11-20
CHRS (Coherus Biosciences Comm) Start Date:2014-11-06
CHRW (C. H. Robinson Worldwide) Start Date:2006-01-03
CHS (Chico's Fas) Start Date:2007-04-30
CHSCL (Chs Inc Class B Cumulative Redeemable Preferred Stock Series 4) Start Date:2015-01-22
CHSCM (Chs Inc Class B Reset Rate Cumulative Redeemable Preferred Stock Series 3) Start Date:2014-09-10
CHSCN (Chs Inc Preferred Class B Series 2 Reset Rate) Start Date:2014-03-06
CHSCO (Chs Class B Cumulative Redeemable Preferred Stock) Start Date:2013-09-23
CHSN (Chanson International Holding) Start Date:2023-03-30
CHT (Chunghwa Telecom Co. Ltd.) Start Date:2007-04-27
CHTR (Charter Communications) Start Date:2010-09-14
CHUY (Chuy's) Start Date:2012-07-24
CHWY (Chewy) Start Date:2019-06-14
CHX (Championx Holding) Start Date:2018-04-27
CI (Cigna) Start Date:2004-01-02
CIA (Citizens) Start Date:2007-05-07
CIB (Bancolombia S.A.) Start Date:2007-05-03
CIEN (Ciena Corporation) Start Date:2006-12-01
CIF (Mfs Intermediate High Income Fund) Start Date:2007-05-16
CIFR (Cipher Mining) Start Date:2021-08-25
CIFRW (Cipher Mining Warrant) Start Date:2020-12-07
CIG (Companhia Energetica De Minas Gerais) Start Date:2007-01-03
CIGI (Colliers International  Subordinate Voting Shares) Start Date:2007-05-16
CII (Blackrock Capital And Income Fund) Start Date:2007-05-16
CIIGU (Ciig Capital Partners Ii Unit) Start Date:2021-09-15
CIIGW (Ciig Capital Partners Ii Warrant) Start Date:2021-11-05
CIK (Credit Suisse Asset Management Income Fund) Start Date:2007-05-08
CIM (Chimera Investment Corporation) Start Date:2007-11-16
CINF (Cincinnati Financial) Start Date:2004-01-02
CING (Cingulate) Start Date:2021-12-08
CINGW (Cingulate Warrants) Start Date:2021-12-08
CINT (Ci&T Inc) Start Date:2021-11-10
CIO (City Office Reit) Start Date:2014-04-15
CION (Cion Investment) Start Date:2021-10-05
CIR (Circor International) Start Date:2007-05-10
CISO (Cerberus Cyber Sentinel) Start Date:2020-06-26
CISS (C3is Inc) Start Date:2023-06-13
CIVB (Civista Bancshares) Start Date:2007-05-16
CIVI (Civitas Resources,) Start Date:2014-09-17
CIX (Compx International) Start Date:2007-05-16
CIXX (Ci Financial) Start Date:2020-11-05
CIZN (Citizens Holding Company) Start Date:2007-05-16
CJJD (China Jo-Jo Drugstores) Start Date:2010-04-22
CKPT (Checkpoint Therapeutics) Start Date:2016-12-19
CKX (Ckx Lands) Start Date:2007-05-17
CL (Colgate-Palmolive) Start Date:2004-01-02
CLAR (Clarus Corp) Start Date:2017-09-01
CLB (Core Laboratories N.V.) Start Date:2007-04-27
CLBK (Columbia Financial) Start Date:2018-04-20
CLBT (Cellebrite Di Ordinary Shares) Start Date:2021-08-31
CLBTW (Cellebrite Di Warrants) Start Date:2021-08-31
CLDT (Chatham Lodging) Start Date:2010-04-16
CLDX (Celldex Therapeutics, Inc) Start Date:2008-10-01
CLEU (China Liberal Education Holdings) Start Date:2020-05-08
CLF (Cleveland-Cliffs) Start Date:2004-01-02
CLFD (Clearfield) Start Date:2008-01-02
CLGN (Collplant Biotechnologies Ordinary Shares) Start Date:2018-01-31
CLH (Clean Harbors) Start Date:2008-12-15
CLIR (Clearsign Technologies) Start Date:2012-04-25
CLLS (Cellectis S.A. American Depositary Shares) Start Date:2015-03-25
CLM (Cornerstone Strategic Value Fund New) Start Date:2007-05-04
CLMB (Climb Global Solutions) Start Date:2007-05-16
CLMT (Calumet Specialty Products Partners, L.P.) Start Date:2007-05-16
CLNE (Clean Energy Fuels) Start Date:2007-05-25
CLNN (Clene) Start Date:2020-12-31
CLNNW (Clene Warrant) Start Date:2020-12-31
CLOE (Clover Leaf Capital Class A) Start Date:2021-09-10
CLOER (Clover Leaf Capital Rights) Start Date:2021-09-10
CLOV (Clover Health Investments, Corp) Start Date:2021-01-08
CLPR (Clipper Realty) Start Date:2017-02-10
CLPS (Clps Incorporation) Start Date:2018-05-24
CLPT (Clearpoint Neuro) Start Date:2019-07-03
CLRB (Cellectar Biosciences) Start Date:2010-02-24
CLRC (Climaterock Class A Ordinary Shares) Start Date:2022-06-02
CLRCR (Climaterock Right) Start Date:2022-06-02
CLRCU (Climaterock Unit) Start Date:2022-04-28
CLRCW (Climaterock Warrant) Start Date:2022-06-02
CLRO (Clearone) Start Date:2007-05-16
CLS (Celestica,) Start Date:2007-04-30
CLSD (Clearside Biomedical) Start Date:2016-06-02
CLSK (Cleanspark Inc) Start Date:2012-07-18
CLST (Catalyst Bancorp) Start Date:2021-10-13
CLVR (Clever Leaves Holdings Common Shares) Start Date:2020-12-18
CLVRW (Clever Leaves Holdings Warrant) Start Date:2020-12-18
CLVS (Clovis Oncology) Start Date:2011-11-16
CLVT (Clarivate Plc) Start Date:2018-10-29
CLW (Clearwater) Start Date:2008-12-17
CLWT (Euro Tech Holdings Company) Start Date:2007-04-17
CLX (The Clorox Company) Start Date:2004-01-02
CM (Canadian Imperial Bank Of Commerce) Start Date:2007-01-03
CMA (Comerica) Start Date:2004-01-02
CMAX (Caremax) Start Date:2021-06-04
CMAXW (Caremax Warrant) Start Date:2020-09-28
CMBM (Cambium Networks Corp) Start Date:2019-06-26
CMC (Commercial Metals Company) Start Date:2007-01-03
CMCL (Caledonia Mining Corp) Start Date:2017-06-29
CMCM (Cheetah Mobile American Depositary Shares Each Representing 10 Class Ordinary Shares) Start Date:2014-05-08
CMCO (Columbus Mckinnon) Start Date:2007-04-27
CMCSA (Comcast) Start Date:2004-01-02
CMCT (Cim Commercial Trust) Start Date:2007-05-16
CME (Cme) Start Date:2004-01-02
CMG (Chipotle Mexican Grill) Start Date:2006-01-26
CMI (Cummins) Start Date:2004-01-02
CMLS (Cumulus Media Class A) Start Date:2018-08-01
CMMB (Chemomab Therapeutics American Depositary Share) Start Date:2019-02-12
CMND (Clearmind Medicine) Start Date:2022-11-15
CMP (Compass Minerals) Start Date:2007-04-30
CMPO (Composecure Class A) Start Date:2021-12-28
CMPOW (Composecure Warrant) Start Date:2020-11-19
CMPR (Cimpress) Start Date:2019-12-05
CMPS (Compass Pathways Plc) Start Date:2020-09-18
CMPX (Compass Therapeutics) Start Date:2021-08-13
CMRA (Comera Life Sciences Holdings) Start Date:2022-05-20
CMRAW (Comera Life Sciences Holdings Warrant) Start Date:2022-05-20
CMRE (Costamare) Start Date:2010-11-04
CMRX (Chimerix) Start Date:2013-04-11
CMS (Cms Energy) Start Date:2004-01-02
CMT (Core Molding Technologies Inc) Start Date:2007-04-20
CMTG (Claros Mortgage Trust) Start Date:2021-11-03
CMTL (Comtech Telecommunications) Start Date:2007-05-03
CMU (Mfs Municipal Income Trust) Start Date:2007-05-16
CNA (Cna Financial Corporation) Start Date:2007-01-03
CNC (Centene Corporation) Start Date:2004-01-02
CNDT (Conduent) Start Date:2016-12-13
CNET (Zw Data Action Technologies) Start Date:2010-09-14
CNEY (Cn Energy) Start Date:2021-02-05
CNF (Cnfinance Holdings American Depositary Shares Each Representing Twenty) Start Date:2018-11-07
CNFR (Conifer Holdings) Start Date:2015-08-13
CNHI (Cnh Industrial N.V.) Start Date:2013-09-30
CNI (Canadian National Railway) Start Date:2007-05-01
CNK (Cinemark) Start Date:2007-05-16
CNM (Core & Main) Start Date:2021-07-23
CNMD (Conmed) Start Date:2020-04-14
CNNE (Cannae Holdings) Start Date:2017-11-20
CNOB (Connectone Bancorp) Start Date:2007-05-16
CNP (Centerpoint Energy) Start Date:2004-01-02
CNQ (Canadian Natural Resources Limited) Start Date:2007-01-03
CNS (Cohen & Steers) Start Date:2007-01-03
CNSL (Consolidated Comm) Start Date:2007-05-03
CNSP (Cns Pharmaceuticals) Start Date:2019-11-08
CNTA (Centessa Pharmaceuticals) Start Date:2021-05-28
CNTB (Connect Biopharma) Start Date:2021-03-19
CNTG (Centogene Bv) Start Date:2019-11-07
CNTX (Context Therapeutics) Start Date:2021-10-20
CNTY (Century Casinos) Start Date:2007-05-07
CNVS (Cinedigm Corp) Start Date:2008-11-28
CNX (Cnx Resources Corporation) Start Date:2004-01-02
CNXA (Connexa Sports Technologies) Start Date:2022-06-15
CNXC (Concentrix) Start Date:2020-11-24
CNXN (Pc Connection) Start Date:2007-05-01
COCO (The Vita Coco Company) Start Date:2021-10-21
COCP (Cocrystal Pharma) Start Date:2018-03-12
CODA (Coda Octopus) Start Date:2017-07-19
CODI (Compass Diversified) Start Date:2007-05-11
CODX (Co-Diagnostics) Start Date:2017-07-12
COE (China Online Education American Depositary Shares Each Representing 15 Class A Ordinary Shares) Start Date:2016-06-10
COEP (Coeptis Therapeutics Holdings) Start Date:2008-12-09
COF (Capital One Financial) Start Date:2004-01-02
COFS (Choiceone Financial) Start Date:2007-05-16
COGT (Cogent Biosciences) Start Date:2018-03-29
COHN (Cohen & Company) Start Date:2010-01-04
COHR (Coherent) Start Date:2007-05-03
COHU (Cohu) Start Date:2007-05-02
COIN (Coinbase) Start Date:2021-04-14
COKE (Coca-Cola Bottling) Start Date:2007-05-16
COLB (Columbia Banking System) Start Date:2007-01-03
COLD (Americold Realty Trust) Start Date:2018-01-19
COLIU (Colicity Units) Start Date:2021-02-24
COLIW (Colicity Warrant) Start Date:2021-04-16
COLL (Collegium Pharmaceutical) Start Date:2015-05-07
COLM (Columbia Sportswear Company) Start Date:2007-01-03
COMM (Commscope Holding Company) Start Date:2013-10-25
COMP (Compass) Start Date:2021-04-01
COMS (Comsovereign Holding) Start Date:2021-01-22
COMSW (Comsovereign Holding Warrants) Start Date:2021-01-22
CONN (Conn's) Start Date:2007-05-04
CONX (Conx) Start Date:2020-12-21
CONXU (Conx Unit) Start Date:2020-11-02
CONXW (Conx Warrant) Start Date:2020-12-21
COO (The Cooper Companies) Start Date:2004-01-02
COOK (Traeger) Start Date:2021-07-29
COOP (Mr. Cooper) Start Date:2012-03-28
COP (Conocophillips) Start Date:2004-01-02
COR (Cencora Inc) Start Date:2005-01-03
CORR (Corenergy Infrastructure) Start Date:2007-05-16
CORT (Corcept Therapeutics) Start Date:2007-05-16
CORZ (Core Scientific) Start Date:2021-04-08
COSM (Cosmos Holdings) Start Date:2012-10-11
COST (Costco Wholesale) Start Date:2007-04-30
COTY (Coty) Start Date:2013-06-13
COUR (Coursera) Start Date:2021-03-31
COYA (Coya Therapeutics) Start Date:2022-12-29
CP (Canadian Pacific Railway Limited) Start Date:2007-01-03
CPA (Copa Holdings S.A.) Start Date:2007-01-03
CPAC (Cementos Pacasmayo S.A.A. American Depositary Shares) Start Date:2013-02-11
CPB (Campbell Soup) Start Date:2004-01-02
CPE (Callon Petroleum Company) Start Date:2007-05-04
CPF (Central Pacific Financial) Start Date:2007-05-02
CPG (Crescent Point Energy) Start Date:2014-01-22
CPHC (Canterbury Park Holding 'New') Start Date:2016-07-01
CPHI (China Pharma Holdings) Start Date:2007-05-16
CPIX (Cumberland Pharmaceuticals) Start Date:2009-08-11
CPK (Chesapeake Utilities) Start Date:2007-05-16
CPLP (Capital Product Partners L.P. Common Units) Start Date:2007-05-16
CPNG (Coupang) Start Date:2021-03-11
CPOP (Pop Culture) Start Date:2021-06-30
CPRI (Capri Holdings) Start Date:2011-12-15
CPRT (Copart Inc) Start Date:2004-01-02
CPRX (Catalyst Pharmaceutical) Start Date:2007-05-16
CPS (Cooper Standard) Start Date:2013-10-17
CPSH (Cps Technologies) Start Date:2007-05-16
CPSI (Computer Programs And Sys) Start Date:2007-05-02
CPSS (Consumer Portfolio Services) Start Date:2007-05-16
CPT (Camden Property Trust) Start Date:2007-01-03
CPTN (Cepton) Start Date:2022-02-11
CPTNW (Cepton Warrant) Start Date:2021-03-23
CPZ (Calamos Long/Short Equity & Dynamic Income Trust) Start Date:2019-11-26
CQP (Cheniere Energy Partners L.P.) Start Date:2007-03-21
CR (Crane Co.) Start Date:2023-04-03
CRAI (Cra International) Start Date:2007-05-10
CRBG (Corebridge Financial) Start Date:2022-09-15
CRBP (Corbus Pharmaceuticals) Start Date:2015-04-16
CRBU (Caribou Biosciences) Start Date:2021-07-23
CRC (California Resources Corp) Start Date:2020-11-02
CRCT (Cricut) Start Date:2021-03-25
CRD.A (Crawford & Company) Start Date:2007-05-16
CRD.B (Crawford & Company) Start Date:2007-05-10
CRDF (Cardiff Oncology) Start Date:2010-03-02
CRDL (Cardiol Therapeutics Class A Common Shares) Start Date:2021-08-10
CRDO (Credo Technology Holding) Start Date:2022-01-27
CREG (Smart Powerr) Start Date:2010-03-22
CRESW (Cresud S.A.C.I.F. Y A. Warrant) Start Date:2021-06-25
CRESY (Cresud S.A.C.I.F. Y A. American Depositary Shares) Start Date:2007-05-01
CREX (Creative Realities) Start Date:2018-11-15
CREXW (Creative Realities Warrant) Start Date:2018-11-15
CRF (Cornerstone Total Return Fund) Start Date:2007-05-16
CRGE (Charge Enterprises) Start Date:2022-04-12
CRGO (Freightos) Start Date:2023-01-26
CRGX (Cargo Therapeutics) Start Date:2023-11-10
CRGY (Crescent Energy Company Class A) Start Date:2021-12-08
CRH (Crh Plc) Start Date:2007-01-03
CRHC (Cohn Robbins Holdings) Start Date:2020-11-02
CRI (Carter's) Start Date:2007-01-03
CRIS (Curis Inc) Start Date:2007-05-07
CRK (Comstock Resources) Start Date:2007-04-30
CRKN (Crown Electrokinetics) Start Date:2021-01-26
CRL (Charles River Laboratories International) Start Date:2007-01-03
CRM (Salesforce.com) Start Date:2004-06-23
CRMD (Cormedix) Start Date:2010-05-13
CRMT (America's Car-Mart) Start Date:2007-04-27
CRNC (Cerence) Start Date:2019-09-16
CRNT (Ceragon Networks Ordinary Shares) Start Date:2007-05-10
CRNX (Crinetics Pharmaceuticals) Start Date:2018-07-18
CRON (Cronos) Start Date:2018-02-27
CROX (Crocs) Start Date:2017-01-18
CRS (Carpenter Technology) Start Date:2007-04-27
CRSP (Crispr Therapeutics Ag) Start Date:2016-10-19
CRSR (Corsair Gaming) Start Date:2020-09-23
CRT (Cross Timbers Royalty Trust) Start Date:2007-05-16
CRTDW (Creatd Warrant) Start Date:2020-09-11
CRTO (Criteo S.A. American Depositary Shares) Start Date:2013-10-30
CRUS (Cirrus Logic) Start Date:2007-01-03
CRVL (Corvel) Start Date:2007-04-17
CRVO (Cervomed Inc) Start Date:2016-11-14
CRVS (Corvus Pharmaceuticals) Start Date:2016-03-23
CRWD (Crowdstrike Holdings) Start Date:2019-06-12
CRWS (Crown Crafts Inc) Start Date:2007-05-16
CRZNU (Corazon Capital V838 Monoceros Unit) Start Date:2021-03-24
CSAN (Cosan S.A. ADS) Start Date:2021-03-08
CSBR (Champions Oncology) Start Date:2015-08-26
CSCO (Cisco Systems) Start Date:2004-01-02
CSCW (Color Star Technology Co. Ordinary Shares) Start Date:2008-12-23
CSGP (Costar) Start Date:2007-05-03
CSGS (Csg Systems International) Start Date:2007-04-30
CSIQ (Canadian Solar Common Shares) Start Date:2007-04-30
CSL (Carlisle Companies) Start Date:2007-05-03
CSPI (Csp) Start Date:2007-05-16
CSR (Centerspace) Start Date:2007-11-01
CSSE (Chicken Soup For The Soul Entertainment Class A) Start Date:2017-08-18
CSTE (Caesarstone) Start Date:2012-03-22
CSTL (Castle Biosciences) Start Date:2019-07-25
CSTM (Constellium Se Class A Ordinary Shares) Start Date:2013-05-23
CSTR (Capstar Financial) Start Date:2016-09-22
CSV (Carriage Services) Start Date:2007-05-16
CSWC (Capital Southwest Corp) Start Date:2007-05-16
CSWI (Csw Industrials) Start Date:2015-09-30
CSX (Csx) Start Date:2004-01-02
CTAS (Cintas Corporation) Start Date:2004-01-02
CTBI (Community Trust Bancorp) Start Date:2007-05-07
CTG (Computer Task) Start Date:2007-05-16
CTGO (Contango Ore) Start Date:2010-12-20
CTHR (Charles & Colvard) Start Date:2007-05-08
CTKB (Cytek Biosciences) Start Date:2021-07-23
CTLP (Cantaloupe,) Start Date:2007-05-16
CTLT (Catalent) Start Date:2014-07-31
CTM (Castellum) Start Date:2022-10-13
CTMX (Cytomx Therapeutics) Start Date:2015-10-08
CTNT (Cheetah Net Supply Chain Service) Start Date:2023-08-01
CTO (Cto Realty Growth) Start Date:2007-05-16
CTOS (Custom Truck One Source,) Start Date:2017-10-06
CTR (Clearbridge Mlp And Midstream Total Return Fund) Start Date:2012-06-27
CTRA (Coterra Energy) Start Date:2007-04-27
CTRE (Caretrust Reit) Start Date:2014-05-23
CTRM (Castor Maritime Common Shares) Start Date:2019-02-11
CTRN (Citi Trends) Start Date:2007-04-30
CTS (Cts) Start Date:2007-05-03
CTSH (Cognizant Technology Solutions) Start Date:2004-01-02
CTSO (Cytosorbents Corp) Start Date:2014-12-23
CTV (Innovid) Start Date:2021-04-05
CTVA (Corteva) Start Date:2019-05-24
CTXR (Citius Pharmaceuticals) Start Date:2017-08-03
CUBA (Herzfeld Caribbean Basin Fund) Start Date:2007-05-16
CUBE (Cubesmart) Start Date:2007-05-01
CUBI (Customers Bancorp Common) Start Date:2013-05-16
CUE (Cue Biopharma) Start Date:2018-01-02
CUEN (Cuentas) Start Date:2021-02-02
CUK (Carnival & Plc) Start Date:2007-01-03
CULL (Cullman Bancorp) Start Date:2009-10-09
CULP (Culp) Start Date:2007-05-16
CURI (Curiositystream Class A) Start Date:2020-01-08
CURIW (Curiositystream Warrant) Start Date:2020-01-07
CURO (Curo  Corp) Start Date:2017-12-07
CURV (Torrid Holdings) Start Date:2021-07-01
CUTR (Cutera) Start Date:2007-05-04
CUZ (Cousins Properties Incorporated) Start Date:2007-01-03
CVAC (Curevac N.V.) Start Date:2020-08-14
CVBF (Cvb Financial) Start Date:2009-07-22
CVCO (Cavco Industries) Start Date:2007-05-09
CVCY (Central Valley Comm Bank) Start Date:2007-05-16
CVE (Cenovus Energy) Start Date:2009-12-09
CVEO (Civeo Corporation) Start Date:2014-06-02
CVGI (Commercial Vehicle) Start Date:2007-05-02
CVGW (Calavo Growers) Start Date:2007-05-16
CVI (Cvr Energy) Start Date:2007-10-23
CVII (Churchill Capital Vii Class A) Start Date:2021-04-05
CVKD (Cadrenal Therapeutics) Start Date:2023-01-20
CVLG (Covenant Logistics  Class A) Start Date:2007-05-16
CVLT (Commvault Systems) Start Date:2007-05-08
CVLY (Codorus Valley Bancorp) Start Date:2007-05-16
CVM (Cel-Sci) Start Date:2007-05-16
CVNA (Carvana Co.) Start Date:2017-04-28
CVR (Chicago Rivet & Machine Co.) Start Date:2007-05-16
CVRX (Cvrx) Start Date:2021-06-30
CVS (Cvs Health) Start Date:2004-01-02
CVU (Cpi Aerostructures) Start Date:2022-10-05
CVV (Cvd Equipment) Start Date:2007-05-16
CVX (Chevron) Start Date:2004-01-02
CW (Curtiss-Wright Corporation) Start Date:2007-01-03
CWAN (Clearwater Analytics) Start Date:2021-09-24
CWBC (Community West Bancshares) Start Date:2007-05-16
CWBR (Cohbar) Start Date:2015-01-28
CWCO (Consolidated Water) Start Date:2007-05-10
CWD (Calibercos) Start Date:2023-05-17
CWEN (Clearway Energy) Start Date:2018-09-17
CWEN.A (Clearway Energy) Start Date:2018-09-17
CWK (Cushman & Wakefield Plc) Start Date:2018-08-02
CWST (Casella Waste Systems) Start Date:2007-01-03
CWT (California Water Service) Start Date:2007-01-03
CX (Cemex S.A.B. De C.V.) Start Date:2007-01-03
CXAI (Cxapp Inc) Start Date:2021-02-04
CXDO (Crexendo) Start Date:2015-01-13
CXE (Mfs High Income Municipal Trust) Start Date:2007-05-16
CXH (Mfs Investment Grade Municipal Trust) Start Date:2007-05-16
CXM (Sprinklr) Start Date:2021-06-23
CXT (Crane Nxt Co.) Start Date:2007-01-03
CXW (Corecivic) Start Date:2007-04-26
CYAD (Celyad Oncology Sa American Depositary Shares) Start Date:2015-06-19
CYAN (Cyanotech) Start Date:2007-05-16
CYBN (Cybin Common Shares) Start Date:2021-08-05
CYBR (Cyberark Software Ltd.) Start Date:2014-09-24
CYCC (Cyclacel Pharmaceuticals) Start Date:2007-05-16
CYCN (Cyclerion Therapeutics) Start Date:2019-03-18
CYD (China Yuchai International) Start Date:2007-05-04
CYH (Community Health Systems) Start Date:2007-04-26
CYN (Cyngn) Start Date:2021-10-20
CYRN (Cyren Ordinary Shares) Start Date:2007-05-16
CYRX (Cryoport) Start Date:2015-07-24
CYT (Cyteir Therapeutics) Start Date:2021-06-18
CYTH (Cyclo Therapeutics) Start Date:2011-02-18
CYTHW (Cyclo Therapeutics Warrant) Start Date:2020-12-09
CYTK (Cytokinetics Com) Start Date:2007-05-04
CYTO (Altamira Therapeutics Common Shares 0.01 Sf) Start Date:2014-08-06
CYXT (Cyxtera Technologies) Start Date:2020-11-02
CZFS (Citizens Financial Services) Start Date:2007-05-24
CZNC (Citizens And Northern) Start Date:2007-05-16
CZOO (Cazoo Class A Ordinary Shares) Start Date:2021-08-27
CZR (Caesars Entertainment Corporation) Start Date:2014-09-22
CZWI (Citizens Community Bancorp) Start Date:2007-05-16
D (Dominion Energy) Start Date:2005-01-03
DAC (Danaos Corporation) Start Date:2007-04-20
DADA (Dada Nexus Limited) Start Date:2020-06-05
DAIO (Data I/O) Start Date:2007-05-16
DAKT (Daktronics) Start Date:2007-04-30
DAL (Delta Air Lines) Start Date:2007-05-16
DALN (Dallasnews Series A) Start Date:2021-06-29
DAN (Dana) Start Date:2008-02-01
DAO (Youdao) Start Date:2019-10-25
DAR (Darling Ingredients) Start Date:2007-01-03
DARE (Dare Bioscience) Start Date:2014-04-10
DASH (Doordash) Start Date:2020-12-09
DATS (Datchat) Start Date:2021-08-13
DATSW (Datchat Series A Warrant) Start Date:2021-08-13
DAVA (Endava Plc American Depositary Shares) Start Date:2018-07-27
DAVE (Dave Class A) Start Date:2022-01-06
DAVEW (Dave Warrants) Start Date:2022-01-06
DAWN (Day One Biopharmaceuticals) Start Date:2021-05-27
DB (Deutsche Bank Aktiengesellschaft) Start Date:2007-01-03
DBGI (Digital Brands) Start Date:2021-05-14
DBGIW (Digital Brands  Warrant) Start Date:2021-05-14
DBI (Designer Brands) Start Date:2007-04-30
DBL (Doubleline Opportunistic Credit Fund Common Shares Of Beneficial Interest) Start Date:2012-01-27
DBRG (Digitalbridge ,) Start Date:2014-06-27
DBTX (Decibel Therapeutics) Start Date:2021-02-12
DBVT (DBv Technologies S.A.) Start Date:2014-10-22
DBX (Dropbox) Start Date:2018-03-23
DC (Dakota Gold) Start Date:2022-04-05
DCBO (Docebo) Start Date:2020-12-03
DCF (Bny Mellon Alcentra Global Credit Income 2024 Target Term Fund) Start Date:2017-10-27
DCFC (Tritium Dcfc) Start Date:2022-01-14
DCFCW (Tritium Dcfc Warrant) Start Date:2022-01-14
DCGO (Docgo) Start Date:2021-11-01
DCI (Donaldson) Start Date:2007-04-23
DCO (Ducommun) Start Date:2007-05-10
DCOM (Dime Community Bancshares) Start Date:2007-05-16
DCOMP (Dime Community Bancshares Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2020-02-13
DCPH (Deciphera Pharmaceuticals) Start Date:2017-09-28
DCTH (Delcath Systems) Start Date:2018-05-02
DD (Dupont De Nemours) Start Date:2019-06-03
DDC (Ddc Enterprise Limited) Start Date:2023-11-17
DDD (3D Systems) Start Date:2011-05-26
DDF (Delaware Investments Dividend & Income Fund) Start Date:2007-05-16
DDI (Doubledown Interactive Co. ADS) Start Date:2021-08-31
DDL (Dingdong) Start Date:2021-06-29
DDOG (Datadog) Start Date:2019-09-19
DDS (Dillard's) Start Date:2005-01-03
DDT (Dillard's Capital Trust I) Start Date:2007-05-16
DE (Deere & Co.) Start Date:2005-01-03
DEA (Easterly Government Properties) Start Date:2015-02-06
DECA (Denali Capital Acquisition) Start Date:2022-06-07
DECK (Deckers Outdoor Corporation) Start Date:2007-01-03
DEI (Douglas Emmett) Start Date:2007-01-03
DELL (Dell Technologies) Start Date:2018-12-26
DEN (Denbury) Start Date:2020-09-21
DENN (Denny's) Start Date:2007-04-27
DEO (Diageo Plc) Start Date:2007-04-27
DERM (Journey Medical) Start Date:2021-11-12
DESP (Despegar.com,) Start Date:2019-03-07
DEX (Delaware Enhanced Global Dividend Common Shares Of Beneficial Interest) Start Date:2007-06-27
DFH (Dream Finders Homes) Start Date:2021-01-21
DFIN (Donnelley Financial Solutions) Start Date:2016-09-26
DFLI (Dragonfly Energy Holdings) Start Date:2021-08-24
DFP (Flaherty & Crumrine Dynamic Preferred And Income Fund) Start Date:2013-05-24
DFS (Discover Financial Services) Start Date:2007-07-02
DG (Dollar General) Start Date:2009-11-13
DGHI (Digihost Technology Common Subordinate Voting Shares) Start Date:2021-11-15
DGICA (Donegal) Start Date:2007-05-08
DGICB (Donegal  Class B) Start Date:2019-03-01
DGII (Digi International) Start Date:2007-04-27
DGLY (Digital Ally) Start Date:2007-05-16
DGX (Quest Diagnostics) Start Date:2005-01-03
DH (Definitive Healthcare) Start Date:2021-09-15
DHBCU (Dhb Capital Unit) Start Date:2021-03-02
DHBCW (Dhb Capital Warrant) Start Date:2021-04-23
DHC (Diversified Healthcare Trust Common Shares Of Bene) Start Date:2007-04-30
DHF (Bny Mellon High Yield Strategies Fund) Start Date:2007-05-08
DHHCU (Diamondhead Holdings Unit) Start Date:2021-01-26
DHI (D. R. Horton) Start Date:2005-01-03
DHIL (Diamond Hill Investment) Start Date:2007-05-16
DHR (Danaher) Start Date:2005-01-03
DHT (Dht) Start Date:2012-07-17
DHX (Dhi) Start Date:2007-07-18
DHY (Credit Suisse High Yield Bond Fund) Start Date:2007-04-30
DIAX (Nuveen Dow 30Sm Dynamic Overwrite Fund Common Shares Of Beneficial Interest) Start Date:2014-12-22
DIBS (1Stdibs.com) Start Date:2021-06-10
DIN (Dine Brands Global) Start Date:2008-06-02
DINO (Hf Sinclair) Start Date:2019-01-04
DIOD (Diodes) Start Date:2007-04-26
DIS (The Walt Disney Company) Start Date:2005-01-03
DISH (Dish Network) Start Date:2005-01-03
DIST (Distoken Acquisition Corporation) Start Date:2023-03-30
DIT (Amcon Distributing Company) Start Date:2007-05-16
DJCO (Daily Journal) Start Date:2007-05-17
DK (Delek Us) Start Date:2007-04-27
DKL (Delek Logistics Partners, Lp) Start Date:2012-11-02
DKNG (Draftkings) Start Date:2019-07-25
DKS (Dick's Sporting Goods) Start Date:2007-01-03
DLA (Delta Apparel) Start Date:2007-05-16
DLB (Dolby Laboratories) Start Date:2007-05-01
DLHC (Dlh Holdings) Start Date:2008-05-19
DLNG (Dynagas Lng Partners Lp Common Units) Start Date:2013-11-13
DLO (Dlocal) Start Date:2021-06-03
DLPN (Dolphin Entertainment) Start Date:2017-12-21
DLR (Digital Realty Trust Inc) Start Date:2005-01-03
DLTH (Duluth) Start Date:2015-11-20
DLTR (Dollar Tree) Start Date:2007-04-27
DLX (Deluxe) Start Date:2005-01-03
DLY (Doubleline Yield Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2020-02-26
DM (Desktop Metal,) Start Date:2019-05-03
DMA (Destra Multi-Alternative Fund) Start Date:2022-01-13
DMAC (Diamedica Therapeutics) Start Date:2009-06-01
DMB (Bny Mellon Municipal Bond Infrastructure Fund) Start Date:2013-04-26
DMF (Bny Mellon Municipal Income) Start Date:2007-05-16
DMK (Dmk Pharmaceuticals Corp) Start Date:2010-04-07
DMLP (Dorchester Minerals Lp) Start Date:2007-05-03
DMO (Western Asset Mortgage Opportunity Fund) Start Date:2010-02-24
DMRC (Digimarc) Start Date:2007-05-02
DMSL (Digital Media Solutions Inc) Start Date:2020-07-16
DMTK (Dermtech) Start Date:2017-08-10
DMYY (Dmy Squared Technology) Start Date:2022-12-07
DNA (Ginkgo Bioworks Holdings,) Start Date:2021-04-19
DNAB (Social Capital Suvretta Holdings Ii Class A Ordinary Shares) Start Date:2021-06-30
DNAD (Social Capital Suvretta Holdings Iv Class A Ordinary Shares) Start Date:2021-06-30
DNAY (Codex Dna) Start Date:2021-06-18
DNB (Dun & Bradstreet Corporation) Start Date:2020-07-01
DNLI (Denali Therapeutics) Start Date:2017-12-08
DNMR (Danimer Scientific,) Start Date:2020-05-28
DNN (Denison Mines Corp) Start Date:2007-05-16
DNOW (Now) Start Date:2014-06-02
DNP (Dnp Select Income Fund) Start Date:2007-01-03
DNTH (Magenta Therapeutics Inc) Start Date:2018-06-21
DNUT (Krispy Kreme) Start Date:2021-07-01
DO (Diamond Offshore Drilling) Start Date:2022-03-30
DOC (Physicians Realty Trust) Start Date:2013-07-19
DOCN (Digitalocean) Start Date:2021-03-24
DOCS (Doximity) Start Date:2021-06-24
DOCU (Docusign) Start Date:2018-04-27
DOGZ (Dogness) Start Date:2017-12-20
DOLE (Dole) Start Date:2021-07-30
DOMA (Doma Holdings,) Start Date:2021-01-22
DOMH (Dominari Holdings) Start Date:2007-05-16
DOMO (Domo) Start Date:2018-06-29
DOOO (Brp Common Subordinate Voting Shares) Start Date:2013-07-16
DOOR (Masonite International Corp) Start Date:2013-09-09
DORM (Dorman Products) Start Date:2007-05-16
DOUG (Douglas Elliman) Start Date:2021-12-30
DOV (Dover) Start Date:2005-01-03
DOW (Dow) Start Date:2019-03-20
DOX (Amdocs Limited) Start Date:2007-01-03
DOYU (Douyu International Holdings Limited) Start Date:2019-07-17
DPG (Duff & Phelps Utility And Infrastructure Fund) Start Date:2011-07-27
DPRO (Draganfly Common Shares) Start Date:2021-07-30
DPSI (Decisionpoint Systems) Start Date:2020-12-08
DPZ (Domino's Pizza) Start Date:2005-01-03
DQ (Daqo New Energy American Depositary Shares Each Representing Five Ordinary Shares) Start Date:2010-10-07
DRCT (Direct Digital) Start Date:2022-02-11
DRCTW (Direct Digital Holdings Warrant) Start Date:2022-02-11
DRD (Drdgold American Depositary Shares) Start Date:2011-12-29
DRH (Diamondrock Hospitality) Start Date:2007-04-30
DRI (Darden Restaurants) Start Date:2005-01-03
DRIO (Dariohealth) Start Date:2016-03-04
DRMA (Dermata Therapeutics) Start Date:2021-08-13
DRMAW (Dermata Therapeutics Warrant) Start Date:2021-08-13
DRQ (Dril-Quip) Start Date:2007-04-27
DRRX (Durect) Start Date:2007-04-27
DRS (Leonardo Drs) Start Date:2022-11-29
DRTS (Alpha Tau Medical) Start Date:2022-03-08
DRTSW (Alpha Tau Medical Warrant) Start Date:2022-03-08
DRTT (Dirtt Environmental Solutions Common Shares) Start Date:2014-01-28
DRUG (Bright Minds Biosciences) Start Date:2021-11-08
DRVN (Driven Brands) Start Date:2021-01-15
DS (Drive Shack) Start Date:2007-05-02
DSGN (Design Therapeutics) Start Date:2021-03-26
DSGR (Distribution Solutions) Start Date:2007-05-16
DSGX (The Descartes Systems Inc) Start Date:2007-01-03
DSKE (Daseke) Start Date:2015-10-12
DSL (Doubleline Income Solutions Fund Common Shares Of Beneficial Interests) Start Date:2013-04-26
DSM (Bny Mellon Strategic Municipal Bond Fund) Start Date:2007-05-16
DSP (Viant Technology) Start Date:2021-02-10
DSS (Dss) Start Date:2007-05-16
DSU (Blackrock Debt Strategies Fund) Start Date:2007-05-04
DSWL (Deswell Industries Common Shares) Start Date:2007-05-16
DSX (Diana Shipping) Start Date:2007-05-08
DT (Dynatrace) Start Date:2019-08-01
DTC (Solo Brands) Start Date:2021-10-28
DTCK (Davis Commodities Limited) Start Date:2023-09-19
DTE (Dte Energy Co.) Start Date:2005-01-03
DTEA (Davidstea) Start Date:2015-06-05
DTF (Dtf Tax-Free Income 2028 Term Fund) Start Date:2007-05-16
DTIL (Precision Biosciences) Start Date:2019-03-28
DTM (Dt) Start Date:2021-06-18
DTOCU (Digital Transformation Opportunities Units) Start Date:2021-03-10
DTOCW (Digital Transformation Opportunities Warrant) Start Date:2021-05-13
DTSS (Datasea) Start Date:2018-12-19
DTST (Data Storage) Start Date:2021-05-14
DTW (Dte Energy Company 2017 Series E 5.25% Junior Subordinated Debentures Due 2077) Start Date:2017-11-22
DUK (Duke Energy) Start Date:2012-07-03
DUO (Fangdd Network American Depositary Shares) Start Date:2019-11-01
DUOL (Duolingo) Start Date:2021-07-28
DUOT (Duos Technologies) Start Date:2008-09-30
DV (Doubleverify) Start Date:2021-04-21
DVA (Davita) Start Date:2005-01-03
DVAX (Dynavax Technologies) Start Date:2007-04-18
DVN (Devon Energy) Start Date:2005-01-03
DWSN (Dawson Geophysical Company) Start Date:2007-05-09
DX (Dynex Capital) Start Date:2007-05-16
DXC (Dxc Technology) Start Date:2017-03-16
DXCM (Dexcom) Start Date:2005-05-02
DXF (Dunxin Financial Holdings American Depositary Shares) Start Date:2010-11-23
DXLG (Destination Xl) Start Date:2007-04-30
DXPE (Dxp Enterprises) Start Date:2007-05-07
DXR (Daxor) Start Date:2007-05-16
DXYN (Dixie) Start Date:2007-05-16
DY (Dycom Industries) Start Date:2007-04-24
DYAI (Dyadic International) Start Date:2008-01-16
DYN (Dyne Therapeutics) Start Date:2020-09-17
DYNT (Dynatronics) Start Date:2007-05-16
DZSI (Dzs) Start Date:2007-04-30
E (Eni S.P.A.) Start Date:2007-01-03
EA (Electronic Arts) Start Date:2007-04-30
EAD (Allspring Income Opportunities Fund Common Shares) Start Date:2007-05-04
EAI (Entergy Arkansas Llc First Mortgage Bonds 4.875% Series Due September 1 2066) Start Date:2016-08-17
EAR (Eargo) Start Date:2020-10-16
EARN (Ellington Residential Mortgage) Start Date:2013-05-01
EAST (Eastside Distilling) Start Date:2014-04-16
EAT (Brinker International) Start Date:2007-05-01
EB (Eventbrite) Start Date:2018-09-20
EBAY (Ebay) Start Date:2005-01-03
EBC (Eastern Bankshares) Start Date:2020-10-15
EBET (Esports Technologies) Start Date:2021-04-15
EBF (Ennis) Start Date:2007-05-02
EBIX (Ebix) Start Date:2007-05-16
EBMT (Eagle Bancorp Montana) Start Date:2007-05-23
EBON (Ebang International Holdings Class A Ordinary Shares) Start Date:2020-06-26
EBR (Centrais Eletricas Brasileiras S.A. - Eletrobras) Start Date:2016-10-13
EBS (Emergent Biosolutions) Start Date:2007-01-03
EBTC (Enterprise Bancorp) Start Date:2007-05-17
EC (Ecopetrol S.A.) Start Date:2008-09-18
ECAT (Blackrock ESG Capital Allocation Trust Common Shares Of Beneficial Interest) Start Date:2021-09-28
ECBK (Ecb Bancorp) Start Date:2022-07-28
ECC (Eagle Point Credit Company) Start Date:2014-10-08
ECDA (Ecd Automotive Design Inc) Start Date:2022-12-08
ECF (Ellsworth Growth And Income Fund Ltd.) Start Date:2007-05-16
ECL (Ecolab) Start Date:2005-01-03
ECOR (Electrocore) Start Date:2018-06-22
ECPG (Encore Capital) Start Date:2007-05-11
ECVT (Ecovyst) Start Date:2021-08-03
ECX (Ecarx Holdings Class A) Start Date:2022-12-21
ED (Consolidated Edison) Start Date:2005-01-03
EDAP (Edap Tms S.A. American Depositary Shares) Start Date:2007-05-16
EDBL (Edible Garden Ag Incorporated) Start Date:2022-05-05
EDBLW (Edible Garden Ag Incorporated Warrant) Start Date:2022-05-05
EDD (Morgan Stanley Emerging Markets Domestic Debt Fund Morgan Stanley Emerging Markets Domestic Debt Fund) Start Date:2007-05-16
EDF (Virtus Stone Harbor Emerging Markets Income Fund Common Shares Of Beneficial Interest) Start Date:2010-12-23
EDI (Virtus Stone Harbor Emerging Markets Total Income Fund Common Shares Of Beneficial Interest) Start Date:2012-10-26
EDIT (Editas Medicine) Start Date:2016-02-03
EDN (Empresa Distribuidora Y Comercializadora Norte S.A.) Start Date:2007-05-16
EDR (Endeavor Holdings) Start Date:2021-04-29
EDRY (Eurdry Drybulk) Start Date:2018-05-31
EDSA (Edesa Biotech Common Shares) Start Date:2010-06-21
EDTK (Skillful Craftsman) Start Date:2020-07-23
EDU (New Oriental Education & Technology) Start Date:2007-01-03
EDUC (Educational Development) Start Date:2007-05-17
EE (Excelerate Energy Class A) Start Date:2022-04-13
EEA (The European Equity Fund) Start Date:2007-05-16
EEFT (Euronet Worldwide) Start Date:2007-01-03
EEIQ (Elite Education) Start Date:2021-03-25
EEX (Emerald Holding) Start Date:2017-04-28
EFC (Ellington Financial) Start Date:2010-10-08
EFL (Eaton Vance Floating-Rate 2022 Target Term Trust Common Shares Of Beneficial Interest) Start Date:2017-07-27
EFOI (Energy Focus) Start Date:2007-05-16
EFR (Eaton Vance Senior Floating-Rate Fund Common Shares Of Beneficial Interest) Start Date:2007-04-30
EFSC (Enterprise Financial Svcs) Start Date:2007-05-16
EFSH (1847 Holdings Llc) Start Date:2022-08-03
EFT (Eaton Vance Floating Rate Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-03
EFTR (Effector Therapeutics,) Start Date:2021-03-01
EFTRW (Effector Therapeutics Warrant) Start Date:2021-03-01
EFX (Equifax) Start Date:2005-01-03
EFXT (Enerflex Ltd) Start Date:2022-10-13
EG (Everest Ltd.) Start Date:2005-01-03
EGAN (Egain) Start Date:2007-05-16
EGBN (Eagle Bancorp) Start Date:2007-05-16
EGF (Blackrock Enhanced Government Fund) Start Date:2007-05-16
EGHT (8 X 8) Start Date:2007-04-30
EGIO (Edgio) Start Date:2007-06-08
EGLE (Eagle Bulk Shipping Commo) Start Date:2007-05-01
EGLX (Enthusiast Gaming Holdings) Start Date:2019-10-21
EGO (Eldorado Gold Corporation) Start Date:2007-04-27
EGP (Eastgroup Properties) Start Date:2007-01-03
EGRX (Eagle Pharmaceuticals Co) Start Date:2014-02-12
EGY (Vaalco Energy) Start Date:2007-04-30
EH (Ehang Holdings ADS) Start Date:2019-12-12
EHAB (Enhabit) Start Date:2022-06-23
EHC (Encompass Health Corporation) Start Date:2007-05-07
EHI (Western Asset Global High Income Fund Inc) Start Date:2007-05-02
EHTH (Ehealth) Start Date:2007-01-03
EIC (Eagle Point Income Company) Start Date:2019-07-24
EIG (Employers) Start Date:2007-05-16
EIGR (Eiger Biopharmaceuticals) Start Date:2014-01-30
EIM (Eaton Vance Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
EIX (Edison Int'l) Start Date:2007-04-30
EJH (E-Home Household Service Holdings Ordinary Shares) Start Date:2021-05-14
EKSO (Ekso Bionics Holdings) Start Date:2014-01-16
EL (Estee Lauder Cos.) Start Date:2005-01-03
ELA (Envela Corp) Start Date:2016-05-31
ELAB (Elevai Labs) Start Date:2023-11-21
ELAN (Elanco Animal Health Incorporated) Start Date:2018-09-20
ELBM (Electra Battery Materials) Start Date:2022-04-27
ELDN (Eledon Pharmaceuticals) Start Date:2014-09-17
ELEV (Elevation Oncology) Start Date:2021-06-25
ELF (E.L.F. Beauty) Start Date:2016-09-22
ELLO (Ellomay Capital Ordinary Shares) Start Date:2008-10-27
ELMD (Electromed) Start Date:2010-08-13
ELME (Elme Communities) Start Date:2007-05-03
ELOX (Eloxx Pharmaceuticals) Start Date:2012-11-23
ELP (Companhia Paranaense De Energia - Copel) Start Date:2007-01-03
ELS (Equity Lifestyle Properties) Start Date:2007-01-03
ELSE (Electro-Sensors) Start Date:2007-05-16
ELTK (Eltek Ordinary Shares) Start Date:2007-05-16
ELTX (Angion Biomedica) Start Date:2021-02-05
ELUT (Elutia Inc) Start Date:2020-10-08
ELV (Elevance Health) Start Date:2007-04-30
ELVN (Enliven Therapeutics Inc) Start Date:2020-03-12
ELWS (Earlyworks Co.) Start Date:2023-07-25
ELYM (Eliem Therapeutics) Start Date:2021-08-10
ELYS (Elys Game Technology) Start Date:2020-11-10
EM (Smart Share Global) Start Date:2021-04-01
EMAN (Emagin) Start Date:2007-05-16
EMBC (Embecta Corp) Start Date:2022-04-01
EMBKW (Embark Technology Warrants) Start Date:2021-11-11
EMCG (WisdomTree Emerging Markets Consumer Growth Fund) Start Date:2022-09-30
EMD (Western Asset Emerging Markets Debt Fund Inc) Start Date:2007-05-08
EME (Emcor) Start Date:2007-01-03
EMF (Templeton Emerging Markets Fund) Start Date:2007-05-08
EMKR (Emcore) Start Date:2007-04-27
EML (Eastern) Start Date:2007-05-16
EMN (Eastman Chemical) Start Date:2005-01-03
EMO (Clearbridge Energy Midstream Opportunity Fund) Start Date:2011-06-10
EMP (Entergy Mississippi, Llc First Mortgage Bonds, 4.90% Series Due October 1, 2066) Start Date:2016-09-16
EMR (Emerson Electric Company) Start Date:2005-01-03
EMX (Emx Royalty Common Shares) Start Date:2008-10-27
ENB (Enbridge, Inc) Start Date:2007-04-30
ENCP (Energem Class A Ordinary Shares) Start Date:2022-01-10
ENCPW (Energem Warrant) Start Date:2022-01-10
ENFN (Enfusion Class A) Start Date:2021-10-21
ENG (Englobal) Start Date:2007-05-08
ENIC (Enel Chile S.A.) Start Date:2016-04-21
ENJ (Entergy New Orleans Llc First Mortgage Bonds 5.0% Series Due December 1 2052) Start Date:2012-12-05
ENLC (Enlink Midstream, Llc) Start Date:2014-03-10
ENLT (Enlight Renewable Energy) Start Date:2023-02-10
ENLV (Enlivex Therapeutics Ordinary Shares) Start Date:2014-07-31
ENO (Entergy New Orleans Llc First Mortgage Bonds 5.50% Series Due April 1 2066) Start Date:2016-03-24
ENOV (Enovis) Start Date:2008-05-08
ENPC (Executive Network Partnering) Start Date:2020-11-06
ENPH (Enphase Energy) Start Date:2012-03-30
ENR (Energizer Holdings) Start Date:2015-07-01
ENS (Enersys) Start Date:2007-01-03
ENSC (Ensysce Biosciences) Start Date:2021-07-02
ENSG (Ensign) Start Date:2007-11-12
ENSV (Enservco) Start Date:2007-05-16
ENTA (Enanta Pharmaceuticals C) Start Date:2013-03-21
ENTG (Entegris) Start Date:2007-01-03
ENTX (Entera Bio Ordinary Shares) Start Date:2018-06-28
ENTXW (Entera Bio Warrant) Start Date:2018-06-28
ENV (Envestnet) Start Date:2010-07-29
ENVA (Enova International) Start Date:2014-11-13
ENVB (Enveric Biosciences) Start Date:2015-07-10
ENVX (Enovix) Start Date:2021-07-12
ENX (Eaton Vance New York Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
ENZ (Enzo Biochem) Start Date:2007-04-27
EOD (Allspring Global Dividend Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
EOG (Eog Resources) Start Date:2005-01-03
EOI (Eaton Vance Enhance Equity Income Fund Eaton Vance Enhanced Equity Income Fund Shares Of Beneficial Interest) Start Date:2007-05-01
EOLS (Evolus) Start Date:2018-02-08
EOS (Eaton Vance Enhance Equity Income Fund Ii) Start Date:2007-04-26
EOSE (Eos Energy Enterprises Class A) Start Date:2020-11-02
EOSEW (Eos Energy Enterprises Warrant) Start Date:2020-06-03
EOT (Eaton Vance Municipal Income Trust Eaton Vance National Municipal Opportunities Trust) Start Date:2009-05-27
EP (Empire Petroleum) Start Date:2004-01-02
EPAC (Enerpac Tool) Start Date:2007-05-03
EPAM (Epam Systems) Start Date:2012-02-08
EPC (Edgewell Personal Care Co) Start Date:2007-04-26
EPD (Enterprise Products Partners L.P.) Start Date:2007-04-30
EPIX (Essa Pharma) Start Date:2015-03-13
EPM (Evolution Petroleum) Start Date:2007-05-16
EPOW (Sunrise New Energy Ltd) Start Date:2021-02-09
EPR (Epr Properties) Start Date:2007-01-03
EPRT (Essential Properties Realty Trust) Start Date:2018-06-21
EPSN (Epsilon Energy Common Share) Start Date:2019-02-19
EQ (Equillium) Start Date:2018-10-12
EQBK (Equity Bancshares) Start Date:2015-11-11
EQC (Equity Commonwealth) Start Date:2007-04-27
EQH (Equitable Holdings) Start Date:2018-05-10
EQIX (Equinix) Start Date:2005-01-03
EQNR (Equinor Asa) Start Date:2013-08-26
EQOS (Eqonex Ordinary Shares) Start Date:2019-05-16
EQR (Equity Residential) Start Date:2005-01-03
EQRX (Eqrx) Start Date:2021-06-03
EQRXW (Eqrx Warrant) Start Date:2021-12-20
EQS (Equus Total Return) Start Date:2007-05-16
EQT (Eqt Corporation) Start Date:2005-01-03
EQX (Equinox Gold) Start Date:2019-09-16
ERAS (Erasca) Start Date:2021-07-16
ERC (Allspring Multi-Sector Income Fund) Start Date:2007-05-10
ERF (Enerplus Corporation) Start Date:2007-04-26
ERH (Allspring Utilities And High Income Fund Common Shares) Start Date:2007-05-16
ERIC (Telefonaktiebolaget Lm Ericsson) Start Date:2007-01-03
ERIE (Erie Indemnity) Start Date:2007-04-27
ERII (Energy Recovery) Start Date:2008-07-02
ERJ (Embraer S.A.) Start Date:2007-04-30
ERNA (Eterna Therapeutics) Start Date:2021-03-26
ES (Eversource Energy) Start Date:2009-03-02
ESAB (Esab) Start Date:2022-04-05
ESBA (Empire State Realty Op, L.P. Series Es) Start Date:2013-10-02
ESCA (Escalade) Start Date:2007-05-16
ESE (Esco Technologies) Start Date:2007-04-30
ESEA (Euroseas) Start Date:2007-05-16
ESGL (Esgl Holdings Ltd.) Start Date:2022-04-07
ESGR (Enstar) Start Date:2007-05-16
ESGRO (Enstar Depository Shares 7.00% Perpetual Non-Cumulative Preference Shares Series E) Start Date:2018-12-03
ESGRP (Enstar Depositary Shares Each Representing 1/1000Th Of An Interest In Preference Shares) Start Date:2018-07-13
ESHA (Esh Acquisition) Start Date:2023-07-21
ESI (Element Solutions Inc) Start Date:2014-01-23
ESLT (Elbit Systems Ltd) Start Date:2010-06-01
ESMT (Engagesmart,) Start Date:2021-09-23
ESNT (Essent Ltd.) Start Date:2013-10-31
ESOA (Energy Services Of America) Start Date:2012-11-16
ESP (Espey Mfg. & Electronics) Start Date:2007-05-16
ESPR (Esperion Therapeutics Co) Start Date:2013-06-26
ESQ (Esquire Financial) Start Date:2017-06-27
ESRT (Empire State Realty Trust) Start Date:2013-10-02
ESS (Essex Property Trust) Start Date:2005-01-03
ESSA (Essa Bancorp) Start Date:2007-05-16
ESTA (Establishment Labs Holdings) Start Date:2018-07-19
ESTC (Elastic N.V.) Start Date:2018-10-05
ESTE (Earthstone Energy) Start Date:2007-05-16
ET (Energy Transfer Lp) Start Date:2007-05-02
ETB (Eaton Vance Tax-Managed Buy-Write Income Fund Eaton Vance Tax-Managed Buy-Write Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-03
ETD (Ethan Allen Interiors Inc) Start Date:2007-04-26
ETG (Eaton Vance Tax-Advantaged Global Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-03
ETJ (Eaton Vance Risk-Managed Diversified Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-07-27
ETN (Eaton Corporation) Start Date:2012-12-03
ETNB (89Bio) Start Date:2019-11-11
ETO (Eaton Vance Tax-Advantage Global Dividend Opp) Start Date:2007-05-16
ETON (Eton Pharmaceutcials) Start Date:2018-11-13
ETR (Entergy) Start Date:2005-01-03
ETRN (Equitrans Midstream Corp) Start Date:2018-10-31
ETSY (Etsy) Start Date:2015-04-16
ETV (Eaton Vance Eaton Vance Tax-Managed Buy-Write Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2007-04-26
ETW (Eaton Vance Eaton Vance Tax-Managed Global Buy-Write Opportunites Fund Common Shares Of Beneficial Interest) Start Date:2007-05-01
ETWO (E2open Parent Holdings,) Start Date:2020-06-15
ETX (Eaton Vance Municipal Income 2028 Term Trust Common Shares Of Beneficial Interest) Start Date:2013-03-26
ETY (Eaton Vance Tax-Managed Diversified Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
EU (Encore Energy) Start Date:2008-05-21
EUDA (Euda Health Holdings) Start Date:2021-12-14
EURN (Euronav Nv) Start Date:2015-01-23
EVA (Enviva Partners, Lp) Start Date:2015-04-29
EVAX (Evaxion Biotech) Start Date:2021-02-05
EVBG (Everbridge) Start Date:2016-09-16
EVBN (Evans Bancorp) Start Date:2007-05-16
EVC (Entravision Communication) Start Date:2007-05-02
EVCM (Evercommerce) Start Date:2021-07-01
EVER (Everquote) Start Date:2018-06-28
EVEX (Eve Holding) Start Date:2022-05-10
EVF (Eaton Vance Senior Income Trust) Start Date:2007-05-16
EVFM (Evofem Biosciences) Start Date:2014-11-20
EVG (Eaton Vance Short Diversified Income Fund Eaton Vance Short Duration Diversified Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
EVGN (Evogene Ordinary Shares) Start Date:2013-11-21
EVGO (Evgo Class A) Start Date:2020-11-20
EVGOW (Evgo Warrants) Start Date:2020-11-20
EVGR (Evergreen Class A Ordinary Share) Start Date:2022-04-06
EVGRU (Evergreen Unit) Start Date:2022-02-09
EVH (Evolent Health) Start Date:2015-06-05
EVI (Evi Industries) Start Date:2009-12-01
EVLO (Evelo Biosciences) Start Date:2018-05-09
EVLV (Evolv Technologies Holdings, Class A) Start Date:2020-09-22
EVLVW (Evolv Technologies Holdings Warrant) Start Date:2021-07-19
EVM (Eaton Vance California Municipal Bond Fund Common Shares Of Beneficial Interest $.01 Par Value) Start Date:2007-05-16
EVN (Eaton Vance Municipal Income Trust) Start Date:2007-05-16
EVO (Evotec Se American Depositary Shares) Start Date:2021-11-04
EVOK (Evoke Pharma) Start Date:2013-09-25
EVR (Evercore) Start Date:2007-01-03
EVRG (Evergy) Start Date:2007-12-18
EVRI (Everi) Start Date:2007-05-08
EVT (Eaton Vance Tax Advantaged Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
EVTC (Evertec) Start Date:2013-12-04
EVTL (Vertical Aerospace Ordinary Shares) Start Date:2021-12-16
EVTV (Envirotech Vehicles) Start Date:2022-07-06
EVV (Eaton Vance Duration Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-01
EW (Edwards Lifesciences) Start Date:2005-01-03
EWBC (East West Bancorp) Start Date:2007-01-03
EWCZ (European Wax Center) Start Date:2021-08-05
EWTX (Edgewise Therapeutics) Start Date:2021-03-26
EXAI (Exscientia Plc American Depositary Shares) Start Date:2021-10-01
EXAS (Exact Sciences Corporation) Start Date:2007-01-03
EXC (Exelon) Start Date:2005-01-03
EXD (Eaton Vance Tax-Managed Buy-Write Strategy Fund Common Shares Of Beneficial Interest) Start Date:2010-06-25
EXEL (Exelixis) Start Date:2007-01-03
EXFY (Expensify, Class A) Start Date:2021-11-10
EXG (Eaton Vance Tax-Managed Global Diversified Equity Income Fund) Start Date:2007-02-23
EXK (Endeavour Silver) Start Date:2007-05-16
EXLS (Exlservice) Start Date:2007-05-02
EXN (Excellon Resources Common Shares) Start Date:2020-09-23
EXP (Eagle Materials) Start Date:2007-01-03
EXPD (Expeditors) Start Date:2005-06-06
EXPE (Expedia) Start Date:2005-08-09
EXPI (Exp World) Start Date:2013-11-19
EXPO (Exponent) Start Date:2007-01-03
EXPR (Express) Start Date:2010-05-13
EXR (Extra Space Storage) Start Date:2005-01-03
EXTO (Almacenes Exito Sa) Start Date:2023-08-23
EXTR (Extreme Networks) Start Date:2007-05-01
EYE (National Vision Holdings) Start Date:2017-10-26
EYEN (Eyenovia) Start Date:2018-01-25
EYPT (Eyepoint Pharmaceuticals) Start Date:2007-05-16
EZFL (Ezfill Holdings) Start Date:2021-09-15
EZGO (Ezgo Technologies) Start Date:2021-01-26
EZPW (Ezcorp) Start Date:2007-04-30
F (Ford Motor) Start Date:2005-01-03
FA (First Advantage) Start Date:2021-06-23
FAF (First American Financial Corporation) Start Date:2010-05-24
FAM (First Trust/Aberdeen Global Opportunity Income Fund First Trust/Aberdeen Global Opportunity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-25
FAMI (Farmmi,) Start Date:2018-02-16
FANG (Diamondback Energy) Start Date:2012-10-12
FANH (Fanhua American Depositary Shares) Start Date:2007-10-31
FARM (Farmer Bros) Start Date:2007-05-16
FARO (Faro Technologies) Start Date:2007-05-03
FAST (Fastenal Co) Start Date:2005-01-03
FAT (Fat Brands Class A) Start Date:2017-10-23
FATBB (Fat Brands Class B) Start Date:2021-08-24
FATBW (Fat Brands Warrant) Start Date:2020-07-14
FATE (Fate Therapeutics) Start Date:2013-10-01
FATH (Fathom Digital Manufacturing Class A) Start Date:2021-03-29
FAX (Aberdeen Asia-Pacific Income Fund Inc) Start Date:2007-05-03
FAZE (Faze Holdings) Start Date:2021-04-13
FBHS (Fortune Brands Home & Security) Start Date:2011-10-04
FBIN (Fortune Brands Innovations) Start Date:2011-10-04
FBIO (Fortress Biotech) Start Date:2011-11-17
FBIOP (Fortress Biotech 9.375% Series A Cumulative Redeemable Perpetual Preferred Stock) Start Date:2017-11-14
FBIZ (First Business Financial) Start Date:2007-05-16
FBK (Fb Financial Corp) Start Date:2016-09-16
FBMS (First Bancshares) Start Date:2007-05-17
FBNC (First Bancorp) Start Date:2007-05-16
FBP (First Bancorp) Start Date:2007-04-26
FBRT (Franklin Bsp Realty Trust) Start Date:2021-10-19
FBRX (Forte Biosciences) Start Date:2017-04-13
FC (Franklin Covey) Start Date:2007-05-16
FCAP (First Capital) Start Date:2007-05-24
FCBC (First Community) Start Date:2007-05-16
FCCO (First Community) Start Date:2007-05-16
FCEL (Fuelcell Energy) Start Date:2007-05-02
FCF (First Commonwealth) Start Date:2007-05-02
FCFS (Firstcash) Start Date:2007-01-03
FCN (Fti Consulting) Start Date:2007-01-03
FCNCA (First Citizens Bancshares) Start Date:2007-05-16
FCNCP (First Citizens Bancshares Depositary Shares) Start Date:2020-03-13
FCO (Aberdeen Global Income Fund) Start Date:2007-05-16
FCPT (Four Corners Property Trust) Start Date:2015-11-10
FCT (First Trust Senior Floating Rate Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
FCUV (Focus Universal) Start Date:2017-09-01
FCX (Freeport-Mcmoran) Start Date:2005-01-03
FDBC (Fidelity D & D Bancorp) Start Date:2007-05-16
FDEU (First Trust Dynamic Europe Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2015-09-25
FDMT (4D Molecular Therapeutics) Start Date:2020-12-11
FDP (Fresh Del Monte Produce) Start Date:2007-05-04
FDS (Factset Research Systems) Start Date:2007-05-01
FDUS (Fidus Investment) Start Date:2011-06-21
FDX (Fedex Corporation) Start Date:2005-01-03
FE (Firstenergy Corp) Start Date:2005-01-03
FEAM (5E Advanced Materials) Start Date:2022-03-15
FEBO (Fenbo Holdings Limited) Start Date:2023-11-30
FEDU (Four Seasons Education) Start Date:2017-11-08
FEI (First Trust Mlp And Energy Income Fund Common Shares Of Beneficial Interest) Start Date:2012-11-28
FEIM (Frequency Electronics) Start Date:2007-05-16
FELE (Franklin Electric) Start Date:2007-05-08
FEMY (Femasys) Start Date:2021-06-18
FEN (First Trust Energy Income And Growth Fund) Start Date:2007-05-16
FENC (Fennec Pharmaceuticals) Start Date:2017-09-13
FENG (Phoenix New Media American Depositary Shares Each Representing 48 Class A Ordinary Shares.) Start Date:2011-05-12
FEO (First Trust/Aberdeen Emerging Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
FERG (Ferguson Plc) Start Date:2021-03-08
FET (Forum Energy Technologies) Start Date:2012-04-12
FEXD (Fintech Ecosystem Development Class A) Start Date:2022-01-13
FEXDR (Fintech Ecosystem Development Right) Start Date:2022-01-13
FEXDW (Fintech Ecosystem Development Warrant) Start Date:2022-01-13
FF (Futurefuel) Start Date:2007-05-16
FFA (First Trust Enhanced Equity Income Fund) Start Date:2007-05-16
FFBC (First Financial Bancorp) Start Date:2007-05-01
FFC (Flaherty & Crumrine Preferred And Income Securities Fund Incorporated) Start Date:2007-05-02
FFHL (Fuwei Films) Start Date:2007-05-16
FFIC (Flushing Financial) Start Date:2007-05-01
FFIE (Faraday Future Intelligent Electric) Start Date:2020-09-02
FFIEW (Faraday Future Intelligent Electric Warrant) Start Date:2020-08-28
FFIN (First Financial Bankshares) Start Date:2007-01-03
FFIV (F5 Networks) Start Date:2005-01-03
FFNW (First Financial Northwest) Start Date:2007-10-10
FFWM (First Foundation) Start Date:2014-11-03
FG (F&G Annuities & Life) Start Date:2022-12-01
FGB (First Trust Specialty Finance And Financial Opportunities Fund) Start Date:2007-05-25
FGBI (First Guaranty Bancshares) Start Date:2015-11-05
FGEN (Fibrogen) Start Date:2014-11-14
FGF (Fg Financial) Start Date:2014-04-01
FGH (Fg Holdings) Start Date:2007-05-16
FGI (Fgi Industries Ordinary Shares) Start Date:2022-01-25
FGMC (Fg Merger) Start Date:2022-04-19
FGMCU (Fg Merger Unit) Start Date:2022-02-25
FGMCW (Fg Merger Warrant) Start Date:2022-04-21
FHB (First Hawaiian) Start Date:2016-08-04
FHI (Federated Hermes) Start Date:2007-05-01
FHLT (Future Health ESG) Start Date:2021-12-08
FHLTU (Future Health ESG Unit) Start Date:2021-09-10
FHLTW (Future Health ESG Warrant) Start Date:2021-12-09
FHN (First Horizon National Corporation) Start Date:2005-01-03
FHTX (Foghorn Therapeutics) Start Date:2020-11-02
FI (Fiserv Inc) Start Date:2005-01-03
FIBK (First Interstate Banc) Start Date:2010-03-24
FICO (Fair Isaac) Start Date:2009-08-18
FICV (Frontier Investment Class A Ordinary Shares) Start Date:2021-09-14
FICVU (Frontier Investment Units) Start Date:2021-07-01
FICVW (Frontier Investment Warrants) Start Date:2021-09-10
FIF (First Trust Energy Infrastructure Fund Common Shares Of Beneficial Interest) Start Date:2011-09-28
FIGS (Figs) Start Date:2021-05-27
FIHL (Fidelis Insurance Holdings Limited) Start Date:2023-06-29
FINMU (Marlin Technology Unit) Start Date:2021-01-13
FINMW (Marlin Technology Warrant) Start Date:2021-03-08
FINS (Angel Oak Financial Strategies Income Term Trust Common Shares Of Beneficial Interest) Start Date:2019-05-29
FINV (Finvolution American Depositary Shares) Start Date:2017-11-10
FINW (Finwise Bancorp) Start Date:2021-11-19
FIP (Ftai Infrastructure) Start Date:2022-07-20
FIS (Fidelity National Information Services) Start Date:2006-02-01
FISI (Financial Institutions) Start Date:2007-05-16
FISK (Empire State Realty Op, L.P. Series 250) Start Date:2013-10-08
FITB (Fifth Third Bancorp) Start Date:2011-01-20
FITBI (Fifth Third Bancorp Depositary Shares) Start Date:2013-12-06
FITBO (Fifth Third Bancorp Depositary Shares Each Representing A 1/1000Th Ownership Interest In A Share Of Non-Cumulative Perpetual Preferred Stock Series K) Start Date:2019-10-02
FITBP (Fifth Third Bancorp Depositary Shares Each Representing 1/40Th Share Of Fifth Third 6.00% Non-Cumulative Perpetual Class B Preferred Stock Series A) Start Date:2019-08-27
FIVE (Five Below) Start Date:2012-07-19
FIVN (Five9) Start Date:2014-04-04
FIX (Comfort Systems) Start Date:2007-05-01
FIXX (Homology Medicines) Start Date:2018-03-28
FIZZ (National Beverage) Start Date:2007-06-12
FKWL (Franklin Wireless) Start Date:2008-01-23
FL (Foot Locker Inc) Start Date:2005-01-03
FLC (Flaherty & Crumrine Total Return Fund Inc) Start Date:2007-05-16
FLEX (Flex Ltd) Start Date:2005-01-03
FLFV (Feutune Light Acquisition Corporation) Start Date:2022-08-08
FLGC (Flora Growth) Start Date:2021-05-11
FLGT (Fulgent Genetics) Start Date:2016-09-29
FLIC (First Of Long Island) Start Date:2007-05-16
FLJ (Flj) Start Date:2019-11-05
FLL (Full House Resorts) Start Date:2007-05-16
FLNC (Fluence Energy, Class A) Start Date:2021-10-28
FLNG (Flex Lng Ordinary Shares) Start Date:2019-06-17
FLNT (Fluent) Start Date:2016-09-26
FLO (Flowers Foods) Start Date:2007-01-03
FLR (Fluor) Start Date:2005-01-03
FLS (Flowserve Corporation) Start Date:2005-01-03
FLT (Fleetcor Technologies Inc) Start Date:2010-12-15
FLUX (Flux Power Holdings) Start Date:2012-06-15
FLWS (1-800 Flowers.com) Start Date:2007-05-02
FLXS (Flexsteel Industries) Start Date:2007-05-16
FLYW (Flywire) Start Date:2021-05-26
FMAO (Farmers & Merchants Bancorp) Start Date:2007-05-16
FMBH (First Mid Bancshares) Start Date:2007-05-17
FMC (Fmc Corporation) Start Date:2005-01-03
FMIVU (Forum Merger Iv Unit) Start Date:2021-03-18
FMIVW (Forum Merger Iv Warrant) Start Date:2021-05-26
FMN (Federated Hermes Premier Municipal Income Fund) Start Date:2007-05-16
FMNB (Farmers National Banc) Start Date:2007-05-16
FMS (Fresenius Medical Care Ag & Co. Kgaa) Start Date:2007-01-03
FMX (Fomento Economico Mexicano S.A.B. De C.V.) Start Date:2007-04-30
FMY (First Trust Motgage Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
FN (Fabrinet) Start Date:2010-06-25
FNA (Paragon 28) Start Date:2021-10-15
FNB (F.N.B. Corporation) Start Date:2007-01-03
FNCB (Fncb Bancorp) Start Date:2007-05-16
FNCH (Finch Therapeutics) Start Date:2021-03-19
FND (Floor & Decor Holdings) Start Date:2017-04-27
FNF (Fidelity National Financial) Start Date:2007-01-03
FNGR (Fingermotion) Start Date:2017-08-01
FNKO (Funko) Start Date:2017-11-02
FNLC (First Bancorp) Start Date:2007-05-16
FNV (Franco-Nevada Corporation) Start Date:2011-09-08
FNWB (First Northwest Bancorp) Start Date:2015-01-30
FNWD (Finward Bancorp) Start Date:2007-05-16
FOA (Finance Of America Companies Class A) Start Date:2019-04-18
FOCS (Focus Financial Partners) Start Date:2018-07-26
FOF (Cohen & Steers Closed-End Opportunity Fund) Start Date:2007-05-16
FOLD (Amicus Therapeutics) Start Date:2007-05-31
FONR (Fonar) Start Date:2007-05-15
FOR (Forestar) Start Date:2017-09-28
FORA (Forian) Start Date:2021-03-03
FORD (Forward Industries) Start Date:2007-05-02
FORM (Formfactor) Start Date:2007-01-03
FORR (Forrester Research) Start Date:2007-05-02
FORTY (Formula Systems) Start Date:2013-02-11
FOSL (Fossil) Start Date:2005-01-03
FOUR (Shift4 Payments) Start Date:2020-06-05
FOX (Twenty-First Century Fox Class B) Start Date:2007-04-30
FOXA (Twenty-First Century Fox Class A) Start Date:2019-02-27
FOXF (Fox Factory Holding) Start Date:2013-08-08
FOXO (Foxo Technologies Class A) Start Date:2022-09-16
FPAY (Flexshopper) Start Date:2012-01-24
FPF (First Trust Intermediate Duration Preferred & Income Fund Common Shares Of Beneficial Interest) Start Date:2013-05-24
FPH (Five Point Holdings, Llc Class A Common Shares) Start Date:2017-05-10
FPI (Farmland Partners) Start Date:2014-04-11
FPL (First Trust New Opportunities Mlp & Energy Fund) Start Date:2014-03-27
FR (First Industrial Realty Trust) Start Date:2007-01-03
FRA (Blackrock Floating Rate Income Strategies Fund Inc) Start Date:2007-05-16
FRAF (Franklin Finl Svcs Corp) Start Date:2007-05-17
FRBA (First Bank Williamstown) Start Date:2007-05-17
FRD (Friedman Industries) Start Date:2007-05-16
FREE (Whole Earth Brands Class A) Start Date:2019-05-14
FREEW (Whole Earth Brands Warrant) Start Date:2020-06-25
FRES (Fresh2 Ltd.) Start Date:2020-01-30
FREY (Freyr Battery) Start Date:2021-07-06
FRGE (Forge Global) Start Date:2022-03-22
FRGI (Fiesta Restaurant) Start Date:2012-04-26
FRGT (Freight Technologies Ordinary Shares) Start Date:2017-08-08
FRHC (Freedom Holding) Start Date:2011-09-30
FRLN (Freeline Therapeutics Plc) Start Date:2020-08-07
FRME (First Merchants) Start Date:2007-05-10
FRMEP (First Merchants Depository Shares) Start Date:2022-04-04
FRO (Frontline) Start Date:2007-05-01
FROG (Jfrog) Start Date:2020-09-16
FRPH (Frp) Start Date:2007-05-16
FRPT (Freshpet) Start Date:2014-11-07
FRSGU (First Reserve Sustainable Growth Unit) Start Date:2021-03-05
FRSH (Freshworks Class A) Start Date:2021-09-22
FRST (Primis Financial) Start Date:2007-05-16
FRSX (Foresight Autonomous Holdings American Depositary Shares) Start Date:2017-06-15
FRT (Federal Realty Investment Trust) Start Date:2005-01-03
FRTX (Fresh Tracks Therapeutics) Start Date:2007-05-01
FRZA (Forza X1) Start Date:2022-08-12
FSBC (Five Star Bancorp) Start Date:2021-05-05
FSBW (Fs Bancorp) Start Date:2012-07-10
FSCO (Fs Credit Opportunities) Start Date:2022-11-14
FSD (First Trust High Income Long Short Fund Common Shares Of Beneficial Interest) Start Date:2010-09-28
FSEA (First Seacoast Bancorp) Start Date:2019-07-17
FSFG (First Savings Financial) Start Date:2008-10-07
FSI (Flexible Solutions International) Start Date:2007-05-16
FSLR (First Solar) Start Date:2006-11-17
FSLY (Fastly) Start Date:2019-05-17
FSM (Fortuna Silver Mines) Start Date:2011-09-19
FSP (Franklin Street Pptys) Start Date:2007-05-03
FSR (Fisker) Start Date:2020-10-30
FSRD (Fast Radius Class A) Start Date:2021-04-06
FSRDW (Fast Radius Warrants) Start Date:2022-02-07
FSS (Federal Signal) Start Date:2007-05-01
FSSIU (Fortistar Sustainable Solutions Unit) Start Date:2021-01-27
FSSIW (Fortistar Sustainable Solutions Warrant) Start Date:2021-03-19
FSTR (Lb Foster) Start Date:2007-05-08
FSV (Firstservice Common Shares) Start Date:2015-06-02
FT (Franklin Universal Trust) Start Date:2007-05-16
FTAI (Fortress Transportation And Infrastructure Investors Llc) Start Date:2015-05-15
FTCH (Farfetch Limited) Start Date:2018-09-21
FTCI (Ftc Solar) Start Date:2021-04-28
FTDR (Frontdoor) Start Date:2018-09-13
FTEK (Fuel Tech) Start Date:2007-05-04
FTEL (Fitell Corporation) Start Date:2023-08-08
FTF (Franklin Duration Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-04
FTFT (Future Fintech) Start Date:2009-03-12
FTHM (Fathom Holdings) Start Date:2020-07-31
FTHY (First Trust High Yield Opportunities 2027 Term Fund) Start Date:2020-06-26
FTI (Technipfmc) Start Date:2017-01-17
FTII (Futuretech Ii Acquisition) Start Date:2022-04-08
FTK (Flotek Industries) Start Date:2007-05-08
FTNT (Fortinet) Start Date:2009-11-18
FTRE (Fortrea Holdings Inc) Start Date:2023-06-16
FTS (Fortis) Start Date:2016-10-14
FTV (Fortive Corp) Start Date:2016-07-05
FUBO (Fubotv /Fl) Start Date:2020-10-08
FUL (H.B. Fuller Company) Start Date:2007-01-03
FULC (Fulcrum Therapeutics) Start Date:2019-07-18
FULT (Fulton Financial) Start Date:2007-05-08
FULTP (Fulton Financial Depositary Shares Each Representing A 1/40Th Interest In A Share Of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2020-11-03
FUN (Cedar Fair L.P.) Start Date:2007-01-03
FUNC (First United) Start Date:2007-05-16
FUND (Sprott Focus Trust) Start Date:2007-05-16
FURY (Fury Gold Mines Common Shares) Start Date:2020-10-12
FUSB (First Us Bancshares) Start Date:2007-05-16
FUSN (Fusion Pharmaceuticals) Start Date:2020-06-26
FUTU (Futu Holdings Limited) Start Date:2019-03-08
FUV (Arcimoto,) Start Date:2017-09-21
FVCB (Fvcbankcorp) Start Date:2017-09-29
FVRR (Fiverr International Ltd.) Start Date:2019-06-13
FWBI (First Wave Biopharma) Start Date:2016-10-28
FWONA (Formula One) Start Date:2013-01-22
FWONK (Formula One) Start Date:2014-07-08
FWRD (Forward Air) Start Date:2007-05-04
FWRG (First Watch Restaurant) Start Date:2021-10-01
FXLV (F45 Training) Start Date:2021-07-15
FXNC (First National) Start Date:2007-05-16
FYBR (Frontier Communications Parent,) Start Date:2021-05-04
G (Genpact Limited) Start Date:2007-08-02
GAB (Gabelli Equity Trust) Start Date:2007-05-08
GABC (German American Bancorp) Start Date:2007-05-16
GAIA (Gaiam) Start Date:2007-05-07
GAIN (Gladstone Investment) Start Date:2007-05-09
GALT (Galectin Therapeutics) Start Date:2009-01-12
GAM (General American Investors) Start Date:2007-05-16
GAMB (Gambling.com) Start Date:2021-07-23
GAMC (Golden Arrow Merger Class A) Start Date:2021-05-07
GAMCU (Golden Arrow Merger Unit) Start Date:2021-03-17
GAMCW (Golden Arrow Merger Warrant) Start Date:2021-06-04
GAME (Engine Gaming And Media) Start Date:2021-06-17
GAN (Gan) Start Date:2020-05-08
GANX (Gain Therapeutics) Start Date:2021-03-18
GASS (Stealthgas) Start Date:2007-05-16
GATO (Gatos Silver) Start Date:2020-11-02
GATX (Gatx Corp) Start Date:2007-04-27
GAU (Galiano Gold) Start Date:2008-01-02
GB (Global Blue Holding Ag Ordinary Shares) Start Date:2018-06-27
GBAB (Guggenheim Taxable Municipal Bond & Investment Grade Debt Trust Common Shares Of Beneficial Interest) Start Date:2010-10-27
GBBK (Global Blockchain Acquisition) Start Date:2022-06-17
GBCI (Glacier Bancorp) Start Date:2014-03-04
GBIO (Generation Bio) Start Date:2020-06-12
GBLI (Global Indemnity) Start Date:2007-05-07
GBNH (Greenbrook Tms Common Shares) Start Date:2021-03-16
GBNY (Generations Bancorp Ny) Start Date:2021-01-13
GBOX (Greenbox Pos) Start Date:2021-02-17
GBR (New Concept Energy Inc) Start Date:2007-05-16
GBS (Gbs) Start Date:2020-12-23
GBTG (Global Business Travel  Class A) Start Date:2020-11-23
GBX (Greenbrier Companies) Start Date:2007-05-02
GCBC (Greene County Bancorp) Start Date:2007-05-16
GCI (Gannett Co.) Start Date:2014-02-04
GCMG (Gcm Grosvenor) Start Date:2020-11-16
GCMGW (Gcm Grosvenor Warrant) Start Date:2019-01-31
GCO (Genesco) Start Date:2007-05-01
GCT (Gigacloud Technology) Start Date:2022-08-18
GCTK (Glucotrack) Start Date:2022-03-11
GCV (Gabelli Convertible And Income Securities Fund) Start Date:2007-05-16
GD (General Dynamics) Start Date:2005-01-03
GDC (Gd Culture) Start Date:2015-12-29
GDDY (Godaddy) Start Date:2015-04-02
GDEN (Golden Entertainment) Start Date:2007-05-02
GDHG (Golden Heaven Holdings Ltd.) Start Date:2023-04-12
GDL (Gdl Fund The Common Shares Of Beneficial Interest) Start Date:2007-05-16
GDO (Western Asset Global Corporate Defined Opportunity Fund Western Asset Global Corporate Defined Opportunity Fund) Start Date:2009-11-24
GDOT (Green Dot Corporation) Start Date:2010-07-22
GDRX (Goodrx) Start Date:2020-09-23
GDS (Gds Holdings Limited) Start Date:2016-11-02
GDST (Goldenstone Acquisition Limited) Start Date:2022-04-14
GDTC (Cytomed Therapeutics Pte. Ltd.) Start Date:2023-04-14
GDV (Gabelli Dividend & Income Trust Common Shares Of Beneficial Interest) Start Date:2007-05-01
GDYN (Grid Dynamics) Start Date:2018-10-05
GE (General Electric) Start Date:2005-01-03
GECC (Great Elm Capital) Start Date:2016-11-04
GEF (Greif) Start Date:2007-05-07
GEF.B (Greif) Start Date:2007-05-16
GEG (Great Elm) Start Date:2007-04-26
GEHC (Ge Healthcare Technologies) Start Date:2022-12-15
GEL (Genesis Energy, L.P.) Start Date:2007-08-01
GEN (Gen Digital) Start Date:2007-04-27
GENC (Gencor Industries) Start Date:2007-12-20
GENE (Genetic Technologies ADS) Start Date:2007-05-16
GENI (Genius Sports Limited) Start Date:2020-10-05
GENK (Gen Restaurant) Start Date:2023-06-28
GENQ (Genesis Unicorn Capital Class A) Start Date:2022-04-07
GEO (Geo) Start Date:2007-05-03
GEOS (Geospace Technologies) Start Date:2007-05-09
GER (Goldman Sachs Mlp Energy Renaissance Fund) Start Date:2014-09-26
GERN (Geron) Start Date:2007-04-30
GES (Guess) Start Date:2007-05-01
GETR (Getaround) Start Date:2021-04-26
GETY (Getty Images Holdings Class A) Start Date:2022-07-25
GEVO (Gevo,) Start Date:2011-02-09
GF (New Germany Fund) Start Date:2007-05-16
GFAI (Guardforce Ai) Start Date:2021-09-29
GFAIW (Guardforce AI Co. Warrant) Start Date:2021-09-29
GFF (Griffon) Start Date:2007-04-30
GFI (Gold Fields Limited) Start Date:2007-01-03
GFL (Gfl Environmental) Start Date:2020-03-03
GFS (Globalfoundries Ordinary Shares) Start Date:2021-10-28
GGAL (Grupo Financiero Galicia S.A.) Start Date:2007-01-03
GGB (Gerdau S.A.) Start Date:2007-01-03
GGE (Green Giant) Start Date:2010-09-13
GGG (Graco) Start Date:2007-01-03
GGMC (Glenfarne Merger Class A) Start Date:2021-05-27
GGN (Gamco Global Gold Natural Resources & Income Trust) Start Date:2007-05-08
GGR (Gogoro) Start Date:2022-04-05
GGROW (Gogoro Warrant) Start Date:2022-04-05
GGT (Gabelli Multi-Media Trust) Start Date:2007-05-16
GGZ (Gabelli Global Small And Mid Cap Value Trust) Start Date:2014-06-12
GH (Guardant Health) Start Date:2018-10-04
GHC (Graham Holdings Company) Start Date:2007-05-16
GHG (Greentree Hospitality American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2018-03-27
GHI (Greystone Housing Impact Investors Lp) Start Date:2008-07-01
GHIX (Gores Holdings Ix Class A) Start Date:2022-03-22
GHL (Greenhill & Co) Start Date:2007-05-04
GHLD (Guild Co) Start Date:2020-11-02
GHM (Graham) Start Date:2007-05-16
GHRS (Gh Research Plc) Start Date:2021-06-25
GHSI (Guardion Health Sciences) Start Date:2019-04-05
GHY (Pgim Global High Yield Fund) Start Date:2012-12-21
GIA (Gigcapital 5) Start Date:2021-11-04
GIB (Cgi) Start Date:2007-05-10
GIC (Global Industrial Company) Start Date:2007-05-01
GIFI (Gulf Island Fabrication) Start Date:2007-04-30
GIGM (Gigamedia Ordinary Shares) Start Date:2007-04-30
GIII (G-Iii Apparel) Start Date:2007-05-16
GIIXU (Gores Holdings Viii Unit) Start Date:2021-02-25
GIIXW (Gores Holdings Viii Warrant) Start Date:2021-04-23
GIL (Gildan Activewear) Start Date:2007-01-03
GILD (Gilead Sciences) Start Date:2005-01-03
GILT (Gilat Satellite Networks Ltd) Start Date:2007-05-04
GIM (Templeton Global Income Fund) Start Date:2007-05-03
GIPR (Generation Income Properties) Start Date:2021-10-05
GIS (General Mills) Start Date:2005-01-03
GIWWW (Giginternational1 Warrant) Start Date:2021-07-12
GJO (Synthetic Fixed-Income Securities Synthetic Fixed-Income Securities On Behalf Of Strats) Start Date:2007-05-16
GJR (Synthetic Fixed-Income Securities Strats Trust For Procter&Gamble Securities Series 2006-1) Start Date:2007-05-17
GJS (Goldman Sachs Securities Strats Trust For Goldman Sachs Securities Series 2006-2) Start Date:2007-05-16
GJT (Synthetic Fixed-Income Securities Synthetic Fixed-Income Securities Floating Rate Structured Repackaged Asset-Backed Trust Securities Certificates Series 2006-3) Start Date:2007-05-16
GKOS (Glaukos) Start Date:2015-06-25
GL (Globe Life) Start Date:2007-05-01
GLAC (Global Lights Acquisition Corp) Start Date:2023-12-04
GLAD (Gladstone Capital) Start Date:2007-05-16
GLBE (Global-E Online) Start Date:2021-05-12
GLBL (Cartesian Growth Class A Ordinary Share) Start Date:2021-04-27
GLBLW (Cartesian Growth Warrant) Start Date:2021-04-28
GLBS (Globus Maritime) Start Date:2010-11-26
GLBZ (Glen Burnie Bancorp) Start Date:2007-05-16
GLDD (Great Lakes Dredge & Dock) Start Date:2007-05-16
GLDG (Goldmining Common Shares) Start Date:2020-10-06
GLLI (Globalink Investment) Start Date:2021-12-23
GLLIR (Globalink Investment Rights) Start Date:2021-12-23
GLLIU (Globalink Investment Unit) Start Date:2021-12-07
GLLIW (Globalink Investment Warrants) Start Date:2021-12-23
GLMD (Galmed Pharmaceuticals Ordinary Shares) Start Date:2014-03-13
GLNG (Golar Lng) Start Date:2007-05-11
GLO (Clough Global Opportunities Fund) Start Date:2007-04-30
GLOB (Globant S.A.) Start Date:2014-07-18
GLP (Global Partners Lp) Start Date:2007-05-16
GLPG (Galapagos Nv American Depositary Shares) Start Date:2015-05-14
GLPI (Gaming And Leisure Properties) Start Date:2013-10-14
GLQ (Clough Global Equity Fund Clough Global Equity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
GLRE (Greenlight Capital Re) Start Date:2007-05-24
GLSI (Greenwich Lifesciences) Start Date:2020-09-25
GLST (Global Star Acquisition,) Start Date:2022-11-10
GLT (Glatfelter Corp) Start Date:2007-04-30
GLTO (Galecto) Start Date:2020-11-02
GLU (Gabelli Global Utility Common Shares Of Beneficial Ownership) Start Date:2007-05-16
GLUE (Monte Rosa Therapeutics) Start Date:2021-06-24
GLV (Clough Global Dividend And Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
GLW (Corning) Start Date:2005-01-03
GLYC (Glycomimetics O) Start Date:2014-01-10
GM (General Motors) Start Date:2010-11-18
GMAB (Genmab A/S) Start Date:2019-07-18
GMBL (Esports Entertainment) Start Date:2010-07-07
GMBLW (Esports Entertainment  Warrant) Start Date:2020-04-14
GMBLZ (Esports Entertainment  Warrant) Start Date:2022-03-14
GMDA (Gamida Cell Ordinary Shares) Start Date:2018-10-26
GME (Gamestop Corporation) Start Date:2005-10-10
GMED (Globus Medical) Start Date:2012-08-03
GMGI (Golden Matrix) Start Date:2018-11-30
GMM (Global Mofy Metaverse Limited) Start Date:2023-10-10
GMRE (Global Medical Reit Commo) Start Date:2016-06-29
GMS (Gms) Start Date:2016-05-26
GMTX (Gemini Therapeutics) Start Date:2020-08-12
GMVD (G Medical Innovations Holdings Ordinary Shares) Start Date:2021-06-25
GMVDW (G Medical Innovations Holdings Warrants) Start Date:2021-06-25
GNE (Genie Energy) Start Date:2011-10-26
GNFT (Genfit S.A. American Depositary Shares) Start Date:2019-03-27
GNK (Genco Shipping & Trading) Start Date:2015-07-20
GNL (Global Net Lease) Start Date:2015-06-02
GNLN (Greenlane) Start Date:2019-04-18
GNLX (Genelux) Start Date:2023-01-26
GNPX (Genprex) Start Date:2018-03-29
GNRC (Generac Holdings) Start Date:2010-02-11
GNS (Genius Ordinary Shares) Start Date:2022-04-12
GNSS (Genasys) Start Date:2007-05-16
GNT (Gamco Natural Resources Gold & Income Trust) Start Date:2011-01-27
GNTA (Genenta Science S.P.A. American Depositary Shares) Start Date:2021-12-15
GNTX (Gentex Corporation) Start Date:2007-01-03
GNTY (Guaranty Bancshares) Start Date:2017-05-09
GNW (Genworth Financial Inc) Start Date:2005-01-03
GO (Grocery Outlet Holding) Start Date:2019-06-20
GOCO (Gohealth) Start Date:2020-07-15
GODN (Golden Star Acquisition Corporation) Start Date:2023-06-28
GOEV (Canoo Class A) Start Date:2019-04-16
GOEVW (Canoo Warrant) Start Date:2019-04-16
GOF (Guggenheim Strategic Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2007-07-27
GOGL (Golden Ocean) Start Date:2007-05-04
GOGO (Gogo) Start Date:2013-06-21
GOL (Gol Linhas Aereas Inteligentes S.A. Sponsored ADR Representing 2 Pfd Shares) Start Date:2007-04-30
GOLD (Barrick Gold) Start Date:2007-04-27
GOLF (Acushnet Holdings) Start Date:2016-10-28
GOOD (Gladstone Commercial) Start Date:2007-05-16
GOODO (Gladstone Commercial 6.00% Series G Cumulative Redeemable Preferred Stock Par Value $0.001 Per Share) Start Date:2021-06-28
GOOG (Alphabet Inc Class C) Start Date:2005-01-03
GOOGL (Alphabet Inc Class A) Start Date:2007-04-27
GOOS (Canada Goose Holdings) Start Date:2017-03-21
GORO (Gold Resource) Start Date:2007-05-16
GOSS (Gossamer Bio) Start Date:2019-02-08
GOTU (Gaotu Techedu American Depositary Shares) Start Date:2019-06-06
GOVX (Geovax Labs) Start Date:2020-09-25
GP (Georgia-Pacific) Start Date:2020-08-28
GPAK (Gamer Pakistan) Start Date:2023-10-09
GPC (Genuine Parts) Start Date:2005-01-03
GPCR (Structure Therapeutics) Start Date:2023-02-03
GPI (1 Automotive) Start Date:2007-04-30
GPK (Graphic Packaging Holding Company) Start Date:2007-01-03
GPMT (Granite Point Mortgage Trust) Start Date:2017-06-23
GPN (Global Payments) Start Date:2005-01-03
GPP (Green Plains Partners Lp Common Units) Start Date:2015-06-26
GPRE (Green Plains) Start Date:2007-05-16
GPRK (Geopark Limited) Start Date:2014-02-07
GPRO (Gopro  O) Start Date:2014-06-26
GPS (Gap) Start Date:2005-01-03
GRAB (Grab) Start Date:2021-12-02
GRABW (Grab Holdings Warrant) Start Date:2021-12-02
GRBK (Green Brick Energy) Start Date:2007-06-19
GRC (Gorman-Rupp Company) Start Date:2007-05-09
GRCL (Gracell Biotechnologies) Start Date:2021-01-08
GREE (Greenidge Generation Holdings Class A Common) Start Date:2021-09-15
GRF (Eagle Capital Growth Fund) Start Date:2007-06-08
GRFS (Grifols S.A.) Start Date:2011-06-02
GRFX (Graphex) Start Date:2022-08-17
GRI (Gri Bio Inc) Start Date:2021-02-10
GRIN (Grindrod Shipping Holdings Ordinary Shares) Start Date:2018-06-18
GRMN (Garmin Ltd.) Start Date:2005-01-03
GRNAW (Greenlight Biosciences Holdings Pbc Warrant) Start Date:2021-03-08
GRND (Grindr) Start Date:2021-01-14
GRNQ (Greenpro Capital) Start Date:2015-07-09
GRNT (Granite Ridge Resources) Start Date:2022-10-25
GROM (Grom Social Enterprises) Start Date:2021-06-17
GROMW (Grom Social Enterprises Warrants) Start Date:2021-06-17
GROV (Grove Collaborative Holdings Class A) Start Date:2021-05-13
GROW (U.S. Global Investors Class A) Start Date:2007-05-01
GROY (Gold Royalty) Start Date:2021-03-09
GRPH (Graphite Bio) Start Date:2021-06-25
GRPN (on) Start Date:2011-11-04
GRRR (Gorilla Technology) Start Date:2022-07-14
GRTS (Gritstone Oncology) Start Date:2018-09-28
GRTX (Galera Therapeutics) Start Date:2019-11-07
GRVY (Gravity Co. ADS) Start Date:2007-05-16
GRWG (Growgeneration) Start Date:2016-11-11
GRX (The Gabelli Healthcare & Wellness Trust Common Shares Of Beneficial Interest) Start Date:2007-06-29
GS (Goldman Sachs) Start Date:2005-01-03
GSAT (Globalstar,) Start Date:2007-05-08
GSBC (Great Southern Bancorp) Start Date:2007-05-16
GSBD (Goldman Sachs Bdc) Start Date:2015-03-18
GSD (Global Systems Dynamics Class A) Start Date:2021-09-28
GSDWU (Global Systems Dynamics Unit) Start Date:2021-08-05
GSEVU (Gores Holdings Vii Units) Start Date:2021-02-23
GSEVW (Gores Holdings Vii Warrant) Start Date:2021-04-15
GSHD (Goosehead Insurance) Start Date:2018-04-27
GSIT (Gsi Technology) Start Date:2007-05-16
GSIW (Garden Stage Limited) Start Date:2023-12-01
GSK (Glaxosmithkline Plc) Start Date:2007-05-01
GSL (Global Ship Lease,) Start Date:2008-08-15
GSM (Ferroglobe Plc Ordinary Shares) Start Date:2015-12-24
GSMGW (Glory Star New Media Holdings Warrant Expiring 2/13/2025) Start Date:2018-09-12
GSUN (Golden Sun Education) Start Date:2022-06-22
GT (The Goodyear Tire & Rubber Company) Start Date:2005-01-03
GTBP (Gt Biopharma) Start Date:2021-02-11
GTE (Gran Tierra Energy) Start Date:2008-04-08
GTEC (Greenland Technologies Holding Ordinary Shares) Start Date:2018-08-08
GTES (Gates Industrial Plc) Start Date:2018-01-25
GTH (Genetron Holdings) Start Date:2020-06-19
GTHX (G1 Therapeutics) Start Date:2017-05-17
GTIM (Good Times Restaurants) Start Date:2007-05-18
GTLB (Gitlab Class A) Start Date:2021-10-14
GTLS (Chart Industries) Start Date:2007-04-27
GTN (Gray Television) Start Date:2007-05-07
GTPBU (Gores Technology Partners Ii Units) Start Date:2021-03-12
GTPBW (Gores Technology Partners Ii Warrant) Start Date:2021-05-06
GTX (Garrett Technologies) Start Date:2021-05-03
GTXAP (Garrett Motion Series A Cumulative Convertible Preferred Stock) Start Date:2021-05-28
GTY (Getty Realty Corp) Start Date:2007-05-08
GUG (Guggenheim Active Allocation Fund Common Shares Of Beneficial Interest) Start Date:2021-11-24
GURE (Gulf Resources) Start Date:2009-10-27
GUT (Gabelli Utility Trust) Start Date:2007-05-16
GV (Visionary Education Technology Holdings Inc) Start Date:2022-05-17
GV (Visionary Education Technology Holdings Inc) Start Date:2023-08-01
GVA (Granite Construction) Start Date:2007-05-02
GVH (Globavend Holdings Limited) Start Date:2023-11-08
GVP (Gse Systems) Start Date:2007-05-16
GWAV (Greenwave Technology Solutions) Start Date:2015-04-09
GWH (Ess Tech,) Start Date:2021-10-11
GWRE (Guidewire Software) Start Date:2012-01-25
GWRS (Global Water Resources) Start Date:2016-04-28
GWW (Grainger) Start Date:2005-01-03
GXO (Gxo Logistics) Start Date:2021-08-02
GYRE (Gyre Therapeutics Inc) Start Date:2007-05-16
GYRO (Gyrodyne, Llc) Start Date:2015-09-01
H (Hyatt Hotels Corporation) Start Date:2009-11-05
HA (Hawaiian) Start Date:2007-05-09
HAE (Haemonetics Corporation) Start Date:2007-01-03
HAFC (Hanmi Financial) Start Date:2007-05-04
HAIN (The Hain Celestial) Start Date:2007-01-03
HAL (Halliburton Co.) Start Date:2005-01-03
HALL (Hallmark Financial Services) Start Date:2007-05-16
HALO (Halozyme Therapeutics) Start Date:2007-05-10
HARP (Harpoon Therapeutics) Start Date:2019-02-08
HAS (Hasbro) Start Date:2005-01-03
HAYN (Haynes International) Start Date:2007-05-16
HAYW (Hayward) Start Date:2021-03-12
HBAN (Huntington Bancshares) Start Date:2009-09-18
HBANM (Huntington Bancshares Incorporated Depositary Shares Each Representing A 1/1000Th Interest In A Share Of Huntington Series I Preferred Stock) Start Date:2021-06-10
HBB (Hamilton Beach Brands Hldg Co) Start Date:2017-10-02
HBCP (Home Bancorp) Start Date:2008-10-03
HBI (Hanesbrands Inc) Start Date:2006-09-06
HBIO (Harvard Bioscience) Start Date:2013-10-21
HBM (Hudbay Minerals) Start Date:2010-10-25
HBNC (Horizon Bancorp) Start Date:2007-05-16
HBT (Hbt Financial) Start Date:2019-10-11
HCA (Hca Holdings) Start Date:2011-03-10
HCAT (Health Catalyst) Start Date:2019-07-25
HCC (Warrior Met Coal) Start Date:2017-04-13
HCCI (Heritage-Crystal Clean) Start Date:2008-03-12
HCDI (Harbor Custom Development) Start Date:2020-08-28
HCDWQ (Harbor Custom Development Inc) Start Date:2021-06-10
HCDZQ (Harbor Custom Development Inc) Start Date:2021-10-05
HCI (Hci) Start Date:2012-10-25
HCICU (Hennessy Capital Investment V Units) Start Date:2021-01-15
HCICW (Hennessy Capital Investment V Warrant) Start Date:2021-03-08
HCIIU (Hudson Executive Investment Ii Unit) Start Date:2021-01-26
HCIIW (Hudson Executive Investment Ii Warrant) Start Date:2021-03-22
HCKT (Hackett) Start Date:2008-01-31
HCM (Hutchmed) Start Date:2016-03-17
HCMA (Hcm Acquisition Corp) Start Date:2022-03-16
HCP (Hashicorp) Start Date:2021-12-09
HCSG (Healthcare Services) Start Date:2007-05-02
HCTI (Healthcare Triangle) Start Date:2021-10-13
HCVI (Hennessy Capital Investment Vi Class A) Start Date:2021-11-24
HCVIU (Hennessy Capital Investment Vi Unit) Start Date:2021-09-29
HCWB (Hcw Biologics) Start Date:2021-07-20
HD (Home Depot) Start Date:2005-01-03
HDB (Hdfc Bank) Start Date:2007-04-27
HDSN (Hudson Technologies) Start Date:2007-05-16
HE (Hawaiian Electric Industries) Start Date:2007-01-03
HEAR (Turtle Beach Commo) Start Date:2012-03-22
HEES (H&E Equipment Services) Start Date:2007-05-03
HEI (Heico Corporation) Start Date:2007-01-03
HEI.A (Heico Corp) Start Date:2007-05-16
HELE (Helen Of Troy) Start Date:2007-04-30
HEP (Holly Energy Partners, L.P.) Start Date:2007-05-16
HEPA (Hepion Pharmaceuticals) Start Date:2014-02-10
HEPS (D-Market Electronic Services & Trading) Start Date:2021-07-01
HEQ (John Hancock Hedged Equity & Income Fund Common Shares Of Beneficial Interest) Start Date:2011-05-26
HES (Hess Corporation) Start Date:2007-04-27
HESM (Hess Midstream Lp Class A Share Representing A Partner Interest) Start Date:2017-04-05
HFBL (Home Federal Bancorp Of Louisiana) Start Date:2007-05-23
HFFG (Hf Foods) Start Date:2017-09-07
HFRO (Highland Income Fund) Start Date:2017-11-06
HFWA (Heritage Financial) Start Date:2007-05-16
HG (Hamilton Insurance) Start Date:2023-11-10
HGBL (Heritage Global) Start Date:2007-05-16
HGLB (Highland Global Allocation Fund) Start Date:2019-02-19
HGTY (Hagerty Class A) Start Date:2021-06-01
HGV (Hilton Grand Vacations) Start Date:2016-12-14
HHGC (Hhg Capital Ordinary Shares) Start Date:2021-11-11
HHGCW (Hhg Capital Warrant) Start Date:2021-11-11
HHH (Howard Hughes Holdings Inc) Start Date:2010-11-05
HHS (Harte-Hanks) Start Date:2021-12-01
HI (Hillenbrand) Start Date:2008-04-01
HIBB (Hibbett Sports) Start Date:2007-04-27
HIE (Miller/Howard High Income Equity Fund Common Shares Of Beneficial Interest) Start Date:2014-11-25
HIFS (Hingham Institution) Start Date:2007-05-16
HIG (Hartford Financial Svc.Gp.) Start Date:2005-01-03
HIHO (Highway Holdings) Start Date:2007-05-16
HII (Huntington Ingalls Industries) Start Date:2011-03-22
HIIIU (Hudson Executive Investment Iii Unit) Start Date:2021-02-24
HIMS (Hims & Hers Health,) Start Date:2019-09-13
HIMX (Himax Technologies American Depositary Shares) Start Date:2007-04-23
HIO (Western Asset High Income Opportunity Fund) Start Date:2007-05-09
HIPO (Hippo Holdings) Start Date:2021-07-29
HITI (High Tide Common Shares) Start Date:2021-06-02
HIVE (Hive Blockchain Technologies Common Shares) Start Date:2021-07-01
HIW (Highwoods Properties) Start Date:2007-01-03
HIX (Western Asset High Income Fund Ii) Start Date:2007-05-04
HKD (Amtd Digital) Start Date:2022-07-15
HKIT (Hitek Global) Start Date:2023-03-31
HL (Hecla Mining) Start Date:2007-04-30
HLAHU (Hamilton Lane Alliance Holdings I Unit) Start Date:2021-01-13
HLAHW (Hamilton Lane Alliance Holdings I Warrant) Start Date:2021-03-15
HLBZW (Helbiz Warrant) Start Date:2019-12-09
HLF (Herbalife Nutrition Ltd.) Start Date:2007-01-03
HLGN (Heliogen) Start Date:2021-05-07
HLI (Houlihan Lokey) Start Date:2015-08-13
HLIO (Helios Technologies) Start Date:2007-05-16
HLIT (Harmonic) Start Date:2007-05-01
HLLY (Holley) Start Date:2020-11-27
HLMN (Hillman Solutions) Start Date:2021-07-12
HLN (Haleon Plc) Start Date:2022-07-18
HLNE (Hamilton Lane Incorporated) Start Date:2017-03-01
HLP (Hongli) Start Date:2023-03-29
HLT (Hilton Worldwide Holdings Inc) Start Date:2013-12-12
HLTH (Cue Health) Start Date:2021-09-24
HLVX (Hillevax) Start Date:2022-04-29
HLX (Helix Energy Solutions) Start Date:2007-04-30
HMA (Heartland Media Acquisition) Start Date:2022-03-14
HMC (Honda Motor Company) Start Date:2007-05-01
HMN (Horace Mann Educators) Start Date:2007-05-01
HMNF (Hmn Financial) Start Date:2007-05-16
HMST (Homestreet) Start Date:2012-02-10
HMY (Harmony Gold Mining Company Limited) Start Date:2007-04-26
HNI (Hni) Start Date:2007-05-08
HNNA (Hennessy Advisors) Start Date:2007-05-16
HNRA (Hnr Acquisition Corp) Start Date:2022-04-06
HNRG (Hallador Energy Company) Start Date:2010-05-21
HNST (The Honest Company) Start Date:2021-05-05
HNVR (Hanover Bancorp) Start Date:2022-05-11
HNW (Pioneer Diversified High Income Fund) Start Date:2007-05-25
HOFT (Hooker Furniture) Start Date:2007-05-07
HOFV (Hall Of Fame Resort & Entertainment Company) Start Date:2020-07-02
HOFVW (Hall Of Fame Resort & Entertainment Company Warrant) Start Date:2020-07-02
HOG (Harley-Davidson) Start Date:2006-09-01
HOLI (Hollsys Automation Technologies International, Common) Start Date:2008-08-01
HOLO (Microcloud Hologram) Start Date:2021-08-06
HOLX (Hologic) Start Date:2005-01-03
HOMB (Home Bancshares) Start Date:2007-01-03
HON (Honeywell Int'l) Start Date:2005-01-03
HONE (Harborone Bancorp) Start Date:2016-06-30
HOOD (Robinhood Markets) Start Date:2021-07-29
HOOK (Hookipa Pharma) Start Date:2019-04-18
HOPE (Hope Bancorp) Start Date:2007-05-01
HOTH (Hoth Therapeutics) Start Date:2019-02-15
HOUR (Hour Loop) Start Date:2022-01-07
HOUS (Anywhere Real Estate) Start Date:2012-10-11
HOV (Hovnanian Enterprises, Class A) Start Date:2007-04-30
HOVNP (Hovnanian Enterprises Inc Dep Shr Srs A Pfd) Start Date:2007-05-16
HOWL (Werewolf Therapeutics) Start Date:2021-04-30
HP (Helmerich & Payne) Start Date:2005-01-03
HPCO (Hempacco Co.) Start Date:2022-08-30
HPE (Hewlett Packard Enterprise) Start Date:2015-11-02
HPF (John Hancock Pfd Income Fund Ii Pfd Income Fund Ii) Start Date:2007-05-16
HPI (John Hancock Preferred Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-23
HPK (Highpeak Energy,) Start Date:2020-08-24
HPKEW (Highpeak Energy Warrant) Start Date:2020-08-24
HPP (Hudson Pacific Properties) Start Date:2010-06-24
HPQ (Hp) Start Date:2005-01-03
HPS (John Hancock Preferred Income Fund Iii Preferred Income Fund Iii) Start Date:2007-05-08
HQH (Tekla Healthcare Investors) Start Date:2007-05-08
HQI (Hirequest) Start Date:2007-05-16
HQL (Teklalife Sciences Investors) Start Date:2007-05-04
HQY (Healthequity) Start Date:2014-07-31
HR (Healthcare Realty Trust Incorporated) Start Date:2007-01-03
HRB (Block H&R) Start Date:2005-01-03
HRI (Herc) Start Date:2007-05-02
HRL (Hormel Foods) Start Date:2005-01-03
HRMY (Harmony Biosciences) Start Date:2020-08-19
HROW (Harrow Health) Start Date:2013-02-08
HRT (Hireright Holdings Corporation) Start Date:2021-10-29
HRTG (Heritage Insurance In) Start Date:2014-05-23
HRTX (Heron Therapeutics Commo) Start Date:2007-05-16
HRYU (Hanryu Holdings) Start Date:2023-08-01
HRZN (Horizon Technology Finance) Start Date:2010-10-29
HSAI (Hesai) Start Date:2023-02-09
HSBC (Hsbc Holdings Plc.) Start Date:2007-04-27
HSCS (Heart Test Laboratories) Start Date:2022-06-15
HSCSW (Heart Test Laboratories Warrant) Start Date:2022-06-15
HSDT (Helius Medical Technologies Class A) Start Date:2014-06-27
HSHP (Himalaya Shipping Ltd.) Start Date:2023-03-31
HSIC (Henry Schein) Start Date:2005-01-03
HSII (Heidrick & Struggles) Start Date:2007-05-07
HSON (Hudson Global) Start Date:2007-04-30
HSPO (Horizon Space Acquisition I) Start Date:2023-01-26
HST (Host Hotels & Resorts) Start Date:2006-04-18
HSTM (Healthstream) Start Date:2007-05-16
HSTO (Histogen) Start Date:2013-07-25
HSY (The Hershey Company) Start Date:2005-01-03
HT (Hersha Hospitality) Start Date:2007-05-04
HTBI (Hometrust Bancshares) Start Date:2012-07-11
HTBK (Heritage Commerce) Start Date:2007-05-16
HTCR (Heartcore Enterprises) Start Date:2022-02-10
HTD (John Hancock Tax Advantaged Dividend Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-04
HTGC (Hercules Capital) Start Date:2007-05-08
HTGM (Htg Molecular Diagnostics) Start Date:2015-05-06
HTH (Hilltop) Start Date:2007-08-01
HTHT (Huazhu Limited) Start Date:2010-03-26
HTIA (Healthcare Trust 7.375% Series A Cumulative Redeemable Perpetual Preferred Stock) Start Date:2020-03-30
HTLD (Heartland Express) Start Date:2007-05-02
HTLF (Heartland Financial Usa) Start Date:2017-03-31
HTLFP (Heartland Financial Usa Depositary Shares Each Representing A 1/400Th Ownership Interest In A Share Of 7.00% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E) Start Date:2020-06-29
HTOO (Fusion Fuel Green Plc Class A Ordinary Shares) Start Date:2020-12-10
HTOOW (Fusion Fuel Green Plc Warrant) Start Date:2020-12-10
HTY (John Hancock Tax-Advantaged Global Shareholder Yield Fund Common Shares Of Beneficial Interest) Start Date:2007-09-26
HTZ (Hertz Global Holdings, Inc) Start Date:2021-11-09
HTZWW (Hertz Global Holdings Inc Warrant) Start Date:2021-11-09
HUBB (Hubbell Corp) Start Date:2009-10-29
HUBG (Hub) Start Date:2007-05-01
HUBS (Hubspot) Start Date:2014-10-09
HUDA (Hudson Acquisition I) Start Date:2022-12-27
HUDI (Huadi International Co., Ordinary Shares) Start Date:2021-01-22
HUGE (Fsd Pharma Class B Subordinate Voting Shares) Start Date:2020-01-09
HUIZ (Huize Holding) Start Date:2020-02-12
HUM (Humana) Start Date:2005-01-03
HUMA (Humacyte) Start Date:2021-08-23
HUMAW (Humacyte Warrant) Start Date:2020-11-24
HUN (Huntsman Corporation) Start Date:2007-01-03
HURC (Hurco Companies) Start Date:2007-05-11
HURN (Huron Consulting) Start Date:2007-05-04
HUSA (Houston American Energy) Start Date:2007-07-05
HUT (Hut 8 Mining Common Shares) Start Date:2021-06-15
HUYA (Huya) Start Date:2018-05-11
HVT (Haverty Furniture) Start Date:2007-05-04
HVT.A (Haverty Furniture Companies) Start Date:2007-05-16
HWBK (Hawthorn Bancshares) Start Date:2007-06-18
HWC (Hancock Whitney Corporation) Start Date:2007-05-03
HWKN (Hawkins) Start Date:2007-05-16
HWM (Howmet Aerospace) Start Date:2016-11-01
HXL (Hexcel Corporation) Start Date:2007-01-03
HY (Hyster-Yale Materials) Start Date:2012-10-01
HYAC (Haymaker Acquisition 4) Start Date:2023-09-15
HYB (New America High Income Fund) Start Date:2007-04-25
HYFM (Hydrofarm) Start Date:2020-12-10
HYI (Western Asset High Yield Defined Opportunity Fund) Start Date:2010-10-27
HYLN (Hyliion Holdings) Start Date:2020-10-02
HYMC (Hycroft Mining Holding Class A) Start Date:2018-03-12
HYMCL (Hycroft Mining Holding Warrants) Start Date:2021-01-25
HYMCW (Hycroft Mining Holding Warrant) Start Date:2020-06-01
HYMCZ (Hycroft Mining Holding Warrant) Start Date:2017-02-17
HYPR (Hyperfine Class A) Start Date:2021-01-27
HYT (Blackrock Corporate High Yield Fund) Start Date:2007-05-09
HYW (Hywin Holdings) Start Date:2021-03-26
HYZN (Hyzon Motors Class A) Start Date:2021-07-14
HYZNW (Hyzon Motors Warrants) Start Date:2020-12-14
HZNP (Horizon Therapeutics Public Company) Start Date:2011-07-28
HZO (Marinemax) Start Date:2007-05-03
IAC (Iac/Interactivecorp) Start Date:2020-07-01
IAE (Voya Asia Pacific High Dividend Equity Income Fund Ing Asia Pacific High Dividend Equity Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
IAF (Aberdeen Australia Equity Fund Inc) Start Date:2007-05-16
IAG (Iamgold Corporation) Start Date:2007-04-25
IART (Integra Lifesciences Holdings Corporation) Start Date:2007-01-03
IAS (Integral Ad Science Holding) Start Date:2021-06-30
IAUX (I-80 Gold Common Shares) Start Date:2022-05-19
IBCP (Independent Bank) Start Date:2007-05-08
IBEX (Ibex) Start Date:2020-08-07
IBIO (Ibio) Start Date:2008-08-19
IBKR (Interactive Brokers) Start Date:2007-05-04
IBM (International Business Machines) Start Date:2005-01-03
IBN (Icici Bank Limited) Start Date:2007-01-03
IBOC (International Bancshares) Start Date:2007-05-04
IBP (Installed Building Products) Start Date:2014-02-13
IBRX (Immunitybio,) Start Date:2021-03-10
IBTX (Independent Bank  Co) Start Date:2013-04-03
ICAD (Icad) Start Date:2007-05-11
ICCC (Immucell) Start Date:2007-05-16
ICCH (Icc Holdings) Start Date:2017-03-28
ICCM (Icecure Medical Ordinary Shares) Start Date:2021-08-26
ICD (Independence Contract Drilling) Start Date:2014-08-08
ICE (Intercontinental Exchange) Start Date:2005-11-16
ICFI (Icf International) Start Date:2007-05-16
ICG (Intchains Limited) Start Date:2023-03-16
ICHR (Ichor) Start Date:2016-12-09
ICL (Icl Ltd.) Start Date:2014-09-24
ICLK (Iclick Interactive Asia American Depositary Shares) Start Date:2017-12-22
ICLR (Icon Plc) Start Date:2007-05-03
ICMB (Investcorp Credit Management Bdc) Start Date:2014-02-06
ICPT (Intercept Pharmaceuticals) Start Date:2012-10-11
ICU (Seastar Medical Holding) Start Date:2021-03-18
ICUI (Icu Medical) Start Date:2007-04-30
ICVX (Icosavax) Start Date:2021-07-29
IDA (Idacorp) Start Date:2007-01-03
IDAI (T Stamp Class A) Start Date:2021-06-21
IDCC (Interdigital) Start Date:2007-04-27
IDE (Voya Infrastructure Industrials And Materials Fund Common Shares Of Beneficial Interest) Start Date:2010-01-27
IDEX (Ideanomics,) Start Date:2007-05-16
IDICQ (Parts Id Inc) Start Date:2007-05-02
IDN (Intellicheck) Start Date:2007-05-16
IDR (Idaho Strategic Resources) Start Date:2022-03-11
IDT (Idt) Start Date:2011-08-01
IDXX (Idexx Laboratories) Start Date:2005-01-03
IDYA (Ideaya Biosciences) Start Date:2019-05-23
IE (Ivanhoe Electric) Start Date:2022-06-28
IEAWW (Infrastructure And Energy Alternatives Warrant) Start Date:2016-08-30
IEP (Icahn Enterprises L.P) Start Date:2007-09-18
IESC (Ies) Start Date:2007-05-16
IEX (Idex Corporation) Start Date:2005-01-03
IFBD (Infobird) Start Date:2021-04-20
IFF (Intl Flavors & Fragrances) Start Date:2005-01-03
IFN (India Fund) Start Date:2007-04-27
IFRX (Inflarx N.V.) Start Date:2017-11-16
IFS (Intercorp Financial Services) Start Date:2019-07-19
IGA (Voya Global Advantage And Premium Opportunity Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
IGC (India Globalization Capital) Start Date:2019-02-26
IGD (Voya Global Equity Dividend And Premium Opportunity Fund) Start Date:2007-05-01
IGI (Western Asset Investment Grade Defined Opportunity Trust) Start Date:2009-06-26
IGIC (International General Insurance Holdings Ordinary Share) Start Date:2018-04-10
IGICW (International General Insurance Holdings Warrants Expiring 03/17/2025) Start Date:2018-04-10
IGMS (Igm Biosciences) Start Date:2019-09-18
IGR (Cbre Global Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2007-04-26
IGT (International Game Technology) Start Date:2015-04-07
IH (Ihuman) Start Date:2020-10-09
IHD (Voya Emerging Markets High Income Dividend Equity Fund Common Shares) Start Date:2011-04-27
IHG (Intercontinental Hotels Plc) Start Date:2007-01-03
IHIT (Invesco High Income 2023 Target Term Fund Common Shares Of Beneficial Interest) Start Date:2016-11-23
IHRT (Iheartmedia) Start Date:2019-05-07
IHS (Ihs Holding Limited) Start Date:2021-10-14
IHT (Innsuites Hospitality Trust Shares Of Beneficial Interest) Start Date:2007-05-17
IHTA (Invesco High Income 2024 Target Term Fund Common Shares Of Beneficial Interest No Par Value Per Share) Start Date:2017-11-30
IIF (Morgan Stanley India Investment Fund) Start Date:2013-11-19
III (Information Services Grp) Start Date:2007-05-16
IIIN (Insteel Industries) Start Date:2007-05-01
IIIV (I3 Verticals) Start Date:2018-06-21
IIM (Invesco Value Municipal Income Trust) Start Date:2007-05-16
IINN (Inspira Technologies Oxy) Start Date:2021-07-14
IINNW (Inspira Technologies Oxy B.H.N. Warrant) Start Date:2021-07-14
IIPR (Innovative Industrial Properties) Start Date:2016-12-01
IIVIP (Ii-Vi Incorporated 6.00% Series A Mandatory Convertible Preferred Stock) Start Date:2020-08-07
IKNA (Ikena Oncology) Start Date:2021-03-26
IKT (Inhibikase Therapeutics) Start Date:2020-12-23
ILAG (Intelligent Living Application) Start Date:2022-07-13
ILLM (Acuityads Holdings Inc) Start Date:2021-06-10
ILMN (Illumina Inc) Start Date:2005-01-03
ILPT (Industrial Logistics Properties Trust Common Share) Start Date:2018-01-12
IMAB (I-Mab) Start Date:2020-01-17
IMACW (Imac Holdings Warrant) Start Date:2019-02-13
IMAX (Imax) Start Date:2007-04-26
IMBI (Imedia Brands Class A) Start Date:2007-05-01
IMCC (Im Cannabis Common Shares) Start Date:2021-03-01
IMCI (Infinite) Start Date:2022-11-21
IMCR (Immunocore Plc) Start Date:2021-02-05
IMGN (Immunogen) Start Date:2007-04-30
IMKTA (Ingles Markets) Start Date:2007-05-04
IMMP (Immutep American Depositary Shares) Start Date:2013-02-11
IMMR (Immersion) Start Date:2007-05-09
IMMX (Immix Biopharma) Start Date:2021-12-16
IMNM (Immunome) Start Date:2020-10-02
IMNN (Imunon) Start Date:2007-07-06
IMO (Imperial Oil Limited) Start Date:2007-01-03
IMOS (Chipmos Technologies American Depositary Shares) Start Date:2013-02-11
IMPH (Impac Mortgage Holdings Inc) Start Date:2007-04-27
IMPL (Impel Neuropharma) Start Date:2021-04-23
IMPP (Imperial Petroleum) Start Date:2021-12-06
IMRN (Immuron American Depositary Shares) Start Date:2017-03-02
IMRX (Immuneering) Start Date:2021-07-30
IMTE (Integrated Media Technology) Start Date:2017-08-11
IMTX (Immatics N.V. Ordinary Shares) Start Date:2020-07-02
IMTXW (Immatics N.V. Warrants) Start Date:2020-07-02
IMUX (Immunic) Start Date:2019-04-17
IMVT (Immunovant) Start Date:2019-06-21
IMXI (International Money Express) Start Date:2017-03-27
INAB (In8bio) Start Date:2021-07-30
INBK (First Internet Bancorp Common) Start Date:2013-02-22
INBS (Intelligent Bio Solutions) Start Date:2020-12-23
INBX (Inhibrx) Start Date:2020-08-19
INCR (Intercure Ordinary Shares) Start Date:2021-09-01
INCY (Incyte) Start Date:2005-01-03
INDB (Independent Bank) Start Date:2007-05-02
INDI (Indie Semiconductor, Class A) Start Date:2021-06-11
INDIW (Indie Semiconductor Warrant) Start Date:2021-06-11
INDO (Indonesia Energy) Start Date:2019-12-19
INDP (Indaptus Therapeutics) Start Date:2021-08-04
INDT (Indus Realty Trust,) Start Date:2007-05-17
INFA (Informatica) Start Date:2021-10-27
INFI (Infinity Pharmaceuticals) Start Date:2007-05-16
INFN (Infinera) Start Date:2007-06-07
INFU (Infusystems) Start Date:2010-12-23
INFY (Infosys ADR) Start Date:2005-01-03
ING (Ing Groep N.V.) Start Date:2007-01-03
INGN (Inogen) Start Date:2014-02-14
INGR (Ingredion) Start Date:2007-04-30
INHD (Inno Holdings) Start Date:2023-12-14
INKT (Mink Therapeutics) Start Date:2021-10-15
INLX (Intellinetics) Start Date:2012-02-14
INM (Inmed Pharmaceuticals Common Shares) Start Date:2020-06-19
INMB (Inmune Bio) Start Date:2019-02-04
INMD (Inmode Ordinary Shares) Start Date:2019-08-08
INN (Summit Hotel Properties) Start Date:2011-02-09
INNV (Innovage Holding) Start Date:2021-03-04
INO (Inovio Pharmaceuticals) Start Date:2007-01-03
INOD (Innodata) Start Date:2007-05-16
INPX (Inpixon) Start Date:2016-12-12
INSE (Inspired Entertainment) Start Date:2014-12-11
INSG (Inseego) Start Date:2007-05-01
INSI (Insight Select Income Fund) Start Date:2007-05-16
INSM (Insmed Incorporated) Start Date:2007-04-23
INSP (Inspire Medical Systems) Start Date:2018-05-03
INST (Instructure) Start Date:2021-07-22
INSW (International Seaways) Start Date:2016-11-16
INTA (Intapp) Start Date:2021-06-30
INTC (Intel) Start Date:2005-01-03
INTG (Intergroup Corporation) Start Date:2007-05-16
INTR (Inter & Class A) Start Date:2022-06-23
INTS (Intensity Therapeutics) Start Date:2023-06-30
INTT (Intest) Start Date:2007-05-16
INTU (Intuit) Start Date:2005-01-03
INTZ (Intrusion) Start Date:2007-05-16
INUV (Inuvo) Start Date:2009-07-31
INVA (Innoviva) Start Date:2007-05-04
INVE (Identive) Start Date:2010-01-15
INVH (Invitation Homes) Start Date:2017-02-01
INVO (Invo Bioscience) Start Date:2020-11-13
INVZ (Innoviz Technologies Ordinary Shares) Start Date:2021-04-06
INVZW (Innoviz Technologies Warrant) Start Date:2021-04-06
INZY (Inozyme Pharma) Start Date:2020-07-24
IOBT (Io Biotech) Start Date:2021-11-05
IONM (Assure Holdings) Start Date:2021-09-29
IONQ (Ionq,) Start Date:2021-01-04
IONR (Ioneer Ltd) Start Date:2022-06-30
IONS (Ionis Pharmaceuticals) Start Date:2007-05-01
IOR (Income Opportunity Realty Investors) Start Date:2007-05-18
IOSP (Innospec) Start Date:2007-05-07
IOT (Samsara) Start Date:2021-12-15
IOVA (Iovance Biotherapeutics) Start Date:2009-09-01
IP (International Paper) Start Date:2005-01-03
IPA (Immunoprecise Antibodies) Start Date:2017-01-03
IPAR (Inter Parfums) Start Date:2007-05-11
IPDN (Professional Diversity Network) Start Date:2013-03-05
IPG (Interpublic) Start Date:2005-01-03
IPGP (Ipg Photonics) Start Date:2006-12-13
IPHA (Innate Pharma S.A. ADS) Start Date:2019-10-17
IPI (Intrepid Potash) Start Date:2008-04-22
IPOD (Social Capital Hedosophia Holdings Iv Class A Ordinary Shares) Start Date:2020-12-15
IPOF (Social Capital Hedosophia Holdings Vi Class A Ordinary Shares) Start Date:2020-11-30
IPSC (Century Therapeutics) Start Date:2021-06-18
IPVF (Interprivate Iii Financial Partners Class A) Start Date:2021-04-26
IPVIU (Interprivate Iv Infratech Partners Units) Start Date:2021-03-05
IPVIW (Interprivate Iv Infratech Partners Warrant) Start Date:2021-04-30
IPW (Ipower) Start Date:2021-05-12
IPWR (Ideal Power) Start Date:2013-11-22
IPX (Iperionx American Depositary Share) Start Date:2022-06-21
IPXX (Inflection Point Acquisition Ii) Start Date:2023-07-17
IQ (IQiyi) Start Date:2018-03-29
IQI (Invesco Quality Municipal Income Trust) Start Date:2007-05-16
IQV (IQvia Holdings) Start Date:2013-05-09
IR (Ingersoll-Rand Plc) Start Date:2017-05-12
IRBT (Irobot Corporation) Start Date:2007-01-03
IRDM (Iridium Communications) Start Date:2009-09-24
IREN (Iris Energy Ordinary Shares) Start Date:2021-11-17
IRIX (Iridex) Start Date:2007-05-16
IRL (New Ireland Fund Inc) Start Date:2007-05-16
IRM (Iron Mountain Incorporated) Start Date:2005-01-03
IRMD (Iradimed Corp) Start Date:2014-07-16
IRON (Disc Medicine) Start Date:2020-08-12
IROQ (If Bancorp) Start Date:2011-07-08
IRS (Irsa Inversiones Y Representaciones S.A.) Start Date:2007-05-02
IRT (Independence Realty Trust) Start Date:2013-09-18
IRTC (Irhythm Technologies) Start Date:2016-10-20
IRWD (Ironwood Pharmaceuticals) Start Date:2010-02-03
ISD (Pgim High Yield Bond Fund) Start Date:2012-04-26
ISDR (Issuer Direct) Start Date:2008-03-26
ISPC (Ispecimen) Start Date:2021-06-17
ISPO (Inspirat) Start Date:2021-02-09
ISPOW (Inspirato Incorporated Warrant) Start Date:2021-02-09
ISPR (Ispire Technology) Start Date:2023-04-04
ISRG (Intuitive Surgical) Start Date:2006-06-01
ISRL (Israel Acquisitions Corp) Start Date:2023-02-28
ISSC (Innovative Solutions And Support) Start Date:2007-05-04
ISTR (Investar Holding Corp) Start Date:2014-07-01
ISUN (Isun) Start Date:2016-04-26
IT (Gartner Inc) Start Date:2005-01-03
ITCI (Intra-Cellular Therapies) Start Date:2014-01-31
ITCL (Banco Itau Chile) Start Date:2007-05-16
ITGR (Integer Holdings Corporation) Start Date:2007-05-08
ITI (Iteris) Start Date:2007-05-16
ITIC (Investors Title) Start Date:2007-05-16
ITOS (Iteos Therapeutics) Start Date:2020-07-24
ITP (It Tech Packaging) Start Date:2009-12-17
ITRG (Integra Resources Common Shares) Start Date:2020-07-31
ITRI (Itron) Start Date:2007-04-30
ITRM (Iterum Therapeutics Plc Ordinary Share) Start Date:2018-05-25
ITRN (Ituran Location And Control Ltd.) Start Date:2007-05-16
ITT (Itt) Start Date:2007-05-01
ITUB (Itau Unibanco Holding S.A.) Start Date:2009-05-20
ITW (Illinois Tool Works) Start Date:2007-04-30
IVA (Inventiva) Start Date:2020-07-13
IVAC (Intevac) Start Date:2007-04-30
IVCA (Investcorp India Acquisition Corp) Start Date:2022-06-30
IVDA (Iveda Solutions) Start Date:2009-10-12
IVH (Delaware Ivy High Income Opportunities Fund) Start Date:2013-05-29
IVP (Inspire Veterinary Partners) Start Date:2023-08-30
IVR (Invesco Mortgage Capital) Start Date:2009-06-26
IVT (Inventrust Properties) Start Date:2021-10-12
IVVD (Invivyd) Start Date:2021-08-06
IVZ (Invesco Ltd.) Start Date:2007-12-04
IX (Orix ADS) Start Date:2007-05-16
IXHL (Incannex Healthcare American Depositary Shares) Start Date:2022-03-02
IZEA (Izea Worldwide) Start Date:2011-06-07
IZM (Iczoom ,) Start Date:2023-03-15
J (Jacobs Engineering) Start Date:2007-05-02
JACK (Jack In The Box) Start Date:2008-12-15
JAGX (Jaguar Health) Start Date:2015-05-13
JAKK (Jakks Pacific) Start Date:2007-05-01
JAMF (Jamf) Start Date:2020-07-22
JAN (Janone) Start Date:2007-05-16
JANX (Janux Therapeutics) Start Date:2021-06-11
JAZZ (Jazz Pharmaceuticals Plc) Start Date:2012-01-18
JBGS (Jbg Smith Properties) Start Date:2017-07-06
JBHT (J. B. Hunt Transport Services) Start Date:2005-01-03
JBI (Janus International ,) Start Date:2019-12-20
JBL (Jabil) Start Date:2005-01-03
JBLU (Jetblue Airways Corporation) Start Date:2007-01-03
JBSS (John B Sanfilippo) Start Date:2007-05-02
JBT (John Bean Technologies Corporation) Start Date:2008-08-01
JCE (Nuveen Core Equity Alpha Fund Nuveen Core Equity Alpha Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
JCI (Johnson Controls International) Start Date:2005-01-03
JCIC (Jack Creek Investment Class A Ordinary Shares) Start Date:2021-03-17
JCICU (Jack Creek Investment Units) Start Date:2021-01-22
JCICW (Jack Creek Investment Warrants) Start Date:2021-03-15
JCSE (Je Cleantech Holdings Ordinary Shares) Start Date:2022-04-22
JCTCF (Jewett-Cameron Trading Company Common Shares) Start Date:2007-05-16
JD (Jd.com Inc) Start Date:2014-05-22
JEF (Jefferies Financial) Start Date:2007-04-24
JELD (Jeld-Wen Holding) Start Date:2017-01-27
JEMD (Nuveen Emerging Markets Debt 2022 Target Term Fund Common Shares Of Beneficial Interest $0.01 Par Value Per Share) Start Date:2017-09-27
JEQ (Aberdeen Japan Equity Fund) Start Date:2007-05-16
JEWL (Adamas One) Start Date:2022-12-09
JFBR (Jeffs' Brands Ltd) Start Date:2022-08-26
JFIN (Jiayin  American Depositary Shares) Start Date:2019-05-10
JFR (Nuveen Floating Rate Income Fund) Start Date:2007-05-01
JFU (9F American Depositary Shares) Start Date:2019-08-15
JG (Aurora Mobile American Depositary Shares) Start Date:2018-07-26
JGGCR (Jaguar Global Growth I Right) Start Date:2022-04-04
JGGCU (Jaguar Global Growth I Unit) Start Date:2022-02-11
JGGCW (Jaguar Global Growth I Warrant) Start Date:2022-04-04
JGH (Nuveen Global High Income Fund Common Shares Of Beneficial Interest) Start Date:2014-11-24
JHAA (Nuveen Corporate Income 2023 Target Term Fund) Start Date:2018-12-19
JHG (Janus Henderson Plc) Start Date:2017-05-30
JHI (John Hancock Investors Trust) Start Date:2007-05-16
JHS (John Hancock Income Securities Trust) Start Date:2007-05-16
JHX (James Hardie Industries Plc American Depositary Shares) Start Date:2007-05-16
JILL (J. Jill) Start Date:2017-03-09
JJSF (J&J Snack Foods) Start Date:2007-05-04
JKHY (Jack Henry & Associates Inc) Start Date:2005-01-03
JKS (Jinkosolar Holding Company American Depositary Shares) Start Date:2010-05-14
JLL (Jones Lang Lasalle) Start Date:2007-05-01
JLS (Nuveen Mortgage And Income Fund) Start Date:2009-11-25
JMIA (Jumia Technologies Ag American Depositary Shares Each Representing Two Ordinary Shares) Start Date:2019-04-12
JMM (Nuveen Multi-Market Income Fund) Start Date:2007-05-16
JMSB (John Marshall Bancorp) Start Date:2013-11-21
JNJ (Johnson & Johnson) Start Date:2005-01-03
JNPR (Juniper Networks) Start Date:2009-10-29
JNVR (Janover) Start Date:2023-07-25
JOAN (Joann) Start Date:2021-03-12
JOB (Gee) Start Date:2007-05-16
JOBY (Joby Aviation,) Start Date:2021-08-11
JOE (St. Joe) Start Date:2007-05-03
JOF (Japan Smaller Capitalization Fund Inc) Start Date:2007-04-25
JOUT (Johnson Outdoors) Start Date:2007-05-16
JPC (Nuveen Preferred & Income Opportunities Fund) Start Date:2007-05-04
JPI (Nuveen Preferred And Income Term Fund Common Shares Of Beneficial Interest) Start Date:2012-07-27
JPM (JP Morgan Chase & Co.) Start Date:2005-01-03
JPS (Nuveen Preferred & Income Securities Fund) Start Date:2007-05-04
JPT (Nuveen Preferred And Income Fund Common Shares Of Beneficial Interest) Start Date:2017-01-27
JQC (Nuveen Credit Strategies Income Fund Shares Of Beneficial Interest) Start Date:2007-04-30
JRI (Nuveen Real Asset Income And Growth Fund Common Shares Of Beneficial Interest) Start Date:2012-04-26
JRO (Nuveen Floating Rate Income Opportuntiy Fund Shares Of Beneficial Interest) Start Date:2007-05-08
JRS (Nuveen Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-09
JRSH (Jerash Holdings) Start Date:2018-05-04
JRVR (James River  Lt) Start Date:2014-12-12
JSD (Nuveen Short Duration Credit Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2011-05-26
JSPR (Jasper Therapeutics) Start Date:2021-09-20
JSPRW (Japer Therapeutics Warrants) Start Date:2020-01-10
JT (Jianpu Technology American Depositary Shares) Start Date:2017-11-16
JUN (Juniper Ii Class A) Start Date:2021-12-23
JUPWW (Jupiter Wellness Warrant) Start Date:2020-10-30
JVA (Coffee Holding Co.) Start Date:2007-05-16
JWEL (Jowell Global) Start Date:2021-03-17
JWN (Nordstrom) Start Date:2005-01-03
JXJT (Jx Luxventure) Start Date:2013-03-07
JXN (Jackson Financial) Start Date:2021-09-01
JYD (Jayud Global Logistics Limited) Start Date:2023-04-21
JYNT (The Joint) Start Date:2014-11-11
JZ (Jianzhi Education Technology) Start Date:2022-08-26
JZXN (Jiuzi Holdings) Start Date:2021-05-18
K (Kellogg Co.) Start Date:2005-01-03
KA (Kineta) Start Date:2016-02-11
KAI (Kadant) Start Date:2007-05-03
KALA (Kala Pharmaceuticals) Start Date:2017-07-20
KALU (Kaiser Aluminum) Start Date:2007-05-16
KALV (Kalvista Pharmaceuticals) Start Date:2015-04-09
KAMN (Kaman) Start Date:2007-05-07
KAR (Kar Auction Services) Start Date:2009-12-11
KARO (Karooooo) Start Date:2021-04-01
KAVL (Kaival Brands Innovations) Start Date:2021-07-29
KB (Kb Financial Inc) Start Date:2007-05-01
KBH (Kb Home) Start Date:2005-01-03
KBNT (Kubient) Start Date:2020-08-12
KBNTW (Kubient Warrant) Start Date:2020-08-12
KBR (Kbr) Start Date:2007-01-03
KC (Kingsoft Cloud Holdings Limited) Start Date:2020-05-08
KD (Kyndryl Holdings,) Start Date:2021-10-22
KDP (Keurig Dr Pepper) Start Date:2008-05-07
KE (Kimball Electronics Comm) Start Date:2014-11-03
KELYA (Kelly Services) Start Date:2007-05-08
KELYB (Kelly Services) Start Date:2008-01-18
KEN (Kenon Holdings Ltd.) Start Date:2015-01-12
KEP (Korea Electric Power) Start Date:2007-05-01
KEQU (Kewaunee Scientific) Start Date:2007-05-16
KERN (Akerna Corp) Start Date:2018-02-26
KERNW (Akerna Warrant) Start Date:2018-02-27
KEX (Kirby) Start Date:2007-04-27
KEY (Keycorp) Start Date:2005-01-03
KEYS (Keysight Technologies) Start Date:2014-11-03
KF (Korea Fund) Start Date:2007-05-16
KFFB (Kentucky First Federal Bancorp) Start Date:2007-05-16
KFRC (Kforce) Start Date:2007-05-04
KFS (Kingsway Financial Services) Start Date:2007-05-16
KFY (Korn Ferry) Start Date:2007-04-27
KGC (Kinross Gold Corporation) Start Date:2007-01-03
KGS (Kodiak Gas Services) Start Date:2023-06-29
KHC (Kraft Heinz Co) Start Date:2015-07-06
KIDS (Orthopediatrics) Start Date:2017-10-12
KIM (Kimco Realty) Start Date:2005-01-03
KIND (Nextdoor Holdings,) Start Date:2021-11-08
KINS (Kingstone Companies) Start Date:2009-07-02
KINZU (Kins Technology  Unit) Start Date:2020-12-15
KINZW (Kins Technology  Warrant) Start Date:2021-02-04
KIO (Kkr Income Opportunities Fund Common Shares) Start Date:2013-07-26
KIQ (Kelso Technologies Inc Ordinary Shares) Start Date:2014-10-14
KIRK (Kirkland's Commonstock) Start Date:2007-05-16
KITT (Nauticus Robotics) Start Date:2021-08-04
KKR (Kkr & Co.) Start Date:2010-07-15
KLAC (Kla-Tencor) Start Date:2005-01-03
KLDO (Kaleido Biosciences) Start Date:2019-02-28
KLG (Wk Kellogg Co.) Start Date:2023-09-27
KLIC (Kulicke & Soffa Industries Inc) Start Date:2007-04-27
KLR (Kaleyra) Start Date:2017-12-08
KLTR (Kaltura) Start Date:2021-07-21
KLXE (Klx Energy Services) Start Date:2018-08-29
KMB (Kimberly-Clark) Start Date:2005-01-03
KMDA (Kamada Ordinary Shares) Start Date:2013-05-31
KMF (Kayne Anderson Nextgen Energy & Infrastructure) Start Date:2010-11-24
KMI (Kinder Morgan) Start Date:2011-02-11
KMPR (Kemper) Start Date:2007-04-30
KMT (Kennametal) Start Date:2007-01-03
KMX (Carmax Inc) Start Date:2005-01-03
KN (Knowles Corp) Start Date:2014-03-03
KNDI (Kandi Technologies Inc) Start Date:2007-09-24
KNF (Knife River Corp) Start Date:2023-06-01
KNOP (Knot Offshore Partners Lp) Start Date:2013-10-04
KNSA (Kiniksa Pharmaceuticals) Start Date:2018-05-24
KNSL (Kinsale Capital) Start Date:2016-07-28
KNSW (Knightswan Acquisition Corporation) Start Date:2022-03-14
KNTE (Kinnate Biopharma) Start Date:2020-12-03
KNTK (Kinetik) Start Date:2017-05-02
KNW (Know Labs) Start Date:2022-09-16
KNX (Knight-Swift Transportation Holdings) Start Date:2010-12-16
KO (Coca-Cola Company) Start Date:2005-01-03
KOD (Kodiak Sciences) Start Date:2018-10-04
KODK (Eastman Kodak Co.) Start Date:2013-11-01
KOF (Coca Cola Femsa S.A.B. De C.V. American Depositary Shares Each Representing 10 Units) Start Date:2007-04-27
KOP (Koppers) Start Date:2007-05-04
KOPN (Kopin Corp) Start Date:2007-05-01
KORE (Kore Holdings) Start Date:2021-10-01
KOS (Kosmos Energy) Start Date:2011-05-11
KOSS (Koss) Start Date:2007-05-21
KPLT (Katapult Holdings,) Start Date:2019-12-30
KPLTW (Katapult Holdings Warrant) Start Date:2019-12-27
KPRX (Kiora Pharmaceuticals) Start Date:2015-07-27
KPTI (Karyopharm Therapeutics C) Start Date:2013-11-06
KR (Kroger Co.) Start Date:2005-01-03
KRBP (Kiromic Biopharma) Start Date:2020-10-16
KRC (Kilroy Realty Corporation) Start Date:2007-01-03
KREF (Kkr Real Estate Finance Trust) Start Date:2017-05-05
KRG (Kite Realty Trust) Start Date:2007-05-07
KRKR (36Kr Holdings American Depositary Shares) Start Date:2019-11-08
KRMD (Repro Med Systems) Start Date:2007-05-17
KRNL (Kernel Holdings) Start Date:2021-04-01
KRNLU (Kernel Holdings Units) Start Date:2021-02-03
KRNLW (Kernel Holdings Warrants) Start Date:2021-03-26
KRNT (Kornit Digital Ltd.) Start Date:2015-04-02
KRNY (Kearny Financial) Start Date:2007-05-10
KRO (Kronos Worldwide) Start Date:2007-05-16
KRON (Kronos Bio) Start Date:2020-10-09
KROS (Keros Therapeutics) Start Date:2020-04-08
KRP (Kimbell Royalty Partners, Lp Common Units Representing Partner Interests) Start Date:2017-02-03
KRRO (Korro Bio Inc) Start Date:2019-10-03
KRT (Karat Packaging) Start Date:2021-04-15
KRTX (Karuna Therapeutics) Start Date:2019-06-28
KRUS (Kura Sushi Usa) Start Date:2019-08-01
KRYS (Krystal Biotech) Start Date:2017-09-20
KSCP (Knightscope Class A) Start Date:2022-01-27
KSICU (Kadem Sustainable Impact Unit) Start Date:2021-03-17
KSM (Dws Strategic Municipal Income Trust) Start Date:2007-05-16
KSS (Kohl's) Start Date:2005-01-03
KT (Kt Corporation) Start Date:2010-01-04
KTB (Kontoor Brands) Start Date:2019-05-09
KTCC (Key Tronic) Start Date:2007-05-16
KTF (Dws Municipal Income Trust) Start Date:2007-05-16
KTOS (Kratos Defense & Security) Start Date:2007-09-17
KTRA (Kintara Therapeutics) Start Date:2013-02-22
KTTA (Pasithea Therapeutics) Start Date:2021-09-15
KTTAW (Pasithea Therapeutics Warrant) Start Date:2021-09-15
KUKE (Kuke Music Holding) Start Date:2021-01-12
KULR (Kulr Technology) Start Date:2018-07-18
KURA (Kura Oncology) Start Date:2015-11-05
KVAC (Keen Vision Acquisition Corporation) Start Date:2023-09-15
KVHI (Kvh Industries) Start Date:2007-05-07
KVUE (Kenvue) Start Date:2023-05-04
KVYO (Klaviyo) Start Date:2023-09-20
KW (Kennedy-Wilson Holdings) Start Date:2010-03-19
KWE (Kwesst Micro Systems) Start Date:2022-12-07
KWR (Quaker Chemical) Start Date:2007-05-16
KXIN (Kaixin Auto Holdings Ordinary Shares) Start Date:2017-11-06
KYCH (Keyarch Acquisition Corporation) Start Date:2022-03-04
KYMR (Kymera Therapeutics) Start Date:2020-08-21
KYN (Kayne Anderson Energy Infrastructure Fund) Start Date:2007-05-04
KZIA (Kazia Therapeutics American Depositary Shares) Start Date:2013-02-11
KZR (Kezar Life Sciences) Start Date:2018-06-21
L (Loews) Start Date:2007-04-27
LAAC (Lithium Americas) Start Date:2008-10-28
LAB (Standard Biotools) Start Date:2022-04-06
LABP (Landos Biopharma) Start Date:2021-02-04
LAC (Lithium Americas Corp) Start Date:2023-09-21
LAD (Lithia Motors) Start Date:2007-05-01
LADR (Ladder Capital Corp) Start Date:2014-02-06
LAES (Sealsq Corp) Start Date:2023-05-22
LAKE (Lakeland Industries) Start Date:2007-05-16
LAMR (Lamar Advertising Company) Start Date:2007-01-03
LANC (Lancaster Colony) Start Date:2007-04-30
LAND (Gladstone Land Com) Start Date:2013-01-29
LANDM (Gladstone Land 5.00% Series D Cumulative Term Preferred Stock) Start Date:2021-01-25
LANV (Lanvin Holdings) Start Date:2022-12-15
LARK (Landmark Bancorp) Start Date:2007-05-16
LASE (Laser Photonics) Start Date:2022-09-30
LASR (Nlight) Start Date:2018-04-26
LATG (Latamgrowth SPAC Class A) Start Date:2022-03-18
LATGU (Latamgrowth SPAC Unit) Start Date:2022-01-25
LAUR (Laureate Education) Start Date:2017-02-01
LAW (Cs Disco) Start Date:2021-07-21
LAZ (Lazard Ltd) Start Date:2007-01-03
LAZR (Luminar Technologies, Class A) Start Date:2020-12-03
LAZY (Lazydays Holdings) Start Date:2018-03-16
LBAI (Lakeland Bancorp) Start Date:2007-05-08
LBBB (Lakeshore Acquisition Ii) Start Date:2022-04-14
LBC (Luther Burbank) Start Date:2017-12-08
LBPH (Longboard Pharmaceuticals) Start Date:2021-03-12
LBRDA (Liberty Broadband) Start Date:2014-11-04
LBRDK (Liberty Broadband Corporation) Start Date:2014-11-04
LBRDP (Liberty Broadband Series A Cumulative Redeemable Preferred Stock) Start Date:2020-12-22
LBRT (Liberty Oilfield Services) Start Date:2018-01-12
LBTYA (Liberty Global Plc) Start Date:2007-01-03
LBTYB (Liberty Global Plc Class B) Start Date:2007-05-16
LBTYK (Liberty Global Plc Class C) Start Date:2005-09-08
LC (Lendingclub Corp) Start Date:2014-12-11
LCA (Landcadia Holdings Iv Class A) Start Date:2021-05-18
LCAHU (Landcadia Holdings Iv Units) Start Date:2021-03-25
LCAHW (Landcadia Holdings Iv Warrant) Start Date:2021-05-18
LCFY (Locafy Ordinary Share) Start Date:2022-03-25
LCID (Lucid ,) Start Date:2020-09-18
LCII (Lci Industries) Start Date:2017-01-03
LCIN (Lannett Co Inc) Start Date:2013-12-13
LCNB (Lcnb) Start Date:2007-05-16
LCTX (Lineage Cell Therapeutics) Start Date:2007-05-16
LCUT (Lifetime Brands) Start Date:2007-05-04
LCW (Learn Cw Investment Class A Ordinary Shares) Start Date:2021-11-29
LDHAU (Ldh Growth I Units) Start Date:2021-03-19
LDI (Loandepot) Start Date:2021-02-11
LDOS (Leidos Holdings) Start Date:2007-04-27
LDP (Cohen & Steers Duration Preferred And Income Fund) Start Date:2012-07-27
LDTC (Leddartech Holdings Inc) Start Date:2021-03-01
LDWY (Lendway Inc) Start Date:2007-05-16
LE (Lands End) Start Date:2014-03-20
LEA (Lear) Start Date:2009-11-20
LECO (Lincoln Electric Holdings) Start Date:2007-01-03
LEDS (Semileds) Start Date:2010-12-09
LEE (Lee Enterprises Incorporated) Start Date:2007-04-30
LEG (Leggett & Platt) Start Date:2005-01-03
LEGAU (Lead Edge Growth Opportunities Units) Start Date:2021-03-23
LEGAW (Lead Edge Growth Opportunities Warrant) Start Date:2021-05-17
LEGH (Legacy Housing) Start Date:2018-12-14
LEGN (Legend Biotech Corporation) Start Date:2020-06-05
LEJU (Leju Holdings American Depositary Shares Each Representing One Ordinary Share) Start Date:2014-04-17
LEN (Lennar) Start Date:2005-01-03
LEN.B (Lennar) Start Date:2007-05-01
LEO (Bny Mellon Strategic Municipals) Start Date:2007-05-16
LESL (Leslie's) Start Date:2020-11-02
LEU (Centrus Energy) Start Date:2014-09-30
LEV (The Lion Electric Company) Start Date:2021-05-07
LEVI (Levi Strauss & Co.) Start Date:2019-03-21
LEXX (Lexaria Bioscience) Start Date:2021-01-12
LEXXW (Lexaria Bioscience Warrant) Start Date:2021-01-12
LFCR (Lifecore Biomedical) Start Date:2007-05-11
LFLY (Leafly Holdings) Start Date:2019-12-13
LFLYW (Leafly Holdings Warrant) Start Date:2022-02-07
LFMD (Lifemd) Start Date:2021-02-22
LFST (Lifestance Health) Start Date:2021-06-10
LFT (Lument Finance Trust) Start Date:2013-03-22
LFUS (Littelfuse) Start Date:2007-05-02
LFVN (Lifevantage Corp) Start Date:2012-09-12
LGCB (Linkage Global Inc) Start Date:2023-12-19
LGF.A (Lions Gate Entertainment) Start Date:2007-08-01
LGF.B (Lions Gate Entertainment) Start Date:2007-08-01
LGHL (Lion Holding American Depositary Share) Start Date:2020-06-16
LGHLW (Lion Holding Warrant) Start Date:2019-06-21
LGI (Lazard Global Total Return And Income Fund) Start Date:2007-05-16
LGIH (Lgi Homes) Start Date:2013-11-07
LGL (Lgl) Start Date:2007-05-16
LGMK (Logicmark) Start Date:2013-08-23
LGND (Ligand Pharmaceuticals) Start Date:2007-05-02
LGO (Largo Common Shares) Start Date:2021-04-19
LGTOU (Legato Merger Ii Unit) Start Date:2021-11-22
LGTOW (Legato Merger Ii Warrants) Start Date:2021-12-22
LGVC (Lamf Global Ventures I Class A Ordinary Shares) Start Date:2022-01-03
LGVCU (Lamf Global Ventures I Unit) Start Date:2021-11-11
LGVN (Longeveron) Start Date:2021-02-12
LH (Laboratory Of America Holding) Start Date:2005-01-03
LHC (Leo Holdings Ii Class A Ordinary Shares) Start Date:2021-03-01
LHDX (Lucira Health) Start Date:2021-02-05
LHX (L3harris Technologies) Start Date:2007-05-01
LI (Li Auto) Start Date:2020-07-30
LIAN (Lianbio American Depositary Shares) Start Date:2021-11-01
LICN (Lichen China) Start Date:2023-02-06
LICY (Li-Cycle Holdings) Start Date:2021-08-11
LIDR (Aeye Class A) Start Date:2021-01-11
LIDRW (Aeye Warrant) Start Date:2021-01-06
LIFE (Atyr Pharma) Start Date:2015-05-07
LIFW (Msp Recovery Class A) Start Date:2020-10-21
LII (Lennox International) Start Date:2007-01-03
LILA (Liberty Latin America) Start Date:2015-07-10
LILAK (Liberty Latin America Ltd.) Start Date:2015-06-23
LILM (Lilium N.V.) Start Date:2021-09-15
LILMW (Lilium N.V. Warrants) Start Date:2021-09-15
LIN (Linde Plc) Start Date:2018-10-29
LINC (Lincoln Educational Services) Start Date:2007-05-07
LIND (Lindblad Expeditions) Start Date:2013-07-03
LINK (Interlink Electronics) Start Date:2007-05-16
LIONU (Lionheart Iii Unit) Start Date:2021-11-04
LIONW (Lionheart Iii Warrant) Start Date:2021-12-07
LIPO (Lipella Pharmaceuticals) Start Date:2022-12-20
LIQT (Liqtech International) Start Date:2011-08-25
LITB (Lightinthebox Holding Co. American Depositary Shares Each Representing 2 Ordinary Shares) Start Date:2013-06-06
LITE (Lumentum Holdings) Start Date:2015-07-23
LITM (Snow Lake Resources) Start Date:2021-11-19
LITTU (Logistics Innovation Technologies Units) Start Date:2021-06-11
LITTW (Logistics Innovation Technologies Warrant) Start Date:2021-08-11
LIVB (Liv Capital Acquisition Ii) Start Date:2022-03-15
LIVE (Live Ventures Incorporated) Start Date:2015-10-09
LIVN (Livanova Plc) Start Date:2015-10-19
LIXT (Lixte Biotechnology Holdings) Start Date:2020-11-25
LIXTW (Lixte Biotechnology Holdings Warrants) Start Date:2020-11-25
LIZI (Lizhi American Depositary Shares) Start Date:2020-01-17
LKCO (Luokung Technology Ordinary Shares) Start Date:2019-01-08
LKFN (Lakeland Financial) Start Date:2007-05-16
LKQ (Lkq Corporation) Start Date:2007-04-27
LL (Lumber Liquidators) Start Date:2010-01-04
LLAP (Terran Orbital) Start Date:2021-04-26
LLL (Jx Luxventure) Start Date:2017-06-01
LLY (Lilly) Start Date:2005-01-03
LMAT (Lemaitre Vascular) Start Date:2007-05-16
LMB (Limbach Holdings) Start Date:2016-11-16
LMDX (Lumiradx Common Shares) Start Date:2021-09-29
LMDXW (Lumiradx Warrant) Start Date:2021-09-29
LMFA (Lm Funding America) Start Date:2015-12-08
LMND (Lemonade Inc) Start Date:2020-07-02
LMNL (Liminal Biosciences Common Shares) Start Date:2019-11-18
LMNR (Limoneira Co) Start Date:2007-05-22
LMPX (Lmp Automotive Holdings) Start Date:2019-12-05
LMT (Lockheed Martin) Start Date:2005-01-03
LNC (Lincoln National) Start Date:2005-01-03
LND (Brasilagro Brazilian Agric Real Estate Co Sponsored ADR) Start Date:2012-11-08
LNDC (Landec) Start Date:2007-05-11
LNG (Cheniere Energy) Start Date:2007-01-03
LNKB (Linkbancorp) Start Date:2022-09-13
LNN (Lindsay) Start Date:2007-05-01
LNSR (Lensar) Start Date:2020-10-02
LNT (Alliant Energy Corp) Start Date:2005-01-03
LNTH (Lantheus) Start Date:2015-06-25
LNW (Light & Wonder) Start Date:2007-05-02
LNZA (Lanzatech Global) Start Date:2021-09-24
LOAN (Manhattan Bridge Capital Inc) Start Date:2008-07-29
LOB (Live Oak Bancshares) Start Date:2015-07-23
LOCL (Local Bounti) Start Date:2021-11-22
LOCO (El Pollo Loco  C) Start Date:2014-07-25
LODE (Comstock) Start Date:2007-05-16
LOGI (Logitech International Sa) Start Date:2012-09-24
LOMA (Loma Negra Compania Industrial Argentina Sociedad Anonima ADS) Start Date:2017-11-01
LOOP (Loop Industries) Start Date:2015-11-11
LOPE (Grand Canyon Education) Start Date:2008-11-20
LOTZW (Carlotz Warrant) Start Date:2019-04-15
LOVE (The Lovesac Company) Start Date:2018-06-27
LOVLY (Spark Networks Se) Start Date:2017-11-17
LOW (Lowe's Cos.) Start Date:2005-01-03
LPCN (Lipocine) Start Date:2014-03-21
LPG (Dorian Lpg) Start Date:2014-05-08
LPI (Laredo Petroleum,) Start Date:2011-12-15
LPL (Lg Display Co. Ltd.) Start Date:2007-01-03
LPLA (Lpl Financial Holdings) Start Date:2010-11-18
LPRO (Open Lending Class A) Start Date:2020-06-11
LPSN (Liveperson) Start Date:2007-01-03
LPTH (Lightpath Technologies Class A) Start Date:2007-05-16
LPTV (Loop Media) Start Date:2022-09-21
LPTX (Leap Therapeutics) Start Date:2017-01-25
LPX (Louisiana-Pacific Corporation) Start Date:2007-01-03
LQDA (Liquidia Corp) Start Date:2018-07-26
LQDT (Liquidity Service) Start Date:2007-05-02
LQR (Lqr House) Start Date:2023-08-10
LRCX (Lam Research) Start Date:2005-01-03
LRE (Lead Real Estate Co.) Start Date:2023-09-27
LRFC (Logan Ridge Finance) Start Date:2013-09-25
LRHC (La Rosa Holdings) Start Date:2023-10-10
LRMR (Larimar Therapeutics) Start Date:2014-06-19
LRN (Stride) Start Date:2007-12-14
LSAK (Lesaka Technologies) Start Date:2007-04-30
LSBK (Lake Shore Bancorp) Start Date:2007-05-16
LSCC (Lattice Semiconductor Corporation) Start Date:2007-01-03
LSDI (Lucy Scientific Discovery) Start Date:2023-02-09
LSEA (Landsea Homes) Start Date:2018-06-29
LSEAW (Landsea Homes Warrant) Start Date:2018-06-29
LSF (Laird Superfood) Start Date:2020-09-23
LSPD (Lightspeed Commerce) Start Date:2020-09-11
LSTA (Lisata Therapeutics) Start Date:2007-08-09
LSTR (Landstar System) Start Date:2007-01-03
LSXMA (The Liberty Siriusxm) Start Date:2016-04-18
LSXMB (Liberty Media Series B Liberty Siriusxm) Start Date:2016-04-21
LSXMK (The Liberty Siriusxm) Start Date:2016-04-18
LTBR (Lightbridge) Start Date:2009-10-09
LTC (Ltc Properties) Start Date:2007-05-01
LTCHW (Latch Warrant Expiring 6/4/2026) Start Date:2020-12-31
LTH (Life Time Holdings,) Start Date:2021-10-07
LTHM (Livent Corp) Start Date:2018-10-11
LTRN (Lantern Pharma) Start Date:2020-06-11
LTRPA (Liberty Tripadvisor) Start Date:2014-08-27
LTRPB (Liberty Tripadvisor Holdings, Series B) Start Date:2014-08-29
LTRX (Lantronix) Start Date:2007-05-16
LTRY (Lottery.com,) Start Date:2018-06-13
LTRYW (Lottery.com Warrants) Start Date:2021-11-01
LU (Lucent Technology) Start Date:2020-11-02
LUCD (Lucid Diagnostics) Start Date:2021-10-14
LUCY (Innovative Eyewear) Start Date:2022-08-15
LULU (Lululemon Athletica) Start Date:2007-07-30
LUMN (Lumen Technologies) Start Date:2007-04-30
LUMO (Lumos Pharma) Start Date:2011-11-11
LUNA (Luna Innovations) Start Date:2007-05-16
LUNG (Pulmonx) Start Date:2020-10-01
LUV (Southwest Airlines) Start Date:2005-01-03
LUXH (Luxurban Hotels) Start Date:2007-05-11
LVLU (Lulu's Fashion Lounge Holdings,) Start Date:2021-11-11
LVO (Liveone) Start Date:2017-12-14
LVOX (Livevox Holding, Class A) Start Date:2019-04-18
LVOXU (Livevox Holdings Unit) Start Date:2019-03-08
LVRAU (Levere Holdings Unit) Start Date:2021-03-19
LVS (Las Vegas Sands) Start Date:2007-04-27
LVTX (Lava Therapeutics Nv) Start Date:2021-03-25
LVWR (Livewire) Start Date:2020-11-23
LW (Lamb Weston Holdings Inc) Start Date:2016-11-01
LWAY (Lifeway Foods) Start Date:2007-05-16
LWLG (Lightwave Logic,) Start Date:2008-03-10
LX (Lexinfintech Holdings American Depositary Shares) Start Date:2017-12-21
LXEH (Lixiang Education) Start Date:2020-10-01
LXEO (Lexeo Therapeutics) Start Date:2023-11-03
LXFR (Luxfer) Start Date:2012-10-03
LXP (Lexington Realty Trust) Start Date:2007-01-03
LXRX (Lexicon Pharmaceuticals) Start Date:2007-05-16
LXU (Lsb Industries) Start Date:2007-05-16
LYB (Lyondellbasell) Start Date:2010-10-14
LYEL (Lyell Immunopharma,) Start Date:2021-06-17
LYFT (Lyft) Start Date:2019-03-29
LYG (Lloyds Banking Plc) Start Date:2007-01-03
LYL (Dragon Victory International Ordinary Shares) Start Date:2017-10-20
LYLT (Loyalty Ventures) Start Date:2021-11-02
LYRA (Lyra Therapeutics) Start Date:2020-05-01
LYT (Lytus Technologies Holdings Ptv. Common Shares) Start Date:2022-06-15
LYTS (Lsi Industries) Start Date:2007-05-01
LYV (Live Nation Entertainment) Start Date:2006-01-03
LZ (Legalzoom.com) Start Date:2021-06-30
LZB (La-Z-Boy) Start Date:2007-04-25
LZM (Lifezone Metals Ltd.) Start Date:2021-12-13
M (Macy's) Start Date:2007-06-01
MA (Mastercard) Start Date:2006-05-25
MAA (Mid-America Apartments) Start Date:2005-01-03
MAC (Macerich) Start Date:2005-01-03
MACK (Merrimack Pharmaceuticals) Start Date:2012-03-29
MAG (Mag Silver) Start Date:2007-07-09
MAIA (Maia Biotechnology) Start Date:2022-07-28
MAIN (Main Street Capital Corporation) Start Date:2007-10-08
MAMA (Mama's Creations Inc) Start Date:2013-05-22
MAN (Manpowergroup) Start Date:2007-01-03
MANH (Manhattan Associates) Start Date:2007-01-03
MANU (Manchester United Plc) Start Date:2012-08-10
MAPS (Wm Technology, Class A) Start Date:2019-10-01
MAPSW (Wm Technology Warrants) Start Date:2019-10-01
MAR (Marriott Int'l.) Start Date:2005-01-03
MARA (Marathon Digital Holdings,) Start Date:2014-07-28
MARK (Remark Holdings) Start Date:2007-10-03
MARPS (Marine Petroleum Trust Units Of Beneficial Interest) Start Date:2007-05-16
MARX (Mars Acquisition) Start Date:2023-03-14
MAS (Masco) Start Date:2005-01-03
MASI (Masimo Corporation) Start Date:2007-08-08
MASS (908 Devices) Start Date:2020-12-18
MAT (Mattel) Start Date:2005-01-03
MATH (Metalpha Technology Holding) Start Date:2017-10-20
MATV (Mativ Holdings) Start Date:2007-05-02
MATW (Matthews International) Start Date:2007-05-02
MATX (Matson) Start Date:2012-07-02
MAV (Pioneer Municipal High Income Advantage Fund) Start Date:2007-05-16
MAX (Mediaalpha) Start Date:2020-11-02
MAXN (Maxeon Solar) Start Date:2020-12-15
MAYS (J. W. Mays) Start Date:2007-05-18
MBC (Masterbrand) Start Date:2022-12-09
MBCN (Middlefield Banc Cmn) Start Date:2007-05-16
MBI (Mbia) Start Date:2005-01-03
MBIN (Merchants Bancorp) Start Date:2017-10-27
MBINN (Merchants Bancorp Depositary Shares Preferred Series C) Start Date:2021-03-23
MBINO (Merchants Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series B Fixed-To-Floating Rate) Start Date:2019-08-20
MBINP (Merchants Bancorp 7.00% Fixed-To-Floating Rate Series A Non-Cumulative Perpetual Preferred Stock) Start Date:2019-03-29
MBIO (Mustang Bio) Start Date:2017-08-22
MBLY (Mobileye Global) Start Date:2022-10-26
MBNKP (Medallion Bank Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series F) Start Date:2019-12-18
MBOT (Microbot Medical) Start Date:2007-04-27
MBRX (Moleculin Biotech) Start Date:2016-06-02
MBUU (Malibu Boats  Com) Start Date:2014-01-31
MBWM (Mercantile Bank) Start Date:2007-05-16
MC (Moelis & Company) Start Date:2014-04-16
MCAC (Monterey Capital Acquisition Corporation) Start Date:2022-07-01
MCB (Metropolitan Bank Hldg Corp) Start Date:2017-11-08
MCBC (Macatawa Bank) Start Date:2007-05-16
MCBS (Metrocity Bankshares) Start Date:2019-10-03
MCD (Mcdonald's) Start Date:2005-01-03
MCFT (Mastercraft Boat) Start Date:2015-07-17
MCHP (Microchip Technology) Start Date:2005-01-03
MCHX (Marchex Class B) Start Date:2007-05-01
MCI (Barings Corporate Investors) Start Date:2007-05-16
MCK (Mckesson) Start Date:2005-01-03
MCLD (Mcloud Technologies Common Shares) Start Date:2021-11-24
MCN (Madison Covered Call & Equity Strategy Fund) Start Date:2007-05-16
MCO (Moody's Corp) Start Date:2005-01-03
MCOM (Micromobilitycom Inc) Start Date:2019-12-09
MCR (Mfs Charter Income Trust) Start Date:2007-05-16
MCRB (Seres Therapeutics) Start Date:2015-06-26
MCRI (Monarch Casino & Resort) Start Date:2007-04-30
MCS (Marcus) Start Date:2007-05-01
MCVT (Mill City Ventures Iii) Start Date:2009-05-27
MCW (Mister Car Wash) Start Date:2021-06-25
MCY (Mercury General Corporation) Start Date:2007-01-03
MD (Mednax) Start Date:2009-01-02
MDB (Mongodb) Start Date:2017-10-19
MDBH (Mdb Capital Holdings) Start Date:2023-09-21
MDC (M.D.C. Holdings) Start Date:2007-01-03
MDGL (Madrigal Pharmaceuticals) Start Date:2007-05-16
MDGS (Medigus American Depositary Shares) Start Date:2015-08-05
MDGSW (Medigus Series C Warrant) Start Date:2018-07-23
MDIA (Mediaco Holding Class A) Start Date:2020-01-06
MDJH (Mdjm Ordinary Share) Start Date:2019-01-08
MDLZ (Mondelez International) Start Date:2007-04-30
MDNA (Medicenna Therapeutics Common Shares) Start Date:2020-08-24
MDRR (Medalist Diversified Reit) Start Date:2018-11-28
MDRRP (Medalist Diversified Reit Series A Cumulative Redeemable Preferred Stock) Start Date:2020-02-13
MDRX (Allscripts-Misys) Start Date:2007-04-27
MDT (Medtronic Plc) Start Date:2005-01-03
MDU (Mdu Resources) Start Date:2007-01-03
MDV (Modiv Class C) Start Date:2022-02-11
MDVL (Medavail Holdings) Start Date:2011-03-04
MDWD (Mediwound Ordinary Shares) Start Date:2014-03-20
MDWT (Midwest Holding) Start Date:2020-11-04
MDXG (Mimedx , Inc) Start Date:2008-04-02
MDXH (Mdxhealth Sa American Depositary Shares) Start Date:2021-11-04
ME (23Andme Holding Co. Class A) Start Date:2021-06-17
MEC (Mayville Engineering Co) Start Date:2019-05-09
MED (Medifast) Start Date:2007-04-25
MEDP (Medpace) Start Date:2016-08-11
MEDS (Trxade) Start Date:2020-02-13
MEG (Montrose Environmental) Start Date:2020-07-23
MEGI (Mainstay Cbre Global Infrastructure Megatrends Fund Common Shares) Start Date:2021-10-27
MEGL (Magic Empire Global) Start Date:2022-08-05
MEI (Methode Electronics) Start Date:2007-10-17
MEIP (Mei Pharma) Start Date:2007-05-16
MELI (Mercadolibre Inc) Start Date:2007-08-10
MEOH (Methanex Corp) Start Date:2007-05-01
MERC (Mercer International Inc) Start Date:2007-05-04
MESA (Mesa Air) Start Date:2018-08-10
MESO (Mesoblast American Depositary Shares) Start Date:2009-01-05
MET (Metlife) Start Date:2005-01-03
META (Meta Platforms) Start Date:2012-05-18
METC (Ramaco Resources,) Start Date:2017-02-03
METCB (Ramaco Resources Inc) Start Date:2023-06-16
METXW (Meten Holding Warrant) Start Date:2020-05-28
MF (Missfresh) Start Date:2021-06-25
MFA (Mfa Financial) Start Date:2007-04-24
MFC (Manulife Financial Corporation) Start Date:2007-01-03
MFD (Macquarie First Trust Global) Start Date:2007-05-16
MFG (Mizuho Financial) Start Date:2007-01-03
MFH (Mercurity Fintech Holding ADS) Start Date:2015-04-08
MFIC (Midcap Financial Investment) Start Date:2007-04-30
MFIN (Medallion Financial) Start Date:2007-05-11
MFM (Mfs Municipal Income Trust) Start Date:2007-05-16
MFV (Mfs Special Value Trust) Start Date:2007-05-16
MG (Mistras) Start Date:2009-10-08
MGA (Magna International) Start Date:2007-01-03
MGAM (Mobile Global Esports) Start Date:2022-07-29
MGEE (Mge Energy) Start Date:2007-05-04
MGF (Mfs Government Markets Income Trust) Start Date:2007-05-16
MGIC (Magic Software Enterprises Ltd) Start Date:2007-05-16
MGIH (Millennium International Holdings Limited) Start Date:2023-04-04
MGLD (The Marygold Companies) Start Date:2022-03-10
MGM (Mgm Resorts International) Start Date:2005-06-01
MGNI (Magnite,) Start Date:2020-06-30
MGNX (Macrogenics) Start Date:2013-10-10
MGOL (Mgo Global) Start Date:2023-01-13
MGPI (Mgp Ingredients) Start Date:2007-05-03
MGRC (Mcgrath Rentcorp) Start Date:2007-05-04
MGRX (Mangoceuticals,) Start Date:2023-03-21
MGTX (Meiragtx) Start Date:2018-06-08
MGU (Macquarie Global Infrastructure Total Return Fund) Start Date:2007-05-08
MGY (Magnolia Oil & Gas Corp) Start Date:2017-06-29
MGYR (Magyar Bancorp) Start Date:2007-05-16
MHD (Blackrock Muniholdings Fund) Start Date:2007-05-16
MHF (Western Asset Municipal High Income Fund) Start Date:2007-05-16
MHH (Mastech Digital) Start Date:2008-10-01
MHI (Pioneer Municipal High Income Fund) Start Date:2007-05-16
MHK (Mohawk Industries) Start Date:2005-01-03
MHLD (Maiden Holdings Ltd.) Start Date:2008-05-06
MHN (Blackrock Muniholdings New York Quality Fund) Start Date:2007-05-16
MHO (M/I Homes) Start Date:2007-05-02
MHUA (Meihua International Medical Technologies Co. Ordinary Shares) Start Date:2022-02-16
MI (Nft Ltd.) Start Date:2015-11-25
MICS (The Singing Machine Company) Start Date:2022-05-24
MIDD (The Middleby Corporation) Start Date:2007-01-03
MIGI (Mawson Infrastructure) Start Date:2021-06-21
MIMO (Airspan Networks Holdings) Start Date:2020-11-19
MIN (Mfs Intermediate Income Trust) Start Date:2007-05-04
MIND (Mind Technology) Start Date:2007-05-10
MINM (Minim) Start Date:2021-07-07
MIO (Pioneer Municipal High Income Opportunities Fund) Start Date:2021-08-06
MIR (Mirion Technologies,) Start Date:2020-08-20
MIRA (Mira Pharmaceuticals) Start Date:2023-08-03
MIRM (Mirum Pharmaceuticals) Start Date:2019-07-18
MIRO (Miromatrix Medical) Start Date:2021-06-24
MIST (Milestone Pharmaceuticals Common Shares) Start Date:2019-05-09
MITK (Mitek Systems) Start Date:2007-05-16
MITQ (Moving Image Technologies) Start Date:2021-07-08
MITT (Ag Mortgage Investment Trust) Start Date:2011-06-30
MIXT (Mix Telematics American Depositary Shares Each Representing 25 Ordinary Shares) Start Date:2013-08-09
MIY (Blackrock Muniyield Michigan Quality Fund) Start Date:2007-05-16
MKC (Mccormick & Co.) Start Date:2005-01-03
MKFG (Markforged Holding) Start Date:2020-10-08
MKL (Markel) Start Date:2007-05-02
MKSI (Mks Instruments) Start Date:2007-04-26
MKTW (Marketwise, Class A) Start Date:2021-07-22
MKTWW (Marketwise Warrant) Start Date:2021-07-22
MKTX (Marketaxess Holdings) Start Date:2005-01-03
MKUL (Molekule) Start Date:2021-11-24
MKULQ (Molekule Inc) Start Date:2021-11-24
ML (Moneylion) Start Date:2020-08-14
MLAB (Mesa Laboratories) Start Date:2007-05-16
MLCO (Melco Resorts & Entertainment Limited) Start Date:2011-12-07
MLEC (Moolec Science Sa) Start Date:2023-01-03
MLGO (Microalgo) Start Date:2022-12-13
MLI (Mueller Industries) Start Date:2007-04-27
MLKN (Millerknoll,) Start Date:2007-04-30
MLM (Martin Marietta Materials) Start Date:2007-04-30
MLNK (Meridianlink) Start Date:2021-07-28
MLP (Maui Land & Pineapple) Start Date:2007-05-16
MLR (Miller Industries) Start Date:2007-05-07
MLSS (Milestone Scientific) Start Date:2007-05-16
MLTX (Moonlake Immunotherapeutics Class A Ordinary Shares) Start Date:2022-04-06
MLYS (Mineralys Therapeutics) Start Date:2023-02-10
MMAT (Meta Materials) Start Date:2010-11-08
MMC (Marsh & Mclennan) Start Date:2005-01-03
MMD (Mainstay Mackay Definedterm Municipal Opportunities Fund) Start Date:2012-06-27
MMI (Marcus & Millichap) Start Date:2013-10-31
MMLP (Martin Midstream Partners L.P. Partnership) Start Date:2007-05-03
MMM (3M Company) Start Date:2005-01-03
MMP (Magellan Midstream Partners L.P.) Start Date:2007-01-03
MMS (Maximus) Start Date:2007-01-03
MMSI (Merit Medical Systems) Start Date:2007-01-03
MMT (Mfs Multimarket Income Trust) Start Date:2007-05-08
MMU (Western Asset Managed Municipals Fund) Start Date:2007-05-16
MMV (Multimetaverse Holdings Class A) Start Date:2021-06-08
MMYT (Makemytrip Limited) Start Date:2010-08-12
MNDO (Mind C.T.I. Ordinary Shares) Start Date:2007-05-16
MNDY (Monday.com) Start Date:2021-06-10
MNKD (Mannkind) Start Date:2007-04-27
MNKTQ (Mallinckrodt Plc) Start Date:2022-06-17
MNMD (Mind Medicine) Start Date:2021-04-27
MNOV (Medicinova) Start Date:2007-05-16
MNP (Western Asset Municipal Partners Fund) Start Date:2007-05-16
MNPR (Monopar Therapeutics) Start Date:2019-12-19
MNR (Mach Natural Resources Lp) Start Date:2023-10-25
MNRO (Monro) Start Date:2007-01-03
MNSB (Mainstreet Bancshares) Start Date:2007-05-17
MNSBP (Mainstreet Bancshares Depositary Shares) Start Date:2020-09-16
MNSO (Miniso Holding) Start Date:2020-10-15
MNST (Monster Beverage) Start Date:2005-01-03
MNTK (Montauk Renewables) Start Date:2021-01-22
MNTS (Momentus Class A) Start Date:2020-01-02
MNTSW (Momentus Warrant) Start Date:2019-12-30
MNTX (Manitex International) Start Date:2008-05-28
MNY (Moneyhero Ltd.) Start Date:2020-12-07
MO (Altria Inc) Start Date:2005-01-03
MOB (Mobilicom Ltd) Start Date:2022-08-25
MOBQ (Mobiquity Technologies) Start Date:2007-05-17
MOBQW (Mobiquity Technologies Warrant) Start Date:2021-12-09
MOD (Modine Manufacturing) Start Date:2007-05-07
MODD (Modular Medical) Start Date:2020-10-08
MODG (Topgolf Callaway Brands) Start Date:2007-05-01
MODN (Model N) Start Date:2013-03-20
MODV (Modivcare) Start Date:2007-04-25
MOFG (Midwestone Financial) Start Date:2008-03-18
MOG.A (Moog) Start Date:2007-04-30
MOGO (Mogo Common Shares) Start Date:2018-04-18
MOGU (Mogu American Depositary Shares) Start Date:2018-12-06
MOH (Molina Healthcare) Start Date:2007-01-03
MOHO (Ecmoho American Depositary Shares) Start Date:2019-11-08
MOLN (Molecular Partners) Start Date:2021-06-16
MOMO (Momo) Start Date:2014-12-11
MOND (Mondee Holdings Class A) Start Date:2021-03-24
MOR (Morphosys Ag American Depositary Shares) Start Date:2018-04-19
MORF (Morphic Holding) Start Date:2019-06-27
MORN (Morningstar) Start Date:2007-05-03
MOS (The Mosaic Company) Start Date:2011-05-20
MOTS (Motus Gi Holdings) Start Date:2018-02-14
MOV (Movado) Start Date:2007-05-07
MOVE (Movano) Start Date:2021-03-23
MP (Mp Materials) Start Date:2020-11-16
MPA (Blackrock Muniyield Pennsylvania Quality Fund) Start Date:2007-05-16
MPAA (Motorcar Parts Of America) Start Date:2007-05-16
MPB (Mid Penn Bancorp) Start Date:2008-08-01
MPC (Marathon Petroleum) Start Date:2011-06-23
MPLN (Multiplan Corporation) Start Date:2020-04-03
MPLX (Mplx Lp) Start Date:2012-10-26
MPTI (M-Tron Industries) Start Date:2022-10-03
MPU (Mega Matrix) Start Date:2007-05-16
MPV (Barings Participation Investors) Start Date:2007-05-16
MPW (Medical Properties Trust) Start Date:2007-01-03
MPWR (Monolithic Power Systems) Start Date:2007-01-03
MPX (Marine Products) Start Date:2007-05-01
MQ (Marqeta) Start Date:2021-06-09
MQT (Blackrock Muniyield Quality Fund Ii) Start Date:2007-05-16
MQY (Blackrock Muniyield Quality Fund) Start Date:2007-05-16
MRAI (Marpai Class A) Start Date:2021-10-27
MRAM (Everspin Technologies) Start Date:2016-10-07
MRBK (Meridian Bank) Start Date:2017-11-07
MRC (Mrc Global) Start Date:2012-04-12
MRCC (Monroe Capital) Start Date:2012-10-25
MRCY (Mercury Systems) Start Date:2007-01-03
MRDB (Mariadb Plc) Start Date:2022-12-19
MREO (Mereo Biopharma Plc American Depositary Shares) Start Date:2019-04-24
MRIN (Marin Software Incorporated) Start Date:2013-03-22
MRK (Merck & Co.) Start Date:2005-01-03
MRKR (Marker Therapeutics) Start Date:2016-11-08
MRM (Medirom Healthcare) Start Date:2020-12-29
MRNA (Moderna) Start Date:2018-12-07
MRNS (Marinus Pharmaceuticals) Start Date:2014-07-31
MRO (Marathon Oil) Start Date:2005-01-03
MRSN (Mersana Therapeutics) Start Date:2017-06-28
MRTN (Marten Transport) Start Date:2007-04-26
MRTX (Mirati Therapeutics) Start Date:2013-07-15
MRUS (Merus N.V. Common Shares) Start Date:2016-05-19
MRVI (Maravai Lifesciences) Start Date:2020-11-20
MRVL (Marvell Technology Ltd.) Start Date:2005-01-03
MS (Morgan Stanley) Start Date:2006-03-01
MSA (Msa Safety Incorporated) Start Date:2007-01-03
MSB (Mesabi Trust) Start Date:2007-05-03
MSBI (Midland States Bancorp) Start Date:2016-05-24
MSC (Studio City International Holdings American Depositary Shares Each Representing Four Class A Ordinary Shares) Start Date:2018-10-18
MSCI (MSCI Inc) Start Date:2007-11-15
MSD (Morgan Stanley Emerging Markets Debt Fund) Start Date:2007-05-07
MSEX (Middlesex Water) Start Date:2007-05-16
MSFT (Microsoft) Start Date:2005-01-03
MSGE (Madison Square Garden Entertainment Corp) Start Date:2023-04-21
MSGM (Motorsport Games) Start Date:2021-01-13
MSGS (Madison Square Garden Sports Corp) Start Date:2015-10-01
MSI (Motorola Solutions) Start Date:2010-12-17
MSM (Msc Industrial Direct Co.) Start Date:2007-01-03
MSN (Emerson Radio) Start Date:2007-05-16
MSPR (Msp Recovery Class A) Start Date:2022-05-24
MSPRW (Msp Recovery Warrant) Start Date:2022-05-24
MSPRZ (Msp Recovery Warrant) Start Date:2020-10-21
MSS (Maison Solutions) Start Date:2023-10-05
MSSA (Metal Sky Star Acquisition Corporation) Start Date:2022-05-31
MSTR (Microstrategy) Start Date:2007-04-26
MT (Arcelormittal) Start Date:2007-01-03
MTA (Metalla Royalty & Streaming Common Shares) Start Date:2020-01-08
MTB (M&T Bank) Start Date:2005-01-03
MTBC (Carecloud) Start Date:2014-07-23
MTBL (Moatable Inc) Start Date:2011-05-04
MTC (Mmtec Common Shares) Start Date:2019-01-08
MTCH (Match) Start Date:2015-11-19
MTD (Mettler Toledo) Start Date:2005-01-03
MTDR (Matador Resources) Start Date:2012-02-02
MTEK (Maris-Tech Ordinary Shares) Start Date:2022-02-02
MTEKW (Maris-Tech Warrants) Start Date:2022-02-02
MTEM (Molecular Templates) Start Date:2007-05-03
MTEX (Mannatech Incorporated) Start Date:2007-04-30
MTG (Mgic Investment Corporation) Start Date:2007-01-03
MTH (Meritage Homes Corporation) Start Date:2007-01-03
MTLS (Materialise Nv American Depositary Shares) Start Date:2014-06-25
MTMT (Mega Matrix) Start Date:2007-05-16
MTN (Vail Resorts) Start Date:2007-01-03
MTNB (Matinas Biopharma Holdings) Start Date:2014-07-21
MTR (Mesa Royalty Trust) Start Date:2007-05-16
MTRN (Materion) Start Date:2007-05-01
MTRX (Matrix Service) Start Date:2007-05-03
MTSI (Macom Technology Solutions Holdings) Start Date:2012-03-15
MTTR (Matterport, Class A) Start Date:2021-02-02
MTW (Manitowoc Company) Start Date:2005-01-03
MTX (Minerals Technologies) Start Date:2007-05-01
MTZ (Mastec) Start Date:2007-01-03
MU (Micron Technology) Start Date:2005-01-03
MUA (Blackrock Muniassets Fund Inc) Start Date:2007-05-16
MUC (Blackrock Muniholdings California Quality Fund) Start Date:2007-05-16
MUE (Blackrock Muniholdings Quality Fund Ii) Start Date:2007-05-16
MUFG (Mitsubishi Ufj Financial) Start Date:2018-04-02
MUI (Blackrock Municipal Income Fund) Start Date:2007-05-16
MUJ (Blackrock Muniholdings New Jersey Quality Fund) Start Date:2007-05-16
MULN (Mullen Automotive,) Start Date:2008-10-28
MUR (Murphy Oil Corporation) Start Date:2005-01-03
MURA (Mural Oncology Plc) Start Date:2023-11-06
MUSA (Murphy Usa) Start Date:2013-09-03
MUX (Mcewen Mining) Start Date:2007-05-16
MVBF (Mvb Financial) Start Date:2008-02-19
MVF (Blackrock Munivest Fund) Start Date:2007-05-16
MVIS (Microvision Inc) Start Date:2007-04-26
MVO (Mv Oil Trust Units Of Beneficial Interests) Start Date:2007-05-16
MVST (Microvast Holdings,) Start Date:2019-03-27
MVSTW (Microvast Holdings Warrants) Start Date:2019-03-27
MVT (Blackrock Munivest Fund Ii) Start Date:2007-05-16
MWA (Mueller Water Products) Start Date:2007-05-01
MWG (Multi Ways Holdings Limited) Start Date:2023-04-03
MX (Magnachip Semiconductor) Start Date:2011-03-11
MXC (Mexco Energy) Start Date:2007-05-16
MXCT (Maxcyte) Start Date:2021-07-30
MXE (Mexico Equity And Income Fund) Start Date:2007-05-16
MXF (Mexico Fund) Start Date:2007-05-09
MXL (Maxlinear) Start Date:2010-03-24
MYD (Blackrock Muniyield Fund) Start Date:2007-05-16
MYE (Myers Industries) Start Date:2007-05-02
MYFW (First Western Financial) Start Date:2018-07-19
MYGN (Myriad Genetics) Start Date:2007-04-30
MYI (Blackrock Muniyield Quality Fund Iii Inc) Start Date:2007-05-16
MYMD (Mymd Pharmaceuticals) Start Date:2020-01-02
MYN (Blackrock Muniyield New York Quality Fund common Stock) Start Date:2007-05-16
MYNA (Mynaric Ag ADS) Start Date:2021-11-12
MYND (Myndai Inc) Start Date:2022-05-24
MYNZ (Mainz Biomed B.V. Ordinary Shares) Start Date:2021-11-05
MYO (Myomo) Start Date:2017-06-12
MYPS (Playstudios, Class A) Start Date:2020-12-21
MYRG (Myr) Start Date:2008-09-09
MYSZ (My Size) Start Date:2016-07-25
MYTE (Myt Netherlands Parent B.V.) Start Date:2021-01-21
NA (Nano Labs Ltd) Start Date:2022-07-12
NAAS (Naas Technology American Depositary Shares) Start Date:2017-10-20
NABL (N-Able) Start Date:2021-07-20
NAC (Nuveen California Quality Municipal Income Fund) Start Date:2007-05-16
NAD (Nuveen Quality Municipal Income Fund) Start Date:2007-01-03
NAII (Natural Alternatives International) Start Date:2007-05-16
NAK (Northern Dynasty Minerals) Start Date:2007-05-07
NAMS (Newamsterdam Pharma) Start Date:2022-11-23
NAN (Nuveen New York Quality Municipal Income Fund) Start Date:2007-05-16
NAOV (Nanovibronix) Start Date:2015-05-28
NAPA (Duckhorn Portfolio) Start Date:2021-03-18
NARI (Inari Medical) Start Date:2020-05-22
NAT (Nordic American Tankers) Start Date:2007-05-03
NATH (Nathans Famous) Start Date:2007-05-16
NATI (National Instruments Corporation) Start Date:2007-01-03
NATL (Ncr Atleos Corp) Start Date:2023-10-11
NATR (Natures Sunshine Products) Start Date:2009-06-25
NAUT (Nautilus Biotechnolgy,) Start Date:2020-08-07
NAVB (Navidea Biopharmaceuticals) Start Date:2005-10-27
NAVI (Navient Corporation) Start Date:2014-04-17
NAZ (Nuveen Arizona Quality Municipal Income Fund) Start Date:2007-05-16
NBB (Nuveen Taxable Municipal Income Fund Common Shares Of Beneficial Interest) Start Date:2010-04-28
NBH (Neuberger Berman Municipal Fund) Start Date:2007-05-16
NBHC (National Bank) Start Date:2012-09-20
NBIX (Neurocrine Biosciences) Start Date:2007-01-03
NBN (Northeast Bancorp) Start Date:2007-05-16
NBO (Neuberger Berman New York Municipal Fund) Start Date:2007-05-16
NBR (Nabors Industries Ltd.) Start Date:2005-11-03
NBRV (Nabriva Therapeutics Plc Ordinary Shares Ireland) Start Date:2015-09-18
NBSE (Neubase Therapeutics) Start Date:2019-07-15
NBTB (Nbt Bancorp) Start Date:2007-05-07
NBTX (Nanobiotix) Start Date:2020-12-11
NBW (Neuberger Berman California Municipal Fund Inc) Start Date:2007-05-16
NBXG (Neuberger Berman Next Generation Connectivity Fund) Start Date:2021-05-26
NBY (Novabay Pharmaceuticals) Start Date:2007-10-26
NC (Nacco Industries) Start Date:2007-05-08
NCA (Nuveen California Municipal Value Fund) Start Date:2007-05-16
NCL (Northann) Start Date:2023-10-19
NCLH (Norwegian Cruise Line) Start Date:2013-01-18
NCMI (National Cinemedia) Start Date:2007-05-16
NCNA (Nucana Plc American Depositary Share) Start Date:2017-09-28
NCNC (Noco-Noco Inc) Start Date:2022-07-06
NCNO (Ncino) Start Date:2020-07-14
NCPL (Netcapital) Start Date:2007-05-29
NCRA (Nocera) Start Date:2007-05-30
NCSM (Ncs Multistage Holdings) Start Date:2017-04-28
NCTY (The9 ADS) Start Date:2007-04-23
NCV (Virtus Convertible & Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-02
NCZ (Virtus Convertible & Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-08
NDAQ (Nasdaq) Start Date:2005-02-10
NDLS (Noodles & Co) Start Date:2013-06-28
NDMO (Nuveen Dynamic Municipal Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2020-08-27
NDP (Tortoise Energy Independence Fund) Start Date:2012-07-27
NDRA (Endra Life Sciences) Start Date:2017-06-30
NDSN (Nordson Corporation) Start Date:2007-01-03
NE (Noble Corporation) Start Date:2021-06-09
NEA (Nuveen Amt-Free Quality Municipal Income Fund) Start Date:2007-01-03
NECB (Northeast Community Bancorp) Start Date:2021-07-13
NEE (Nextera Energy) Start Date:2007-04-30
NEGG (Newegg Commerce, Common Shares) Start Date:2010-06-14
NEM (Newmont Mining Corporation) Start Date:2005-01-03
NEN (New England Realty Associates Partnership Class A Depositary Receipts Evidencing Units Of Partnership) Start Date:2007-05-16
NEO (Neogenomics) Start Date:2012-12-10
NEOG (Neogen) Start Date:2007-05-16
NEON (Neonode) Start Date:2007-08-13
NEOV (Neovolta) Start Date:2020-05-20
NEP (Nextera Energy Partners Lp) Start Date:2014-06-27
NEPH (Nephros) Start Date:2009-01-22
NEPT (Neptune Wellness Solutions Ordinary Shares) Start Date:2007-08-13
NERV (Minerva Neurosciences Com) Start Date:2014-07-01
NESRW (National Energy Services Reunited Warrant) Start Date:2017-06-05
NET (Cloudflare) Start Date:2019-09-13
NETD (Nabors Energy Transition Ii) Start Date:2023-09-05
NETI (Eneti) Start Date:2013-12-12
NEU (Newmarket) Start Date:2007-05-01
NEWP (New Pacific Metals Common Shares) Start Date:2021-05-20
NEWR (New Relic) Start Date:2014-12-12
NEWT (Newtek Business Services Corp) Start Date:2007-05-16
NEX (Nextier Oilfield Solutions) Start Date:2019-10-31
NEXA (Nexa Resources S.A. Common Shares) Start Date:2017-10-27
NEXI (Neximmune) Start Date:2021-02-12
NEXT (Nextdecade Corp) Start Date:2015-06-04
NFBK (Northfield Bancorp) Start Date:2007-11-08
NFE (New Fortress Energy Class A) Start Date:2019-01-31
NFG (National Fuel Gas Company) Start Date:2007-01-03
NFGC (New Found Gold Common Shares) Start Date:2021-09-29
NFJ (Virtus Dividend Interest & Premium Strategy Fund Common Shares Of Beneficial Interest) Start Date:2007-04-23
NFLX (Netflix) Start Date:2005-01-03
NFTG (The Nft Gaming) Start Date:2023-02-15
NG (Novagold Resources) Start Date:2007-01-03
NGD (New Gold) Start Date:2007-05-16
NGG (National Grid Plc) Start Date:2007-01-03
NGL (Ngl Energy Partners Lp Common Units Representing Partner Interests) Start Date:2011-05-12
NGM (Ngm Biopharmaceuticals) Start Date:2019-04-04
NGMS (Neogames S.A.) Start Date:2020-11-19
NGNE (Neurogene Inc) Start Date:2014-03-12
NGS (Natural Gas Services) Start Date:2007-04-26
NGVC (Natural Grocers) Start Date:2012-07-25
NGVT (Ingevity Corporation) Start Date:2016-05-02
NHC (National Healthcare) Start Date:2007-05-16
NHI (National Health Investors) Start Date:2007-01-03
NHICU (Newhold Investment Ii Unit) Start Date:2021-10-21
NHICW (Newhold Investment Ii Warrant) Start Date:2021-12-27
NHS (Neuberger Berman High Yield Strategies Fund) Start Date:2008-12-19
NHTC (Natural Health Trends) Start Date:2007-05-16
NHWK (Nighthawk Biosciences) Start Date:2013-07-24
NI (Nisource) Start Date:2005-01-03
NIC (Nicolet Bankshares) Start Date:2013-05-17
NICE (Nice American Depositary Shares) Start Date:2007-05-03
NICK (Nicholas Financial) Start Date:2007-05-16
NID (Nuveen Intermediate Duration Municipal Term Fund Common Shares Of Beneficial Interest) Start Date:2012-12-06
NIE (Virtus Equity & Convertible Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
NILE (Bitnile) Start Date:2007-05-16
NIM (Nuveen Select Maturities Municipal Fund) Start Date:2007-05-16
NIMC (Nisource Inc Series A Corporate Units) Start Date:2021-04-22
NINE (Nine Energy Service) Start Date:2018-01-19
NIO (Nio) Start Date:2018-09-12
NIQ (Nuveenn Intermediate Duration Quality Municipal Term Fund Common Shares Of Beneficial Interest) Start Date:2013-08-02
NISN (Nisun International Enterprise Development Co. Class A Common Shares) Start Date:2016-12-27
NIU (Niu Technologies American Depositary Shares) Start Date:2018-10-19
NJR (New Jersey Resources Corporation) Start Date:2007-01-03
NKE (Nike) Start Date:2005-01-03
NKG (Nuveen Georgia Quality Municipal Income Fund) Start Date:2007-05-16
NKLA (Nikola Corporation) Start Date:2018-06-11
NKSH (National Bankshares) Start Date:2007-05-16
NKTR (Nektar Therapeutics) Start Date:2005-01-03
NKTX (Nkarta) Start Date:2020-07-13
NKX (Nuveen California Amt-Free Quality Municipal Income Fund) Start Date:2007-05-16
NL (Nl Industries) Start Date:2007-04-30
NLOK (Nortonlifelock) Start Date:2007-04-27
NLSP (Nls Pharmaceutics) Start Date:2021-01-29
NLSPW (Nls Pharmaceutics Warrant) Start Date:2021-01-29
NLY (Annaly Capital Management) Start Date:2007-01-03
NM (Navios Maritime Holdings) Start Date:2007-05-14
NMAI (Nuveen Multi-Asset Income Fund Common Shares Of Beneficial Interest) Start Date:2021-11-22
NMCO (Nuveen Municipal Credit Opportunities Fund Common Shares) Start Date:2019-09-17
NMFC (New Mountain Finance Corporation) Start Date:2011-05-20
NMG (Nouveau Monde Graphite Common Shares) Start Date:2021-05-24
NMI (Nuveen Municipal Income Fund) Start Date:2007-05-16
NMIH (Nmi  Comm) Start Date:2013-11-08
NML (Neuberger Berman Mlp And Energy Income Fund) Start Date:2013-03-26
NMM (Navios Maritime Partners L.P.) Start Date:2007-11-13
NMMC (North Mountain Merger Class A) Start Date:2020-11-18
NMMCU (North Mountain Merger Unit) Start Date:2020-09-18
NMMCW (North Mountain Merger Warrant) Start Date:2020-11-13
NMR (Nomura Holdings) Start Date:2007-01-03
NMRA (Neumora Therapeutics) Start Date:2023-09-15
NMRD (Nemaura Medical) Start Date:2014-12-18
NMRK (Newmark) Start Date:2017-12-15
NMS (Nuveen Minnesota Quality Municipal Income Fund) Start Date:2014-10-08
NMT (Nuveen Massachusetts Quality Municipal Income Fund) Start Date:2007-05-16
NMTC (Neuroone Medical Technologies) Start Date:2021-05-26
NMTR (9 Meters Biopharma) Start Date:2016-07-08
NMZ (Nuveen Municipal High Income Opportunity Fund $0.01 Par Value Per Share) Start Date:2007-05-16
NN (Nextnav) Start Date:2021-10-29
NNAG (99 Acquisition) Start Date:2023-10-09
NNAVW (Nextnav Warrant) Start Date:2021-10-29
NNBR (Nn) Start Date:2007-04-26
NNDM (Nano Dimension American Depositary Shares) Start Date:2016-03-07
NNI (Nelnet) Start Date:2007-04-25
NNN (National Retail Properties) Start Date:2007-01-03
NNOX (Nano-X Imaging) Start Date:2020-12-15
NNVC (Nanoviricides) Start Date:2007-05-16
NNY (Nuveen New York Municipal Value Fund) Start Date:2007-05-16
NOA (North American Construction Ltd.) Start Date:2007-05-03
NOAH (Noah Holdings Limited) Start Date:2010-11-10
NOC (Northrop Grumman) Start Date:2005-01-03
NODK (Ni) Start Date:2017-03-16
NOG (Northern Oil And Gas,) Start Date:2008-03-26
NOGN (Nogin) Start Date:2021-09-20
NOK (Nokia Corporation) Start Date:2007-01-03
NOM (Nuveen Missouri Quality Municipal Income Fund) Start Date:2007-05-16
NOMD (Nomad Foods Limited) Start Date:2015-11-27
NOTE (Fiscalnote Holdings Class A) Start Date:2022-08-01
NOTV (Inotiv) Start Date:2007-05-16
NOV (National Oilwell Varco) Start Date:2005-03-15
NOVA (Sunnova Energy International) Start Date:2019-07-25
NOVN (Novan) Start Date:2016-09-21
NOVT (Novanta) Start Date:2011-02-14
NOW (Servicenow) Start Date:2012-06-29
NPCT (Nuveen Core Plus Impact Fund Common Shares Of Beneficial Interest) Start Date:2021-04-28
NPFD (Nuveen Variable Rate Preferred & Income Fund Common Shares) Start Date:2021-12-16
NPK (National Presto) Start Date:2007-05-16
NPO (Enpro Industries) Start Date:2007-05-03
NPV (Nuveen Virginia Quality Municipal Income Fund) Start Date:2007-05-16
NQP (Nuveen Pennsylvania Quality Municipal Income Fund) Start Date:2007-05-16
NR (Newpark Resources) Start Date:2007-04-27
NRBO (Neurobo Pharmaceuticals) Start Date:2016-08-05
NRC (National Research) Start Date:2013-05-23
NRDS (Nerdwallet, Class A) Start Date:2021-11-04
NRDY (Nerdy Class A) Start Date:2020-11-27
NREF (Nexpoint Real Estate Finance) Start Date:2020-02-07
NRG (Nrg Energy) Start Date:2005-01-03
NRGV (Energy Vault) Start Date:2022-02-14
NRGX (Pimco Energy And Tactical Credit Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2019-01-30
NRIM (Northrim Bancorp) Start Date:2007-05-16
NRIX (Nurix Therapeutics) Start Date:2020-07-24
NRK (Nuveen New York Amt-Free Quality Municipal Income Fund) Start Date:2007-05-16
NRO (Neuberger Berman Real Estate Securities Income Fund Neuberger Berman Real Estate Securities Income Fund) Start Date:2007-05-09
NRP (Natural Resource Partners Lp Partnership) Start Date:2007-05-08
NRSN (Neurosense Therapeutics Ordinary Shares) Start Date:2021-12-09
NRSNW (Neurosense Therapeutics Warrant) Start Date:2021-12-09
NRT (North European Oil Royality Trust) Start Date:2007-05-16
NRXP (Nrx Pharmaceuticals) Start Date:2017-12-04
NRXPW (Nrx Pharmaceuticals Warrant) Start Date:2017-12-01
NRXS (Neuraxis) Start Date:2023-08-09
NS (Nustar Energy L.P.) Start Date:2007-05-16
NSA (National Storage Affiliates Trust) Start Date:2015-04-23
NSC (Norfolk Southern) Start Date:2005-01-03
NSIT (Insight Enterprises) Start Date:2007-04-30
NSL (Nuveen Senior Income Fund) Start Date:2007-05-07
NSP (Insperity) Start Date:2007-01-03
NSPR (Inspiremd) Start Date:2016-07-13
NSSC (Napco Security Systems) Start Date:2007-05-07
NSTB (Northern Star Investment Ii Class A) Start Date:2021-02-11
NSTC (Northern Star Investment Iii Class A) Start Date:2021-04-22
NSTD (Northern Star Investment Iv Class A) Start Date:2021-04-22
NSTG (Nanostring Technologies) Start Date:2013-06-26
NSTS (Nsts Bancorp) Start Date:2022-01-19
NSYS (Nortech Systems Incorporated) Start Date:2007-05-16
NTAP (Netapp) Start Date:2005-01-03
NTB (The Bank Of N.T. Butterfield & Son) Start Date:2016-09-16
NTBL (Notable Labs Ltd.) Start Date:2014-10-01
NTCO (Natura &Co Holding S.A.) Start Date:2020-01-07
NTCT (Netscout Systems) Start Date:2007-05-03
NTES (Netease Inc) Start Date:2005-01-03
NTG (Tortoise Midstream Energy Fund) Start Date:2010-07-28
NTGR (Netgear) Start Date:2007-04-30
NTIC (Northern Technologies International) Start Date:2008-06-30
NTIP (Network-1 Technologies) Start Date:2007-05-16
NTLA (Intellia Therapeutics) Start Date:2016-05-06
NTNX (Nutanix) Start Date:2016-09-30
NTR (Nutrien Ltd.) Start Date:2018-01-02
NTRA (Natera) Start Date:2015-07-02
NTRB (Nutriband) Start Date:2017-11-30
NTRBW (Nutriband Warrant) Start Date:2021-10-01
NTRS (Northern Trust) Start Date:2009-04-29
NTRSO (Northern Trust Depositary Shares Each Representing A 1/1000Th Interest In A Share Of Series E Non-Cumulative Perpetual Preferred Stock) Start Date:2019-11-27
NTST (Netstreit) Start Date:2020-08-13
NTWK (Netsol Technologies) Start Date:2007-05-16
NTZ (Natuzzi S.P.A.) Start Date:2007-05-16
NUBI (Nubia Brand International Class A) Start Date:2022-05-02
NUBIU (Nubia Brand International Unit) Start Date:2022-03-11
NUE (Nucor) Start Date:2005-01-03
NUO (Nuveen Ohio Quality Municipal Income Fund) Start Date:2007-05-16
NURO (Neurometrix) Start Date:2007-04-19
NUS (Nu Skin Enterprises) Start Date:2007-01-03
NUTX (Nutex Health) Start Date:2022-04-04
NUV (Nuveen Municipal Value Fund) Start Date:2007-01-03
NUVA (Nuvasive) Start Date:2007-01-03
NUVB (Nuvation Bio) Start Date:2020-08-26
NUVL (Nuvalent) Start Date:2021-07-29
NUW (Nuveen Amt-Free Municipal Value Fund) Start Date:2009-02-25
NUWE (Nuwellis) Start Date:2012-08-10
NUZE (Nuzee) Start Date:2014-04-14
NVAX (Novavax) Start Date:2007-04-25
NVCR (Novocure Limited) Start Date:2015-10-02
NVCT (Nuvectis Pharma) Start Date:2022-02-04
NVDA (Nvidia Corporation) Start Date:2005-01-03
NVEC (Nve) Start Date:2007-04-20
NVEE (Nv5 Global) Start Date:2013-09-30
NVEI (Nuvei Subordinate Voting Shares) Start Date:2021-10-06
NVFY (Nova Lifestyle) Start Date:2014-01-17
NVG (Nuveen Amt-Free Municipal Credit Income Fund) Start Date:2007-01-03
NVGS (Navigator Holdings Ltd.) Start Date:2013-11-21
NVIV (Invivo Therapeutics Holdings) Start Date:2015-04-17
NVMI (Nova Ordinary Shares) Start Date:2007-05-16
NVNO (Envveno Medical) Start Date:2018-05-31
NVNOW (Envveno Medical Warrants) Start Date:2018-05-31
NVO (Novo Nordisk A/S) Start Date:2007-05-04
NVOS (Novo Integrated Sciences) Start Date:2014-04-21
NVR (Nvr) Start Date:2008-01-02
NVRI (Enviri Corp) Start Date:2007-05-03
NVRO (Nevro) Start Date:2014-11-06
NVS (Novartis Ag) Start Date:2007-04-26
NVST (Envista Holdings Corporation) Start Date:2019-09-18
NVT (Nvent Electric Plc) Start Date:2018-04-17
NVTS (Navitas Semiconductor) Start Date:2021-10-20
NVVE (Nuvve Holding) Start Date:2020-05-01
NVVEW (Nuvve Holding Warrant) Start Date:2020-04-30
NVX (Novonix ADS) Start Date:2022-02-02
NWBI (Northwest Bancshares) Start Date:2007-05-03
NWE (Northwestern Corporation) Start Date:2008-05-01
NWFL (Norwood Financial) Start Date:2007-05-18
NWG (Natwest Plc American Depositary Shares) Start Date:2007-10-18
NWGL (Nature Wood Limited) Start Date:2023-09-12
NWL (Newell Brands) Start Date:2005-01-03
NWLI (National Western Life) Start Date:2008-10-03
NWN (Northwest Natural Holding Co) Start Date:2007-04-30
NWPX (Northwest Pipe Co) Start Date:2007-05-16
NWS (News Class B) Start Date:2013-06-19
NWSA (News Class A) Start Date:2013-06-19
NWTN (Nwtn Class B) Start Date:2022-11-14
NX (Quanex Building Products) Start Date:2007-04-26
NXC (Nuveen California Select Tax-Free Income Portfolio) Start Date:2007-05-16
NXDT (Nexpoint Diversified Real Estate Trust) Start Date:2007-05-07
NXE (Nexgen Energy Common Shares) Start Date:2017-05-17
NXG (Nxg Nextgen Infrastructure Income Fund) Start Date:2012-09-26
NXGL (Nexgel Inc) Start Date:2021-12-22
NXGLW (Nexgel Inc Warrant) Start Date:2021-12-22
NXGN (Nextgen Healthcare) Start Date:2007-04-27
NXJ (Nuveen New Jersey Qualified Municipal Fund) Start Date:2007-05-16
NXL (Nexalin Technology) Start Date:2022-09-16
NXN (Nuveen New York Select Tax-Free Income Portfolio) Start Date:2007-05-16
NXP (Nuveen Select Tax Free Income Portfolio) Start Date:2007-05-16
NXPI (Nxp Semiconductors Nv) Start Date:2010-08-06
NXPL (Nextplat) Start Date:2021-05-28
NXPLW (Nextplat Warrants) Start Date:2021-05-28
NXRT (Nexpoint Residential Trust In) Start Date:2015-04-01
NXST (Nexstar Media) Start Date:2007-01-03
NXT (Nextracker) Start Date:2023-02-09
NXTC (Nextcure) Start Date:2019-05-09
NXTP (Nextplay Technologies) Start Date:2018-02-22
NXU (Nxu Inc) Start Date:2022-09-27
NYAX (Nayax) Start Date:2022-09-21
NYCB (New York Community Bancorp) Start Date:2007-04-27
NYMT (New York Mortgage Trust) Start Date:2008-06-05
NYMTN (New York Mortgage Trust 8.00% Series D Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock) Start Date:2017-10-13
NYMX (Nymox Pharmaceutical) Start Date:2007-05-16
NYT (New York Times Company) Start Date:2005-01-03
NYXH (Nyxoah) Start Date:2021-07-02
NZF (Nuveen Municipal Credit Income Fund) Start Date:2007-05-16
O (Realty Income Corporation) Start Date:2012-02-10
OABI (Omniab) Start Date:2021-09-30
OB (Outbrain) Start Date:2021-07-23
OBDC (Blue Owl Capital Corp) Start Date:2019-07-18
OBE (Obsidian Energy) Start Date:2022-01-31
OBIO (Orchestra Biomed Holdings) Start Date:2020-08-04
OBK (Origin Bancorp Inc) Start Date:2018-05-09
OBLG (Oblong) Start Date:2007-05-16
OBSV (Obseva Sa Ordinary Shares) Start Date:2018-07-13
OBT (Orange County Bancorp) Start Date:2021-08-05
OC (Owens Corning) Start Date:2007-01-03
OCC (Optical Cable) Start Date:2007-05-16
OCCI (Ofs Credit Company) Start Date:2018-10-05
OCFC (Oceanfirst Financial) Start Date:2007-05-16
OCFCP (Oceanfirst Financial Depositary Shares) Start Date:2020-05-08
OCFT (Oneconnect Financial Technology Co. Ltd.) Start Date:2019-12-13
OCG (Oriental Culture Holding) Start Date:2020-12-15
OCGN (Ocugen,) Start Date:2014-12-03
OCN (Ocwen Financial New) Start Date:2007-04-30
OCSL (Oaktree Specialty Lending Corporation) Start Date:2008-06-12
OCTO (Eightco Holdings Inc) Start Date:2022-05-18
OCUL (Ocular Therapeutix Commo) Start Date:2014-07-25
OCUP (Ocuphire Pharma) Start Date:2019-04-12
OCX (Oncocyte Corp) Start Date:2016-01-04
ODC (Oil-Dri Of America) Start Date:2007-05-16
ODD (Oddity Tech Ltd.) Start Date:2023-07-19
ODFL (Old Dominion Freight Line) Start Date:2005-01-03
ODP (Office Depot) Start Date:2005-01-03
ODV (Osisko Development Common Shares) Start Date:2022-05-27
OEC (Orion Engineered Carbons S.A.) Start Date:2014-07-25
OEPWW (One Equity Partners Open Water I Warrant) Start Date:2021-03-15
OESX (Orion Energy Systems) Start Date:2007-12-19
OFG (Ofg Bancorp) Start Date:2007-05-04
OFIX (Orthofix International) Start Date:2007-05-03
OFLX (Omega Flex) Start Date:2007-05-16
OFS (Ofs Capital) Start Date:2012-11-08
OGCP (Empire State Realty Op, L.P. Series 60) Start Date:2013-10-08
OGE (Oge Energy) Start Date:2007-01-03
OGEN (Oragenics) Start Date:2012-09-24
OGI (Organigram Holdings Common Shares) Start Date:2014-08-27
OGN (Organon) Start Date:2021-05-14
OGS (One Gas) Start Date:2014-01-16
OHI (Omega Healthcare Investors) Start Date:2007-01-03
OI (O-I Glass) Start Date:2005-01-03
OIA (Invesco Municipal Income Opportunities Trust) Start Date:2007-05-16
OIGBQ (Orbital Infrastructure Inc) Start Date:2008-01-07
OII (Oceaneering International) Start Date:2007-04-27
OIS (Oil States International) Start Date:2007-04-27
OKE (Oneok) Start Date:2005-01-03
OKTA (Okta) Start Date:2017-04-07
OKYO (Okyo Pharma American Depositary Shares) Start Date:2022-05-17
OLB (The Olb) Start Date:2020-08-07
OLED (Universal Display Corporation) Start Date:2007-05-04
OLK (Olink Holding Ab) Start Date:2021-03-25
OLLI (Ollie's Bargain Outlet Holdings) Start Date:2015-07-16
OLMA (Olema Pharmaceuticals) Start Date:2020-11-19
OLN (Olin Corporation) Start Date:2007-04-30
OLO (Olo) Start Date:2021-03-17
OLP (One Liberty Properties) Start Date:2007-05-16
OLPX (Olaplex Holdings,) Start Date:2021-09-30
OM (Outset Medical) Start Date:2020-09-15
OMAB (Grupo Aeroportuario Del Centro Norte S.A.B. De C.V. ADS) Start Date:2007-05-09
OMC (Omnicom) Start Date:2005-01-03
OMCL (Omnicell) Start Date:2007-05-03
OMER (Omeros) Start Date:2009-10-08
OMEX (Odyssey Marine Exploration) Start Date:2007-07-10
OMF (Onemain Holdings) Start Date:2013-10-16
OMGA (Omega Therapeutics) Start Date:2021-07-30
OMH (Ohmyhome Limited) Start Date:2023-03-21
OMI (Owens & Minor) Start Date:2007-05-02
OMIC (Singular Genomics Systems) Start Date:2021-05-27
OMQS (Omniq) Start Date:2011-01-14
ON (On Semiconductor Corporation) Start Date:2015-04-06
ONB (Old National Bancorp) Start Date:2007-01-03
ONBPO (Old National Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series C Preferred Stock) Start Date:2022-02-16
ONBPP (Old National Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of Series A Preferred Stock) Start Date:2022-02-16
ONCO (Onconetix Inc) Start Date:2022-02-18
ONCS (Oncosec Medical Incorporated) Start Date:2015-05-29
ONCT (Oncternal Therapeutics) Start Date:2018-09-17
ONCY (Oncolytics Biotech Common Shares) Start Date:2018-06-01
ONDS (Ondas Holdings) Start Date:2020-12-04
ONEW (Onewater Marine) Start Date:2020-02-07
ONFO (Onfolio Holdings) Start Date:2022-08-26
ONL (Orion Office Reit) Start Date:2021-11-01
ONON (On Holding Ag) Start Date:2021-09-15
ONTF (On24) Start Date:2021-02-03
ONTO (Onto Innovation) Start Date:2007-05-07
ONTX (Onconova Therapeutics) Start Date:2013-07-25
ONVO (Organovo Holdings) Start Date:2013-08-02
OOMA (Ooma) Start Date:2015-07-17
OP (Oceanpal) Start Date:2021-11-30
OPAD (Offerpad Solutions) Start Date:2020-12-11
OPAL (Opal Fuels Class A) Start Date:2021-05-24
OPBK (Op Bancorp) Start Date:2007-05-18
OPCH (Option Care Health) Start Date:2007-04-27
OPEN (Opendoor Technologies Inc) Start Date:2020-12-15
OPFI (Oppfi Class A) Start Date:2021-01-20
OPGN (Opgen) Start Date:2015-05-05
OPHC (Optimumbank Holdings) Start Date:2007-05-16
OPI (Office Properties Ome Trust Common Shares Of Be) Start Date:2009-06-03
OPK (Opko Health) Start Date:2007-06-13
OPOF (Old Point Financial) Start Date:2007-05-16
OPP (Rivernorth/Doubleline Strategic Opportunity Fund) Start Date:2016-09-28
OPRA (Opera American Depositary Shares) Start Date:2018-07-27
OPRT (Oportun Financial) Start Date:2019-09-26
OPRX (Optimizerx) Start Date:2008-04-30
OPT (Opthea) Start Date:2020-10-16
OPTN (Optinose) Start Date:2017-10-13
OPTT (Ocean Power Technologies) Start Date:2007-05-16
OPY (Oppenheimer) Start Date:2007-05-16
OR (Osisko Gold Royalties Ltd) Start Date:2016-07-06
ORA (Ormat Technologies) Start Date:2007-05-04
ORAN (Orange S.A.) Start Date:2007-05-01
ORC (Orchid Island Capital) Start Date:2013-02-14
ORCL (Oracle) Start Date:2005-01-03
ORGN (Origin Materials,) Start Date:2020-09-04
ORGNW (Origin Materials Warrants) Start Date:2020-09-04
ORGO (Organogenesis) Start Date:2017-01-05
ORGS (Orgenesis) Start Date:2012-02-08
ORI (Old Republic International Corporation) Start Date:2007-01-03
ORIAU (Orion Biotech Opportunities Units) Start Date:2021-05-13
ORIAW (Orion Biotech Opportunities Warrant) Start Date:2021-07-07
ORIC (Oric Pharmaceuticals) Start Date:2020-04-24
ORLA (Orla Mining Ltd.) Start Date:2020-12-22
ORLY (O'reilly Automotive) Start Date:2005-01-03
ORMP (Oramed Pharmaceuticals) Start Date:2007-05-16
ORN (Orion Holdings Common) Start Date:2009-05-14
ORRF (Orrstown Financial) Start Date:2007-05-17
ORTX (Orchard Therapeutics Plc American Depositary Shares) Start Date:2018-10-31
OSA (Prosomnus) Start Date:2022-12-07
OSBC (Old Second Bancorp) Start Date:2007-05-08
OSCR (Oscar Health) Start Date:2021-03-03
OSG (Overseas Shipholding) Start Date:2015-12-01
OSIS (Osi Systems) Start Date:2007-04-30
OSK (Oshkosh Corporation) Start Date:2009-08-07
OSPN (Onespan) Start Date:2007-05-03
OSS (One Stop Systems) Start Date:2018-02-01
OST (Ostin Technology Co. Ordinary Shares) Start Date:2022-04-27
OSUR (Orasure Technologies) Start Date:2007-04-26
OSW (Onespaworld) Start Date:2017-11-17
OTEX (Open Text Corporation) Start Date:2007-01-03
OTIS (Otis Worldwide) Start Date:2020-03-19
OTLK (Outlook Therapeutics) Start Date:2016-06-14
OTLY (Oatly) Start Date:2021-05-20
OTMO (Otonomo Technologies Ordinary Shares) Start Date:2021-08-16
OTMOW (Otonomo Technologies Warrant) Start Date:2021-08-16
OTRK (Ontrak) Start Date:2017-04-26
OTTR (Otter Tail) Start Date:2007-05-01
OUST (Ouster,) Start Date:2020-10-09
OUT (Outfront Media) Start Date:2014-03-28
OVBC (Ohio Valley Banc) Start Date:2007-05-16
OVID (Ovid Therapeutics) Start Date:2017-05-05
OVLY (Oak Valley Bancorp) Start Date:2008-08-18
OVV (Ovintiv) Start Date:2007-04-27
OWL (Blue Owl Capital Class A) Start Date:2020-12-14
OWLT (Owlet Class A) Start Date:2020-11-05
OXBR (Oxbridge Re Holdings Ordinary Shares) Start Date:2014-03-27
OXBRW (Oxbridge Re Holdings Warrant Expiring 3/26/2024) Start Date:2014-05-09
OXLC (Oxford Lane Capital) Start Date:2011-01-20
OXM (Oxford Industries) Start Date:2007-05-03
OXSQ (Oxford Square Capital) Start Date:2014-03-05
OXY (Occidental Petroleum) Start Date:2005-01-03
OZ (Belpointe Prep Llc Class A Units) Start Date:2021-10-18
OZK (Bank Ozk) Start Date:2007-05-10
PAA (Plains All American Pipeline L.P.) Start Date:2007-01-03
PAAS (Pan American Silver) Start Date:2007-01-03
PAC (Grupo Aeroportuario Del Pacifico S.A. B. De C.V. Grupo Aeroportuario Del Pacifico S.A. De C.V.) Start Date:2007-05-03
PACB (Pacific Biosciences) Start Date:2010-10-27
PACK (Ranpak Corp) Start Date:2018-03-05
PACW (Pacwest Bancorp) Start Date:2008-05-14
PACX (Pioneer Merger Class A Ordinary Share) Start Date:2021-03-01
PACXU (Pioneer Merger Unit) Start Date:2021-01-08
PACXW (Pioneer Merger Warrant) Start Date:2021-03-01
PAG (Penske Automotive) Start Date:2007-07-02
PAGP (Plains Gp Holdings L.P. Class A Units Representing Partner Interests) Start Date:2013-10-16
PAGS (Pagseguro Digital Ltd.) Start Date:2018-01-24
PAHC (Phibro Animal Health) Start Date:2014-04-11
PAI (Western Asset Investment Grade Income Fund) Start Date:2007-05-16
PALI (Palisade Bio) Start Date:2019-07-18
PALT (Paltalk) Start Date:2018-03-12
PAM (Pampa Energia S.A. Pampa Energia S.A.) Start Date:2009-10-09
PANW (Palo Alto Networks) Start Date:2012-07-20
PAPL (Pineapple Financial) Start Date:2023-11-01
PAR (Par Technology) Start Date:2007-05-16
PARA (Paramount Global) Start Date:2007-04-30
PARAA (Paramount Global Class A) Start Date:2007-05-09
PARR (Par Pacific) Start Date:2012-09-05
PASG (Passage Bio) Start Date:2020-02-28
PATH (Uipath) Start Date:2010-08-06
PATI (Patriot Transportation Holding) Start Date:2015-02-02
PATK (Patrick Industries) Start Date:2007-05-16
PAVM (Pavmed) Start Date:2016-07-28
PAVMZ (Pavmed Series Z Warrant) Start Date:2018-04-10
PAVS (Paranovus Entertainment Technology Ltd.) Start Date:2019-10-25
PAX (Patria Investments) Start Date:2021-01-22
PAXS (Pimco Access Income Fund Common Shares Of Beneficial Interest) Start Date:2022-01-27
PAY (Paymentus Holdings) Start Date:2021-05-26
PAYC (Paycom) Start Date:2014-04-15
PAYO (Payoneer Global) Start Date:2021-06-28
PAYOW (Payoneer Global Warrant) Start Date:2021-06-28
PAYS (Paysign) Start Date:2007-05-18
PAYX (Paychex) Start Date:2005-06-06
PB (Prosperity Bancshares) Start Date:2011-12-28
PBA (Pembina Pipeline Corporation) Start Date:2012-04-02
PBBK (Pb Bankshares) Start Date:2021-07-15
PBF (Pbf Energy) Start Date:2012-12-13
PBFS (Pioneer Bancorp) Start Date:2019-07-18
PBH (Prestige Consumer Healthcare) Start Date:2007-01-03
PBHC (Pathfinder Bancorp) Start Date:2007-05-22
PBI (Pitney Bowes) Start Date:2005-01-03
PBLA (Panbela Therapeutics) Start Date:2020-12-02
PBPB (Potbelly) Start Date:2013-10-04
PBR (Petroleo Brasileiro S.A.- Petrobras) Start Date:2007-04-27
PBR.A (Petroleo Brasileiro ADR Reptg 2 Pref Shares) Start Date:2007-04-26
PBT (Permian Basin Royalty Trust) Start Date:2007-05-02
PBTS (Powerbridge Technologies Co. Ordinary Shares) Start Date:2019-04-02
PBYI (Puma Biotechnology) Start Date:2012-04-20
PCAR (Paccar) Start Date:2005-01-03
PCB (Pcb Bancorp) Start Date:2018-08-10
PCCTU (Perception Capital Ii Units) Start Date:2021-10-28
PCCTW (Perception Capital Ii Warrants) Start Date:2021-12-20
PCF (High Income Securities Fund) Start Date:2007-05-01
PCG (Pacific Gas & Electric Co.) Start Date:2005-01-03
PCH (Potlatchdeltic Corporation) Start Date:2007-01-03
PCK (Pimco California Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PCM (Pcm Fund) Start Date:2007-05-16
PCN (Pimco Corporate & Income Strategy Fund) Start Date:2007-05-03
PCOR (Procore Technologies) Start Date:2021-05-20
PCQ (Pimco California Municipal Income Fund) Start Date:2007-05-16
PCRX (Pacira Biosciences) Start Date:2011-02-03
PCSA (Processa Pharmaceuticals) Start Date:2013-11-21
PCT (Purecycle Technologies,) Start Date:2021-03-18
PCTI (Pctel) Start Date:2007-05-03
PCTTU (Purecycle Technologies Unit) Start Date:2021-03-18
PCTTW (Purecycle Technologies Warrant) Start Date:2021-03-18
PCTY (Paylocity Holding) Start Date:2014-03-19
PCVX (Vaxcyte) Start Date:2020-06-12
PCYO (Pure Cycle) Start Date:2007-05-16
PD (Pagerduty) Start Date:2019-04-11
PDCO (Patterson Companies) Start Date:2005-01-03
PDD (Pinduoduo) Start Date:2018-07-26
PDEX (Pro-Dex) Start Date:2007-05-16
PDFS (Pdf Solutions) Start Date:2007-05-03
PDI (Pimco Dynamic Income Fund) Start Date:2012-05-25
PDLB (Pdl Community Bancorp) Start Date:2017-10-02
PDM (Piedmont Office Realty Trust) Start Date:2010-02-10
PDO (Pimco Dynamic Income Opportunities Fund Common Shares Of Beneficial Interest) Start Date:2021-01-27
PDS (Precision Drilling Corporation) Start Date:2010-06-02
PDSB (Pds Biotechnology) Start Date:2015-10-01
PDT (John Hancock Premium Dividend Fund) Start Date:2007-05-16
PEAK (Healthpeak Properties) Start Date:2007-04-30
PEAR (Pear Therapeutics Class A) Start Date:2021-03-31
PEB (Pebblebrook Hotel Trust) Start Date:2009-12-09
PEBK (Peoples Bancorp Of N) Start Date:2007-05-16
PEBO (Peoples Bancorp) Start Date:2007-05-16
PECO (Phillips Edison & Company) Start Date:2021-07-15
PED (Pedevco) Start Date:2007-05-17
PEG (Public Serv. Enterprise) Start Date:2005-01-03
PEGA (Pegasystems) Start Date:2007-05-03
PEGY (Pineapple Energy) Start Date:2007-05-16
PEI (Pennsylvania Real Estate Investment Trust) Start Date:2007-04-27
PEN (Penumbra) Start Date:2015-09-18
PENN (Penn National Gaming) Start Date:2007-01-03
PEO (Adams Natural Resources Fund) Start Date:2007-04-30
PEP (Pepsico) Start Date:2005-01-03
PEPG (Pepgen) Start Date:2022-05-06
PERF (Perfect Class A) Start Date:2022-10-31
PERI (Perion Network Ltd.) Start Date:2007-05-16
PESI (Perma-Fix Environmental Services) Start Date:2007-05-16
PET (Wag) Start Date:2021-09-27
PETQ (Petiq) Start Date:2017-07-21
PETS (Petmed Express) Start Date:2007-05-01
PETV (Petvivo Holdings) Start Date:2013-05-21
PETVW (Petvivo Holdings Warrant) Start Date:2021-08-11
PETZ (Tdh Holdings, Common Shares) Start Date:2017-09-21
PEV (Phoenix Motor) Start Date:2022-06-08
PFBC (Preferred Bank) Start Date:2007-05-16
PFC (Premier Financial Corp) Start Date:2007-05-16
PFD (Flaherty & Crumrine Preferred And Income Fund Incorporated) Start Date:2007-05-16
PFE (Pfizer) Start Date:2005-01-03
PFG (Principal Financial) Start Date:2005-01-03
PFGC (Performance Food Company) Start Date:2015-10-01
PFHC (Profrac Holding Class A) Start Date:2022-05-13
PFIE (Profire Energy) Start Date:2011-07-06
PFIN (P & F Industries Class A) Start Date:2007-05-16
PFIS (Peoples Financial Services Cor) Start Date:2007-05-21
PFL (Pimco Income Strategy Fund Shares Of Beneficial Interest) Start Date:2007-05-04
PFLT (Pennantpark Floating Rate Capital) Start Date:2011-04-08
PFMT (Performant Financial) Start Date:2012-08-10
PFN (Pimco Income Strategy Fund Ii) Start Date:2007-05-09
PFO (Flaherty & Crumrine Preferred And Income Opportunity Fund Incorporated) Start Date:2007-05-16
PFS (Provident Financial) Start Date:2007-05-02
PFSI (Pennymac Financial Services) Start Date:2013-05-09
PFSW (Pfsweb) Start Date:2007-05-16
PFX (Phenixfin) Start Date:2011-01-20
PG (Procter & Gamble) Start Date:2005-01-03
PGC (Peapack Gladstone) Start Date:2007-05-16
PGEN (Precigen) Start Date:2013-08-08
PGNY (Progyny) Start Date:2019-10-25
PGP (Pimco Global Stocksplus & Income Fund Pimco Global Stocksplus & Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-16
PGR (Progressive) Start Date:2007-04-26
PGRE (Paramount) Start Date:2014-11-19
PGRU (Propertyguru Ordinary Shares) Start Date:2022-03-18
PGTI (Pgt) Start Date:2007-05-03
PGY (Pagaya Technologies Class A Ordinary Shares) Start Date:2022-06-23
PGYWW (Pagaya Technologies Warrants) Start Date:2022-06-23
PGZ (Principal Real Estate Income Fund Common Shares Of Beneficial Interest) Start Date:2013-06-26
PH (Parker-Hannifin) Start Date:2005-01-03
PHAR (Pharming N.V. ADS, Each Representing 10 Ordinary Shares) Start Date:2020-12-23
PHAS (Phasebio Pharmaceuticals) Start Date:2018-10-18
PHAT (Phathom Pharmaceuticals) Start Date:2019-10-25
PHCF (Puhui Wealth Investment Management Co. Ordinary Shares) Start Date:2018-12-27
PHD (Pioneer Floating Rate Fund) Start Date:2007-05-08
PHG (Koninklijke Philips N.V.) Start Date:2007-01-03
PHGE (Biomx) Start Date:2019-03-13
PHI (Pldt Sponsored ADR) Start Date:2007-05-01
PHICU (Population Health Investment Co. Unit) Start Date:2020-11-18
PHICW (Population Health Investment Co. Warrant) Start Date:2021-01-12
PHIN (Phinia Inc) Start Date:2023-06-28
PHIO (Phio Pharmaceuticals) Start Date:2012-05-10
PHK (Pimco High Income Fund Pimco High Income Fund) Start Date:2007-04-30
PHM (Pulte Homes) Start Date:2005-01-03
PHR (Phreesia) Start Date:2019-07-18
PHT (Pioneer High Income Fund) Start Date:2007-05-04
PHUN (Phunware) Start Date:2016-10-28
PHUNW (Phunware Warrants) Start Date:2018-12-28
PHVS (Pharvaris N.V.) Start Date:2021-02-05
PHX (Phx Minerals) Start Date:2007-05-16
PHXM (Phaxiam Therapeutics Sa) Start Date:2017-11-10
PI (Impinj) Start Date:2016-07-21
PII (Polaris) Start Date:2007-01-03
PIII (P3 Health Partners Class A) Start Date:2021-04-06
PIIIW (P3 Health Partners Warrant) Start Date:2021-12-03
PIK (Kidpik) Start Date:2021-11-11
PIM (Putnam Master Intermediate Income Trust) Start Date:2007-04-30
PINC (Premier) Start Date:2013-09-26
PINE (Alpine Ome Property Trust) Start Date:2019-11-22
PINS (Pinterest) Start Date:2019-04-18
PIPR (Piper Sandler Companies) Start Date:2020-01-06
PIRS (Pieris Pharmaceuticals) Start Date:2015-06-26
PIXY (Shiftpixy) Start Date:2017-06-30
PJT (Pjt Partners) Start Date:2015-10-01
PK (Park Hotels & Resorts) Start Date:2016-12-13
PKBK (Parke Bancorp) Start Date:2007-05-16
PKE (Park Aerospace Corp) Start Date:2007-05-01
PKG (Packaging Of America) Start Date:2005-01-03
PKOH (Park-Ohio) Start Date:2007-05-08
PKX (Posco Holdings American Depositary Shares) Start Date:2007-04-30
PL (Planet Labs Pbc) Start Date:2021-04-26
PLAB (Photronics) Start Date:2007-04-25
PLAG (Planet Green Holdings) Start Date:2009-09-08
PLAO (Patria Latin American Opportunity Acquisition) Start Date:2022-05-04
PLAY (Dave & Busters Entertainment) Start Date:2014-10-10
PLBC (Plumas Bancorp) Start Date:2007-05-16
PLBY (Plby ,) Start Date:2020-08-31
PLCE (Childrens Place) Start Date:2007-04-27
PLD (Prologis) Start Date:2007-04-27
PLG (Platinum Metals Ordinary Shares) Start Date:2007-06-28
PLL (Piedmont Lithium Limited) Start Date:2018-05-07
PLM (Polymet Mining Ordinary Shares) Start Date:2007-05-10
PLMR (Palomar) Start Date:2019-04-17
PLNT (Planet Fitness) Start Date:2015-08-06
PLOW (Douglas Dynamics) Start Date:2010-05-05
PLPC (Preformed Line Products) Start Date:2007-05-16
PLRX (Pliant Therapeutics) Start Date:2020-06-03
PLSE (Pulse Biosciences) Start Date:2016-05-18
PLTK (Playtika Holding) Start Date:2021-01-15
PLTN (Plutonian Acquisition) Start Date:2023-01-11
PLTR (Palantir Technologies) Start Date:2020-09-30
PLUG (Plug Power) Start Date:2007-04-27
PLUR (Pluri) Start Date:2007-01-03
PLUS (Eplus) Start Date:2007-05-16
PLX (Protalix Biotherapeutics) Start Date:2010-09-07
PLXP (Plx Pharma) Start Date:2014-03-13
PLXS (Plexus) Start Date:2007-04-27
PLYA (Playa Hotels & Resorts N.V. Ordinary Shares) Start Date:2017-03-13
PLYM (Plymouth Industrial Reit) Start Date:2017-06-09
PM (Philip Morris International) Start Date:2008-03-31
PMCB (Pharmacyte Biotech) Start Date:2009-03-18
PMD (Psychemedics Corporation) Start Date:2007-05-16
PMEC (Primech Holdings Ltd.) Start Date:2023-10-10
PMF (Pimco Municipal Income Fund) Start Date:2007-05-16
PML (Pimco Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PMM (Putnam Managed Municipal Income Trust) Start Date:2007-05-16
PMN (Promis Neurosciences) Start Date:2022-07-08
PMO (Putnam Municipal Opportunities Trust) Start Date:2007-05-16
PMT (Pennymac Mortgage) Start Date:2009-07-30
PMTS (Cpi Card) Start Date:2015-10-09
PMVP (Pmv Pharmaceuticals) Start Date:2020-09-25
PMX (Pimco Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PNBK (Patriot National Bancorp) Start Date:2007-05-16
PNC (Pnc Financial Services) Start Date:2005-01-03
PNF (Pimco New York Municipal Income Fund) Start Date:2007-05-16
PNFP (Pinnacle Financial Partners) Start Date:2007-01-03
PNI (Pimco New York Municipal Income Fund Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PNM (Pnm Resources) Start Date:2007-01-03
PNNT (Pennantpark Investment) Start Date:2007-05-16
PNR (Pentair Plc) Start Date:2012-09-17
PNRG (Primeenergy Resources Corp) Start Date:2007-05-16
PNT (Point Biopharma Global) Start Date:2020-07-08
PNTG (Pennant) Start Date:2019-10-01
PNW (Pinnacle West Capital) Start Date:2005-01-03
POAI (Predictive Oncology) Start Date:2010-04-09
POCI (Precision Optics) Start Date:2022-11-16
PODC (Courtside Inc) Start Date:2023-09-08
PODD (Insulet Corporation) Start Date:2007-05-15
POET (Poet Technologies Common Shares) Start Date:2022-03-14
POL (Polished) Start Date:2020-07-31
POLA (Polar Power) Start Date:2016-12-07
POND (Angel Pond Holdings) Start Date:2021-07-09
PONO (Pono Capital Class A) Start Date:2021-10-12
PONOU (Pono Capital Unit) Start Date:2021-08-11
POOL (Pool Corporation) Start Date:2005-01-03
POR (Portland General Electric Company) Start Date:2007-01-03
POST (Post) Start Date:2012-01-27
POWI (Power Integrations) Start Date:2007-03-15
POWL (Powell Industries) Start Date:2007-05-16
POWRU (Powered Brands Units) Start Date:2021-01-08
POWRW (Powered Brands Warrants) Start Date:2021-03-03
POWW (Ammo,) Start Date:2007-05-17
PPBI (Pacific Premier Bancorp) Start Date:2007-05-16
PPBT (Purple Biotech American Depositary Shares) Start Date:2015-11-20
PPC (Pilgrim's Pride Corporation) Start Date:2009-12-29
PPG (Ppg Industries) Start Date:2005-01-03
PPIH (Perma-Pipe International Holdings) Start Date:2007-05-16
PPL (Ppl) Start Date:2005-01-03
PPSI (Pioneer Power Solutions) Start Date:2013-09-19
PPT (Putnam Premier Income Trust) Start Date:2007-04-30
PPTA (Perpetua Resources Common Shares) Start Date:2021-02-18
PPYA (Papaya Growth Opportunity I Class A) Start Date:2022-03-04
PPYAU (Papaya Growth Opportunity I Unit) Start Date:2022-01-14
PPYAW (Papaya Growth Opportunity I Warrant) Start Date:2022-03-04
PR (Permian Resources Class A) Start Date:2016-04-15
PRA (Proassurance) Start Date:2007-05-02
PRAA (Pra) Start Date:2007-05-02
PRAX (Praxis Precision Medicines) Start Date:2020-10-16
PRCH (Porch ,) Start Date:2020-01-13
PRCT (Procept Biorobotics) Start Date:2021-09-15
PRDO (Perdoceo Education) Start Date:2007-05-01
PRDS (Pardes Biosciences) Start Date:2021-02-17
PRE (Prenetics Global Class A Ordinary Share) Start Date:2022-05-18
PRFT (Perficient) Start Date:2007-04-25
PRFX (Painreform) Start Date:2020-09-01
PRG (Prog Holdings) Start Date:2020-12-01
PRGO (Perrigo) Start Date:2005-01-03
PRGS (Progress Software) Start Date:2007-05-01
PRI (Primerica) Start Date:2010-04-01
PRIM (Primoris Services) Start Date:2008-08-04
PRK (Park National) Start Date:2007-05-16
PRLB (Proto Labs) Start Date:2012-02-24
PRLD (Prelude Therapeutics) Start Date:2020-09-25
PRM (Perimeter Solutions Sa Ordinary Shares) Start Date:2021-11-09
PRME (Prime Medicine) Start Date:2022-10-20
PRO (Pros) Start Date:2007-06-28
PROC (Procaps S.A. Ordinary Shares) Start Date:2021-09-30
PROCW (Procaps S.A. Warrants) Start Date:2021-09-30
PROF (Profound Medical) Start Date:2016-06-09
PROK (Prokidney Class A) Start Date:2021-06-30
PROV (Provident Financial) Start Date:2007-05-16
PRPC (Cc Neuberger Principal Holdings Iii Class A Ordinary Shares) Start Date:2021-03-30
PRPH (Prophase Labs) Start Date:2007-05-16
PRPL (Purple Innovation) Start Date:2015-10-29
PRPO (Precipio) Start Date:2017-06-30
PRQR (Proqr Therapeutics N.V. Ordinary Shares) Start Date:2014-09-18
PRSO (Peraso) Start Date:2019-08-28
PRSRU (Prospector Capital Unit) Start Date:2021-01-08
PRSRW (Prospector Capital Warrants) Start Date:2021-03-01
PRST (Presto Automation) Start Date:2021-02-05
PRT (Permrock Royalty Trust Trust Units) Start Date:2018-05-02
PRTA (Prothena  Ordin) Start Date:2012-12-21
PRTC (Puretech Health Plc American Depositary Shares) Start Date:2020-11-16
PRTG (Portage Biotech) Start Date:2021-02-25
PRTH (Priority Technology) Start Date:2016-12-06
PRTK (Paratek Pharmaceuticals) Start Date:2009-02-02
PRTS (Carparts) Start Date:2007-05-16
PRTY (Party City Holdco) Start Date:2015-04-16
PRU (Prudential Financial) Start Date:2005-01-03
PRVA (Privia Health) Start Date:2021-04-29
PRZO (Parazero Technologies Ltd.) Start Date:2023-07-27
PSA (Public Storage) Start Date:2005-01-03
PSF (Cohen & Steers Select Preferred And Income Fund) Start Date:2010-11-24
PSFE (Paysafe Limited) Start Date:2020-10-09
PSHG (Performance Shipping Common Shares) Start Date:2011-01-03
PSMT (Pricesmart) Start Date:2007-05-11
PSN (Parsons Corporation) Start Date:2019-05-08
PSNL (Personalis) Start Date:2019-06-20
PSNY (Polestar Automotive Holding Uk Plc Class A ADS) Start Date:2022-06-24
PSNYW (Polestar Automotive Holding Uk Plc Class C-1 ADS) Start Date:2022-06-24
PSO (Pearson Plc) Start Date:2013-02-11
PSTG (Pure Storage) Start Date:2015-10-07
PSTV (Plus Therapeutics) Start Date:2007-05-16
PSTX (Poseida Therapeutics) Start Date:2020-07-10
PSX (Phillips 66) Start Date:2012-05-01
PT (Pintec Technology Holdings American Depositary Shares) Start Date:2018-10-25
PTA (Cohen & Steers Tax-Advantaged Preferred Securities And Income Fund Common Shares Of Beneficial Interest) Start Date:2020-11-02
PTC (Ptc) Start Date:2007-04-27
PTCT (Ptc Therapeutics) Start Date:2013-06-20
PTEN (Patterson-Uti Energy) Start Date:2007-04-27
PTGX (Protagonist Therapeutics) Start Date:2016-08-11
PTHRU (Pono Capital Three Unit) Start Date:2023-02-10
PTICU (Proptech Investment Ii Unit) Start Date:2020-12-04
PTICW (Proptech Investment Ii Warrant) Start Date:2021-01-25
PTIX (Protagenic Therapeutics) Start Date:2017-01-11
PTIXW (Protagenic Therapeutics Warrant) Start Date:2021-04-27
PTLO (Portillo's Class A) Start Date:2021-10-21
PTMN (Portman Ridge Finance) Start Date:2007-05-16
PTN (Palatin Technologies) Start Date:2007-04-25
PTNR (Partner Communications Company American Depositary Shares) Start Date:2013-02-11
PTON (Peloton Interactive) Start Date:2019-09-26
PTPI (Petros Pharmaceuticals) Start Date:2020-12-02
PTRA (Proterra) Start Date:2020-11-25
PTRS (Partners Bancorp) Start Date:2007-05-16
PTSI (P.A.M. Transportation) Start Date:2007-05-10
PTVE (Pactiv Evergreen) Start Date:2020-09-17
PTWO (Pono Capital Two) Start Date:2022-09-26
PTWOU (Pono Capital Two Unit) Start Date:2022-08-05
PTY (Pimco Corporate & Income Opportunity Fund) Start Date:2007-04-30
PUBM (Pubmatic) Start Date:2020-12-09
PUK (Prudential Plc) Start Date:2013-02-11
PULM (Pulmatrix) Start Date:2014-03-21
PUMP (Propetro Holding Corp) Start Date:2017-03-17
PUYI (Puyi ADS) Start Date:2019-03-29
PVBC (Provident Bancorp) Start Date:2015-07-16
PVH (Pvh) Start Date:2005-01-03
PVL (Permianville Royalty Trust Trust Units) Start Date:2011-11-03
PW (Power Reit) Start Date:2007-05-16
PWFL (Powerfleet) Start Date:2007-05-07
PWM (Prestige Wealth) Start Date:2023-07-06
PWOD (Penns Woods Bancorp) Start Date:2007-05-16
PWP (Perella Weinberg Partners Class A) Start Date:2020-11-24
PWR (Quanta Services) Start Date:2005-01-03
PWSC (Powerschool Holdings) Start Date:2021-07-28
PWUP (Powerup Acquisition) Start Date:2022-04-11
PX (P10) Start Date:2021-10-21
PXD (Pioneer Natural Resources) Start Date:2005-01-03
PXDT (Pixie Dust Technologies) Start Date:2023-08-01
PXLW (Pixelworks) Start Date:2007-04-30
PXMD (Paxmedica) Start Date:2022-08-26
PXS (Pyxis Tankers) Start Date:2015-11-03
PYCR (Paycor) Start Date:2021-07-21
PYN (Pimco New York Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PYPD (Polypid) Start Date:2020-06-26
PYPL (Paypal) Start Date:2015-07-06
PYR (Pyrogenesis Canada Common Shares) Start Date:2021-03-11
PYS (Merrill Lynch Depositor Inc Pplus Tr Ser Rrd-1 Tr Ctf Cl A) Start Date:2007-05-16
PYT (Pplus Tr Gsc-2 Tr Ctf Fltg Rate) Start Date:2007-05-17
PYXS (Pyxis Oncology) Start Date:2021-10-08
PZC (Pimco California Municipal Income Fund Iii Common Shares Of Beneficial Interest) Start Date:2007-05-16
PZG (Paramount Gold Nevada) Start Date:2015-04-10
PZZA (Papa John's International) Start Date:2007-01-03
QBTS (D-Wave Quantum) Start Date:2022-08-08
QCOM (Qualcomm) Start Date:2005-01-03
QCRH (Qcr) Start Date:2007-05-16
QD (Qudian American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2017-10-18
QDEL (Quidel Corporation) Start Date:2007-01-03
QETA (Quetta Acquisition Corporation) Start Date:2023-11-30
QFIN (360 Digitech American Depositary Shares) Start Date:2018-12-14
QGEN (Qiagen Nv) Start Date:2005-02-15
QH (Quhuo) Start Date:2020-07-13
QIPT (Quipt Home Medical Common Shares) Start Date:2021-05-27
QLGN (Qualigen Therapeutics) Start Date:2015-06-24
QLI (Qilian International Holding Ordinary Shares) Start Date:2021-01-12
QLYS (Qualys) Start Date:2012-09-28
QMCO (Quantum) Start Date:2019-01-15
QNCX (Quince Therapeutics) Start Date:2019-05-09
QNGY (Quanergy Systems) Start Date:2022-02-09
QNRX (Quoin Pharmaceuticals American Depositary Shares) Start Date:2021-10-28
QNST (Quinstreet) Start Date:2010-02-11
QOMO (Qomolangma Acquisition) Start Date:2022-11-25
QRHC (Quest Resource Holding) Start Date:2009-07-16
QRTEA (Qurate Retail) Start Date:2018-03-12
QRTEB (Qurate Retail, Series B) Start Date:2018-03-16
QRVO (Qorvo) Start Date:2015-01-02
QS (Quantumscape Corporation) Start Date:2020-11-23
QSG (Quantasing) Start Date:2023-01-25
QSI (Quantum-Si Orporated) Start Date:2020-11-13
QSIAW (Quantum-Si Incorporated Warrant) Start Date:2020-11-04
QSR (Restaurant Brands International) Start Date:2014-12-15
QTEK (Qualtek Services Class A) Start Date:2022-02-15
QTEWQ (Qualtek Services Inc) Start Date:2021-03-26
QTNT (Quotient R) Start Date:2014-05-27
QTRX (Quanterix) Start Date:2017-12-07
QTWO (Q2 Holdings) Start Date:2014-03-20
QUAD (Quad/Graphics) Start Date:2010-07-06
QUBT (Quantum Computing) Start Date:2018-07-11
QUIK (Quicklogic) Start Date:2007-05-03
QUOT (Quotient Technology) Start Date:2014-03-07
QURE (Uniqure N.V.) Start Date:2014-02-05
R (Ryder System) Start Date:2005-01-03
RA (Brookfield Real Assets Income Fund) Start Date:2016-12-05
RAAS (Cloopen Holding) Start Date:2021-02-09
RACE (Ferrari N.V.) Start Date:2016-01-04
RACY (Relativity Acquisition) Start Date:2022-04-04
RADCQ (Rite Aid Corp) Start Date:2007-04-27
RADI (Radius Global Infrastructure, Class A) Start Date:2018-02-22
RAIL (Freightcar America) Start Date:2007-05-01
RAIN (Rain Therapeutics) Start Date:2021-04-23
RAMP (Liveramp Holdings) Start Date:2018-10-01
RAND (Rand Capital) Start Date:2007-05-16
RANI (Rani Therapeutics) Start Date:2021-07-30
RAPT (Rapt Therapeutics) Start Date:2019-10-31
RARE (Ultragenyx Pharmaceutical) Start Date:2014-01-31
RAVE (Rave Restaurant) Start Date:2007-05-16
RAYA (Erayak Power Solution) Start Date:2022-12-14
RBA (Ritchie Bros. Auctioneers Incorporated) Start Date:2007-05-04
RBB (Rbb Bancorp) Start Date:2017-07-26
RBBN (Ribbon Communication) Start Date:2007-04-30
RBC (Rbc Bearings Incorporated) Start Date:2007-05-04
RBCAA (Republic Bancorp) Start Date:2007-05-16
RBKB (Rhinebeck Bancorp) Start Date:2019-01-17
RBLX (Roblox) Start Date:2021-03-10
RBOT (Vicarious Surgical) Start Date:2020-09-04
RBT (Rubicon Technologies Class A) Start Date:2022-08-16
RC (Ready Capital Corp) Start Date:2013-02-08
RCAT (Red Cat Holdings) Start Date:2007-12-28
RCEL (Avita Medical) Start Date:2012-03-29
RCG (Renn Fund Inc) Start Date:2007-05-22
RCI (Rogers Communications) Start Date:2007-06-15
RCKT (Rocket Pharmaceuticals) Start Date:2015-02-18
RCKY (Rocky Brands) Start Date:2007-05-08
RCL (Royal Caribbean Cruises Ltd) Start Date:2005-01-03
RCM (R1 Rcm) Start Date:2017-03-15
RCMT (Rcm Technologies) Start Date:2007-05-16
RCON (Recon Technology Class A Ordinary Shares) Start Date:2009-07-30
RCRT (Recruiter.com) Start Date:2021-06-30
RCRTW (Recruiter.com  Warrant) Start Date:2021-06-30
RCS (Pimco Strategic Income Fund) Start Date:2007-05-04
RCUS (Arcus Biosciences) Start Date:2018-03-15
RDCM (Radcom Ordinary Shares) Start Date:2008-07-15
RDFN (Redfin Corporation) Start Date:2017-07-28
RDHL (Redhill Biopharma American Depositary Shares) Start Date:2012-12-27
RDI (Reading International Inc Class A) Start Date:2007-05-16
RDIB (Reading International) Start Date:2019-12-16
RDN (Radian) Start Date:2007-01-03
RDNT (Radnet) Start Date:2007-05-16
RDUS (Radius Recycling) Start Date:2007-04-30
RDVT (Red Violet) Start Date:2018-03-26
RDW (Redwire) Start Date:2021-09-03
RDWR (Radware Ltd.) Start Date:2007-04-25
RDY (Dr. Reddy's Laboratories) Start Date:2007-04-23
REAL (The Realreal) Start Date:2019-06-28
REAX (The Real Brokerage Common Shares) Start Date:2021-06-15
REBN (Reborn Coffee) Start Date:2022-08-12
REE (Ree Automotive) Start Date:2021-07-23
REEAW (Ree Automotive Warrant) Start Date:2021-07-23
REFI (Chicago Atlantic Real Estate Finance) Start Date:2021-12-08
REFR (Research Frontiers) Start Date:2007-05-16
REG (Regency Centers Corporation) Start Date:2005-01-03
REGN (Regeneron) Start Date:2005-01-03
REI (Ring Energy) Start Date:2008-06-04
REKR (Rekor Systems) Start Date:2017-08-29
RELI (Reliance Global) Start Date:2021-02-09
RELIW (Reliance Global  Series A Warrants) Start Date:2021-02-09
RELL (Richardson Electronics) Start Date:2007-05-03
RELX (Relx Plc Plc American Depositary Shares) Start Date:2007-05-07
RELY (Remitly Global,) Start Date:2021-09-23
RENB (Renovaro Biosciences Inc) Start Date:2015-02-02
RENE (Cartesian Growth Ii) Start Date:2022-07-08
RENEU (Cartesian Growth Ii Unit) Start Date:2022-05-06
RENT (Rent The Runway, Class A) Start Date:2021-10-27
REPL (Replimune) Start Date:2018-07-20
REPX (Riley Exploration Permian,) Start Date:2007-05-16
RERE (Atrenew American Depositary Shares) Start Date:2021-06-18
RES (Rpc) Start Date:2007-04-26
RETA (Reata Pharmaceuticals) Start Date:2016-05-26
RETO (Reto Eco-Solutions Common Shares) Start Date:2017-11-29
REVB (Revelation Biosciences) Start Date:2020-11-17
REVBU (Revelation Biosciences Unit) Start Date:2020-10-08
REVBW (Revelation Biosciences Warrant) Start Date:2020-11-16
REVG (Rev) Start Date:2017-01-27
REX (Rex American Resources) Start Date:2007-05-16
REXR (Rexford Industrial Realty) Start Date:2013-07-19
REYN (Reynolds Consumer Products) Start Date:2020-01-31
REZI (Resideo Technologies) Start Date:2018-10-29
RF (Regions Financial) Start Date:2005-01-03
RFAC (Rf Acquisition) Start Date:2022-04-20
RFI (Cohen & Steers Total Return Realty Fund) Start Date:2007-05-16
RFIL (Rf Industries) Start Date:2007-05-16
RFL (Rafael) Start Date:2018-03-27
RFM (Rivernorth Flexible Municipal Income Fund) Start Date:2020-03-27
RFMZ (Rivernorth Flexible Municipal Income Fund Ii) Start Date:2021-02-24
RGA (Reinsurance) Start Date:2007-04-25
RGC (Regencell Bioscience) Start Date:2007-05-01
RGCO (Rgc Resources) Start Date:2007-05-17
RGEN (Repligen Corporation) Start Date:2007-01-03
RGF (The Real Good Food Company Class A) Start Date:2021-11-05
RGLD (Royal Gold) Start Date:2010-04-19
RGLS (Regulus Therapeutics) Start Date:2012-10-04
RGNX (Regenxbio) Start Date:2015-09-17
RGP (Resources Connection) Start Date:2007-05-02
RGR (Sturm Ruger) Start Date:2007-04-27
RGS (Regis) Start Date:2007-05-01
RGT (Royce Global Value Trust) Start Date:2013-10-18
RGTI (Rigetti Computing) Start Date:2022-03-02
RGTIW (Rigetti Computing Warrants) Start Date:2022-03-02
RH (Rh) Start Date:2012-11-02
RHE (Regional Health Properties) Start Date:2017-10-02
RHI (Robert Half International) Start Date:2005-01-03
RIBT (Ricebran Technologies) Start Date:2007-05-09
RICK (Rci Hospitality) Start Date:2007-05-08
RIDE (Lordstown Motors Class A) Start Date:2019-04-17
RIG (Transocean Ltd.) Start Date:2008-12-19
RIGL (Rigel Pharmaceuticals) Start Date:2007-05-01
RILY (B. Riley Financial) Start Date:2009-08-04
RILYP (B. Riley Financial Depositary Shares Each Representing A 1/1000Th Fractional Interest In A Share Of Series A Cumulative Perpetual Preferred Stock) Start Date:2019-10-08
RIO (Rio Tinto Plc) Start Date:2013-02-11
RIOT (Riot Blockchain,) Start Date:2007-08-28
RITM (Rithm Capital) Start Date:2013-05-02
RIV (Rivernorth Opportunities Fund) Start Date:2015-12-24
RIVN (Rivian Automotive, Class A) Start Date:2021-11-10
RJF (Raymond James Financial) Start Date:2005-01-03
RKDA (Arcadia Biosciences) Start Date:2015-05-15
RKLB (Rocket Lab Usa,) Start Date:2021-08-19
RKLY (Rockley Photonics Holdings Ordinary Shares) Start Date:2021-08-12
RKT (Rocket Cos) Start Date:2020-08-06
RL (Polo Ralph Lauren) Start Date:2005-01-03
RLAY (Relay Therapeutics) Start Date:2020-07-16
RLGT (Radiant Logistics) Start Date:2007-05-18
RLI (Rli) Start Date:2016-01-04
RLJ (Rlj Lodging) Start Date:2011-05-11
RLMD (Relmada Therapeutics) Start Date:2015-09-08
RLTY (Cohen & Steers Real Estate Opportunities And Income Fund Common Shares Of Beneficial Interest) Start Date:2022-02-24
RLX (Rlx Technology) Start Date:2021-01-22
RLYB (Rallybio) Start Date:2021-07-29
RM (Regional Management) Start Date:2012-03-28
RMAX (Re/Max) Start Date:2013-10-02
RMBI (Richmond Mutual Bancorporation) Start Date:2019-07-02
RMBL (Rumbleon Class B) Start Date:2017-01-09
RMBS (Rambus) Start Date:2007-04-25
RMCF (Rocky Mountain Chocolate Factory) Start Date:2007-05-16
RMD (Resmed) Start Date:2005-01-03
RMI (Rivernorth Opportunistic Municipal Income Fund) Start Date:2018-10-26
RMMZ (Rivernorth Managed Duration Municipal Income Fund Ii) Start Date:2022-02-11
RMNI (Rimini Street) Start Date:2015-08-28
RMR (The Rmr) Start Date:2015-12-14
RMT (Royce Micro-Cap Trust) Start Date:2007-05-16
RMTI (Rockwell Medical) Start Date:2007-05-16
RNA (Avidity Biosciences) Start Date:2020-06-12
RNAC (Cartesian Therapeutics Inc) Start Date:2016-06-22
RNAZ (Transcode Therapeutics) Start Date:2021-07-09
RNG (Ringcentral) Start Date:2013-09-27
RNGR (Ranger Energy Services Class A) Start Date:2017-08-11
RNLX (Renalytix Ai) Start Date:2020-07-17
RNP (Cohen & Steers Reit And Preferred And Income Fund Common Shares) Start Date:2007-05-09
RNR (Renaissancere Holdings Ltd.) Start Date:2007-01-03
RNST (Renasant) Start Date:2007-05-10
RNW (Renew Energy Global) Start Date:2021-08-24
RNWWW (Renew Energy Global Plc Warrant) Start Date:2021-08-24
RNXT (Renovorx) Start Date:2021-08-26
ROAD (Construction Partners) Start Date:2018-05-04
ROCK (Gibraltar Industries) Start Date:2007-04-30
ROG (Rogers) Start Date:2007-05-01
ROI (Riskon International Inc) Start Date:2010-02-12
ROIC (Retail Opportunity) Start Date:2014-03-06
ROIV (Roivant Sciences Common Shares) Start Date:2021-10-01
ROIVW (Roivant Sciences Warrant) Start Date:2021-10-01
ROK (Rockwell Automation) Start Date:2005-01-03
ROKU (Roku) Start Date:2017-09-28
ROL (Rollins) Start Date:2005-01-03
ROOT (Root Insurance) Start Date:2020-11-02
ROP (Roper Technologies) Start Date:2007-04-30
ROST (Ross Stores) Start Date:2005-01-03
ROVR (Rover , Class A) Start Date:2021-02-01
RPAY (Repay Corp) Start Date:2018-07-17
RPD (Rapid7) Start Date:2015-07-17
RPHM (Reneo Pharmaceuticals) Start Date:2021-04-09
RPID (Rapid Micro Biosystems) Start Date:2021-07-15
RPM (Rpm International) Start Date:2007-01-03
RPRX (Royalty Pharma) Start Date:2020-06-16
RPT (Rpt Realty) Start Date:2007-05-01
RPTX (Repare Therapeutics) Start Date:2020-06-19
RQI (Cohen & Steers Quality Income Realty Fund Inc Common Shares) Start Date:2007-05-08
RR (Richtech Robotics) Start Date:2023-11-17
RRBI (Red River Bancshares) Start Date:2019-05-03
RRC (Range Resources Corporation) Start Date:2005-01-03
RRGB (Red Robin Gourmet Burgers) Start Date:2007-04-24
RRR (Red Rock Resorts) Start Date:2016-04-27
RRX (Regal Rexnord Corporation) Start Date:2007-05-01
RS (Reliance Steel) Start Date:2007-04-30
RSF (Rivernorth Specialty Finance Corporation) Start Date:2019-06-12
RSG (Republic Services Inc) Start Date:2005-01-03
RSI (Rush Street Interactive,) Start Date:2020-04-23
RSKD (Riskified) Start Date:2021-07-29
RSLS (Reshape Lifesciences) Start Date:2017-01-12
RSSS (Research Solutions Inc) Start Date:2009-05-15
RSVR (Reservoir Media) Start Date:2021-01-05
RSVRW (Reservoir Media Warrant) Start Date:2021-01-07
RTC (Baijiayun Class A) Start Date:2007-05-16
RTO (Rentokil Initial Plc) Start Date:2008-10-27
RTX (Raytheon Co.) Start Date:2007-04-27
RUM (Rumble Class A) Start Date:2021-04-14
RUN (Sunrun) Start Date:2015-08-05
RUSHA (Rush Enterprises) Start Date:2007-05-04
RUSHB (Rush Enterprises) Start Date:2007-05-16
RVLP (Rvl Pharmaceuticals Plc Ordinary Shares) Start Date:2018-10-19
RVLV (Revolve ,) Start Date:2019-06-07
RVMD (Revolution Medicines) Start Date:2020-02-13
RVNC (Revance Therapeutics Com) Start Date:2014-02-06
RVP (Retractable Technologies) Start Date:2007-05-16
RVPH (Reviva Pharmaceuticals Holdings) Start Date:2018-10-18
RVPHW (Reviva Pharmaceuticals Holdings Warrants) Start Date:2018-10-18
RVSB (Riverview Bancorp) Start Date:2007-05-16
RVSN (Rail Vision Ordinary Share) Start Date:2022-03-31
RVSNW (Rail Vision Warrant) Start Date:2022-03-31
RVT (Royce Value Trust) Start Date:2007-05-10
RVTY (Revvity Inc) Start Date:2005-01-03
RVYL (Ryvyl) Start Date:2021-02-17
RWAY (Runway Growth Finance) Start Date:2021-10-21
RWLK (Rewalk Robotics Ordinary Shares) Start Date:2014-09-12
RWOD (Redwoods Acquisition) Start Date:2022-04-29
RWT (Redwood Trust) Start Date:2007-04-27
RXO (Rxo) Start Date:2022-10-27
RXRX (Recursion Pharmaceuticals) Start Date:2021-04-16
RXST (Rxsight) Start Date:2021-07-30
RXT (Rackspace Technologies) Start Date:2020-08-05
RY (Royal Bank Of Canada) Start Date:2007-04-30
RYAAY (Ryanair Holdings Plc) Start Date:2013-02-11
RYAM (Rayonier Advanced Materials In) Start Date:2014-06-30
RYAN (Ryan Specialty) Start Date:2021-07-22
RYI (Ryerson Holding) Start Date:2014-08-08
RYN (Rayonier) Start Date:2007-01-03
RYTM (Rhythm Pharmaceuticals) Start Date:2017-10-05
RYZB (Rayzebio) Start Date:2023-09-15
RZB (Reinsurance Of America Incorporated 5.75% Fixed-To-Floating Rate Subordinated Debentures Due 2056) Start Date:2016-06-13
RZLT (Rezolute) Start Date:2017-12-19
S (Sprint Corporation) Start Date:2021-06-30
SA (Seabridge Gold,) Start Date:2007-05-02
SABR (Sabre Corporation) Start Date:2014-04-17
SABS (Sab Biotherapeutics) Start Date:2021-02-09
SABSW (Sab Biotherapeutics Warrant) Start Date:2021-10-25
SACH (Sachem Capital Common Shares) Start Date:2017-02-10
SAFE (Safehold) Start Date:2017-06-22
SAFT (Safety Insurance) Start Date:2007-05-09
SAGE (Sage Therapeutics) Start Date:2014-07-18
SAH (Sonic Automotive) Start Date:2007-04-30
SAIA (Saia) Start Date:2007-05-02
SAIC (Science Applications International Corporation) Start Date:2013-09-16
SAITW (Sai.Tech Global Warrant) Start Date:2021-06-28
SALM (Salem Media  Class A) Start Date:2007-05-16
SAM (Boston Beer Company) Start Date:2007-05-09
SAMG (Silvercrest Asset Management G) Start Date:2013-06-27
SAN (Banco Santander S.A.) Start Date:2007-04-27
SANA (Sana Biotechnology) Start Date:2021-02-04
SAND (Sandstorm Gold Ltd) Start Date:2009-06-01
SANG (Sangoma Technologies Common Shares) Start Date:2021-12-16
SANM (Sanmina) Start Date:2007-04-30
SANW (S&W Seed Company) Start Date:2010-06-14
SAP (Sap Se ADS) Start Date:2013-02-11
SAR (Saratoga Investment New) Start Date:2010-08-13
SASI (Sigma Labs) Start Date:2010-10-14
SASR (Sandy Spring Bancorp) Start Date:2007-05-16
SATL (Satellogic Class A Ordinary Shares) Start Date:2022-01-26
SATLW (Satellogic Warrant) Start Date:2022-01-26
SATS (Echostar) Start Date:2008-01-02
SATX (Satixfy Communications) Start Date:2021-11-08
SAVA (Cassava Sciences) Start Date:2007-04-30
SAVE (Spirit Airlines) Start Date:2011-05-26
SB (Safe Bulkers) Start Date:2008-05-29
SBAC (Sba Communications) Start Date:2005-01-03
SBCF (Seacoast Banking O) Start Date:2007-05-08
SBET (Sharplink Gaming Ordinary Shares) Start Date:2007-05-16
SBEV (Splash Beverage) Start Date:2020-12-24
SBFG (Sb Financial  Commo) Start Date:2007-05-16
SBFM (Sunshine Biopharma) Start Date:2022-02-15
SBFMW (Sunshine Biopharma Warrant) Start Date:2022-02-15
SBGI (Sinclair Broadcast) Start Date:2007-05-02
SBH (Sally Beauty) Start Date:2007-04-27
SBI (Western Asset Intermediate Muni Fund Inc) Start Date:2007-05-16
SBIG (Springbig Holdings) Start Date:2021-04-06
SBIGW (Springbig Holdings Warrant) Start Date:2021-04-05
SBLK (Star Bulk Carriers) Start Date:2007-12-03
SBOW (Silverbow Resorces) Start Date:2017-05-05
SBR (Sabine Royalty Trust) Start Date:2007-05-04
SBRA (Sabra Health Care Reit) Start Date:2010-11-08
SBS (Companhia De Saneamento Basico Do Estado De Sao Paulo - Sabesp) Start Date:2013-02-11
SBSI (Southside Bancshares) Start Date:2007-05-16
SBSW (Sibanye Stillwater Limited) Start Date:2013-02-21
SBT (Sterling Bancorp) Start Date:2017-11-17
SBTX (Silverback Therapeutics) Start Date:2020-12-04
SBUX (Starbucks) Start Date:2005-01-03
SCCO (Southern Copper Corporation) Start Date:2010-02-17
SCD (Lmp Capital And Income Fund) Start Date:2007-05-08
SCHL (Scholastic) Start Date:2007-05-03
SCHW (Charles Schwab Corporation) Start Date:2010-03-05
SCI (Service International) Start Date:2007-01-03
SCKT (Socket Mobile) Start Date:2007-05-16
SCL (Stepan) Start Date:2007-05-16
SCLX (Scilex Holding Company) Start Date:2021-03-05
SCM (Stellus Capital Investment) Start Date:2012-11-08
SCNI (Scinai Immunotherapeutics Ltd.) Start Date:2015-05-12
SCOAU (Scion Tech Growth I Unit) Start Date:2020-12-17
SCOAW (Scion Tech Growth I Warrant) Start Date:2021-02-08
SCOBU (Scion Tech Growth Ii Units) Start Date:2021-02-10
SCOBW (Scion Tech Growth Ii Warrants) Start Date:2021-04-08
SCOR (Comscore) Start Date:2007-06-27
SCPH (Scpharmaceuticals) Start Date:2017-11-17
SCPL (Sciplay Class A) Start Date:2019-05-03
SCS (Steelcase) Start Date:2007-05-03
SCSC (Scansource) Start Date:2007-05-02
SCTL (Societal Cdmo) Start Date:2014-03-07
SCU (Sculptor Capital Management) Start Date:2019-10-01
SCVL (Shoe Carnival) Start Date:2007-04-18
SCWO (374Water) Start Date:2008-10-03
SCWX (Secureworks) Start Date:2016-04-22
SCX (L.S. Starrett Company) Start Date:2007-05-16
SCYX (Scynexis) Start Date:2014-05-02
SD (Sandridge Energy,) Start Date:2016-10-04
SDCCQ (Smiledirectclub Inc) Start Date:2019-09-12
SDGR (Schrodinger) Start Date:2020-02-06
SDHY (Pgim Short Duration High Yield Opportunities Fund Common Shares) Start Date:2020-11-25
SDIG (Stronghold Digital Mining) Start Date:2021-10-20
SDOT (Sadot Inc) Start Date:2020-02-13
SDPI (Superior Drilling Products) Start Date:2014-05-23
SDRL (Seadrill) Start Date:2022-06-01
SE (Sea Limited) Start Date:2017-10-20
SEAC (Seachange International) Start Date:2007-04-26
SEAS (Seaworld Entertainment) Start Date:2013-04-19
SEAT (Vivid Seats Class A) Start Date:2021-10-19
SEATW (Vivid Seats Warrant) Start Date:2021-10-19
SEB (Seaboard) Start Date:2007-05-02
SECO (Secoo Holding ADS) Start Date:2017-09-22
SEDG (Solaredge Technologies) Start Date:2015-03-26
SEE (Sealed Air) Start Date:2005-01-03
SEED (Origin Agritech) Start Date:2007-04-13
SEEL (Seelos Therapeutics) Start Date:2007-05-16
SEER (Seer, Class A) Start Date:2020-12-04
SEIC (Sei Investments Company) Start Date:2007-01-03
SELF (Global Self Storage) Start Date:2008-04-07
SEM (Select Medical Holdings Corporation) Start Date:2009-09-25
SEMR (Semrush) Start Date:2021-03-25
SENEA (Seneca Foods) Start Date:2007-05-16
SENEB (Seneca Foods Class B) Start Date:2007-05-16
SENS (Senseonics Holdings,) Start Date:2016-03-18
SEQL (Seqll Inc) Start Date:2021-08-27
SERA (Sera Prognostics) Start Date:2021-07-15
SES (Ses Ai) Start Date:2022-02-04
SEVN (Seven Hills Realty Trust) Start Date:2014-10-31
SF (Stifel Financial) Start Date:2012-02-08
SFBC (Sound Financial Bancorp) Start Date:2012-08-23
SFBS (Servisfirst Bancshares) Start Date:2014-05-14
SFE (Safeguard Scientifics) Start Date:2007-05-02
SFET (Safe-T American Depositary Share) Start Date:2018-09-11
SFIX (Stitch Fix) Start Date:2017-11-17
SFL (Sfl Corp) Start Date:2007-04-25
SFM (Sprouts Farmers Market) Start Date:2013-08-01
SFNC (Simmons First National) Start Date:2007-05-08
SFRT (Appreciate Holdings Inc) Start Date:2021-01-25
SFRT (Appreciate Holdings Inc) Start Date:2021-01-25
SFST (Southern First Bancshares) Start Date:2007-07-06
SFTGQ (Shift Technologies Inc) Start Date:2019-06-04
SFWL (Shengfeng Development Limited) Start Date:2023-03-31
SG (Sweetgreen) Start Date:2021-11-18
SGA (Saga Communications) Start Date:2007-05-16
SGBX (Sg Blocks) Start Date:2017-06-22
SGC (Superior Uniform) Start Date:2007-05-16
SGD (Safe &Amp; Green Development Corp) Start Date:2023-09-19
SGE (Strong Global Entertainment) Start Date:2023-05-16
SGEN (Seattle Genetics) Start Date:2007-01-03
SGH (Smart Global) Start Date:2017-05-24
SGHC (Super) Start Date:2022-01-28
SGHL (Signal Hill Acquisition) Start Date:2022-03-28
SGHT (Sight Sciences) Start Date:2021-07-15
SGLY (Singularity Future Technology) Start Date:2022-01-07
SGMA (Sigmatron International) Start Date:2007-05-16
SGML (Sigma Lithium Common Shares) Start Date:2021-09-13
SGMO (Sangamo Therapeutics) Start Date:2007-04-27
SGMT (Sagimet Biosciences) Start Date:2023-07-14
SGN (Signing Day Sports) Start Date:2023-11-14
SGRP (Spar) Start Date:2007-05-16
SGRY (Surgery Partners) Start Date:2015-10-01
SGU (Star L.P.) Start Date:2007-05-11
SHAK (Shake Shack) Start Date:2015-01-30
SHBI (Shore Bancshares) Start Date:2007-05-16
SHC (Sotera Health Co) Start Date:2020-11-20
SHCO (Soho House &Amp; Co Inc) Start Date:2021-07-15
SHCR (Sharecare, Class A) Start Date:2020-11-23
SHCRW (Sharecare Warrant) Start Date:2020-11-25
SHEL (Royal Dutch Shell Plc American Depositary Shares) Start Date:2007-04-26
SHEN (Shenandoah Telecommunicat) Start Date:2007-05-16
SHFS (Shf Holdings Class A) Start Date:2021-08-20
SHG (Shinhan Financial Co American Depositary Shares) Start Date:2013-02-11
SHIM (Shimmick Corporation) Start Date:2023-11-14
SHIP (Seanergy Maritime Holdings) Start Date:2008-10-15
SHLS (Shoals Technologies) Start Date:2021-01-27
SHOO (Steven Madden Ltd.) Start Date:2007-01-03
SHOP (Shopify Class A Subordinate Voting Shares) Start Date:2015-05-21
SHOT (Safety Shot Inc) Start Date:2020-10-30
SHPH (Shuttle Pharmaceuticals Holdings) Start Date:2022-08-31
SHPW (Shapeways Holdings) Start Date:2019-11-14
SHUA (Shuaa Partners Acquisition I) Start Date:2022-04-26
SHW (Sherwin-Williams) Start Date:2005-01-03
SHYF (Shyft) Start Date:2007-05-04
SIBN (Si-Bone) Start Date:2018-10-17
SID (Companhia Siderurgica Nacional) Start Date:2013-02-11
SIDU (Sidus Space Class A) Start Date:2021-12-14
SIEB (Siebert Financial) Start Date:2007-05-16
SIEN (Sientra) Start Date:2014-10-29
SIF (Sifco Industries) Start Date:2007-05-16
SIFY (Sify Technologies American Depositary Shares) Start Date:2007-04-25
SIG (Signet Jewelers Limited) Start Date:2005-01-03
SIGA (Siga Technologies) Start Date:2015-03-20
SIGI (Selective Insurance) Start Date:2007-01-03
SII (Sprott Common Shares) Start Date:2007-04-30
SILC (Silicom Ordinary Shares) Start Date:2007-05-16
SILK (Silk Road Medical) Start Date:2019-04-04
SILO (Silo Pharma) Start Date:2022-09-27
SILV (Silvercrest Metals Common Shares) Start Date:2018-08-21
SIM (Grupo Simec S.A.B. De C.V. American Depositary Shares) Start Date:2013-02-11
SIMO (Silicon Motion Technology American Depositary Shares) Start Date:2007-05-04
SINT (Sintx Technologies) Start Date:2014-02-13
SIRI (Sirius Xm Holdings Inc) Start Date:2005-01-03
SISI (Shineco) Start Date:2016-09-28
SITC (Site Centers) Start Date:2007-05-01
SITE (Siteone Landscape Supply) Start Date:2016-05-12
SITM (Sitime) Start Date:2019-11-21
SIX (Six Flags Entertainment Corporation) Start Date:2010-06-21
SJ (Scienjoy Holding Class A Ordinary Shares) Start Date:2019-02-06
SJM (Jm Smucker) Start Date:2005-01-03
SJT (San Juan Basin Royalty Trust) Start Date:2007-04-27
SJW (Sjw) Start Date:2007-05-14
SKE (Skeena Resources Common Shares) Start Date:2008-03-25
SKGR (Sk Growth Opportunities Class A) Start Date:2022-08-18
SKGRU (Sk Growth Opportunities Unit) Start Date:2022-06-24
SKIL (Skillsoft Class A) Start Date:2019-07-26
SKIN (The Beauty Health Company Class A) Start Date:2020-11-24
SKLZ (Skillz) Start Date:2020-12-15
SKM (Sk Telecom Co.Ltd) Start Date:2013-02-11
SKT (Tanger Factory Outlet) Start Date:2007-05-01
SKWD (Skyward Specialty Insurance) Start Date:2023-01-13
SKX (Skechers U.S.A.) Start Date:2007-01-03
SKY (Skyline) Start Date:2007-05-10
SKYH (Sky Harbour) Start Date:2022-01-26
SKYT (Skywater Technology) Start Date:2021-04-21
SKYW (Skywest) Start Date:2007-04-27
SKYX (Skyx Platforms) Start Date:2022-02-10
SLAB (Silicon Laboratories) Start Date:2007-01-03
SLAM (Slam) Start Date:2021-04-16
SLAMU (Slam Unit) Start Date:2021-02-23
SLAMW (Slam Warrant) Start Date:2021-04-16
SLB (Schlumberger Ltd.) Start Date:2005-01-03
SLCA (Us Silica) Start Date:2012-02-01
SLDB (Solid Biosciences) Start Date:2018-01-26
SLDP (Solid Power) Start Date:2021-05-18
SLDPW (Solid Power Warrant) Start Date:2021-12-09
SLE (Super League Enterprise Inc) Start Date:2019-02-26
SLF (Sun Life Financial) Start Date:2007-01-03
SLG (Sl Green Realty) Start Date:2005-01-03
SLGC (Somalogic) Start Date:2021-04-23
SLGCW (Somalogic Warrant) Start Date:2021-04-16
SLGL (Sol-Gel Technologies Ordinary Shares) Start Date:2018-02-01
SLGN (Silgan Holdings) Start Date:2007-01-03
SLI (Standard Lithium Ltd.) Start Date:2021-07-13
SLM (Slm Corporation) Start Date:2011-12-12
SLMBP (Slm Floating Rate Non-Cumulative Preferred Stock Series B) Start Date:2007-05-16
SLN (Silence Therapeutics Plc American Depository Share) Start Date:2020-09-08
SLNA (Selina Hospitality Plc) Start Date:2022-10-27
SLND (Southland Holdings Inc) Start Date:2021-12-23
SLNG (Stabilis Solutions) Start Date:2007-05-16
SLNH (Soluna Holdings) Start Date:2009-04-23
SLNO (Soleno Therapeutics) Start Date:2014-11-13
SLP (Simulations Plus) Start Date:2007-05-16
SLQT (Selectquote) Start Date:2020-05-21
SLRC (Slr Investment) Start Date:2010-02-09
SLRN (Acelyrin) Start Date:2023-05-05
SLRX (Salarius Pharmaceuticals) Start Date:2015-01-29
SLS (Sellas Life Sciences) Start Date:2008-03-13
SLVM (Sylvamo Corporation) Start Date:2021-10-01
SLVR (Silverspac Class A) Start Date:2021-11-01
SM (Sm Energy) Start Date:2007-04-30
SMAR (Smartsheet) Start Date:2018-04-27
SMBC (Southern Missouri Bancorp) Start Date:2007-05-16
SMBK (Smartfinancial) Start Date:2007-05-16
SMCI (Super Micro Computer) Start Date:2007-05-16
SMFG (Sumitomo Mitsui Financial) Start Date:2013-02-11
SMFL (Smart For Life) Start Date:2022-02-16
SMFR (Sema4 Holdings Class A) Start Date:2020-11-04
SMFRW (Sema4 Holdings Warrant) Start Date:2020-11-02
SMG (The Scotts Miracle-Gro Company) Start Date:2007-01-03
SMHI (Seacor Marine) Start Date:2017-06-02
SMID (Smith-Midland) Start Date:2007-05-16
SMLP (Summit Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2012-09-28
SMLR (Semler Scientific,) Start Date:2014-02-21
SMMF (Summit Financial) Start Date:2007-05-16
SMMT (Summit Therapeutics) Start Date:2015-03-05
SMP (Standard Motor Products) Start Date:2007-05-09
SMPL (The Simply Good Foods Company) Start Date:2017-07-10
SMR (Nuscale Power Class A) Start Date:2022-05-03
SMRT (Smartrent) Start Date:2021-08-25
SMSI (Smith Micro Software) Start Date:2007-04-30
SMTC (Semtech Corporation) Start Date:2007-01-03
SMTI (Sanara Medtech) Start Date:2008-06-12
SMTS (Sierra Metals) Start Date:2017-07-11
SMWB (Similarweb) Start Date:2021-05-12
SMX (Smx) Start Date:2021-12-09
SNA (Snap-On) Start Date:2005-01-03
SNAL (Snail) Start Date:2022-11-10
SNAP (Snap) Start Date:2017-03-02
SNAX (Stryve Foods Class A) Start Date:2019-03-06
SNAXW (Stryve Foods Warrant) Start Date:2019-03-06
SNBR (Sleep Number Corp) Start Date:2007-04-27
SNCE (Science 37 Holdings) Start Date:2020-11-23
SNCR (Synchronoss) Start Date:2007-05-04
SNCY (Sun Country Airlines) Start Date:2021-03-17
SND (Smart Sand) Start Date:2016-11-04
SNDA (Sonida Senior Living) Start Date:2007-05-01
SNDL (Sundial Growers Common Shares) Start Date:2019-08-01
SNDR (Schneider National) Start Date:2017-04-06
SNDX (Syndax Pharmaceuticals) Start Date:2016-03-03
SNES (Senestech) Start Date:2016-12-08
SNEX (Stonex) Start Date:2007-04-16
SNFCA (Security Natl Financial) Start Date:2007-05-16
SNGX (Soligenix) Start Date:2009-09-30
SNMP (Evolve Transition Infrastructure Lp) Start Date:2007-04-10
SNN (Smith & Nephew Plc) Start Date:2013-02-11
SNOA (Sonoma Pharmaceuticals) Start Date:2007-05-16
SNOW (Snowflake) Start Date:2020-09-16
SNPO (Snap One Holdings) Start Date:2021-07-28
SNPS (Synopsys) Start Date:2005-01-03
SNPX (Synaptogenix) Start Date:2021-06-07
SNSE (Sensei Biotherapeutics) Start Date:2021-02-04
SNT (Senstar Technologies Ordinary Shares) Start Date:2007-05-16
SNTG (Sentage Holdings) Start Date:2021-07-09
SNTI (Senti Biosciences) Start Date:2021-05-26
SNV (Synovus Financial) Start Date:2007-01-03
SNX (Synnex Corporation) Start Date:2007-01-03
SNY (Sanofi ADS) Start Date:2013-02-11
SO (Southern Co.) Start Date:2005-01-03
SOBR (Sobr Safe) Start Date:2022-05-16
SOFI (Sofi Technologies,) Start Date:2021-06-01
SOFO (Sonic Foundry) Start Date:2007-05-02
SOHO (Sotherly Hotels) Start Date:2007-05-16
SOHU (Sohu.com American Depositary Shares) Start Date:2007-04-30
SOI (Solaris Oilfield Infrastructure) Start Date:2017-05-12
SOL (Renesola American Depsitary Shares) Start Date:2008-01-29
SOLO (Electrameccanica Vehicles) Start Date:2018-08-09
SOLOW (Electrameccanica Vehicles Warrants) Start Date:2018-08-09
SON (Sonoco Products Company) Start Date:2007-01-03
SOND (Sonder Holdings Class A) Start Date:2021-03-15
SONDW (Sonder Holdings Warrants) Start Date:2021-03-15
SONM (Sonim Technologies) Start Date:2019-05-10
SONN (Sonnet Biotherapeutics Holdings) Start Date:2012-06-21
SONO (Sonos) Start Date:2018-08-02
SONX (Sonendo) Start Date:2021-10-29
SONY (Sony American Depositary Shares) Start Date:2013-02-11
SOPA (Society Pass Incorporated) Start Date:2021-11-09
SOPH (Sophia Genetics) Start Date:2021-07-23
SOR (Source Capital) Start Date:2007-05-16
SOS (Sos American Depositary Shares) Start Date:2017-04-28
SOTK (Sono-Tek) Start Date:2007-05-16
SOUN (Soundhound AI Inc Class A) Start Date:2022-04-28
SOUNW (Soundhound AI Warrant) Start Date:2021-04-26
SOVO (Sovos Brands) Start Date:2021-09-23
SP (Sp Plus O) Start Date:2007-05-16
SPB (Spectrum Brands Holdings) Start Date:2010-03-18
SPCB (Supercom Ordinary Shares) Start Date:2008-12-22
SPCE (Virgin Galactic Holdings) Start Date:2017-09-29
SPCM (Sound Point Acquisition I, Ltd) Start Date:2022-04-25
SPE (Special Opportunities Fund Inc) Start Date:2007-05-16
SPEC (Spectaire Holdings Inc) Start Date:2021-12-27
SPFI (South Plains Financial) Start Date:2019-05-09
SPG (Simon Property Inc) Start Date:2005-01-03
SPGC (Sacks Parente Golf) Start Date:2023-08-15
SPGI (S&P Global) Start Date:2007-04-27
SPH (Suburban Propane Partners L P) Start Date:2007-05-09
SPHR (Sphere Entertainment Co.) Start Date:2020-04-09
SPI (Spi Energy Co., Ordinary Shares) Start Date:2016-01-19
SPIR (Spire Global Class A) Start Date:2020-11-03
SPKL (Spark I Acquisition Corporation) Start Date:2023-11-27
SPLK (Splunk) Start Date:2012-04-19
SPLP (Steel Partners Holdings L.P.) Start Date:2012-04-10
SPNS (Sapiens International) Start Date:2007-05-16
SPNT (Siriuspoint Ltd.) Start Date:2013-08-15
SPOK (Spok  O) Start Date:2007-05-04
SPOT (Spotify Technology S.A.) Start Date:2018-04-03
SPPL (Simpple Ltd.) Start Date:2023-09-13
SPR (Spirit Aerosystems Holdings) Start Date:2007-01-03
SPRB (Spruce Biosciences) Start Date:2020-10-09
SPRC (Scisparc Ordinary Shares) Start Date:2021-12-22
SPRO (Spero Therapeutics) Start Date:2017-11-02
SPRU (Spruce Power Holding Class A) Start Date:2022-11-14
SPRY (Ars Pharmaceuticals) Start Date:2020-12-04
SPSC (Sps Commerce) Start Date:2010-04-23
SPT (Sprout Social) Start Date:2019-12-13
SPTN (Spartannash Company O) Start Date:2007-05-03
SPWH (Sportsmans Warehouse) Start Date:2014-04-17
SPWR (Sunpower) Start Date:2007-05-02
SPXC (Spx Corp) Start Date:2007-04-30
SPXX (Nuveen S&P 500 Dynamic Overwrite Fund) Start Date:2007-04-24
SQ (Square) Start Date:2015-11-19
SQFT (Presidio Property Trust) Start Date:2020-10-07
SQFTW (Presidio Property Trust Series A Purchase Warrants) Start Date:2022-01-24
SQLLW (Seqll Warrant) Start Date:2021-08-27
SQM (Sociedad Quimica Y Minera De Chile S.A.) Start Date:2013-02-11
SQNS (Sequans Communications S.A. American Depositary Shares) Start Date:2011-04-15
SQSP (Squarespace) Start Date:2021-05-19
SR (Spire) Start Date:2007-05-07
SRAD (Sportradar) Start Date:2021-09-14
SRC (Spirit Realty Capital) Start Date:2012-09-20
SRCE (1St Source) Start Date:2007-05-16
SRCL (Stericycle) Start Date:2005-01-03
SRDX (Surmodics) Start Date:2007-04-30
SRE (Sempra Energy) Start Date:2005-01-03
SRFM (Surf Air Mobility) Start Date:2023-07-27
SRG (Seritage Growth Properties) Start Date:2015-07-06
SRGA (Surgalign Holdings) Start Date:2007-05-14
SRI (Stoneridge) Start Date:2007-05-16
SRL (Scully Royalty Ltd.) Start Date:2019-06-04
SRM (Srm Entertainment) Start Date:2023-08-15
SRNE (Sorrento Therapeutics  C) Start Date:2009-12-31
SRPT (Sarepta Therapeutics) Start Date:2007-05-02
SRRK (Scholar Rock Holding) Start Date:2018-05-24
SRT (Startek) Start Date:2007-05-08
SRTS (Sensus Healthcare) Start Date:2016-07-26
SRV (Cushing Mlp & Infrastructure Total Return Fund) Start Date:2007-08-27
SRZN (Surrozen) Start Date:2021-08-12
SRZNW (Surrozen Warrant) Start Date:2021-08-12
SSB (South State Corp) Start Date:2007-05-16
SSBI (Summit State Bank) Start Date:2007-05-16
SSBK (Southern States Bancshares) Start Date:2021-08-12
SSD (Simpson Manufacturing Co.) Start Date:2007-01-03
SSIC (Silver Spike Investment) Start Date:2022-02-04
SSKN (Strata Skin Sciences) Start Date:2007-05-16
SSL (Sasol Limited) Start Date:2013-02-11
SSNC (Ss&C Technologies Holdings) Start Date:2010-03-31
SSNT (Silversun Technologies) Start Date:2007-05-16
SSP (E. W. Scripps Co) Start Date:2005-01-03
SSRM (Ssr Mining) Start Date:2007-04-27
SSSS (Suro Capital) Start Date:2011-04-28
SST (System1) Start Date:2022-01-28
SSTI (Shotspotter) Start Date:2017-06-07
SSTK (Shutterstock) Start Date:2012-11-12
SSU (Signa Sports United N.V. Ordinary Share) Start Date:2021-12-15
SSY (Sunlink Health Systems) Start Date:2007-05-17
SSYS (Stratasys Inc) Start Date:2012-12-03
ST (Sensata Technologies Holding Plc) Start Date:2010-03-11
STAA (Staar Surgical Company) Start Date:2007-01-03
STAF (Staffing 360 Solutions) Start Date:2015-09-29
STAG (Stag Industrial) Start Date:2011-04-15
STAR (Istar Corp) Start Date:2006-11-30
STBA (S&T Bancorp) Start Date:2007-05-03
STBX (Starbox Holdings) Start Date:2022-08-23
STC (Stewart Information Svcs) Start Date:2007-05-01
STCN (Steel Connect) Start Date:2008-09-30
STE (Steris Plc) Start Date:2015-11-03
STEL (Stellar Bancorp) Start Date:2017-11-08
STEM (Stem,) Start Date:2020-10-08
STEP (Stepstone) Start Date:2020-09-16
STER (Sterling Check) Start Date:2021-09-23
STEW (Srh Total Return Fund) Start Date:2022-04-04
STG (Sunlands Technology American Depositary Shares Representing Class A Ordinary Shares) Start Date:2018-03-23
STGW (Stagwell) Start Date:2007-05-16
STHO (Star Holdings) Start Date:2023-04-03
STIM (Neuronetics) Start Date:2018-06-28
STIX (Semantix Class A) Start Date:2022-08-04
STK (Columbia Seligman Premium Technology Growth Fund Inc) Start Date:2009-11-25
STKH (Steakholder Foods) Start Date:2021-03-12
STKL (Sunopta,) Start Date:2007-05-01
STKS (The One Hospitality) Start Date:2015-05-08
STLA (Stellantis N.V.) Start Date:2008-10-27
STLD (Steel Dynamics) Start Date:2007-01-03
STM (Stmicroelectronics N.V.) Start Date:2013-02-11
STN (Stantec Inc) Start Date:2008-07-31
STNE (Stoneco Ltd.) Start Date:2018-10-25
STNG (Scorpio Tankers) Start Date:2010-03-31
STOK (Stoke Therapeutics) Start Date:2019-06-19
STR (Sitio Royalties Class A) Start Date:2022-06-14
STRA (Strayer Education) Start Date:2007-04-30
STRC (Sarcos Technology And Robotics) Start Date:2021-03-08
STRCW (Sarcos Technology And Robotics Warrants) Start Date:2021-09-27
STRL (Sterling Construction Co) Start Date:2007-05-03
STRM (Streamline Health Solutions) Start Date:2007-05-16
STRN (86260J102 Nasdaq Pillar Stran & Company,) Start Date:2021-11-09
STRNW (Stran & Company Warrant) Start Date:2021-11-09
STRO (Sutro Biopharma) Start Date:2018-09-27
STRR (Star Equity Holdings) Start Date:2007-04-19
STRRP (Star Equity Holdings Series A Cumulative Perpetual Preferred Stock) Start Date:2019-09-13
STRS (Stratus Properties) Start Date:2007-05-16
STRT (Strattec Security) Start Date:2007-05-16
STRY (Starry Holdings Class A) Start Date:2022-03-29
STSS (Sharps Technology) Start Date:2022-04-14
STSSW (Sharps Technology Warrant) Start Date:2022-04-14
STT (State Street) Start Date:2005-01-03
STTK (Shattuck Labs) Start Date:2020-10-09
STVN (Stevanato) Start Date:2021-07-16
STWD (Starwood Property Trust) Start Date:2009-08-12
STX (Seagate Technology) Start Date:2005-01-03
STXS (Stereotaxis) Start Date:2007-05-01
STZ (Constellation Brands) Start Date:2005-01-03
SU (Suncor Energy) Start Date:2007-01-03
SUI (Sun Communities) Start Date:2007-01-03
SUM (Summit Materials) Start Date:2015-03-12
SUN (Sunoco Lp) Start Date:2012-09-20
SUNL (Sunlight Financial) Start Date:2021-01-15
SUNW (Sunworks) Start Date:2015-03-04
SUP (Superior Industries International) Start Date:2009-07-21
SUPN (Supernus Pharmaceuticals) Start Date:2012-05-01
SUPV (Grupo Supervielle S.A.) Start Date:2016-05-19
SURF (Surface Oncology) Start Date:2018-04-19
SURG (Surgepays) Start Date:2015-06-01
SURGW (Surgepays Warrant) Start Date:2021-11-02
SUZ (Suzano S.A.) Start Date:2018-12-10
SVC (Service Properties Trust) Start Date:2019-09-25
SVFAU (Svf Investment Unit) Start Date:2021-01-08
SVFAW (Svf Investment Warrant) Start Date:2021-01-27
SVFD (Save Foods) Start Date:2021-05-14
SVII (Spring Valley Acquisition Ii) Start Date:2022-10-28
SVM (Silvercorp Metals Common Shares) Start Date:2017-05-15
SVMH (Srivaru Holding Ltd.) Start Date:2022-09-26
SVRA (Savara) Start Date:2017-04-28
SVRE (Saverone 2014 American Depositary Shares) Start Date:2022-06-03
SVREW (Saverone 2014 Warrant) Start Date:2022-06-03
SVT (Servotronics) Start Date:2007-05-17
SVV (Savers Value Village) Start Date:2023-06-29
SVVC (Firsthand Technology Value Fund) Start Date:2011-04-19
SWAG (Stran & Company) Start Date:2021-11-09
SWAV (Shockwave Medical) Start Date:2019-03-07
SWBI (Smith & Wesson Brands) Start Date:2007-05-01
SWI (Solar Winds Corp) Start Date:2018-10-19
SWIM (Latham) Start Date:2021-04-23
SWIN (Solowin Holdings) Start Date:2023-09-07
SWK (Stanley Black & Decker) Start Date:2005-01-03
SWKH (Swk) Start Date:2010-02-04
SWKS (Skyworks Solutions) Start Date:2005-01-03
SWN (Southwestern Energy Company) Start Date:2005-01-03
SWSS (Springwater Special Situations) Start Date:2021-09-23
SWSSU (Springwater Special Situations Unit) Start Date:2021-08-26
SWSSW (Springwater Special Situations Warrant) Start Date:2021-09-23
SWTX (Springworks Therapeutics) Start Date:2019-09-13
SWVL (Swvl Holdings Class A Common Shares) Start Date:2022-04-01
SWVLW (Swvl Holdings Warrant) Start Date:2022-04-01
SWX (Southwest Gas Holdings) Start Date:2007-01-03
SWZ (Swiss Helvetia Fund) Start Date:2007-05-16
SXC (Suncoke Energy) Start Date:2011-07-21
SXI (Standex International) Start Date:2007-05-10
SXT (Sensient Technologies Corporation) Start Date:2007-01-03
SXTC (China Sxt Pharmaceuticals) Start Date:2019-01-04
SXTP (60 Degrees Pharmaceuticals) Start Date:2023-07-12
SY (So-Young International ADS) Start Date:2019-05-02
SYBT (Stock Yards Bancorp Comm) Start Date:2007-05-16
SYBX (Synlogic) Start Date:2015-10-01
SYF (Synchrony Financial) Start Date:2014-07-31
SYK (Stryker) Start Date:2005-01-03
SYM (Symbotic Class A) Start Date:2021-03-09
SYN (Synthetic Biologics) Start Date:2007-05-16
SYNA (Synaptics Incorporated) Start Date:2007-01-03
SYNH (Syneos Health) Start Date:2014-11-07
SYPR (Sypris Solutions) Start Date:2007-05-16
SYRA (Syra Health) Start Date:2023-09-29
SYRE (Spyre Therapeutics Inc) Start Date:2016-04-07
SYRS (Syros Pharmaceuticals) Start Date:2016-06-30
SYT (Syla Technologies Co.) Start Date:2023-03-31
SYTA (Siyata Mobile) Start Date:2020-09-25
SYTAW (Siyata Mobile Warrant) Start Date:2020-09-25
SYY (Sysco) Start Date:2005-01-03
SZC (Cushing Nextgen Infrastructure Income Fund Common Shares Of Beneficial Interest) Start Date:2012-09-26
T (At&T) Start Date:2006-01-03
TAC (Transalta Corporation) Start Date:2007-05-16
TACT (Transact Technologies Incorporated) Start Date:2007-05-16
TAIT (Taitron Components Incorporated Class A) Start Date:2007-05-16
TAK (Takeda Pharmaceutical Company American Depositary Shares) Start Date:2018-12-24
TAL (Tal Education) Start Date:2010-10-20
TALK (Talkspace) Start Date:2020-07-30
TALKW (Talkspace Warrant) Start Date:2020-07-30
TALO (Talos Energy) Start Date:2018-05-10
TANH (Tantech Holdings Common Shares) Start Date:2015-03-24
TAOP (Taoping Ordinary Shares) Start Date:2007-05-16
TAP (Molson Coors Brewing Company) Start Date:2005-03-01
TARA (Protara Therapeutics) Start Date:2020-02-03
TARO (Taro Pharmaceutical Industries Ltd.) Start Date:2012-03-22
TARS (Tarsus Pharmaceuticals) Start Date:2020-10-16
TASK (Taskus) Start Date:2021-06-11
TAST (Carrols Restaurant) Start Date:2007-05-16
TATT (Tat Technologies Ordinary Shares) Start Date:2010-01-08
TAYD (Taylor Devices) Start Date:2007-05-16
TBBK (Bancorp) Start Date:2007-05-16
TBCP (Thunder Bridge Capital Partners Iii Class A) Start Date:2021-04-01
TBCPU (Thunder Bridge Capital Partners Iii Units) Start Date:2021-02-05
TBCPW (Thunder Bridge Capital Partners Iii Warrant) Start Date:2021-03-31
TBI (Trueblue) Start Date:2007-12-18
TBIO (Telesis Bio) Start Date:2021-06-18
TBK (Triumph Bancorp) Start Date:2014-11-07
TBKCP (Triumph Bancorp Depositary Shares Each Representing A 1/40Th Interest In A Share Of 7.125% Series C Fixed-Rate Non-Cumulative Perpetual Preferred Stock) Start Date:2020-06-24
TBLA (Taboola.com Ordinary Shares) Start Date:2021-06-30
TBLAW (Taboola.com Warrant) Start Date:2021-06-30
TBLD (Thornburg Income Builder Opportunities Trust) Start Date:2021-07-28
TBLT (Toughbuilt Industries) Start Date:2018-11-09
TBLTW (Toughbuilt Industries Warrant) Start Date:2018-12-03
TBNK (Territorial Bancorp) Start Date:2009-07-14
TBPH (Theravance Biopharma) Start Date:2014-05-16
TC (Tuanche American Depositary Shares) Start Date:2018-11-20
TCBC (Tc Bancshares) Start Date:2021-07-21
TCBI (Texas Capital Bancshares) Start Date:2007-05-09
TCBK (Trico Bancshares) Start Date:2007-05-08
TCBP (Tc Biopharm) Start Date:2022-02-11
TCBPW (Tc Biopharm) Start Date:2022-02-11
TCBS (Texas Community Bancshares) Start Date:2021-07-16
TCBX (Third Coast Bancshares) Start Date:2021-11-09
TCDA (Tricida) Start Date:2018-06-28
TCI (Transcontinental Realty) Start Date:2007-05-16
TCJH (Top Kingwin Ltd) Start Date:2023-04-18
TCMD (Tactile Systems Technology) Start Date:2016-07-28
TCN (Tricon Residential Common Shares) Start Date:2021-10-07
TCOM (Trip.com Limited) Start Date:2007-04-26
TCON (Tracon Pharmaceuticals) Start Date:2015-01-30
TCPC (Blackrock Tcp Capital) Start Date:2012-04-04
TCRT (Alaunos Therapeutics) Start Date:2007-05-16
TCRX (Tscan Therapeutics) Start Date:2021-07-16
TCS (The Container Store) Start Date:2013-11-01
TCX (Tucows  O) Start Date:2007-05-16
TD (Toronto Dominion Bank) Start Date:2007-05-01
TDC (Teradata Corporation) Start Date:2007-10-01
TDCX (Tdcx American Depositary Shares Each Representing One Class A Ordinary Share) Start Date:2021-10-01
TDF (Templeton Dragon Fund) Start Date:2007-05-10
TDG (Transdigm) Start Date:2006-03-15
TDOC (Teladoc Health) Start Date:2015-07-01
TDS (Telephone And Data Systems) Start Date:2012-01-25
TDUP (Thredup) Start Date:2021-03-26
TDW (Tidewater) Start Date:2007-04-30
TDY (Teledyne Technologies Incorporated) Start Date:2007-01-03
TEAF (Ecofin Sustainable And Social Impact Term Fund) Start Date:2019-03-27
TEAM (Atlassian) Start Date:2015-12-10
TECH (Bio-Techne Corporation) Start Date:2007-01-03
TECK (Teck Resources Limited) Start Date:2016-12-05
TEDU (Tarena International American Depositary Shares) Start Date:2014-04-03
TEF (Telefonica S.A.) Start Date:2013-02-11
TEI (Templeton Emerging Markets Income Fund) Start Date:2007-05-08
TEL (Te Connectivity Ltd.) Start Date:2009-06-26
TELA (Tela Bio) Start Date:2019-11-08
TELL (Tellurian) Start Date:2007-05-16
TENB (Tenable Holdings) Start Date:2018-07-26
TENK (Tenx Keane Acquisition Ordinary Share) Start Date:2022-12-08
TENX (Tenax Therapeutics) Start Date:2009-11-09
TEO (Telecom Argentina Sa) Start Date:2013-02-11
TER (Teradyne) Start Date:2005-01-03
TERN (Terns Pharmaceuticals) Start Date:2021-02-05
TETCU (Tech And Energy Transition Unit) Start Date:2021-03-17
TETCW (Tech And Energy Transition Warrant) Start Date:2021-05-14
TEVA (Teva Pharmaceutical Industries Ltd) Start Date:2013-02-11
TEX (Terex) Start Date:2005-01-03
TFC (Truist Financial Corporation) Start Date:2007-04-30
TFFP (Tff Pharmaceuticals) Start Date:2019-10-25
TFII (Tfi International) Start Date:2020-02-13
TFIN (Triumph Financial) Start Date:2014-11-07
TFPM (Triple Flag Precious Metals) Start Date:2022-08-30
TFSL (Tfs Financial) Start Date:2007-05-16
TFX (Teleflex Inc) Start Date:2005-01-03
TG (Tredegar) Start Date:2007-04-27
TGAN (Transphorm) Start Date:2020-12-24
TGB (Taseko Mines Limited) Start Date:2007-05-03
TGH (Textainer) Start Date:2007-10-10
TGI (Triumph) Start Date:2007-05-01
TGL (Treasure Global) Start Date:2022-08-11
TGLS (Tecnoglass) Start Date:2012-05-10
TGNA (Tegna) Start Date:2007-04-30
TGR (Kimbell Tiger Acquisition Corporation) Start Date:2022-03-28
TGS (Transportadora De Gas Del Sur Sa Tgs) Start Date:2013-02-11
TGT (Target) Start Date:2005-01-03
TGTX (Tg Therapeutics) Start Date:2013-07-18
TH (Target Hospitality) Start Date:2018-03-08
THAR (Tharimmune Inc) Start Date:2022-01-12
THC (Tenet Healthcare Corporation) Start Date:2005-01-03
THCAW (Tuscan Holdings Ii Warrant) Start Date:2019-08-13
THCH (Th International) Start Date:2022-09-29
THCP (Thunder Bridge Capital Partners Iv Class A) Start Date:2021-09-09
THCPU (Thunder Bridge Capital Partners Iv Unit) Start Date:2021-06-30
THCPW (Thunder Bridge Capital Partners Iv Warrant) Start Date:2021-09-01
THFF (First Financial) Start Date:2007-05-16
THG (The Hanover Insurance) Start Date:2007-01-03
THM (International Tower Hill Mines Ordinary Shares) Start Date:2007-08-03
THMO (Thermogenesis Holdings) Start Date:2007-05-04
THNPY (Partial Technip Energies) Start Date:2021-06-17
THO (Thor Industries) Start Date:2007-01-03
THQ (Tekla Healthcare Opportunies Fund Shares Of Beneficial Interest) Start Date:2014-07-29
THR (Thermon) Start Date:2011-05-05
THRD (Third Harmonic Bio) Start Date:2022-09-15
THRM (Gentherm) Start Date:2007-05-16
THRN (Thorne Healthtech) Start Date:2021-09-23
THRX (Theseus Pharmaceuticals) Start Date:2021-10-07
THRY (Thryv Holdings) Start Date:2020-10-01
THS (Treehouse Foods) Start Date:2007-01-03
THTX (Theratechnologies Common Shares) Start Date:2013-02-05
THW (Tekla World Healthcare Fund Shares Of Beneficial Interest) Start Date:2015-06-26
THWWW (Target Hospitality Warrant Expiring 3/15/2024) Start Date:2019-03-18
TIGO (Millicom International Cellular S.A.) Start Date:2019-01-09
TIGR (Up Fintech Holding American Depositary Share Representing Fifteen Class A Ordinary Shares) Start Date:2019-03-20
TIL (Instil Bio) Start Date:2021-03-19
TILE (Interface) Start Date:2013-01-18
TIMB (Tim S.A. American Depositary Shares) Start Date:2020-10-12
TIO (Tingo Inc) Start Date:2013-04-09
TIOAU (Tio Tech A Units) Start Date:2021-04-08
TIOAW (Tio Tech A Warrants) Start Date:2021-06-09
TIPT (Tiptree) Start Date:2010-09-03
TIRX (Tian Ruixiang Holdings) Start Date:2021-01-27
TISI (Team) Start Date:2012-01-03
TITN (Titan Machinery) Start Date:2007-12-07
TIVC (Tivic Health Systems,) Start Date:2021-11-11
TIXT (Telus International) Start Date:2021-02-03
TJX (Tjx Companies) Start Date:2005-01-03
TK (Teekay) Start Date:2007-05-01
TKC (Turkcell Iletisim Hizmetleri As) Start Date:2013-02-11
TKLF (Yoshitsu Co. American Depositary Shares) Start Date:2022-01-18
TKNO (Alpha Teknova) Start Date:2021-06-25
TKR (The Timken Company) Start Date:2007-01-03
TLF (Tandy Leather Factory) Start Date:2022-09-07
TLIS (Talis Biomedical) Start Date:2021-02-12
TLK (Perusahaan Perseroan) Start Date:2007-01-03
TLRY (Tilray, Class 2) Start Date:2018-07-19
TLS (Telos Corp) Start Date:2020-11-20
TLSA (Tiziana Life Sciences Common Shares) Start Date:2018-11-20
TLYS (Tilly's) Start Date:2012-05-04
TM (Toyota Motor) Start Date:2013-02-11
TMBR (Timber Pharmaceuticals) Start Date:2015-06-11
TMC (Tmc The Metals Company) Start Date:2021-09-10
TMCI (Treace Medical Concepts) Start Date:2021-04-23
TMCWW (Tmc The Metals Company Warrants) Start Date:2021-09-10
TMDI (Titan Medical Ordinary Shares) Start Date:2018-06-27
TMDX (Transmedics) Start Date:2019-05-02
TME (Tencent Music Entertainment) Start Date:2018-12-12
TMHC (Taylor Morrison Home Corporation) Start Date:2013-04-10
TMO (Thermo Fisher Scientific) Start Date:2005-01-03
TMP (Tompkins Financial) Start Date:2007-05-16
TMPO (Tempo Automation Holdings) Start Date:2020-09-21
TMQ (Trilogy Metals) Start Date:2012-05-01
TMST (Timkensteel Corp) Start Date:2014-06-19
TMUS (T-Mobile Us) Start Date:2007-05-16
TNC (Tennant) Start Date:2007-05-08
TNDM (Tandem Diabetes Care) Start Date:2013-11-14
TNET (Trinet) Start Date:2014-03-27
TNGX (Tango Therapeutics,) Start Date:2021-08-09
TNK (Teekay Tankers Ltd.) Start Date:2007-12-13
TNL (Travel + Leisure Co.) Start Date:2018-05-21
TNON (Tenon Medical) Start Date:2022-04-27
TNP (Tsakos Energy Navigation Common Shares) Start Date:2007-05-02
TNXP (Tonix Pharmaceuticals Holding) Start Date:2013-08-09
TNYA (Tenaya Therapeutics) Start Date:2021-07-30
TOI (The Oncology Institute) Start Date:2021-11-15
TOIIW (The Oncology Institute Warrant) Start Date:2020-06-04
TOL (Toll Brothers) Start Date:2007-01-03
TOMZ (Tomi Environmental Solutions) Start Date:2020-10-01
TOON (Kartoon Studios Inc) Start Date:2016-11-21
TOP (Zhong Yang Financial Ordinary Shares) Start Date:2022-06-01
TOPS (Top Ships) Start Date:2017-11-03
TORO (Toro Corp) Start Date:2023-04-03
TOST (Toast,) Start Date:2021-09-22
TOUR (Tuniu American Depositary Shares) Start Date:2014-05-09
TOVX (Theriva Biologics) Start Date:2007-05-16
TOWN (Towne Bank) Start Date:2007-05-16
TPB (Turning Point Brands) Start Date:2016-05-11
TPC (Tutor Perini) Start Date:2009-06-01
TPET (Trio Petroleum) Start Date:2023-04-18
TPG (Tpg) Start Date:2022-01-13
TPH (Tri Pointe Homes) Start Date:2013-01-31
TPHS (Trinity Place Holdings) Start Date:2012-09-26
TPIC (Tpi Composites) Start Date:2016-07-22
TPL (Texas Pacific Land Corporation) Start Date:2007-05-16
TPR (Tapestry) Start Date:2007-04-27
TPST (Tempest Therapeutics) Start Date:2021-06-24
TPVG (Triplepoint Venture Growth Bdc) Start Date:2014-03-06
TPX (Tempur Sealy International) Start Date:2007-01-03
TPZ (Tortoise Power And Energy Infrastructure Fund Inc) Start Date:2009-07-29
TR (Tootsie Roll Industries) Start Date:2007-01-03
TRAK (Park City Inc) Start Date:2007-05-16
TRC (Tejon Ranch) Start Date:2007-05-10
TRDA (Entrada Therapeutics) Start Date:2021-10-29
TREE (Lendingtree) Start Date:2008-08-21
TREX (Trex Company) Start Date:2009-11-23
TRGP (Targa Resources) Start Date:2010-12-07
TRHC (Tabula Rasa Healthcare) Start Date:2016-09-29
TRI (Thomson Reuters Corporation) Start Date:2008-04-17
TRIB (Trinity Biotech Plc American Depositary Shares) Start Date:2007-05-16
TRIN (Trinity Capital) Start Date:2021-01-29
TRIP (Tripadvisor) Start Date:2011-12-21
TRKA (Troika Media) Start Date:2021-04-20
TRKWQ (Troika Media Inc) Start Date:2021-04-20
TRMB (Trimble) Start Date:2007-01-03
TRMD (Torm Plc Class A) Start Date:2018-02-23
TRMK (Trustmark) Start Date:2007-05-01
TRML (Tourmaline Bio Inc) Start Date:2021-05-07
TRMR (Tremor International ADS) Start Date:2021-06-18
TRN (Trinity Industries) Start Date:2007-01-03
TRNO (Terreno Realty Corporation) Start Date:2010-02-10
TRNR (Interactive Strength) Start Date:2023-04-28
TRNS (Transcat) Start Date:2007-05-16
TROO (Troops Ordinary Shares) Start Date:2010-12-20
TROW (T. Rowe Price) Start Date:2005-01-03
TROX (Tronox) Start Date:2012-06-18
TRP (Tc Energy Corporation) Start Date:2007-01-03
TRS (Trimas) Start Date:2007-05-18
TRST (Trustco Bank N) Start Date:2007-05-02
TRT (Trio-Tech International) Start Date:2007-04-27
TRTN (Triton International Limited) Start Date:2007-05-10
TRTX (Tpg Re Finance Trust) Start Date:2017-07-20
TRU (Transunion) Start Date:2015-06-25
TRUE (Truecar) Start Date:2014-05-16
TRUP (Trupanion) Start Date:2014-07-18
TRV (The Travelers Companies) Start Date:2007-02-27
TRVG (Trivago N.V. American Depositary Shares) Start Date:2016-12-16
TRVI (Trevi Therapeutics) Start Date:2019-05-07
TRVN (Trevena) Start Date:2014-01-31
TRX (Trx Gold) Start Date:2007-04-20
TS (Tenaris S.A.) Start Date:2013-02-11
TSAT (Telesat Class A Common Shares And Class B Variable Voting Shares) Start Date:2021-11-19
TSBK (Timberland Bancorp) Start Date:2007-05-16
TSBX (Turnstone Biologics) Start Date:2023-07-21
TSCO (Tractor Supply Company) Start Date:2005-01-03
TSE (Trinseo Sa) Start Date:2014-06-12
TSEM (Tower Semiconductor Ltd.) Start Date:2007-01-03
TSHA (Taysha Gene Therapies) Start Date:2020-09-24
TSI (TCWStrategic Income Fund) Start Date:2007-05-16
TSIBU (Tishman Speyer Innovation Ii Unit) Start Date:2021-02-12
TSIBW (Tishman Speyer Innovation Ii Warrant) Start Date:2021-04-05
TSLA (Tesla Inc) Start Date:2010-06-29
TSLX (Sixth Street Specialty Lending,) Start Date:2014-03-21
TSM (Taiwan Semiconductor Manufacturing Company Ltd.) Start Date:2007-04-27
TSN (Tyson Foods) Start Date:2005-01-03
TSP (Tusimple) Start Date:2021-04-15
TSQ (Townsquare Media Class A) Start Date:2014-07-24
TSRI (Tsr) Start Date:2007-05-16
TSVT (2Seventy Bio,) Start Date:2021-11-05
TT (Trane Technologies Plc) Start Date:2007-04-30
TTC (The Toro Company) Start Date:2007-01-03
TTCF (Tattooed Chef, Inc Class A) Start Date:2018-09-12
TTD (The Trade Desk) Start Date:2016-09-21
TTE (Totalenergies Se) Start Date:2007-04-30
TTEC (Teletech) Start Date:2007-05-01
TTEK (Tetra Tech) Start Date:2007-01-03
TTGT (Techtarget) Start Date:2007-05-17
TTI (Tetra Technologies) Start Date:2007-04-30
TTMI (Ttm Technologies) Start Date:2007-05-01
TTNP (Titan Pharmaceuticals) Start Date:2015-10-12
TTOO (T2 Biosystems) Start Date:2014-08-07
TTP (Tortoise Pipeline & Energy Fund) Start Date:2011-10-27
TTSH (Tile Shop Holdings) Start Date:2021-06-17
TTWO (Take-Two Interactive) Start Date:2005-01-03
TU (Telus Corporation) Start Date:2007-01-03
TUEM (Tuesday Morning) Start Date:2021-05-25
TUP (Tupperware Brands) Start Date:2005-01-03
TURB (Turbo Energy) Start Date:2023-09-22
TURN (180 Degree Capital) Start Date:2007-05-03
TUSK (Mammoth Energy Services) Start Date:2016-10-14
TUYA (Tuya) Start Date:2021-03-18
TV (Grupo Televisa S.A.B.) Start Date:2013-02-11
TVC (Tennessee Valley Authority) Start Date:2013-02-11
TVE (Tennessee Valley Authority) Start Date:2013-11-11
TVTX (Travere Therapeutics,) Start Date:2012-11-02
TW (Tradeweb Markets) Start Date:2019-04-04
TWI (Titan International) Start Date:2007-05-02
TWIN (Twin Disc Incorporated) Start Date:2007-05-16
TWKS (Thoughtworks Holding,) Start Date:2021-09-15
TWLO (Twilio) Start Date:2016-06-23
TWLV (Twelve Seas Investment Company Ii Class A) Start Date:2021-04-29
TWLVU (Twelve Seas Investment Company Ii Unit) Start Date:2021-02-26
TWLVW (Twelve Seas Investment Company Ii Warrant) Start Date:2021-04-26
TWN (Taiwan Fund) Start Date:2007-05-16
TWNK (Hostess Brands) Start Date:2015-11-30
TWO (Two Harbors Investment) Start Date:2009-10-29
TWOA (Two) Start Date:2021-03-30
TWST (Twist Bioscience) Start Date:2018-10-31
TX (Ternium S.A.) Start Date:2007-01-03
TXG (10X Genomics) Start Date:2019-09-12
TXMD (Therapeuticsmd) Start Date:2017-10-10
TXN (Texas Instruments) Start Date:2005-01-03
TXO (Txo Energy Partners Lp) Start Date:2023-01-27
TXRH (Texas Roadhouse) Start Date:2007-01-03
TXT (Textron) Start Date:2005-01-03
TY (Tri Continental) Start Date:2007-05-11
TYG (Tortoise Energy Infrastructure) Start Date:2007-05-04
TYL (Tyler Technologies) Start Date:2007-01-03
TYRA (Tyra Biosciences,) Start Date:2021-09-15
TZOO (Travelzoo) Start Date:2007-05-02
U (Unity Software) Start Date:2020-09-18
UA (Under Armour Class C) Start Date:2016-03-23
UAA (Under Armour Class A) Start Date:2007-05-14
UAL (United Continental Holdings) Start Date:2010-10-01
UAMY (United States Antimony) Start Date:2007-05-16
UAN (Cvr Partners, Lp) Start Date:2011-04-08
UAVS (Ageagle Aerial Systems) Start Date:2014-06-17
UBCP (United Bancorp) Start Date:2007-05-16
UBER (Uber Technologies) Start Date:2019-05-10
UBFO (United Security) Start Date:2007-05-16
UBOH (United Bancshares) Start Date:2007-05-16
UBS (Ubs Ag) Start Date:2014-11-28
UBSI (United Bankshares) Start Date:2007-01-03
UBX (Unity Biotechnology) Start Date:2018-05-03
UCAR (U Power Limited) Start Date:2023-04-20
UCBI (United Community Banks) Start Date:2007-05-07
UCBIO (United Community Banks Depositary Shares Each Representing 1/1000Th Interest In A Share Of Series I Non-Cumulativepreferred Stock) Start Date:2020-06-11
UCL (Unocal Co) Start Date:2020-06-10
UCTT (Ultra Clean) Start Date:2007-05-03
UDMY (Udemy,) Start Date:2021-10-29
UDR (Udr Inc) Start Date:2005-01-03
UE (Urban Edge Properties) Start Date:2015-01-16
UEC (Uranium Energy) Start Date:2015-01-16
UEIC (Universal Electronics) Start Date:2007-05-09
UFAB (Unique Fabricating) Start Date:2015-07-01
UFCS (United Fire) Start Date:2007-05-01
UFI (Unifi) Start Date:2007-05-02
UFPI (Ufp Industries) Start Date:2007-01-03
UFPT (Ufp Technologies) Start Date:2007-05-16
UG (United-Guardian) Start Date:2007-05-16
UGI (Ugi Corporation) Start Date:2007-01-03
UGIC (Ugi Corporate Units) Start Date:2021-05-28
UGP (Ultrapar Participacoes S.A.) Start Date:2013-02-11
UGRO (Urban-Gro) Start Date:2021-02-02
UHAL (Amerco) Start Date:2007-05-01
UHG (United Homes Inc) Start Date:2021-03-29
UHS (Universal Health Services) Start Date:2005-01-03
UHT (Universal Health Realty) Start Date:2007-05-10
UI (Ubiquiti Networks) Start Date:2011-10-14
UIS (Unisys) Start Date:2004-01-02
UK (Ucommune International Ordinary Shares) Start Date:2019-11-07
UKOMW (Ucommune International Warrant Expiring 11/17/2025) Start Date:2019-11-07
UL (Unilever Plc) Start Date:2013-02-11
ULBI (Ultralife Batteries) Start Date:2007-05-08
ULCC (Frontier Holdings) Start Date:2021-04-01
ULH (Universal Logistics) Start Date:2007-05-16
ULTA (Ulta Beauty) Start Date:2007-10-25
UMBF (Umb Financial Corporation) Start Date:2007-01-03
UMC (United Microelectronics Corporation) Start Date:2013-02-11
UMH (Umh Properties) Start Date:2007-05-16
UNAM (Unico American) Start Date:2007-05-16
UNB (Union Bankshares) Start Date:2007-05-16
UNCY (Unicycive Therapeutics) Start Date:2021-07-13
UNF (Unifirst) Start Date:2007-05-10
UNFI (United Natural Foods) Start Date:2007-04-25
UNH (United Health) Start Date:2005-01-03
UNIT (Unit) Start Date:2015-04-20
UNM (Unum) Start Date:2005-01-03
UNP (Union Pacific) Start Date:2005-01-03
UNTY (Unity Bancorp) Start Date:2007-05-16
UONE (Urban One Class A) Start Date:2007-05-16
UONEK (Urban One Class D) Start Date:2007-05-01
UP (Wheels Up Experience) Start Date:2021-07-14
UPBD (Upbound Inc) Start Date:2007-04-27
UPC (Union Planters) Start Date:2021-03-23
UPHL (Uphealth Inc) Start Date:2019-07-01
UPLD (Upland Software) Start Date:2014-11-06
UPS (United Parcel Service) Start Date:2005-01-03
UPST (Upstart Holdings) Start Date:2020-12-16
UPWK (Upwork) Start Date:2018-10-03
UPXI (Upexi) Start Date:2021-06-24
URBN (Urban Outfitters) Start Date:2005-01-03
URG (Ur Energy Inc Common Shares) Start Date:2008-07-24
URGN (Urogen Pharma) Start Date:2017-05-04
URI (United Rentals) Start Date:2005-01-03
UROY (Uranium Royalty) Start Date:2021-04-28
USA (Liberty All-Star Equity Fund) Start Date:2007-05-08
USAC (Usa Compression Partners Lp) Start Date:2013-01-15
USAP (Universal Stainless & Alloy Products) Start Date:2007-05-04
USAS (Americas Gold And Silver Common Shares No Par Value) Start Date:2017-01-19
USAU (U.S. Gold) Start Date:2007-05-16
USB (U.S. Bancorp) Start Date:2005-01-03
USCB (Uscb Financial Holdings Class A) Start Date:2021-07-23
USCT (Tkb Critical Technologies 1 Class A Ordinary Shares) Start Date:2021-12-27
USDP (Usd Partners Lp Common Units Representing Partner Interest) Start Date:2014-10-09
USEA (United Maritime) Start Date:2022-07-06
USEG (U.S. Energy) Start Date:2007-05-08
USFD (Us Foods Holding) Start Date:2016-05-26
USGO (U.S. Goldmining) Start Date:2023-04-20
USIO (Usio) Start Date:2015-08-11
USLM (United States Lime) Start Date:2007-05-16
USM (United States Cellular) Start Date:2007-05-02
USNA (Usana Health Sciences) Start Date:2007-05-04
USPH (U.S. Physical Therapy) Start Date:2007-05-16
USWSW (U.S. Well Services Warrants) Start Date:2018-11-07
UTF (Cohen & Steers Infrastructure Fund) Start Date:2007-01-03
UTG (Reaves Utility Income Fund Common Shares Of Beneficial Interest) Start Date:2007-05-08
UTHR (United Therapeutics Corporation) Start Date:2007-01-03
UTI (Universal Technical Inst) Start Date:2007-05-02
UTL (Unitil) Start Date:2007-05-16
UTMD (Utah Medical Products) Start Date:2007-05-16
UTRS (Minerva Surgical) Start Date:2021-10-22
UTSI (Utstarcom Holdings Ordinary Shares) Start Date:2007-05-01
UTZ (Utz Brands,) Start Date:2020-03-02
UUU (Universal Security Instruments) Start Date:2007-04-23
UUUU (Energy Fuels) Start Date:2008-10-27
UVE (Universal Insurance) Start Date:2007-05-16
UVSP (Univest Of Pa) Start Date:2007-05-16
UVV (Universal) Start Date:2007-04-27
UWMC (Uwm Holdings Corporation) Start Date:2020-12-28
UXIN (Uxin ADS) Start Date:2018-06-27
V (Visa) Start Date:2008-03-19
VABK (Virginia National Bankshares) Start Date:2007-05-16
VAC (Marriott Vacations Worldwide Corporation) Start Date:2011-11-08
VAL (Ensco Plc) Start Date:2021-05-03
VALE (Vale S.A. American Depositary Shares Each Representing One Common Share) Start Date:2013-02-11
VALN (Valneva) Start Date:2021-05-06
VALU (Value Line) Start Date:2007-05-16
VANI (Vivani Medical) Start Date:2014-11-19
VAPO (Vapotherm) Start Date:2018-11-14
VATE (Innovate) Start Date:2021-09-20
VAXX (Vaxxinity, Class A) Start Date:2021-11-11
VBF (Invesco Bond Fund) Start Date:2007-05-16
VBFC (Village Bank And Trust Financial) Start Date:2007-05-16
VBIV (Vbi Vaccines) Start Date:2014-07-29
VBNK (Versabank Common Shares) Start Date:2021-09-22
VBTX (Veritex  Common) Start Date:2014-10-09
VC (Visteon Corporation) Start Date:2011-01-10
VCEL (Aastrom Biosciences Comm) Start Date:2007-04-26
VCIF (Vertical Capital Income Fund Common Shares Of Beneficial Interest) Start Date:2019-05-30
VCIG (Vci Global Limited) Start Date:2023-04-13
VCKA (Vickers Vantage I Ordinary Shares) Start Date:2021-03-05
VCKAU (Vickers Vantage I Unit) Start Date:2021-01-07
VCKAW (Vickers Vantage I Warrant) Start Date:2021-03-08
VCNX (Vaccinex) Start Date:2018-08-09
VCSA (Vacasa Class A) Start Date:2021-12-07
VCTR (Victory Capital Holdings Class A) Start Date:2018-02-08
VCV (Invesco California Value Municipal Income Trust) Start Date:2007-05-16
VCYT (Veracyte) Start Date:2013-10-30
VECO (Veeco Instruments) Start Date:2007-05-02
VEEE (Twin Vee Powercats Co.) Start Date:2021-07-21
VEEV (Veeva Systems) Start Date:2013-10-16
VEL (Velocity Financial) Start Date:2020-01-17
VEON (Veon Ltd.) Start Date:2013-02-11
VERA (Vera Therapeutics) Start Date:2021-05-14
VERB (Verb Technology Company) Start Date:2019-04-05
VERBW (Verb Technology Company Warrant) Start Date:2019-04-05
VERI (Veritone) Start Date:2017-05-12
VERO (Venus Concept) Start Date:2017-10-12
VERU (Veru) Start Date:2009-06-09
VERV (Verve Therapeutics) Start Date:2021-06-17
VERX (Vertex) Start Date:2020-07-29
VERY (Vericity) Start Date:2019-08-15
VET (Vermilion Energy) Start Date:2013-03-12
VEV (Vicinity Motor) Start Date:2021-07-07
VFC (V.F.) Start Date:2005-01-03
VFF (Village Farms International, Common Shares) Start Date:2019-02-21
VFL (Delaware Investments National Municipal Income Fund) Start Date:2007-05-16
VFS (Vinfast Auto) Start Date:2023-08-15
VGFC (The Very Good Food Company Common Shares) Start Date:2021-10-13
VGI (Virtus Global Multi-Sector Income Fund Common Shares Of Beneficial Interest) Start Date:2012-02-24
VGM (Invesco Trust For Investment Grade Municipals) Start Date:2016-12-23
VGR (Vector) Start Date:2007-04-30
VGZ (Vista Gold) Start Date:2007-04-24
VHC (Virnetx Holding) Start Date:2007-12-26
VHI (Valhi,) Start Date:2007-05-16
VIA (Via Renewables Class A) Start Date:2021-08-09
VIAO (Via Optronics Ag) Start Date:2020-09-25
VIAV (Viavi Solutions) Start Date:2007-04-27
VICI (Vici Properties) Start Date:2017-10-17
VICR (Vicor Corporation) Start Date:2007-01-03
VIEW (View Class A) Start Date:2020-10-19
VIEWW (View Warrant) Start Date:2020-10-21
VIGL (Vigil Neuroscience) Start Date:2022-01-07
VIIAW (7Gc & Co. Holdings Warrant) Start Date:2021-02-12
VINC (Vincerx Pharma) Start Date:2020-05-27
VINE (Fresh Vine Wine) Start Date:2021-12-14
VINO (Gaucho Holdings) Start Date:2021-02-17
VINP (Vinci Partners Investments) Start Date:2021-01-28
VIOT (Viomi Technology Co. American Depositary Shares) Start Date:2018-09-25
VIPS (Vipshop Holdings Limited) Start Date:2012-03-23
VIR (Vir Biotechnology) Start Date:2019-10-11
VIRC (Virco Manufacturing) Start Date:2007-06-20
VIRI (Virios Therapeutics) Start Date:2020-12-17
VIRT (Virtu Financial) Start Date:2015-04-16
VIRX (Viracta Therapeutics) Start Date:2011-03-16
VISL (Vislink Technologies) Start Date:2011-11-22
VIST (Vista Energy S.A.B. De C.V. American Depositary Shares Each Representing One Series A Share With No Par Value) Start Date:2019-07-26
VITL (Vital Farms) Start Date:2020-07-31
VIV (Telefonica Brasil S.A.) Start Date:2007-05-01
VIVK (Vivakor) Start Date:2022-02-14
VJET (Voxeljet Ag American Depositary Shares) Start Date:2013-10-18
VKI (Invesco Advantage Municipal Income Trust Ii Common Shares Of Beneficial Interest) Start Date:2007-05-16
VKQ (Invesco Municipal Trust) Start Date:2007-05-16
VKTX (Viking Therapeutics) Start Date:2015-04-29
VLCN (Volcon) Start Date:2021-10-06
VLD (Velo3d,) Start Date:2021-09-24
VLDRW (Velodyne Lidar Warrants) Start Date:2020-09-30
VLGEA (Village Super Market) Start Date:2007-05-16
VLN (Valens Semiconductor Ordinary Shares) Start Date:2021-09-30
VLO (Valero Energy) Start Date:2005-01-03
VLRS (Controladora Vuela Compania De Aviacion S.A.B. De C.V. American Depositary Shares Each Representing Ten) Start Date:2013-09-18
VLT (Invesco High Income Trust Ii) Start Date:2007-05-16
VLTO (Veralto Corp) Start Date:2023-09-27
VLY (Valley National Bancorp) Start Date:2007-01-03
VLYPO (Valley National Bancorp 5.50% Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series B) Start Date:2018-10-10
VLYPP (Valley National Bancorp 6.25% Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series A) Start Date:2018-10-10
VMAR (Vision Marine Technologies) Start Date:2020-11-24
VMC (Vulcan Materials) Start Date:2007-11-19
VMCA (Valuence Merger I Class A Ordinary Shares) Start Date:2022-04-25
VMCAU (Valuence Merger I Unit) Start Date:2022-03-01
VMD (Viemed Healthcare) Start Date:2019-08-09
VMEO (Vimeo) Start Date:2021-05-19
VMI (Valmont Industries) Start Date:2007-05-04
VMO (Invesco Municipal Opportunity Trust) Start Date:2007-05-16
VMW (Vmware) Start Date:2007-08-14
VNCE (Vince Holding) Start Date:2013-11-22
VNDA (Vanda Pharmaceuticals) Start Date:2007-05-02
VNET (Vnet  American Depositary Shares) Start Date:2011-04-21
VNO (Vornado Realty Trust) Start Date:2005-01-03
VNOM (Viper Energy Partners Lp) Start Date:2015-01-16
VNRX (Volitionrx Limited) Start Date:2015-02-06
VNT (Vontier) Start Date:2020-10-05
VNTR (Venator Materials Plc) Start Date:2017-08-03
VOC (Voc Energy Trust Units Of Beneficial Interest) Start Date:2011-05-05
VOD (Vodafone Plc) Start Date:2005-01-03
VOR (Vor Biopharma) Start Date:2021-02-05
VORB (Virgin Orbit Holdings) Start Date:2021-12-27
VORBW (Virgin Orbit Holdings Warrant) Start Date:2021-05-21
VOXR (Vox Royalty) Start Date:2022-10-10
VOXX (Voxx International) Start Date:2007-05-09
VOYA (Voya Financial) Start Date:2013-05-02
VPG (Vishay Precision) Start Date:2010-07-07
VPV (Invesco Pennsylvania Value Municipal Income Trust) Start Date:2007-05-16
VQS (Viq Solutions Common Shares) Start Date:2008-10-29
VRA (Vera Bradley) Start Date:2010-10-21
VRAR (Glimpse) Start Date:2021-07-01
VRAX (Virax Biolabs) Start Date:2022-07-21
VRAY (Viewray) Start Date:2015-08-10
VRCA (Verrica Pharmaceuticals) Start Date:2018-06-15
VRDN (Viridian Therapeutics) Start Date:2021-01-20
VRE (Veris Residential) Start Date:2012-11-08
VREX (Varex Imaging) Start Date:2017-01-20
VRM (Vroom) Start Date:2020-06-09
VRME (Verifyme) Start Date:2007-05-23
VRMEW (Verifyme Warrant) Start Date:2020-06-18
VRNA (Verona Pharma Plc American Depositary Share) Start Date:2017-04-27
VRNS (Varonis Systems) Start Date:2014-02-28
VRNT (Verint Systems) Start Date:2007-01-03
VRPX (Virpax Pharmaceuticals) Start Date:2021-02-17
VRRM (Verra Mobility Corp) Start Date:2017-03-24
VRSK (Verisk Analytics) Start Date:2009-10-09
VRSN (Verisign) Start Date:2005-01-03
VRT (Vertiv Holdings Co.) Start Date:2018-07-30
VRTS (Veritas Software) Start Date:2009-01-02
VRTV (Veritiv Corp) Start Date:2014-07-02
VRTX (Vertex Pharmaceuticals Inc) Start Date:2005-01-03
VS (Versus Systems Common Shares) Start Date:2020-12-29
VSAT (Viasat) Start Date:2007-01-03
VSCO (Victoria's Secret) Start Date:2021-07-21
VSEC (Vse) Start Date:2007-05-16
VSH (Vishay Intertechnology) Start Date:2007-01-03
VSME (Vs Media Holdings Limited) Start Date:2023-09-28
VST (Vistra Energy) Start Date:2017-05-10
VSTA (Vasta Platform) Start Date:2020-07-31
VSTE (Vast Renewables Ltd.) Start Date:2022-01-10
VSTM (Verastem) Start Date:2012-01-27
VSTO (Vista Outdoor) Start Date:2015-02-09
VSTS (Vestis Corp) Start Date:2023-09-27
VTAK (Ra Medical Systems Inc) Start Date:2018-09-27
VTEX (Vtex) Start Date:2021-07-22
VTGN (Vistagen Therapeutics,) Start Date:2016-05-11
VTLE (Vital Energy) Start Date:2011-12-15
VTMX (Vesta Real Estate Corporation) Start Date:2023-06-30
VTN (Invesco Trust For Investment Grade New York Municipals) Start Date:2007-05-16
VTNR (Vertex Energy Inc) Start Date:2013-02-13
VTOL (Bristow) Start Date:2013-01-22
VTR (Ventas Inc) Start Date:2005-01-03
VTRS (Viatris) Start Date:2020-11-12
VTRU (Vitru) Start Date:2020-09-18
VTS (Vitesse Energy) Start Date:2023-01-17
VTSI (Virtra) Start Date:2018-03-29
VTVT (Vtv Therapeutics) Start Date:2015-07-30
VTYX (Ventyx Biosciences) Start Date:2021-10-21
VUZI (Vuzix Corporation) Start Date:2010-04-01
VVI (Viad) Start Date:2007-04-27
VVOS (Vivos Therapeutics) Start Date:2020-12-11
VVPR (Vivopower International Plc Ordinary Shares) Start Date:2016-12-29
VVR (Invesco Senior Income Trust) Start Date:2007-05-04
VVV (Valvoline) Start Date:2016-09-23
VVX (V2x) Start Date:2014-09-29
VWE (Vintage Wine Estates) Start Date:2021-02-08
VWEWW (Vintage Wine Estates Warrants) Start Date:2022-01-19
VXRT (Vaxart) Start Date:2012-11-09
VYGR (Voyager Therapeutics) Start Date:2015-11-11
VYNE (Vyne Therapeutics) Start Date:2018-01-25
VYX (Ncr Voyix Corp) Start Date:2007-01-03
VZ (Verizon Communications) Start Date:2005-01-03
VZIO (Vizio Holding) Start Date:2021-03-25
VZLA (Vizsla Silver Common Shares) Start Date:2022-01-21
W (Wayfair) Start Date:2014-10-02
WAB (Wabtec Corporation) Start Date:2005-01-03
WABC (Westamerica Bancorp) Start Date:2009-07-21
WAFD (Washington Federal) Start Date:2007-05-01
WAFDP (Washington Federal Depositary Shares) Start Date:2021-02-11
WAFU (Wah Fu Education Ordinary Shares) Start Date:2019-04-30
WAL (Western Alliance Bancorporation) Start Date:2007-01-03
WALD (Waldencast Plc Class A) Start Date:2021-05-12
WASH (Washington Trust) Start Date:2007-05-04
WAT (Waters Corporation) Start Date:2005-01-03
WATT (Energous) Start Date:2014-03-28
WAVD (Wavedancer) Start Date:2007-05-17
WAVE (Eco Wave Power Global) Start Date:2021-07-01
WB (Weibo Corporation) Start Date:2014-04-17
WBA (Walgreens Boots Alliance) Start Date:2014-12-31
WBD (Warner Bros Discovery) Start Date:2022-04-04
WBEV (Winc,) Start Date:2021-11-11
WBS (Webster Financial Corporation) Start Date:2007-01-03
WBUY (Webuy Global Ltd) Start Date:2023-10-19
WBX (Wallbox N.V. Class A Ordinary Shares) Start Date:2021-04-19
WCC (Wesco International) Start Date:2007-05-01
WCN (Waste Connections) Start Date:2007-01-03
WD (Walker & Dunlop) Start Date:2010-12-15
WDAY (Workday) Start Date:2012-12-10
WDC (Western Digital) Start Date:2005-01-03
WDFC (Wd-40) Start Date:2007-05-09
WDH (Waterdrop) Start Date:2021-05-07
WDI (Western Asset Diversified Income Fund Common Shares Of Beneficial Interest) Start Date:2021-06-25
WDS (Woodside Energy American Depositary Shares Each Representing One Ordinary Share) Start Date:2022-06-02
WEA (Western Asset Bond Fund Share Of Beneficial Interest) Start Date:2007-05-16
WEAV (Weave Communications,) Start Date:2021-11-11
WEC (Wec Energy Inc) Start Date:2005-01-03
WEJO (Wejo Common Shares) Start Date:2021-11-19
WELL (Welltower) Start Date:2007-04-30
WEN (The Wendy's Company) Start Date:2007-01-03
WERN (Werner Enterprises) Start Date:2007-01-03
WES (Western Midstream Partners Lp) Start Date:2012-12-07
WEST (Westrock Coffee Company) Start Date:2022-08-29
WETF (WisdomTree Investments) Start Date:2007-05-16
WETG (Wetrade) Start Date:2020-07-23
WEWKQ (Wework Inc) Start Date:2021-10-21
WEX (Wex) Start Date:2007-04-30
WEYS (Weyco) Start Date:2007-05-16
WF (Woori Financial  American Depositary Shares) Start Date:2007-05-16
WFC (Wells Fargo) Start Date:2005-01-03
WFCF (Where Food Comes From) Start Date:2021-01-05
WFG (West Fraser Timber Co. Ltd) Start Date:2021-02-01
WFRD (Weatherford International Plc Ordinary Shares) Start Date:2021-06-02
WGO (Winnebago Industries) Start Date:2007-01-03
WGS (Genedx Holdings Class A) Start Date:2020-11-04
WH (Wyndham Hotels & Resorts) Start Date:2018-05-18
WHD (Cactus) Start Date:2018-02-08
WHF (Whitehorse Finance) Start Date:2012-12-05
WHG (Westwood) Start Date:2007-05-16
WHLM (Wilhelmina International) Start Date:2009-02-19
WHLR (Wheeler Real Estate Investment Trust) Start Date:2012-11-19
WHLRD (Wheeler Real Estate Investment Trust Series D Cumulative Preferred Stock) Start Date:2016-09-16
WHLRP (Wheeler Real Estate Investment Trust Class B Preferred Stock) Start Date:2014-04-30
WHR (Whirlpool) Start Date:2005-01-03
WIA (Western Asset Inflation-Linked Income Fund) Start Date:2007-05-07
WILC (G Willi-Food International Ltd) Start Date:2016-04-07
WIMI (Wimi Hologram Cloud) Start Date:2020-04-01
WINA (Winmark) Start Date:2007-05-18
WING (Wingstop) Start Date:2015-06-12
WINT (Windtree Therapeutics) Start Date:2020-05-20
WIRE (Encore Wire) Start Date:2007-04-26
WISA (Wisa Technologies) Start Date:2018-07-27
WISH (Contextlogic) Start Date:2020-12-16
WIT (Wipro Limited) Start Date:2013-02-11
WIW (Western Asset Inflation-Linked Opportunities & Income Fund) Start Date:2007-05-02
WIX (Wix.com Ltd.) Start Date:2013-11-06
WK (Workiva) Start Date:2014-12-12
WKC (World Kinect Corp) Start Date:2007-04-30
WKEY (Wisekey International Holding Ag American Depositary Shares) Start Date:2019-12-27
WKHS (Workhorse) Start Date:2016-01-07
WKME (Walkme) Start Date:2021-06-16
WKSP (Worksport) Start Date:2021-08-04
WKSPW (Worksport Warrant) Start Date:2021-08-04
WLDN (Willdan) Start Date:2007-05-16
WLDS (Wearable Devices) Start Date:2022-09-13
WLFC (Willis Lease Finance) Start Date:2007-05-16
WLGS (Wang &Amp; Lee) Start Date:2023-04-20
WLK (Westlake Chemical) Start Date:2007-05-01
WLKP (Westlake Chemical Partners Lp) Start Date:2014-07-30
WLMS (Williams Industrial Services) Start Date:2008-02-13
WLY (John Wiley & Sons) Start Date:2022-04-01
WLYB (John Wiley & Sons) Start Date:2007-05-16
WM (Waste Management) Start Date:2007-04-30
WMB (Williams Cos.) Start Date:2005-01-03
WMC (Western Asset Mortgage) Start Date:2012-05-10
WMG (Warner Music) Start Date:2020-06-03
WMK (Weis Markets) Start Date:2007-05-10
WMPN (William Penn Bancorporation) Start Date:2021-03-25
WMS (Advanced Drainage Systems) Start Date:2014-07-25
WMT (Walmart) Start Date:2005-01-03
WNC (Wabash National) Start Date:2007-05-01
WNEB (Western New England Bancorp) Start Date:2007-05-16
WNS (Wns) Start Date:2007-01-03
WNW (Wunong Net Technology) Start Date:2020-12-15
WOLF (Wolfspeed,) Start Date:2007-04-30
WOOF (Petco Health & Wellness Company) Start Date:2021-01-14
WOR (Worthington Industries) Start Date:2005-01-03
WORX (Scworx) Start Date:2016-10-06
WOW (Wideopenwest) Start Date:2017-05-25
WPC (W. P. Carey) Start Date:2007-01-03
WPM (Wheaton Precious Metals) Start Date:2007-05-01
WPP (Wpp Plc) Start Date:2017-11-28
WPRT (Westport Fuel Systems Inc Common Shares) Start Date:2008-08-15
WRAP (Wrap Technologies) Start Date:2018-05-29
WRB (W. R. Berkley Corporation) Start Date:2007-04-27
WRBY (Warby Parker) Start Date:2021-09-29
WRE (Washington Real Estate Investment Trust) Start Date:2007-01-03
WRK (Westrock) Start Date:2015-06-24
WRLD (World Acceptance) Start Date:2007-05-01
WRN (Western Copper And Gold) Start Date:2008-10-27
WRNT (Warrantee) Start Date:2023-07-25
WS (Worthington Steel Inc) Start Date:2023-11-28
WSBC (Wesbanco) Start Date:2007-05-10
WSBF (Waterstone Financial Com) Start Date:2008-08-04
WSC (Willscot Mobile Mini Corp) Start Date:2015-11-05
WSFS (Wsfs Financial) Start Date:2007-05-07
WSM (Williams-Sonoma) Start Date:2007-01-03
WSO (Watsco) Start Date:2007-05-02
WSO.B (Watsco) Start Date:2007-05-16
WSR (Whitestone Reit) Start Date:2010-08-26
WST (West Pharmaceutical Services) Start Date:2007-01-03
WSTG (Wayside Technology) Start Date:2007-05-16
WT (WisdomTree) Start Date:2007-05-16
WTBA (West Bancorporation) Start Date:2007-05-16
WTER (The Alkaline Water Company) Start Date:2013-07-09
WTFC (Wintrust Financial Corporation) Start Date:2007-01-03
WTFCM (Wintrust Financial Fixed-To-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D) Start Date:2015-07-09
WTFCP (Wintrust Financial Depositary Shares Each Representing A 1/1000Th Interest In A Share Of 6.875% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E) Start Date:2020-05-29
WTI (W&T Offshore) Start Date:2007-04-30
WTM (White Mountains Insurance) Start Date:2007-05-16
WTO (Utime Ltd.) Start Date:2021-04-06
WTRG (Essential Utilities) Start Date:2007-04-27
WTS (Watts Water Technologies) Start Date:2007-04-27
WTTR (Select Energy Services) Start Date:2017-04-21
WTW (Willis Towers Watson) Start Date:2016-01-05
WU (Western Union Co) Start Date:2006-10-02
WULF (Terawulf) Start Date:2007-05-18
WVE (Wave Life Sciences) Start Date:2015-11-11
WVVI (Willamette Valley Vineyards) Start Date:2007-05-16
WVVIP (Willamette Valley Vineyards Series A Redeemable Preferred Stock) Start Date:2016-06-29
WW (Ww International) Start Date:2007-05-02
WWD (Woodward) Start Date:2007-05-03
WWE (World Wrestling Entertainment) Start Date:2007-01-03
WWR (Westwater Resources) Start Date:2007-05-08
WWW (Wolverine World Wide) Start Date:2007-01-03
WY (Weyerhaeuser) Start Date:2005-01-03
WYNN (Wynn Resorts Ltd) Start Date:2005-01-03
WYY (Widepoint) Start Date:2007-04-26
X (United States Steel Corporation) Start Date:2005-01-03
XAIR (Beyond Air) Start Date:2019-05-07
XBIO (Xenetic Biosciences) Start Date:2016-11-07
XBIOW (Xenetic Biosciences Warrants) Start Date:2019-07-23
XBIT (Xbiotech) Start Date:2015-04-15
XCUR (Exicure) Start Date:2018-05-22
XEL (Xcel Energy Inc) Start Date:2005-01-03
XELA (Exela Technologies) Start Date:2015-03-27
XELB (Xcel Brands) Start Date:2007-05-23
XENE (Xenon Pharmaceuticals Inc) Start Date:2014-11-05
XERS (Xeris Pharmaceuticals) Start Date:2018-06-21
XFLT (Xai Octagon Floating Rate & Alternative Income Term Trust Common Shares Of Beneficial Interest) Start Date:2017-09-27
XFOR (X4 Pharmaceuticals) Start Date:2019-04-16
XGN (Exagen) Start Date:2019-09-19
XHR (Xenia Hotels & Resorts) Start Date:2015-02-04
XIN (Xinyuan Real Estate Co American Depositary Shares) Start Date:2007-12-12
XL (Xl Fleet) Start Date:2019-09-03
XLO (Xilio Therapeutics) Start Date:2021-10-22
XMTR (Xometry) Start Date:2021-06-30
XNCR (Xencor) Start Date:2013-12-03
XNET (Xunlei American Depositary Shares) Start Date:2014-06-24
XOM (Exxon Mobil) Start Date:2005-01-03
XOMA (Xoma) Start Date:2007-05-04
XOS (Xos,) Start Date:2020-12-08
XOSWW (Xos Warrants) Start Date:2020-12-07
XP (Xp) Start Date:2019-12-11
XPEL (Xpel) Start Date:2019-07-22
XPER (Xperi Holding Corp) Start Date:2020-05-29
XPEV (Xpeng) Start Date:2020-08-27
XPL (Solitario Zinc) Start Date:2007-05-16
XPO (Xpo Logistics) Start Date:2007-01-03
XPOF (Xponential Fitness) Start Date:2021-07-23
XPON (Expion360) Start Date:2022-04-01
XPRO (Expro Holdings N.V.) Start Date:2013-08-09
XRAY (Dentsply Sirona) Start Date:2005-01-03
XRTX (Xortx Therapeutics) Start Date:2021-10-13
XRX (Xerox) Start Date:2005-01-03
XSPA (Xpresspa) Start Date:2010-07-27
XTLB (Xtl Biopharmaceuticals American Depositary Shares) Start Date:2014-02-18
XTNT (Xtant Medical Holdings) Start Date:2015-10-19
XWEL (Xwell) Start Date:2010-07-27
XXII (22Nd Century) Start Date:2011-01-26
XYF (X Financial American Depositary Shares Each Representing Six Class A Ordinary Shares) Start Date:2018-09-19
XYL (Xylem) Start Date:2011-10-13
YALA (Yalla) Start Date:2020-09-30
YCBD (Cbdmd) Start Date:2017-11-17
YELL (Yellow) Start Date:2007-05-01
YELP (Yelp) Start Date:2012-03-02
YETI (Yeti Holdings) Start Date:2018-10-25
YEXT (Yext) Start Date:2017-04-13
YGF (Yangufang International Co., Ltd.) Start Date:2023-03-28
YGMZ (Mingzhu Logistics) Start Date:2020-11-02
YHGJ (Yunhong Green Cti Ltd.) Start Date:2007-05-16
YI (111 American Depositary Shares) Start Date:2018-09-12
YJ (Yunji ADS) Start Date:2019-05-03
YMAB (Y-Mabs Therapeutics) Start Date:2018-09-21
YMM (Full Truck Alliance Co.) Start Date:2021-06-22
YMTX (Yumanity Therapeutics) Start Date:2016-02-11
YORW (York Water) Start Date:2007-05-16
YOSH (Yoshiharu Global Co.) Start Date:2022-09-09
YOTA (Yotta Acquisition Corporation) Start Date:2022-06-27
YOU (Clear Secure) Start Date:2021-06-30
YPF (Ypf Sociedad Anonima) Start Date:2013-02-11
YQ (17 Education & Technology) Start Date:2020-12-04
YRD (Yiren Digital American Depositary Shares Each Representing Two Ordinary Shares) Start Date:2015-12-18
YSG (Yatsen Holding) Start Date:2020-11-19
YTEN (Yield10 Bioscience) Start Date:2007-05-10
YTRA (Yatra Online, Ordinary Shares) Start Date:2016-12-19
YUM (Yum! Brands Inc) Start Date:2005-01-03
YUMC (Yum China Holdings) Start Date:2016-10-31
YVR (Liquid Media Common Shares) Start Date:2018-08-13
YY (Joyy) Start Date:2012-11-21
Z (Zillow) Start Date:2015-08-03
ZAPP (Zapp Electric Vehicles Ltd.) Start Date:2021-11-05
ZBH (Zimmer Biomet Holdings) Start Date:2007-04-30
ZBRA (Zebra Technologies) Start Date:2005-01-03
ZCMD (Zhongchao) Start Date:2020-02-24
ZD (Ziff Davis,) Start Date:2007-04-30
ZDGE (Zedge Class B) Start Date:2016-05-26
ZENV (Zenvia) Start Date:2021-07-22
ZEPP (Zepp Health American Depositary Shares) Start Date:2018-02-08
ZETA (Zeta Global Holdings) Start Date:2021-06-10
ZEUS (Olympic Steel) Start Date:2007-04-26
ZEVY (Lightning Emotors Inc) Start Date:2020-07-02
ZFOX (Zerofox Holdings) Start Date:2022-08-04
ZG (Zillow) Start Date:2011-07-20
ZGN (Ermenegildo Zegna N.V. Ordinary Shares) Start Date:2021-12-20
ZH (Zhihu) Start Date:2021-03-26
ZI (Zoominfo Technologies) Start Date:2020-06-04
ZIM (Zim Integrated Shipping Services) Start Date:2021-01-28
ZIMV (Zimvie) Start Date:2022-02-24
ZION (Zions Bancorp) Start Date:2005-01-03
ZIONO (Zions Bancorporation N.A. Dep Shs Repstg 1/40Th Perp Pfd Ser G) Start Date:2020-01-02
ZIONP (Zions Bancorporation N.A. Depositary Shares) Start Date:2020-01-02
ZIP (Ziprecruiter) Start Date:2021-05-26
ZIVO (Zivo Bioscience) Start Date:2021-05-28
ZIVOW (Zivo Bioscience Warrants) Start Date:2021-05-28
ZJYL (Jin Medical International Ltd.) Start Date:2023-03-28
ZKH (Zkh Limited) Start Date:2023-12-15
ZKIN (Zk International Co. Ordinary Share) Start Date:2017-09-01
ZLAB (Zai Lab Limited) Start Date:2017-09-20
ZM (Zoom) Start Date:2019-04-18
ZNTL (Zentalis Pharmaceuticals) Start Date:2020-04-03
ZOM (Zomedica) Start Date:2016-07-29
ZS (Zscaler) Start Date:2018-03-16
ZTEK (Zentek) Start Date:2022-03-22
ZTO (Zto Express) Start Date:2016-10-27
ZTR (Virtus Total Return Fund) Start Date:2007-05-08
ZTS (Zoetis) Start Date:2013-02-01
ZUMZ (Zumiez) Start Date:2007-04-27
ZUO (Zuora) Start Date:2018-04-12
ZVIA (Zevia) Start Date:2021-07-22
ZVRA (Zevra Therapeutics Inc) Start Date:2021-01-08
ZVSA (Zyversa Therapeutics) Start Date:2022-02-10
ZWS (Zurn Water Solutions Corporation) Start Date:2012-03-29
ZYME (Zymeworks) Start Date:2017-04-28
ZYNE (Zynerba Pharmaceuticals) Start Date:2015-08-05
ZYXI (Zynex) Start Date:2008-07-08
AABA-DELISTED () Start Date:2007-04-27
AATC-DELISTED (Autoscope Technologies) Start Date:2021-07-21
AAWW-DELISTED (Atlas Air Worldwide) Start Date:2007-04-25
ABI-DELISTED (Safety First Trust Series 2009-) Start Date:2007-04-30
ABK-DELISTED (Ambac Financial Inc) Start Date:2004-01-02
ABMD-DELISTED (Abiomed Inc) Start Date:2005-01-03
ABS-DELISTED (Albertsons) Start Date:2004-01-02
ABST-DELISTED (Absolute Software) Start Date:2020-11-02
ABTX-DELISTED (Allegiance Bancshares) Start Date:2015-10-08
ACAS-DELISTED (American Capital) Start Date:2004-01-02
ACBI-DELISTED (Atlantic Capital Bancshares) Start Date:2015-11-02
ACC-DELISTED (American Campus Communities) Start Date:2007-01-03
ACGN-DELISTED (Aceragen) Start Date:2007-12-10
ACII-DELISTED (Atlas Crest Investment Ii Class A) Start Date:2021-03-29
ACQR-DELISTED (Independence Holdings) Start Date:2021-05-19
ACTD-DELISTED (Arclight Clean Transition Ii Class A Ordinary Share) Start Date:2021-05-24
ACTDU-DELISTED (Arclight Clean Transition Ii Unit) Start Date:2021-03-23
ACTDW-DELISTED (Arclight Clean Transition Ii Warrant) Start Date:2021-05-21
ACXM-DELISTED (Acxiom Holdings) Start Date:2004-01-02
ADF-DELISTED (Aldel Financial) Start Date:2007-06-04
ADGI-DELISTED (Adagio Therapeutics) Start Date:2021-08-06
ADS-DELISTED (Alliance Data Systems) Start Date:2005-01-03
AERI-DELISTED (Aerie Pharmaceuticals Co) Start Date:2013-10-25
AET-DELISTED (Aetna) Start Date:2004-01-02
AFIN-DELISTED (American Finance Trust) Start Date:2018-07-19
AGCB-DELISTED (Altimeter Growth 2) Start Date:2021-01-07
AGFS-DELISTED (Agrofresh Solutions) Start Date:2014-04-24
AGGR-DELISTED (Agile Growth Class A Ordinary Share) Start Date:2021-05-19
AGTC-DELISTED (Applied Genetic Technologies C) Start Date:2014-03-27
AIMAU-DELISTED (Aimfinity Investment I Unit) Start Date:2022-04-26
AIMC-DELISTED (Altra Industrial Motion) Start Date:2007-01-03
AINV-DELISTED (Apollo Investment Corp) Start Date:2005-01-03
AJRD-DELISTED (Aerojet Rocketdyne Holdings) Start Date:2007-04-26
AKUS-DELISTED (Akouos) Start Date:2020-06-26
ALBO-DELISTED (Albireo Pharma) Start Date:2007-05-16
ALFIQ-DELISTED (Alfi Inc) Start Date:2021-05-04
ALJJ-DELISTED (Alj Regional Holdings) Start Date:2007-05-16
ALNA-DELISTED (Allena Pharmaceuticals) Start Date:2017-11-02
ALR-DELISTED (Alerislife) Start Date:2017-07-03
ALSK-DELISTED (Alaska Comm Sys) Start Date:2007-05-01
ALXN-DELISTED (Alexion Pharmaceuticals) Start Date:2005-01-03
AMLN-DELISTED (Amylin Pharmaceuticals) Start Date:2004-01-02
AMOV-DELISTED (America Movil S.A.B. De C.V. Class A American Depositary Shares) Start Date:2007-05-16
AMPI-DELISTED (Advanced Merger Partners Class A) Start Date:2021-04-22
AMTBB-DELISTED (Amerant Bancorp Class B) Start Date:2018-08-29
AMYT-DELISTED (Amryt Pharma Plc American Depositary Shares) Start Date:2020-07-08
ANAT-DELISTED (American National) Start Date:2007-05-16
ANDV-DELISTED (Andeavor) Start Date:2007-04-30
ANR-DELISTED (Alpha Natural Resources C) Start Date:2005-02-15
ANTM-DELISTED (Anthem) Start Date:2007-04-30
APC-DELISTED (Anadarko Petroleum Corp) Start Date:2004-01-02
APEN-DELISTED (Apollo Endosurgery) Start Date:2007-05-16
APGN-DELISTED (Apexigen) Start Date:2021-02-22
APNC-DELISTED (Apeiron Capital Investment Corp) Start Date:2021-12-30
APOL-DELISTED (Apollo Education) Start Date:2004-01-02
APR-DELISTED (Apria) Start Date:2021-02-11
APTS-DELISTED (Preferred Apartment) Start Date:2011-04-01
APTX-DELISTED (Aptinyx) Start Date:2018-06-21
AQUA-DELISTED (Evoqua Water Technologies) Start Date:2017-11-02
ARCK-DELISTED (Arbor Rapha Capital Bioholdings I Class A) Start Date:2021-12-20
ARCP-DELISTED (Vereit) Start Date:2011-09-07
ARD-DELISTED (Ardagh S.A.) Start Date:2017-03-15
ARDS-DELISTED (Aridis Pharmaceuticals) Start Date:2018-08-14
ARG-DELISTED (Airgas) Start Date:2004-01-02
ARGU-DELISTED (Argus Capital Class A) Start Date:2021-11-15
ARNA-DELISTED (Arena Pharmaceuticals) Start Date:2007-01-03
ARNC-DELISTED (Arconic) Start Date:2020-04-01
ASAP-DELISTED (Waitr Holdings Inc) Start Date:2016-05-26
ASBC-DELISTED (Associated Banc-Corp) Start Date:2004-01-02
ASPL-DELISTED (Aspirational Consumer Lifestyle) Start Date:2020-11-13
ASPU-DELISTED (Aspen) Start Date:2011-06-30
ATC-DELISTED (Atotech) Start Date:2021-02-04
ATCO-DELISTED (Atlas) Start Date:2007-05-07
ATCX-DELISTED (Atlas Technical Consultants Class A) Start Date:2018-11-16
ATH-DELISTED (Athene Holding Ltd.) Start Date:2016-12-09
ATRS-DELISTED (Antares Pharma) Start Date:2007-05-16
ATVC-DELISTED (Tribe Capital Growth I Class A) Start Date:2021-05-26
ATVCU-DELISTED (Tribe Capital Growth I Units) Start Date:2021-03-05
ATVCW-DELISTED (Tribe Capital Growth I Warrant) Start Date:2021-05-19
AUDA-DELISTED (Audacy Inc) Start Date:2007-04-27
AUTO-DELISTED (Autoweb) Start Date:2007-05-08
AUY-DELISTED (Yamana Gold) Start Date:2007-06-12
AV-DELISTED (Aviva Plc Unsponsored ADR) Start Date:2009-10-20
AVEO-DELISTED (Aveo Pharmaceuticals) Start Date:2010-03-12
AVLR-DELISTED (Avalara) Start Date:2018-06-15
AVP-DELISTED (Avon Products) Start Date:2004-01-02
AXHI-DELISTED (Industrial Human Capital Inc) Start Date:2021-12-10
AXU-DELISTED (Alexco Resource Common Shares) Start Date:2007-09-20
AYLA-DELISTED (Ayala Pharmaceuticals) Start Date:2020-05-08
AZRE-DELISTED (Azure Power Global Limited) Start Date:2016-10-12
BBI-DELISTED (Brickell Biotech) Start Date:2007-05-01
BBIG-DELISTED (Vinco Ventures) Start Date:2018-05-03
BBQ-DELISTED (Bbq Holdings) Start Date:2007-05-16
BBT-DELISTED (Bb&T Corporation) Start Date:2004-01-02
BCEI-DELISTED (Bonanza Creek Energy) Start Date:2011-12-15
BCR-DELISTED (C.R. Bard) Start Date:2004-01-02
BDSI-DELISTED (Biodelivery Sciences) Start Date:2007-05-16
BDXB-DELISTED (Becton Dickinson And Company Depositary Shares Each Representing A 1/20Th Interest In A Share Of 6.00% Mandatory Convertible Preferred Stock Series B) Start Date:2020-06-03
BEAM-DELISTED () Start Date:2007-05-01
BGRY-DELISTED (Berkshire Grey) Start Date:2021-02-11
BHGE-DELISTED (Baker Hughes) Start Date:2017-07-05
BHI-DELISTED (Baker Hughes Incorporated Commo) Start Date:2004-01-02
BKEP-DELISTED (Blueknight Energy Partners L.P. Common Units) Start Date:2010-11-01
BKEPP-DELISTED (Blueknight Energy Partners L.P. Series A Preferred Units) Start Date:2011-11-10
BLCM-DELISTED (Bellicum Pharmaceuticals) Start Date:2014-12-18
BLCT-DELISTED (Bluecity Holdings) Start Date:2020-07-08
BLU-DELISTED (Bellus Health) Start Date:2007-05-16
BMC-DELISTED (Bmc Software) Start Date:2004-01-02
BMS-DELISTED (Bemis Company Common Stoc) Start Date:2004-01-02
BMTC-DELISTED (Bryn Mawr Bank) Start Date:2007-05-16
BNFT-DELISTED (Benefitfocus) Start Date:2013-09-18
BOCH-DELISTED (Bank Of Commerce) Start Date:2007-05-16
BOMN-DELISTED (Boston Omaha) Start Date:2016-09-06
BPFH-DELISTED (Boston Private Financial) Start Date:2007-05-08
BPMP-DELISTED (Bp Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2017-10-26
BPY-DELISTED (Brookfield Property Partners L.P.) Start Date:2013-03-22
BPYU-DELISTED (Brookfield Property Reit) Start Date:2018-08-28
BRCM-DELISTED (Broadcom) Start Date:2004-01-02
BRCN-DELISTED (Burcon Nutrascience) Start Date:2021-05-25
BRG-DELISTED (Bluerock Residential Growth) Start Date:2014-03-28
BRKS-DELISTED (Brooks Automation) Start Date:2007-01-03
BRMK-DELISTED (Broadmark Realty Capital) Start Date:2019-11-15
BRPM-DELISTED (B. Riley Principal 150 Merger Class A) Start Date:2021-04-13
BRPMU-DELISTED (B. Riley Principal 150 Merger Unit) Start Date:2021-02-19
BRPMW-DELISTED (B. Riley Principal 150 Merger Warrant) Start Date:2021-04-13
BSKY-DELISTED (Big Sky Growth Partners Class A) Start Date:2021-07-01
BSMX-DELISTED (Banco Santander Mexico S.A. Institucion De Banca Multiple Grupo Financiero Santander Mexico) Start Date:2012-09-26
BTRS-DELISTED (Btrs Holdings Class 1) Start Date:2019-08-06
BWC-DELISTED (Bwx Technologies) Start Date:2005-11-01
BXLT-DELISTED () Start Date:2015-06-15
BXS-DELISTED (Bancorpsouth Bank) Start Date:2017-11-07
CA-DELISTED (Ca Technologies) Start Date:2004-01-02
CAI-DELISTED (Cai International) Start Date:2007-05-16
CAJPY-DELISTED (Canon Inc) Start Date:2007-01-03
CAM-DELISTED (Cameron International Corporati) Start Date:2004-01-02
CATB-DELISTED (Catabasis Pharmaceuticals) Start Date:2015-06-25
CBB-DELISTED (Cincinnati Bell) Start Date:2012-12-20
CBE-DELISTED (Cooper Industries Plc) Start Date:2004-01-02
CBG-DELISTED (Cbre Inc Cla) Start Date:2004-07-01
CBRGU-DELISTED (Chain Bridge I Units) Start Date:2021-11-10
CCE-DELISTED (Coca-Cola Enterprises Com) Start Date:2004-01-02
CCIV-DELISTED (Churchill Capital Iv) Start Date:2020-09-18
CCMP-DELISTED (Cmc Materials) Start Date:2007-04-26
CCXI-DELISTED (Chemocentryx) Start Date:2012-02-08
CDEV-DELISTED (Centennial Resource Development, Class A Business Combination) Start Date:2016-04-15
CDK-DELISTED (Cdk Global) Start Date:2014-09-22
CDR-DELISTED (Cedar Realty Trust) Start Date:2007-04-26
CEAYY-DELISTED (China Eastern Airlines Ltd.) Start Date:2007-05-16
CEG-DELISTED (Constellation Energy Inc) Start Date:2004-01-02
CELG-DELISTED (Celgene) Start Date:2004-01-02
CEMI-DELISTED (Chembio Diagnostics) Start Date:2007-05-16
CERC-DELISTED (Cerecor) Start Date:2015-11-13
CERN-DELISTED (Cerner) Start Date:2005-01-03
CFN-DELISTED (Carefusion Common S) Start Date:2009-09-01
CFX-DELISTED (Colfax Corporation) Start Date:2008-05-08
CHMA-DELISTED (Chiasma) Start Date:2015-07-16
CHNG-DELISTED (Change Healthcare) Start Date:2019-06-27
CHNGU-DELISTED (Change Healthcare Tangible Equity Units) Start Date:2019-06-27
CHRA-DELISTED (Charah Solutions) Start Date:2018-06-14
CIH-DELISTED (China Index Holdings ADS) Start Date:2019-06-12
CINC-DELISTED (Cincor Pharma) Start Date:2022-01-07
CIT-DELISTED (Cit Inc) Start Date:2009-12-10
CLAS-DELISTED (Class Acceleration) Start Date:2021-03-08
CLBS-DELISTED (Caladrius Biosciences) Start Date:2007-08-09
CLDR-DELISTED (Cloudera) Start Date:2017-04-28
CLI-DELISTED (Mack-Cali Realty) Start Date:2007-04-27
CLOEU-DELISTED (Clover Leaf Capital Unit) Start Date:2021-07-20
CLR-DELISTED (Continental Resources) Start Date:2007-05-15
CLSN-DELISTED (Celsion) Start Date:2008-06-30
CMCSK-DELISTED (Comcast Corporation) Start Date:2004-01-02
CMO-DELISTED (Capstead Mortgage) Start Date:2007-05-07
CMPI-DELISTED (Checkmate Pharmaceuticals) Start Date:2020-08-07
CNBKA-DELISTED (Century Bancorp) Start Date:2007-05-16
CNCE-DELISTED (Concert Pharmaceuticals) Start Date:2014-02-13
CNNB-DELISTED (Cincinnati Bancorp) Start Date:2015-10-15
CNR-DELISTED (Cornerstone Building Brands) Start Date:2007-04-27
CNST-DELISTED (Constellation Pharmaceuticals) Start Date:2018-07-19
CNVY-DELISTED (Convey Holding Parent) Start Date:2021-06-16
CO-DELISTED (Global Cord Blood) Start Date:2009-11-19
COG-DELISTED (Cabot Oil & Gas) Start Date:2004-01-02
COH-DELISTED (Coach) Start Date:2004-01-02
COHR-DELISTED (Coherent) Start Date:2007-04-27
COL-DELISTED (Rockwell Collins Common S) Start Date:2004-01-02
COLI-DELISTED (Colicity) Start Date:2021-04-16
CONE-DELISTED (Cyrusone) Start Date:2013-01-18
COR-DELISTED (Coresite Realty Corporation) Start Date:2007-05-02
CORE-DELISTED (Core Mark Holding Co) Start Date:2017-01-26
CORS-DELISTED (Corsair Partnering) Start Date:2021-08-24
COUP-DELISTED (Coupa Software Incorporated) Start Date:2016-10-06
COV-DELISTED (Covidien Plc. Ordinary Shares) Start Date:2007-07-02
COWN-DELISTED (Cowen) Start Date:2007-05-03
CPGX-DELISTED () Start Date:2015-06-17
CPL-DELISTED (Carolina Power & Light) Start Date:2004-10-01
CPLG-DELISTED (Corepoint Lodging) Start Date:2018-05-31
CREE-DELISTED (Cree) Start Date:2007-01-03
CRTD-DELISTED (Creatd) Start Date:2020-09-11
CRTX-DELISTED (Cortexyme) Start Date:2019-05-09
CRXT-DELISTED (Clarus Therapeutics Holdings) Start Date:2021-09-07
CRY-DELISTED (Cryolife) Start Date:2007-05-10
CRZN-DELISTED (Corazon Capital V838 Monoceros Class A Ordinary Shares) Start Date:2021-06-11
CRZWQ-DELISTED (Core Scientific Inc) Start Date:2021-04-08
CSC-DELISTED (Computer Sciences C) Start Date:2004-01-02
CS-DELISTED (Credit Suisse Ag) Start Date:2007-01-03
CSII-DELISTED (Cardiovascular Systems) Start Date:2009-02-26
CSOD-DELISTED (Cornerstone Ondemand) Start Date:2011-03-17
CSPR-DELISTED (Casper) Start Date:2020-02-06
CSRA-DELISTED () Start Date:2015-11-16
CTEK-DELISTED (Cynergistek) Start Date:2017-02-14
CTIC-DELISTED (Cti Biopharma) Start Date:2007-05-14
CTRP-DELISTED (Ctrip.com International Ltd.) Start Date:2004-01-02
CTRX-DELISTED (Catamaran Corporation) Start Date:2006-06-23
CTT-DELISTED (Catchmark Timber Trust) Start Date:2013-12-12
CTX-DELISTED (Centex Corp) Start Date:2007-04-30
CTXRW-DELISTED (Citius Pharmaceuticals Warrant) Start Date:2017-08-03
CTXS-DELISTED (Citrix Systems) Start Date:2004-01-02
CU-DELISTED (Cuc International) Start Date:2004-01-02
CVA-DELISTED (Covanta Holding) Start Date:2007-05-02
CVC-DELISTED (Cablevision Systems Corporation) Start Date:2004-01-02
CVET-DELISTED (Covetrus) Start Date:2019-02-05
CVG-DELISTED (Convergys Common St) Start Date:2004-01-02
CVH-DELISTED (Coventry Health Care Comm) Start Date:2004-01-02
CVT-DELISTED (Cvent Holding) Start Date:2020-11-17
CXP-DELISTED (Columbia Property Trust) Start Date:2007-05-16
CYBE-DELISTED (Cyberoptics) Start Date:2007-05-16
DBDQQ-DELISTED (Diebold Nixdorf Inc) Start Date:2007-04-30
DCGOW-DELISTED (Docgo Warrants) Start Date:2020-12-17
DCP-DELISTED (Dcp Midstream Lp) Start Date:2007-05-09
DCT-DELISTED (Duck Creek Technologies) Start Date:2020-08-14
DCUE-DELISTED (Dominion Energy 2019 Series A Corporate Units) Start Date:2019-06-19
DDR-DELISTED (Ddr) Start Date:2004-01-02
DEH-DELISTED (D8 Holdings) Start Date:2020-09-04
DF-DELISTED (Dean Foods Company) Start Date:2004-01-02
DGNU-DELISTED (Dragoneer Growth Opportunities Iii Class A Ordinary Shares) Start Date:2021-03-23
DHBC-DELISTED (Dhb Capital Class A) Start Date:2021-04-23
DICE-DELISTED (Dice Therapeutics) Start Date:2021-09-15
DIDI-DELISTED (Xiaoju Kuaizhi) Start Date:2021-06-30
DISCA-DELISTED (Discovery Class A) Start Date:2007-05-02
DISCB-DELISTED (Discovery, Series B) Start Date:2007-05-16
DISCK-DELISTED (Discovery Class C) Start Date:2008-09-18
DMYQ-DELISTED (Dmy Technology , Iv) Start Date:2021-04-26
DMYS-DELISTED (Dmy Technology  Vi Class A) Start Date:2021-11-22
DNAA-DELISTED (Social Capital Suvretta Holdings I Class A Ordinary Share) Start Date:2021-06-30
DNAC-DELISTED (Social Capital Suvretta Holdings Iii Class A Ordinary Shares) Start Date:2021-06-30
DPS-DELISTED (Dr Pepper Snapple Inc Dr) Start Date:2008-05-07
DRE-DELISTED (Duke Realty Corp) Start Date:2005-01-03
DRNA-DELISTED (Dicerna Pharmaceuticals) Start Date:2014-01-30
DSEY-DELISTED (Diversey) Start Date:2021-03-25
DSPG-DELISTED (Dsp) Start Date:2007-05-02
DSSI-DELISTED (Diamond S Shipping) Start Date:2019-03-28
DV-DELISTED (Devry) Start Date:2004-01-02
DWDP-DELISTED (Dowdupont) Start Date:2007-04-27
DYFN-DELISTED (Angel Oak Dynamic Financial Strategies Income Term Trust Common Shares Of Beneficial Interest) Start Date:2020-06-26
DYN-DELISTED () Start Date:2012-10-03
DYNS-DELISTED (Dynamics Special Purpose) Start Date:2021-05-26
EBSB-DELISTED (Meridian Bancorp Common) Start Date:2008-01-23
ECHO-DELISTED (Echo Global Logistics) Start Date:2009-10-02
ECOL-DELISTED (Us Ecology) Start Date:2011-04-19
ECOM-DELISTED (Channeladvisor) Start Date:2013-05-23
EDS-DELISTED (Exceed Company Ltd.) Start Date:2007-04-30
ELMS-DELISTED (Electric Last Mile Solutions, Class A) Start Date:2020-09-21
ELVT-DELISTED (Elevate Credit) Start Date:2017-04-06
ELY-DELISTED (Callaway Golf) Start Date:2007-05-01
EMBK-DELISTED (Embark Technology) Start Date:2021-11-11
EMC-DELISTED (Emc) Start Date:2004-01-02
EMCF-DELISTED (Emclaire Financial) Start Date:2007-05-21
EMWP-DELISTED (Eros Media World Plc A Ordinary Shares Gbp 0.30 Par Value) Start Date:2013-11-13
ENBL-DELISTED (Enable Midstream Partners Lp) Start Date:2014-04-11
ENDP-DELISTED (Endo International Plc) Start Date:2014-03-03
ENFA-DELISTED (890 5Th Avenue Partners) Start Date:2021-03-05
ENIA-DELISTED (Enel Americas S.A.) Start Date:2007-05-01
ENJY-DELISTED (Enjoy Technology) Start Date:2021-10-13
ENJYW-DELISTED (Enjoy Technology Warrant) Start Date:2021-02-04
EOCW-DELISTED (Elliott Opportunity Ii Class A Ordinary Shares) Start Date:2021-08-19
EPAY-DELISTED (Bottomline Technologies) Start Date:2007-05-09
EP-DELISTED (El Paso Common Stoc) Start Date:2004-01-02
EPWR-DELISTED (Empowerment & Inclusion Capital I Class A) Start Date:2021-03-01
EPZM-DELISTED (Epizyme) Start Date:2013-05-31
ESRX-DELISTED (Express Scripts Holding Company) Start Date:2004-01-02
ESV-DELISTED (Ensco Plc American Depositary S) Start Date:2004-01-02
ESXB-DELISTED (Community Bankers Trust Corpor) Start Date:2007-05-16
ETH-DELISTED (Ethan Allen Interiors) Start Date:2007-04-26
ETTX-DELISTED (Entasis Therapeutics Holdings) Start Date:2018-09-26
EVHC-DELISTED () Start Date:2013-08-14
EVKG-DELISTED (Ever-Glory International Inc) Start Date:2008-07-16
EVOP-DELISTED (Evo Payments) Start Date:2018-05-23
EXTN-DELISTED (Exterran Corp) Start Date:2015-11-04
EYES-DELISTED (Second Sight Medical Products) Start Date:2014-11-19
EYESW-DELISTED (Second Sight Medical Products Warrants Expiring 03/14/2024) Start Date:2017-03-29
FBC-DELISTED (Flagstar Bancorp) Start Date:2007-05-02
FCBP-DELISTED (First Choice Bancorp) Start Date:2007-05-02
FCCY-DELISTED (1St Constitution) Start Date:2007-05-16
FCRD-DELISTED (First Eagle Alternative Capital Bdc) Start Date:2010-04-22
FDC-DELISTED (First Data Corp) Start Date:2004-01-02
FDO-DELISTED (Family Dollar Stores Comm) Start Date:2004-01-02
FEXDU-DELISTED (Fintech Ecosystem Development Units) Start Date:2021-10-19
FEYE-DELISTED (Fireeye) Start Date:2013-09-20
FFBW-DELISTED (Ffbw) Start Date:2017-10-11
FHSEY-DELISTED (First High-School Education Co Ltd.) Start Date:2021-03-11
FI-DELISTED (Franks International) Start Date:2013-08-09
FII-DELISTED (Federated Investors) Start Date:2004-01-02
FINM-DELISTED (Marlin Technology) Start Date:2021-03-09
FLDM-DELISTED (Fluidigm) Start Date:2011-02-10
FLMN-DELISTED (Falcon Minerals) Start Date:2017-09-08
FLOW-DELISTED (Spx Flow) Start Date:2015-09-28
FLXN-DELISTED (Flexion Therapeutics Com) Start Date:2014-02-12
FMBI-DELISTED (First Midwest Bancorp) Start Date:2007-05-04
FMIV-DELISTED (Forum Merger Iv Class A) Start Date:2021-06-07
FMTX-DELISTED (Forma Therapeutics) Start Date:2020-06-19
FNHC-DELISTED (Federated National) Start Date:2007-05-10
FOE-DELISTED (Ferro) Start Date:2007-05-03
FORG-DELISTED (Forgerock,) Start Date:2021-09-16
FRBK-DELISTED (Republic First Bancorp) Start Date:2007-05-16
FRG-DELISTED (Franchise) Start Date:2018-08-02
FRSG-DELISTED (First Reserve Sustainable Growth Class A) Start Date:2021-04-29
FRTA-DELISTED (Forterra) Start Date:2016-10-20
FRX-DELISTED (Forest Laboratories Class) Start Date:2004-01-02
FSSI-DELISTED (Fortistar Sustainable Solutions) Start Date:2021-03-22
FSTX-DELISTED (F-Star Therapeutics) Start Date:2016-05-06
FTRP-DELISTED (Field Trip Health Common Shares) Start Date:2021-07-29
FVE-DELISTED (Five Star Quality Care) Start Date:2007-05-03
FWLT-DELISTED (Foster Wheeler Ag) Start Date:2005-06-03
FWPAY-DELISTED (Forward Pharma A) Start Date:2014-10-15
GAMCU-DELISTED (Golden Arrow Merger Unit) Start Date:2021-03-17
GAMI-DELISTED (Gamco Investors Inc Et Al) Start Date:2007-05-16
GAS-DELISTED (Agl Resources Common Stoc) Start Date:2004-01-02
GBT-DELISTED (Global Blood Therapeutics) Start Date:2015-08-12
GCP-DELISTED (Gcp Applied Technologies) Start Date:2016-01-26
GDP-DELISTED (Goodrich Petroleum Corp) Start Date:2017-04-11
GET-DELISTED (Getnet Adquirencia E Servicos Para Meios De Pagamento S.A. American Depositary Shares) Start Date:2021-10-18
GFLU-DELISTED (Gfl Environmental Tangible Equity Units) Start Date:2020-03-03
GGMCW-DELISTED (Glenfarne Merger Warrant) Start Date:2021-05-18
GGP-DELISTED (General Growth Properties) Start Date:2004-01-02
GGPI-DELISTED (Gores Guggenheim) Start Date:2021-05-18
GIIX-DELISTED (Gores Holdings Viii Class A) Start Date:2021-04-26
GIW-DELISTED (Giginternational1) Start Date:2021-07-12
GLBLU-DELISTED (Cartesian Growth Unit) Start Date:2021-02-24
GLK-DELISTED (Great Lakes Chemical) Start Date:2006-06-01
GLOP-DELISTED (Gaslog Partners Lp Common Units Representing Partnership Interests) Start Date:2014-05-07
GLSH-DELISTED (Gelesis Holdings Inc) Start Date:2022-01-14
GMCR-DELISTED (Keurig Green Mountain) Start Date:2004-01-02
GNCMA-DELISTED (Gci Liberty) Start Date:2004-01-02
GNOG-DELISTED (Golden Nugget Online Gaming, Class A) Start Date:2020-12-15
GOED-DELISTED (1847 Goedeker) Start Date:2020-07-31
GPL-DELISTED (Great Panther Mining Ordinary Shares) Start Date:2008-10-27
GPX-DELISTED (Gp Strategies) Start Date:2007-05-16
GRA-DELISTED (W.R. Grace & Co.) Start Date:2005-01-03
GR-DELISTED (Goodrich Corporation) Start Date:2004-01-02
GRNA-DELISTED (Greenlight Biosciences Holdings Pbc) Start Date:2022-02-02
GRUB-DELISTED (Grubhub) Start Date:2021-06-15
GRVI-DELISTED (Grove) Start Date:2021-06-24
GSEV-DELISTED (Gores Holdings Vii, Class A) Start Date:2021-04-15
GSKY-DELISTED (Greensky) Start Date:2018-05-24
GSQB-DELISTED (G Squared Ascend Ii Class A Ordinary Shares) Start Date:2021-08-05
GSQD-DELISTED (G Squared Ascend I Class A Ordinary Shares) Start Date:2021-03-26
GSV-DELISTED (Gold Standard Ventures) Start Date:2010-02-03
GTPA-DELISTED (Gores Technology Partners) Start Date:2021-05-06
GTPB-DELISTED (Gores Technology Partners Ii Class A) Start Date:2021-05-05
GTS-DELISTED (Triple-S Management) Start Date:2007-12-07
GTT-DELISTED (Gtt Communications) Start Date:2013-06-17
GTYH-DELISTED (Gty Technology) Start Date:2016-11-18
GWB-DELISTED (Great Western Bancorp) Start Date:2014-10-15
GWGH-DELISTED (Gwg) Start Date:2014-09-25
HAR-DELISTED (Harman International Industries) Start Date:2004-01-02
HBHC-DELISTED (Hancock Holding) Start Date:2004-01-02
HBMD-DELISTED (Howard Bancorp Md) Start Date:2007-05-23
HCBK-DELISTED (Hudson City Bancorp) Start Date:2004-01-02
HCHC-DELISTED (Hc2) Start Date:2011-06-23
HCIC-DELISTED (Hennessy Capital Investment V Class A) Start Date:2021-03-08
HCII-DELISTED (Hudson Executive Investment Ii Class A) Start Date:2021-03-29
HCN-DELISTED (Health Care Reit Common S) Start Date:2004-01-02
HCP-DELISTED (Hcp) Start Date:2004-01-02
HEXO-DELISTED (Hexo Common Shares) Start Date:2019-01-22
HFC-DELISTED (Hollyfrontier Corp) Start Date:2007-04-27
HGEN-DELISTED (Humanigen,) Start Date:2016-01-13
HGH-DELISTED (Hartford Financial Services) Start Date:2012-04-25
HIII-DELISTED (Hudson Executive Investment Iii Class A) Start Date:2021-04-20
HIL-DELISTED (Hill International) Start Date:2008-02-22
HLAH-DELISTED (Hamilton Lane Alliance Holdings I Class A) Start Date:2021-03-18
HLG-DELISTED (Hailiang Education  American Depositary Shares) Start Date:2015-07-07
HLS-DELISTED (Hls Therapeutics) Start Date:2006-11-01
HMHC-DELISTED (Houghton Mifflin Harcourt Comp) Start Date:2013-11-14
HMLP-DELISTED (Hoegh Lng Partners Lp) Start Date:2014-08-07
HMPT-DELISTED (Home Point Capital Inc) Start Date:2021-01-29
HMT-DELISTED (Host Marriott Corp) Start Date:2004-01-02
HMTV-DELISTED (Hemisphere Media  C) Start Date:2013-04-05
HNGR-DELISTED (Hanger) Start Date:2007-05-11
HNZ-DELISTED (H.J. Heinz Company) Start Date:2004-01-02
HOME-DELISTED (At Home) Start Date:2007-06-04
HORI-DELISTED (Emerging Markets Horizon Class A Ordinary Shares) Start Date:2022-02-07
HOT-DELISTED (Starwood Hotels & Resorts World) Start Date:2004-01-02
HRC-DELISTED (Hill-Rom) Start Date:2008-04-01
HRS-DELISTED (Harris Corporation) Start Date:2004-01-02
HSH-DELISTED (Hillshire Brands Company) Start Date:2012-06-12
HSKA-DELISTED (Heska) Start Date:2007-05-16
HSP-DELISTED (Hospira Inc) Start Date:2004-05-03
HTA-DELISTED (Healthcare Trust Of America) Start Date:2012-06-06
HTPA-DELISTED (Highland Transcend Partners I Class A Ordinary Shares) Start Date:2021-01-25
HVBC-DELISTED (Hv Bancorp) Start Date:2017-01-12
HYRE-DELISTED (Hyrecar) Start Date:2018-06-27
HZN-DELISTED (Horizon Global Common Shares) Start Date:2015-06-23
IAA-DELISTED (Iaa) Start Date:2019-06-17
IBAAY-DELISTED (Industrias Bachoco Sab De Cv) Start Date:2007-05-16
IBER-DELISTED (Ibere Pharmaceuticals) Start Date:2021-04-20
ICBK-DELISTED (County Bancorp) Start Date:2015-01-16
IDBA-DELISTED (Idex Biometrics Asa American Depositary Shares) Start Date:2021-03-01
IDWM-DELISTED (Idw Media Holdings Inc) Start Date:2021-08-04
IEA-DELISTED (Infrastructure And Energy Alternatives) Start Date:2016-10-06
IHC-DELISTED (Independence Holding) Start Date:2007-05-16
IIN-DELISTED (Intricon) Start Date:2007-05-16
IIVI-DELISTED (Ii-Vi Incorporated) Start Date:2007-01-03
IMAC-DELISTED (Imac Holdings) Start Date:2019-02-13
IMGO-DELISTED (Imago Biosciences) Start Date:2021-07-16
IMPX-DELISTED (Aea-Bridges Impact Class A Ordinary Shares) Start Date:2020-12-15
IMVIQ-DELISTED (Imv Inc) Start Date:2018-06-01
INFO-DELISTED (Ihs Markit Ltd.) Start Date:2014-06-19
INOV-DELISTED (Inovalon Holdings) Start Date:2015-02-12
INS-DELISTED (Intelligent Systems) Start Date:2007-05-18
IPVI-DELISTED (Interprivate Iv Infratech Partners Class A) Start Date:2021-04-30
IRCP-DELISTED (Irsa Propiedades Comerciales S.A. American Depositary Shares) Start Date:2020-11-23
IRNT-DELISTED (Ironnet) Start Date:2020-03-23
ISAA-DELISTED (Iron Spark I Class A) Start Date:2021-06-09
ISBC-DELISTED (Investors Bancorp) Start Date:2007-01-03
IS-DELISTED (Ironsource Ltd.) Start Date:2021-06-29
ISEE-DELISTED (Iveric Bio) Start Date:2013-09-25
ISO-DELISTED (Isoplexis) Start Date:2021-10-08
IVCRQ-DELISTED (Invacare Corp) Start Date:2007-05-03
JCOM-DELISTED (J2 Global) Start Date:2007-01-03
JEC-DELISTED (Jacobs Engineering) Start Date:2004-01-02
JNCE-DELISTED (Jounce Therapeutics) Start Date:2017-01-27
JNS-DELISTED (Janus Capital Cmn S) Start Date:2004-01-02
JNY-DELISTED (Jones) Start Date:2004-01-02
JOBS-DELISTED (51Job American Depositary Shares) Start Date:2007-04-18
JOY-DELISTED (Joy Global) Start Date:2007-04-30
JOYG-DELISTED () Start Date:2004-01-02
JP-DELISTED (Jefferson-Pilot) Start Date:2015-07-16
JW.A-DELISTED (John Wiley & Sons) Start Date:2007-05-01
KALRQ-DELISTED (Kalera Public Co.) Start Date:2022-06-29
KBAL-DELISTED (Kimball International Cl) Start Date:2007-04-25
KDMN-DELISTED (Kadmon) Start Date:2016-07-27
KDNY-DELISTED (Chinook Therapeutics,) Start Date:2015-04-15
KFT-DELISTED (Kraft Foods) Start Date:2004-01-02
KIN-DELISTED (Kindred Biosciences Comm) Start Date:2013-12-12
KL-DELISTED (Kirkland Lake Gold Ltd.) Start Date:2017-08-16
KNL-DELISTED (Knoll) Start Date:2007-05-04
KOR-DELISTED (Corvus Gold Common Shares) Start Date:2010-09-02
KORS-DELISTED (Michael Kors Holdings O) Start Date:2011-12-15
KRA-DELISTED (Kraton Corp) Start Date:2009-12-17
KRFT-DELISTED (Kraft Foods) Start Date:2012-09-17
KSICW-DELISTED (Kadem Sustainable Impact Warrant) Start Date:2021-05-17
KSI-DELISTED (Kadem Sustainable Impact Class A) Start Date:2021-05-18
KSPN-DELISTED (Kaspien Holdings) Start Date:2007-05-04
KSU-DELISTED (Kansas City Southern) Start Date:2005-01-03
LAWS-DELISTED (Lawson Products) Start Date:2007-05-16
LB-DELISTED (L Brands) Start Date:2007-04-27
LBPSW-DELISTED (4D Pharma Plc Warrant) Start Date:2021-03-23
LDHA-DELISTED (Ldh Growth I Class A Ordinary Shares) Start Date:2021-05-13
LDL-DELISTED (Lydall) Start Date:2007-05-11
LEAP-DELISTED (Ribbit Leap) Start Date:2020-11-02
LEGA-DELISTED (Lead Edge Growth Opportunities Class A Ordinary Shares) Start Date:2021-05-26
LEH-DELISTED (Lehman Brothers) Start Date:2004-01-02
LEVL-DELISTED (Level One Bancorp) Start Date:2018-04-20
LFG-DELISTED (Archaea Energy) Start Date:2020-12-14
LHCG-DELISTED (Lhc) Start Date:2007-01-03
LITT-DELISTED (Logistics Innovation Technologies Class A) Start Date:2021-08-12
LIVX-DELISTED (Livexlive Media) Start Date:2017-12-14
LIZ-DELISTED (Liz Claiborne) Start Date:2004-01-02
LJPC-DELISTED (La Jolla Pharmaceutical Compan) Start Date:2007-05-14
LLL-DELISTED (L-3 Communications Holdings) Start Date:2007-04-30
LLNW-DELISTED (Limelight Networks) Start Date:2007-06-08
LLTC-DELISTED (Linear Technology Corporation) Start Date:2004-01-02
LMCA-DELISTED (Liberty Media Corporation) Start Date:2013-02-01
LMCK-DELISTED () Start Date:2014-08-08
LMNX-DELISTED (Luminex) Start Date:2007-04-25
LMST-DELISTED (Limestone Bancorp) Start Date:2007-05-16
LO-DELISTED (Lorillard Inc) Start Date:2008-06-10
LOGC-DELISTED (Logicbio Therapeutics) Start Date:2018-10-19
LORL-DELISTED (Loral Space) Start Date:2007-05-07
LOTZ-DELISTED (Carlotz Class A) Start Date:2019-05-09
LSI-DELISTED (Life Storage) Start Date:2016-08-15
LTCH-DELISTED (Latch,) Start Date:2020-12-31
LUK-DELISTED (Leucadia National C) Start Date:2004-01-02
LVLT-DELISTED (Level 3 Communications Co) Start Date:2004-01-02
LVNTA-DELISTED (Liberty Ventures) Start Date:2012-08-10
LVRA-DELISTED (Levere Holdings) Start Date:2021-05-14
LXK-DELISTED (Lexmark International Com) Start Date:2004-01-02
MACC-DELISTED (Mission Advancement) Start Date:2021-04-28
MANT-DELISTED (Mantech International) Start Date:2007-05-01
MBII-DELISTED (Marrone Bio Innovations) Start Date:2013-08-02
MBT-DELISTED (Mobile Telesystems Public Joint Stock Company) Start Date:2007-01-03
MCF-DELISTED (Contango Oil & Gas) Start Date:2007-05-11
MCFE-DELISTED (Mcafee) Start Date:2020-11-02
MDLA-DELISTED (Medallia) Start Date:2019-07-19
MDP-DELISTED (Meredith Corporation) Start Date:2005-01-03
MEKA-DELISTED (Meli Kaszek Pioneer Class A Ordinary Shares) Start Date:2021-09-29
MFCB-DELISTED () Start Date:2007-05-01
MFGP-DELISTED (Softwareinto Micro Focus) Start Date:2017-09-01
MFNC-DELISTED (Mackinac Financial) Start Date:2007-05-16
MGHL-DELISTED (Morgan Holding) Start Date:2007-05-16
MGI-DELISTED (Moneygram International) Start Date:2007-04-26
MGLN-DELISTED (Magellan Health) Start Date:2007-05-02
MGP-DELISTED (Mgm Growth Properties Llc) Start Date:2016-04-20
MHS-DELISTED (Medcohealth Solutions Inc Commo) Start Date:2004-01-02
MIC-DELISTED (Macquarie Infrastructure Corporation) Start Date:2007-01-03
MILE-DELISTED (Metromile,) Start Date:2020-11-09
MILEW-DELISTED (Metromile Warrant) Start Date:2020-11-20
MIME-DELISTED (Mimecast Limited) Start Date:2015-11-19
MITC-DELISTED (Meatech 3D American Depositary Shares) Start Date:2021-03-12
MIT-DELISTED (Mason Industrial Technology,) Start Date:2021-03-22
MITO-DELISTED (Stealth Biotherapeutics ADS) Start Date:2019-02-15
MJN-DELISTED (Mead Johnson Nutrition Company) Start Date:2009-02-11
MLHR-DELISTED (Herman Miller) Start Date:2007-04-30
MLVF-DELISTED (Malvern Bancorp) Start Date:2008-05-20
MMAC-DELISTED (Mma Capital Management Co) Start Date:2008-02-06
MMX-DELISTED (Maverix Metals Common Shares) Start Date:2019-06-25
MN-DELISTED (Manning & Napier Class A) Start Date:2011-11-18
MNDT-DELISTED (Mandiant,) Start Date:2013-09-20
MNR-DELISTED (Monmouth Real Estate) Start Date:2007-05-16
MNRL-DELISTED (Brigham Minerals) Start Date:2019-04-18
MNTV-DELISTED (Momentive Global) Start Date:2018-09-26
MOLX-DELISTED (Molex Incorporated) Start Date:2005-03-24
MON-DELISTED (Monsanto Company) Start Date:2004-01-02
MRLN-DELISTED (Marlin Business Services) Start Date:2007-05-11
MSGN-DELISTED (The Madison Square Garden Company) Start Date:2010-02-10
MSON-DELISTED (Misonix) Start Date:2007-05-16
MSP-DELISTED (Datto Holding) Start Date:2020-11-02
MSVB-DELISTED (Mid-Southern Bancorp) Start Date:2018-07-12
MTCR-DELISTED (Metacrine) Start Date:2020-09-16
MTOR-DELISTED (Meritor) Start Date:2007-04-30
MTVC-DELISTED (Motive Capital Ii Class A Ordinary Shares) Start Date:2022-01-27
MWV-DELISTED (Meadwestvaco Common) Start Date:2004-01-02
MWW-DELISTED (Monster Worldwide Common) Start Date:2007-04-27
MXIM-DELISTED (Maxim Integrated Products Inc) Start Date:2007-04-27
MYOV-DELISTED (Myovant Sciences Ltd.) Start Date:2016-10-27
NAKD-DELISTED (Naked Brand Ordinary Shares) Start Date:2018-06-20
NAV-DELISTED (Navistar International Corporation) Start Date:2008-06-30
NCBS-DELISTED (Nicolet Bankshares) Start Date:2013-05-17
NCR-DELISTED (Ncr Corporation) Start Date:2007-01-03
NESR-DELISTED (National Energy Services Reunited Ordinary S) Start Date:2017-06-05
NFH-DELISTED (New Frontier Health Ordinary Shares) Start Date:2018-06-28
NFX-DELISTED (Newfield Exploration Company Co) Start Date:2004-01-02
NHIC-DELISTED (Newhold Investment Ii Class A) Start Date:2021-12-28
NHIQ-DELISTED (Nanthealth Inc) Start Date:2016-06-02
NIHD-DELISTED (Nii Holdings) Start Date:2007-04-26
NLSN-DELISTED (Nielsen Holdings) Start Date:2015-08-31
NP-DELISTED (Neenah) Start Date:2007-04-25
NPTN-DELISTED (Neophotonics) Start Date:2011-02-02
NRZ-DELISTED (New Residential Investment) Start Date:2013-05-02
NSEC-DELISTED (National Security) Start Date:2007-05-16
NSM-DELISTED (National Semiconductor Corp) Start Date:2007-04-25
NSR-DELISTED (Nomad Royalty Company Common Shares) Start Date:2021-08-31
NTP-DELISTED (Nam Tai Property) Start Date:2007-05-04
NTUS-DELISTED (Natus Medical) Start Date:2007-05-09
NU (Northeast Utilities Common Stoc) Start Date:2021-12-09
NUAN-DELISTED (Nuance Communications) Start Date:2007-01-03
NUBIW-DELISTED (Nubia Brand International Warrant) Start Date:2022-05-02
NVCN-DELISTED (Neovasc Common Shares) Start Date:2008-12-22
NYX-DELISTED (Nyse Euronext) Start Date:2006-03-08
OAS-DELISTED (Oasis Petroleum) Start Date:2020-11-20
OBCI-DELISTED (Ocean Bio-Chem) Start Date:2007-04-13
OCDX-DELISTED (Ortho Clinical Diagnostics Plc) Start Date:2021-01-28
ODT-DELISTED (Odonate Therapeutics) Start Date:2017-12-07
OEG-DELISTED (Orbital Energy) Start Date:2008-01-07
OEPW-DELISTED (One Equity Partners Open Water I Class A) Start Date:2021-03-18
OFED-DELISTED (Oconee Federal Financial) Start Date:2011-01-14
OGBLY-DELISTED (Onion Global Ltd.) Start Date:2021-05-07
OIIM-DELISTED (O2micro International American Depositary Shares) Start Date:2007-05-03
OMP-DELISTED (Oasis Midstream Partners Lp Common Units Representing Partner Interests) Start Date:2017-09-21
ONCR-DELISTED (Oncorus) Start Date:2020-10-02
ONE-DELISTED (Bank One) Start Date:2018-03-28
ONEM-DELISTED (1Life Healthcare) Start Date:2020-01-31
ONNN-DELISTED (On Semiconductor) Start Date:2004-01-02
OPNT-DELISTED (Opiant Pharmaceuticals) Start Date:2009-12-02
ORBC-DELISTED (Orbcomm) Start Date:2007-05-07
ORIA-DELISTED (Orion Biotech Opportunities Class A Ordinary Share) Start Date:2021-07-13
ORPH-DELISTED (Orphazyme A/S) Start Date:2020-09-29
OSH-DELISTED (Oak Street Health) Start Date:2020-08-06
OSMT-DELISTED (Osmotica Pharmaceuticals) Start Date:2018-10-18
OTIC-DELISTED (Otonomy) Start Date:2014-08-13
OYST-DELISTED (Oyster Point Pharma) Start Date:2019-10-31
OZON-DELISTED (Ozon Plc) Start Date:2020-11-24
OZRK-DELISTED (Bank Ozk) Start Date:2004-01-02
PAE-DELISTED (Pae) Start Date:2018-09-07
PAYA-DELISTED (Paya Holdings Class A) Start Date:2020-10-19
PBCT-DELISTED (People's United Financial) Start Date:2007-03-29
PBCTP-DELISTED (People's United Financial Perpetual Preferred Series A Fixed-To-Floating Rate) Start Date:2016-11-29
PBFX-DELISTED (Pbf Logistics Lp) Start Date:2014-05-09
PBIP-DELISTED (Prudential Bancorp Commo) Start Date:2007-05-16
PCGU-DELISTED (Pacific Gas & Electric Co. Equity Unit) Start Date:2020-07-07
PCI-DELISTED (Pimco Dynamic Credit And Mortgage Income Fund) Start Date:2013-01-29
PCL-DELISTED (Plum Creek Timber Company) Start Date:2004-01-02
PCLN-DELISTED (The Priceline) Start Date:2004-01-02
PCOM-DELISTED (Points.com Common Shares) Start Date:2007-05-16
PCPC-DELISTED (Periphas Capital Partnering Class A) Start Date:2021-02-02
PCP-DELISTED (Precision Castparts Corporation) Start Date:2004-01-02
PCSB-DELISTED (Pcsb Financial) Start Date:2017-04-21
PDCE-DELISTED (Pdc Energy) Start Date:2007-04-27
PETM-DELISTED (Petsmart Inc) Start Date:2004-01-02
PFBI-DELISTED (Premier Financial) Start Date:2007-05-17
PFHD-DELISTED (Professional Hldg Corp) Start Date:2017-03-15
PFPT-DELISTED (Proofpoint) Start Date:2012-04-20
PGN-DELISTED (Progress Energy Common St) Start Date:2014-09-02
PHIC-DELISTED (Population Health Investment Co. Class A Ordinary Share) Start Date:2021-01-12
PICC-DELISTED (Pivotal Investment Iii Class A) Start Date:2021-04-01
PING-DELISTED (Ping Identity Holding) Start Date:2019-09-19
PLAN-DELISTED (Anaplan) Start Date:2018-10-12
PME-DELISTED (Pingtan Marine Enterprise Ltd.) Start Date:2013-02-26
PMTC-DELISTED (Parametric Technology) Start Date:2006-05-01
PNTM-DELISTED (Pontem) Start Date:2021-03-05
POLY-DELISTED (Plantronics,) Start Date:2021-05-24
POM-DELISTED (Pepco Holdings Inc) Start Date:2004-01-02
POSH-DELISTED (Poshmark) Start Date:2021-01-14
POW-DELISTED (Powered Brands) Start Date:2021-03-04
PPD-DELISTED (Ppd) Start Date:2020-02-06
PPDI-DELISTED (Pharmaceutical Product Development Inc) Start Date:2004-01-02
PPGH-DELISTED (Poema Global) Start Date:2021-03-01
PQG-DELISTED (Pq) Start Date:2017-09-29
PRAH-DELISTED (Pra Health Sciences Comm) Start Date:2014-11-13
PROG-DELISTED (Progenity) Start Date:2020-06-19
PROS-DELISTED (Prosight Global) Start Date:2019-07-25
PRPB-DELISTED (Cc Neuberger Principal Holdings Ii Class A Ordinary Shares) Start Date:2020-09-21
PRVB-DELISTED (Provention Bio) Start Date:2018-07-24
PSB-DELISTED (Ps Business Parks) Start Date:2007-05-03
PSFT-DELISTED (People Soft) Start Date:2008-10-07
PSPC-DELISTED (Post Holdings Partnering) Start Date:2021-07-16
PSTH-DELISTED (Pershing Square Tontine Holdings, Ltd.) Start Date:2020-09-11
PSTI-DELISTED (Pluristem Therapeutics) Start Date:2007-12-10
PSXP-DELISTED (Phillips 66 Partners Lp) Start Date:2013-07-23
PTEIQ-DELISTED (Polarityte Inc) Start Date:2007-05-16
PVAC-DELISTED (Penn Virginia) Start Date:2016-11-15
PVG-DELISTED (Pretium Resources) Start Date:2010-12-16
PWPPW-DELISTED (Perella Weinberg Partners Warrant) Start Date:2020-11-20
PX-DELISTED (Praxair) Start Date:2004-01-02
PZN-DELISTED (Pzena Investment) Start Date:2007-10-25
QADA-DELISTED (Qad) Start Date:2010-12-16
Q-DELISTED (Qwest Communications International Inc) Start Date:2013-06-03
QK-DELISTED (Q&K International American Depositary Shares) Start Date:2019-11-05
QLGC-DELISTED (Qlogic Corporation) Start Date:2004-01-02
QTS-DELISTED (Qts Realty Trust) Start Date:2013-10-09
QTT-DELISTED (Qutoutiao American Depositary Shares) Start Date:2018-09-14
QUMU-DELISTED (Qumu) Start Date:2007-05-16
QVCA-DELISTED (Liberty Interactive Corporation) Start Date:2007-04-26
RACB-DELISTED (Research Alliance Ii Class A) Start Date:2021-03-18
RADA-DELISTED (Rada Electronic Industries) Start Date:2007-05-16
RAI-DELISTED (Reynolds American Inc Common St) Start Date:2004-08-02
RAVN-DELISTED (Raven Industries) Start Date:2007-04-30
RBC-DELISTED (Regal Beloit Corporation) Start Date:2007-01-03
RBCN-DELISTED (Rubicon Technology) Start Date:2007-11-16
RBNC-DELISTED (Reliant Bancorp) Start Date:2009-10-30
RCOR-DELISTED (Renovacor) Start Date:2021-09-03
RDBX-DELISTED (Redbox Entertainment Class A) Start Date:2020-12-10
RDBXW-DELISTED (Redbox Entertainment Warrant) Start Date:2021-10-25
RDC-DELISTED (Rowan Companies Common St) Start Date:2004-01-02
RDUS-DELISTED (Radius Health O) Start Date:2014-06-06
REED-DELISTED (Reeds) Start Date:2007-05-16
REGI-DELISTED (Renewable Energy) Start Date:2012-01-19
REPH-DELISTED (Recro Pharma) Start Date:2014-03-07
RESN-DELISTED (Resonant) Start Date:2014-05-29
REUN-DELISTED (Reunion Neuroscience) Start Date:2021-07-29
REVRQ-DELISTED (Revlon Inc) Start Date:2008-09-16
RFP-DELISTED (Resolute Forest Products) Start Date:2008-03-03
RHT-DELISTED (Red Hat) Start Date:2007-05-14
RKTA-DELISTED (Rocket Internet Growth Opportunities Class A Ordinary Shares) Start Date:2021-05-13
RLGY-DELISTED (Realogy Holdings) Start Date:2012-10-11
RMO-DELISTED (Romeo Power,) Start Date:2019-04-01
RNDB-DELISTED (Randolph Bancorp) Start Date:2016-07-01
RNWK-DELISTED (Realnetworks) Start Date:2007-04-26
ROCC-DELISTED (Ranger Oil Class A) Start Date:2021-01-05
ROLL-DELISTED (Rbc Bearings) Start Date:2007-05-04
RPAI-DELISTED (Retail Properties) Start Date:2012-04-05
RRD-DELISTED (R.R. Donnelley & Sons Company) Start Date:2005-01-03
RSH-DELISTED (Radioshack Common S) Start Date:2004-01-02
RTLR-DELISTED (Rattler Midstream Lp Common Units) Start Date:2019-05-23
RTP-DELISTED (Reinvent Technology Partners) Start Date:2020-11-09
RTPY-DELISTED (Reinvent Technology Partners Y) Start Date:2021-05-10
RUBY-DELISTED (Rubius Therapeutics) Start Date:2018-07-18
RUTH-DELISTED (Ruth's Hospitality) Start Date:2007-05-02
RVI-DELISTED (Retail Value) Start Date:2018-06-26
RXDX-DELISTED (Prometheus Biosciences) Start Date:2021-03-12
RXN-DELISTED (Rexnord Corporation) Start Date:2012-03-29
RZA-DELISTED (Reinsurance Of America Incorporated 6.20% Fixed-To-Floating Rate Subordinated Debentures Due 2042) Start Date:2013-02-11
SAF-DELISTED (Safeco) Start Date:2008-03-03
SAFM-DELISTED (Sanderson Farms) Start Date:2007-05-01
SAL-DELISTED (Salisbury Bancorp Common) Start Date:2007-05-16
SBBP-DELISTED (Strongbridge Biopharma) Start Date:2015-10-16
SBII-DELISTED (Sandbridge X2) Start Date:2021-04-30
SBNY-DELISTED (Signature Bank) Start Date:2007-05-04
SC-DELISTED (Santander Consumer Usa Holding) Start Date:2014-01-23
SCG-DELISTED (Scana) Start Date:2004-01-02
SCOA-DELISTED (Scion Tech Growth I) Start Date:2021-02-08
SCOB-DELISTED (Scion Tech Growth Ii Class A Ordinary Shares) Start Date:2021-04-06
SCPS-DELISTED (Scopus Biopharma) Start Date:2020-12-16
SCR-DELISTED (Score Media & Gaming) Start Date:2014-01-10
SCVX-DELISTED (Scvx) Start Date:2020-03-20
SDH-DELISTED (Global Internet Of People Ordinary Shares) Start Date:2021-02-09
SEVCQ-DELISTED (Sono Nv) Start Date:2021-11-17
SGFY-DELISTED (Signify Health) Start Date:2021-02-11
SGMS-DELISTED (Scientific Games) Start Date:2007-05-02
SGP-DELISTED (Merck & Co/Inc) Start Date:2004-01-02
SGTX-DELISTED (Sigilon Therapeutics) Start Date:2020-12-04
SHLX-DELISTED (Shell Midstream Partners L.P.) Start Date:2014-10-29
SIAL-DELISTED (Sigma-Aldrich Corporation) Start Date:2004-01-02
SICP-DELISTED (Silvergate Capital Corp) Start Date:2019-11-07
SIOX-DELISTED (Sio Gene Therapies) Start Date:2015-06-11
SIRE-DELISTED (Sisecam Resources Lp Common Units Representing Partner Interests) Start Date:2022-03-01
SIVB-DELISTED (Svb Financial) Start Date:2006-03-01
SJI-DELISTED (South Jersey Industries) Start Date:2007-01-03
SJIV-DELISTED (South Jersey Industries Corporate Units) Start Date:2021-03-25
SJR-DELISTED (Shaw Communications) Start Date:2007-01-03
SLCT-DELISTED (Select Bancorp) Start Date:2007-05-16
SLHG-DELISTED (Skylight Health  Ordinary Shares) Start Date:2021-06-07
SLR-DELISTED (Solectron) Start Date:2004-01-02
SMED-DELISTED (Sharps Compliance) Start Date:2009-05-06
SMIT-DELISTED (Schmitt Industries) Start Date:2007-05-16
SMM-DELISTED (Salient Midstream Common Shares Of Beneficial Interest) Start Date:2012-05-25
SNDK-DELISTED (Sandisk) Start Date:2004-01-02
SNI-DELISTED (Scripps Networks Interactive I) Start Date:2008-07-01
SNR-DELISTED (New Senior Investment  I) Start Date:2014-11-07
SOLN-DELISTED (The Southern Company) Start Date:2019-08-21
SOLY-DELISTED (Soliton) Start Date:2019-02-19
SPKE-DELISTED (Spark Energy  Com) Start Date:2014-07-29
SPNE-DELISTED (Seaspine) Start Date:2015-06-17
SPPI-DELISTED (Spectrum Pharmaceuticals) Start Date:2007-05-07
SQZB-DELISTED (Sqz Biotechnologies Co.) Start Date:2020-11-02
SRAX-DELISTED (Srax Class A) Start Date:2016-10-13
SREV-DELISTED (Servicesource) Start Date:2011-03-25
SRLP-DELISTED (Sprague Resources Lp Common Units Representing Partner Interests) Start Date:2013-10-25
SRRA-DELISTED (Sierra Oncology) Start Date:2015-07-16
SSS-DELISTED (Sovran Self Storage) Start Date:2004-01-02
STAB-DELISTED (Statera Biopharma) Start Date:2007-05-16
STET-DELISTED (St Energy Transition I Class A Ordinary Shares) Start Date:2022-01-24
STFC-DELISTED (State Auto Financial) Start Date:2007-05-02
STI-DELISTED (Suntrust Banks) Start Date:2004-01-02
STJ-DELISTED (St. Jude Medical Common S) Start Date:2004-01-02
STL-DELISTED (Sterling Bancorp) Start Date:2007-01-03
STMP-DELISTED (Stamps.com) Start Date:2007-01-03
STON-DELISTED (Stonemor) Start Date:2007-05-16
STOR-DELISTED (Store Capital Corporation) Start Date:2014-11-18
STR-DELISTED (Questar Common Stoc) Start Date:2004-01-02
STSA-DELISTED (Satsuma Pharmaceuticals) Start Date:2019-09-13
STXB-DELISTED (Spirit Of Texas Bancshares) Start Date:2018-05-04
STZ.B-DELISTED (Constellation Brands Inc) Start Date:2007-05-16
SUMO-DELISTED (Sumo Logic) Start Date:2020-09-17
SUNE-DELISTED () Start Date:2013-06-03
SVA-DELISTED (Sinovac Biotech, Ltd) Start Date:2007-04-26
SVFA-DELISTED (Svf Investment Class A Ordinary Shares) Start Date:2021-01-27
SVFB-DELISTED (Svf Investment 2 Class A Ordinary Shares) Start Date:2021-03-09
SVU-DELISTED (Supervalu) Start Date:2004-01-02
SWCH-DELISTED (Switch) Start Date:2017-10-06
SWIR-DELISTED (Sierra Wireless) Start Date:2007-05-09
SWM-DELISTED (Schweitzer-Mauduit Intl) Start Date:2007-05-02
SWT-DELISTED (Stanley Black & Decker Corporate Unit) Start Date:2019-11-14
SWY-DELISTED (Safeway) Start Date:2004-01-02
SYKE-DELISTED (Sykes Enterprises) Start Date:2007-04-30
SYMC-DELISTED (Symantec) Start Date:2018-01-02
SYNL-DELISTED (Synalloy) Start Date:2007-05-16
TACO-DELISTED (Levy Acquisition) Start Date:2014-01-08
TA-DELISTED (Travelcenters Of America Llc) Start Date:2007-05-16
TBIO-DELISTED (Translate Bio) Start Date:2018-06-28
TCFC-DELISTED (The Community Financial Corpor) Start Date:2007-06-04
TCRR-DELISTED (Tcr2 Therapeutics) Start Date:2019-02-14
TE-DELISTED (Teco Energy) Start Date:2004-01-02
TEG-DELISTED (Integrys Energy Com) Start Date:2007-02-22
TEN-DELISTED (Tenneco) Start Date:2007-05-01
TESS-DELISTED (Tessco Technologies Incorporated) Start Date:2007-05-16
TETC-DELISTED (Tech & Energy Transition) Start Date:2021-05-20
TGA-DELISTED (Transglobe Energy Ordinary Shares) Start Date:2007-04-27
TGP-DELISTED (Teekay Lng Partners L.P.) Start Date:2007-05-16
THCA-DELISTED (Tuscan Holdings Ii) Start Date:2019-07-30
THCAU-DELISTED (Tuscan Holdings Ii Unit) Start Date:2019-07-12
TIE-DELISTED (Titanium Metals Com) Start Date:2004-01-02
TIG-DELISTED (Trean Insurance ,) Start Date:2020-07-16
TIOA-DELISTED (Tio Tech A) Start Date:2021-06-10
TLAB-DELISTED (Tellabs) Start Date:2004-01-02
TLMD-DELISTED (Soc Telemed, Class A) Start Date:2020-01-28
TMK-DELISTED (Torchmark) Start Date:2004-01-02
TMX-DELISTED (Terminix Global Holdings,) Start Date:2014-06-26
TPGS-DELISTED (Tpg Pace Solutions) Start Date:2021-04-09
TPGY-DELISTED (Tpg Pace Beneficial Finance) Start Date:2020-12-15
TPTX-DELISTED (Turning Point Therapeutics) Start Date:2019-04-17
TREC-DELISTED (Trecora Resources) Start Date:2007-05-16
TRIL-DELISTED (Trillium Therapeutics) Start Date:2014-12-19
TRQ-DELISTED (Turquoise Hill Resources Ltd) Start Date:2007-05-02
TSC-DELISTED (Tristate Capital) Start Date:2013-05-09
TSG-DELISTED (Sabre Holdings) Start Date:2004-01-02
TSIB-DELISTED (Tishman Speyer Innovation Ii Class A) Start Date:2021-04-05
TSO-DELISTED (Tesoro) Start Date:2004-01-02
TSS-DELISTED (Total System Services) Start Date:2004-01-02
TTM-DELISTED (Tata Motors Limited) Start Date:2013-02-11
TUFN-DELISTED (Tufin Software Technologies Ordinary Shares) Start Date:2019-04-11
TUGC-DELISTED (Tradeup Global) Start Date:2021-06-28
TVTY-DELISTED (Tivity Health) Start Date:2007-04-30
TWC-DELISTED (Time Warner Cable Inc Common St) Start Date:2007-03-01
TWTR-DELISTED (Twitter) Start Date:2013-11-07
TWX-DELISTED (Time Warner New Common Sto) Start Date:2004-01-02
TYME-DELISTED (Tyme Technologies) Start Date:2015-03-12
UBA-DELISTED (Urstadt Biddle Properties) Start Date:2007-05-07
UBP-DELISTED (Urstadt Biddle Properties) Start Date:2013-02-11
UFS-DELISTED (Domtar) Start Date:2007-05-16
UMPQ-DELISTED (Umpqua Holdings Corporation) Start Date:2007-01-03
UNVR-DELISTED (Univar Solutions) Start Date:2015-06-18
USAK-DELISTED (Usa Truck) Start Date:2007-04-30
USCR-DELISTED (Us Concrete) Start Date:2010-10-15
USER-DELISTED (Usertesting) Start Date:2021-11-17
USWS-DELISTED (U.S. Well Services Class A) Start Date:2017-05-05
USX-DELISTED (Us Xpress Enterprises) Start Date:2018-06-14
VCRA-DELISTED (Vocera Communications) Start Date:2012-03-28
VEC-DELISTED (Vectrus) Start Date:2014-09-29
VECT-DELISTED (Vectivbio Holding) Start Date:2021-04-09
VEDL-DELISTED (Vedanta Limited) Start Date:2013-09-09
VEI-DELISTED (Vine Energy) Start Date:2021-03-18
VER-DELISTED (Vereit) Start Date:2011-09-07
VG-DELISTED (Vonage Holdings) Start Date:2007-01-03
VIAB-DELISTED (Viacom) Start Date:2007-04-30
VIACA-DELISTED (Viacomcbs) Start Date:2019-12-05
VIAC-DELISTED (Viacomcbs) Start Date:2007-04-30
VIA-DELISTED (Viacom Inc) Start Date:2004-01-02
VIP-DELISTED (Vimpelcom Ltd.) Start Date:2004-01-02
VIVE-DELISTED (Viveve Medical) Start Date:2016-06-14
VIVO-DELISTED (Meridian Bioscience) Start Date:2007-05-04
VLDR-DELISTED (Velodyne Lidar,) Start Date:2018-10-26
VLNS-DELISTED (The Valens Company Common Shares) Start Date:2021-12-09
VLTA-DELISTED (Volta) Start Date:2020-11-02
VMED-DELISTED (Virgin Media) Start Date:2007-02-08
VNE-DELISTED (Veoneer) Start Date:2018-06-11
VRS-DELISTED (Verso Corp) Start Date:2016-07-19
VVNT-DELISTED (Vivint Smart Home) Start Date:2017-10-19
VYGG-DELISTED (Vy Global Growth) Start Date:2020-12-15
VYNT-DELISTED (Vyant Bio) Start Date:2013-04-10
WBT-DELISTED (Welbilt) Start Date:2016-02-18
WCG-DELISTED (Wellcare) Start Date:2004-07-01
WCRX-DELISTED (Warner Chilcott Plc) Start Date:2006-09-21
WEBR-DELISTED (Weber) Start Date:2021-08-05
WEJWQ-DELISTED (Wejo Ltd.) Start Date:2021-11-19
WFM-DELISTED (Whole Foods Market) Start Date:2007-04-27
WIN-DELISTED (Windstream Corporation) Start Date:2006-07-18
WLL-DELISTED (Whiting Petroleum) Start Date:2020-09-02
WLTW-DELISTED (Willis Towers Watson) Start Date:2016-01-05
WORK-DELISTED (Slack Technologies) Start Date:2019-06-20
WPCA-DELISTED (Warburg Pincus Capital Ia Class A Ordinary Shares) Start Date:2021-04-26
WPCB-DELISTED (Warburg Pincus Capital Ib Class A Ordinary Shares) Start Date:2021-04-26
WRI-DELISTED (Weingarten Realty Investors) Start Date:2007-01-03
WSH-DELISTED (Willis Holdings) Start Date:2004-01-02
WSO.B-DELISTED (Watsco) Start Date:2007-05-16
WTRE-DELISTED (Watford  Common Shares) Start Date:2019-03-28
WTT-DELISTED (Wireless Telecom) Start Date:2007-05-16
WXS-DELISTED (Wex) Start Date:2005-03-01
WYN-DELISTED (Wyndham Worldwide Common) Start Date:2006-08-01
XEC-DELISTED (Cimarex Energy) Start Date:2005-01-03
XENT-DELISTED (Intersect Ent O) Start Date:2014-07-24
XL-DELISTED (Xl Plc) Start Date:2004-01-02
XLNX-DELISTED (Xilinx) Start Date:2005-01-03
XLRN-DELISTED (Acceleron Pharma) Start Date:2013-09-19
XM-DELISTED (Qualtrics International) Start Date:2021-01-28
XONE-DELISTED (The Exone Company) Start Date:2013-02-07
XPOA-DELISTED (Dpcm Capital Class A) Start Date:2020-12-15
Y-DELISTED (Yte) Start Date:2019-01-02
YHOO-DELISTED (Yahoo!) Start Date:2004-01-02
YNDX-DELISTED (Yandex N.V.) Start Date:2011-05-24
YTPG-DELISTED (Tpg Pace Beneficial Ii Class A Ordinary Shares) Start Date:2021-04-14
ZEAL-DELISTED (Zealand Pharma A/S American Depositary Shares) Start Date:2017-08-09
ZEN-DELISTED (Zendesk) Start Date:2014-05-15
ZGNX-DELISTED (Zogenix) Start Date:2010-11-23
ZIOP-DELISTED (Ziopharm Oncology) Start Date:2007-05-16
ZIXI-DELISTED (Zix) Start Date:2007-05-09
ZME-DELISTED (Zhangmen Education) Start Date:2021-06-08
ZNGA-DELISTED (Zynga) Start Date:2011-12-16
ZNHYY-DELISTED (China Southern Airlines Co Ltd.) Start Date:2013-02-11
ZVOI-DELISTED (Zovio Inc) Start Date:2009-04-15








Crypto Tickers
---------------
ADA (Cardano) Start Date:2018-03-01
BAT (Basic Attention Token) Start Date:2018-01-08
BCH (Bitcoin Cash) Start Date:2017-12-04
BNT (Bancor) Start Date:2017-08-01
BSV (Bitcoin Sv) Start Date:2018-12-01
BTC (Bitcoin) Start Date:2013-04-01
BTC-EUR (Bitcoin-Eur) Start Date:2017-01-01
BTG (Bitcoin Gold) Start Date:2017-11-01
CVC (Civic) Start Date:2017-07-01
DAI (Dai) Start Date:2018-04-07
DASH (Dash) Start Date:2017-05-01
DCR (Decred) Start Date:2019-05-08
DOGE (Dogecoin) Start Date:2017-06-01
EOS (Eos) Start Date:2017-07-01
ETC (Ethereum Classic) Start Date:2017-01-01
ETH (Ethereum) Start Date:2016-03-11
ETH-BTC (Ethereum-Bitcoin) Start Date:2017-01-01
FUN (Funfair) Start Date:2017-09-01
HT (Huboi Token) Start Date:2019-03-06
ICX (Icon) Start Date:2017-10-01
IOST (Iost) Start Date:2018-06-06
KNC (Kyber Network) Start Date:2018-06-01
LINK (Chainlink) Start Date:2019-07-01
LRC (Loopring) Start Date:2018-04-07
LSK (Lisk) Start Date:2018-02-01
LTC (Litecoin) Start Date:2017-01-01
MAID (Maid Safe Coin) Start Date:2017-06-02
MANA (Decentraland) Start Date:2017-08-01
MKR (Maker) Start Date:2018-06-01
NEO (Neo) Start Date:2017-09-07
OMG (Omg Network) Start Date:2017-08-01
ONT (Ontology) Start Date:2018-05-01
PAX (Paxos Standard) Start Date:2018-12-04
QTUM (Qtun) Start Date:2018-04-01
REP (Augur) Start Date:2017-01-02
SC (Siacoin) Start Date:2019-11-01
SNT (Status) Start Date:2018-01-01
TRX (Tron) Start Date:2017-10-07
USDC (Usd Coin) Start Date:2020-01-08
USDT (Tether) Start Date:2017-04-01
UST (Terraust) Start Date:2018-12-01
UTK (Utrust) Start Date:2018-02-07
VET (Vechain) Start Date:2018-09-01
WAVES (Waves) Start Date:2019-09-01
XEM (Nem) Start Date:2017-06-01
XLM (Stellar) Start Date:2018-03-01
XMR (Monero) Start Date:2017-01-01
XRP (Ripple) Start Date:2017-02-01
XTZ (Tezos) Start Date:2017-07-03
XVG (Verge) Start Date:2017-10-01
ZEC (Zcash) Start Date:2017-01-01
ZIL (Zilliqa) Start Date:2018-06-07
ZRX (Ox) Start Date:2017-09-01








Index Tickers
---------------
AEX (Amsterdam Exchange Index) Start Date:2008-01-02
ASX (FTSE All Share) Start Date:2015-12-10
BKX (Kbw Nasdaq Bank Index) Start Date:2008-01-02
BRR (Cme Cf Bitcoin Reference Rate) Start Date:2018-06-12
BRTI (Cme Cf Bitcoin Real-Time Index) Start Date:2016-11-13
BXD (CBOE Djia Buywrite Index) Start Date:2008-01-02
BXM (CBOE S&P 500 Buywrite Index) Start Date:2008-01-02
BXN (CBOE Nasdaq-100 Buywrite Index) Start Date:2008-01-02
BXR (CBOE Russell 2000 Buywrite Index) Start Date:2008-01-02
CEX (Standard & Poors Chemicals Index) Start Date:2008-01-02
CLL (CBOE S&P 500 95-110 Collar Index) Start Date:2008-08-26
COMP (Nasdaq Composite) Start Date:2008-01-02
CXU (U.S.-Europe-Japan Basket) Start Date:2008-01-02
DAX (DAX 30) Start Date:2008-01-02
DJCIAGC (Dow Jones Commodity Index Agriculture Capped Component) Start Date:2017-07-19
DJCICC (Dow Jones Commodity Index Cocoa) Start Date:2017-07-19
DJCIEN (Dow Jones Commodity Index Energy) Start Date:2017-07-19
DJCIGC (Dow Jones Commodity Index Gold) Start Date:2017-07-19
DJCIGR (Dow Jones Commodity Index Grains) Start Date:2017-07-19
DJCIIK (Dow Jones Commodity Index Nickel) Start Date:2017-07-19
DJCIKC (Dow Jones Commodity Index Coffee) Start Date:2017-07-19
DJCISB (Dow Jones Commodity Index Sugar) Start Date:2017-07-19
DJCISI (Dow Jones Commodity Index Silver) Start Date:2017-07-19
DJI (Dow Jones Industrial Average) Start Date:2008-01-02
DJINET (Dow Jones Internet) Start Date:2008-01-02
DJR (Dow Jones Equity Real Estate Investment Trust Index) Start Date:2008-01-02
DJTTR (Dow Jones Transportation) Start Date:2008-01-02
DJX (Dj Industrials 1/100 Index) Start Date:2008-01-02
DRG (Nyse Pharmaceutical) Start Date:2008-01-02
DUX (Dow Jones Utility Average Index) Start Date:2008-01-02
DVS (S&P 500 Dividend Index 10X) Start Date:2010-02-05
DWCF (Dow Jones Total Us Stock Market) Start Date:2011-11-07
DWCPF (Dow Jones Us Completion Total Stock Market) Start Date:2011-11-07
DWLG (Dow Jones Large-Cap Growth Total Market) Start Date:2011-11-07
DWLV (Dow Jones Large-Cap Value Total Market) Start Date:2011-11-07
DXL (CBOE Jumbo Djx Index) Start Date:2008-01-02
DXY (US Dollar Index) Start Date:2020-12-11
EVZ (CBOE Eurocurrency Volatility Index) Start Date:2008-08-01
FVX (CBOE 5 Year Treasury) Start Date:2008-01-02
GVZ (CBOE Gold Volatility Index) Start Date:2008-08-01
HGX (Phlx Housing Sector) Start Date:2008-01-02
LOVOL (CBOE Low Volatility Index) Start Date:2014-07-15
MID (S&P Midcap 400) Start Date:2010-12-06
MIDG (S&P Midcap 400 Growth) Start Date:2011-11-07
MIDV (S&P Midcap 400 Value) Start Date:2011-11-07
MRUT (Mini-Russell 2000 Index) Start Date:2021-02-22
NDX (Nasdaq 100) Start Date:2008-01-02
NQX (Nasdaq 100 Reduced Value Index) Start Date:2019-03-12
NYA (Nyse Composite) Start Date:2008-01-02
NYFANG (Nyse Fang+ Index) Start Date:2017-09-28
NYXBT (Nyse Bitcoin Index) Start Date:2015-05-19
OEX (S&P 100) Start Date:2008-01-02
OSX (Phlx Oil Service Sector Index) Start Date:2008-01-02
OVX (CBOE Crude Oil Volatility Index) Start Date:2008-07-15
PUT (CBOE S&P 500 Put-Write Index) Start Date:2008-01-02
REIT (Dow Jones Equity Reit) Start Date:2008-01-02
RUA (Russell 3000 Index) Start Date:2008-01-02
RUI (Russell 1000) Start Date:2008-01-02
RUT (Russell 2000) Start Date:2008-01-02
RVX (Russell 2000 Volatility Index) Start Date:2008-01-02
RXM (CBOE S&P 500 Risk Reversal Index) Start Date:2017-08-04
SET (S&P 500 Settlement Index) Start Date:2008-01-02
SGX (S&P 500 Growth) Start Date:2010-12-06
SMILE (CBOE S&P 500 Smile Index) Start Date:2017-08-04
SMLG (S&P Small Cap 600 Growth) Start Date:2011-11-07
SP500LVOL (S&P 500 Low Volatility) Start Date:2011-04-04
SP600 (S&P 600 Small Cap) Start Date:2010-12-06
SPEN (CBOE S&P 500 Enhanced Growth Balanced Series) Start Date:2017-08-04
SPGSCI (S&P Goldman Sachs Commodity) Start Date:2020-12-11
SPMPG (S&P Midcap 400 Pure Growth) Start Date:2011-11-07
SPMPV (S&P Midcap 400 Pure Value) Start Date:2011-11-07
SPRI (CBOE S&P 500 Range Bound Premium) Start Date:2017-08-04
SPRO (CBOE S&P 500 Buffer Protect Index Series) Start Date:2017-08-04
SPSIBI (S&P Biotechnology Select Industry) Start Date:2010-12-06
SPSPG (S&P Small Cap 600 Pure Growth) Start Date:2011-11-07
SPSPV (S&P Small Cap 600 Pure Value) Start Date:2011-11-07
SPSV (S&P Small Cap 600 Value) Start Date:2011-11-07
SPTMI (S&P Total Market Index) Start Date:2011-11-07
SPX (S&P 500) Start Date:2008-01-02
SPXPG (S&P 500 Pure Growth) Start Date:2008-01-02
SPXPV (S&P 500 Pure Value) Start Date:2008-01-02
SVX (S&P 500 Value) Start Date:2010-12-06
TNX (CBOE 10 Year Treasury) Start Date:2008-01-02
TYX (CBOE 30 Year Treasury) Start Date:2008-01-02
UKX (FTSE 100) Start Date:2015-12-10
UTIL (Dow Jones Utilities) Start Date:2008-01-02
UTY (Phlx Utility Sector) Start Date:2008-01-02
VAF (S&P 500 Variance Futures Settlement Prices) Start Date:2013-02-15
VIF (CBOE Spx Far-Term VIX Index) Start Date:2008-08-25
VIN (CBOE Spx Near-Term VIX Index) Start Date:2008-08-25
VIX (CBOE Volatility Index) Start Date:2008-01-02
VIX1Y (CBOE 1-Year Volatility Index) Start Date:2018-04-25
VIX3M (S&P 500 3 Month Volatility) Start Date:2008-01-02
VIX6M (CBOE Mid-Term Volatility Index) Start Date:2014-06-04
VIX9D (S&P 500 9-Day Volatility) Start Date:2013-10-01
VOLI (Nations Voldex) Start Date:2013-06-21
VPD (CBOE VIX Premium Strategy Index) Start Date:2008-01-02
VPN (CBOE Capped VIX Premium Strategy Index) Start Date:2008-01-02
VVIX (VIX Volatility Index) Start Date:2012-03-14
VWA (CBOE VIX Indicative Ask Index) Start Date:2008-01-02
VWB (CBOE VIX Indicative Bid Index) Start Date:2008-01-02
VXD (CBOE Djia Volatility Index) Start Date:2008-01-02
VXN (CBOE Nasdaq Volatility Index) Start Date:2008-01-02
VXTH (CBOE VIX Tail Hedge Index) Start Date:2011-07-29
VXTLT (20+ Year Treasury Bond Volatility Index) Start Date:2020-05-28
W5000 (Wilshire 5000) Start Date:2016-03-31
WPUT (CBOE S&P 500 One-Week Putwrite Index) Start Date:2017-07-19
XAU (Philadelphia Gold And Silver Index) Start Date:2008-01-02
XAX (Amex Composite) Start Date:2020-12-11
XDA (Phlx Aud Currency Index) Start Date:2013-04-08
XDB (Phlx British Pound Index) Start Date:2013-04-08
XEO (S&P European 100 Index) Start Date:2008-01-02
XMI (Nyse Arca Major Market) Start Date:2020-12-11
XND (Nasdaq 100 Total Return Index) Start Date:2008-01-02
XSP (Mini Standard & Poor's 500) Start Date:2008-01-02
XSR (S&P 500 Settlement Reduced) Start Date:2008-01-02








FX Tickers
---------------
AUDBRL Start Date:2010-01-01
AUDCAD Start Date:2010-01-01
AUDCHF Start Date:2010-01-01
AUDCNH Start Date:2010-01-01
AUDHUF Start Date:2010-01-01
AUDILS Start Date:2010-01-01
AUDINR Start Date:2010-01-01
AUDJPY Start Date:2010-01-01
AUDMXN Start Date:2010-01-01
AUDSGD Start Date:2010-01-01
AUDTHB Start Date:2010-01-01
AUDTRY Start Date:2010-01-01
AUDUSD Start Date:2010-01-01
AUDZAR Start Date:2010-01-01
EURAUD Start Date:2010-01-01
EURBRL Start Date:2010-01-01
EURCAD Start Date:2010-01-01
EURCHF Start Date:2010-01-01
EURCNH Start Date:2010-01-01
EURCNY Start Date:2010-01-01
EURGBP Start Date:2010-01-01
EURHUF Start Date:2010-01-01
EURILS Start Date:2010-01-01
EURINR Start Date:2010-01-01
EURMXN Start Date:2010-01-01
EURSGD Start Date:2010-01-01
EURTHB Start Date:2010-01-01
EURTRY Start Date:2010-01-01
EURUSD Start Date:2010-01-01
EURZAR Start Date:2010-01-01
GBPAUD Start Date:2010-01-01
GBPBRL Start Date:2010-01-01
GBPCHF Start Date:2010-01-01
GBPCNH Start Date:2010-01-01
GBPHUF Start Date:2010-01-01
GBPILS Start Date:2010-01-01
GBPINR Start Date:2010-01-01
GBPMXN Start Date:2010-01-01
GBPSGD Start Date:2010-01-01
GBPTHB Start Date:2010-01-01
GBPTRY Start Date:2010-01-01
GBPUSD Start Date:2010-01-01
GBPZAR Start Date:2010-01-01
NZDBRL Start Date:2010-01-01
NZDCAD Start Date:2010-01-01
NZDCHF Start Date:2010-01-01
NZDCNH Start Date:2010-01-01
NZDHUF Start Date:2010-01-01
NZDILS Start Date:2010-01-01
NZDINR Start Date:2010-01-01
NZDJPY Start Date:2010-01-01
NZDMXN Start Date:2010-01-01
NZDSGD Start Date:2010-01-01
NZDTHB Start Date:2010-01-01
NZDTRY Start Date:2010-01-01
NZDUSD Start Date:2010-01-01
NZDZAR Start Date:2010-01-01
USDBRL Start Date:2010-01-01
USDCAD Start Date:2010-01-01
USDCHF Start Date:2010-01-01
USDCNH Start Date:2010-01-01
USDCNY Start Date:2010-01-01
USDHKD Start Date:2010-01-01
USDHUF Start Date:2010-01-01
USDILS Start Date:2010-01-01
USDINR Start Date:2010-01-01
USDJPY Start Date:2010-01-01
USDMXN Start Date:2010-01-01
USDSGD Start Date:2010-01-01
USDTHB Start Date:2010-01-01
USDTRY Start Date:2010-01-01
USDZAR Start Date:2010-01-01

