# SectorRotationUSMarkets2022
Demonstrating Sector Rotation Dynamics through Timely Identification of Stock Bottoms of Various Sectors during the 2022 Bear Market


* "Sector rotation is the movement of money invested in stocks from one industry to another as investors and traders anticipate the next stage of the economic cycle" - Investopedia
* Conducting a historical analysis of the sequence in which individual sector bottoms occur in relation to the market bottom (S&P500) can provide valuable insights into market timing.
* An Excel file named 'companyProfile_NYSE_NASDAQ_NSE_TSX_BSE.xlsx' contains stock symbols from various sectors, industries, and exchanges: NYSE, NASDAQ, NSE, TSX, and BSE. This file essentially serves as a reference for industries and sectors, encompassing around 13,000 symbols. Its compilation was established through a separate personal project.   
* A self-explanatory script titled 'main_SectorRotation.py' calls upon historical closing price data from the financialmodelingprep.com API (subscription required) for each symbol. It subsequently determines the lowest points of the stocks around the bear market bottom of 2022. These individual stock bottoms, along with their respective sectors and industries, are stored in 'stock_bottoms_final.xlsx'. The relative difference of a stock bottom relative the 2022 market bottom is calculated and the average of these relative differences is grouped by sectors (and also for various industries). The relative differences are presented in terms of days in relation to the market bottom, as indicated in the 'days_wrBottom' column, as demonstrated in the snapshot below.

<img width="400" src="https://github.com/DDataDudeADi/SectorRotationUSMarkets2022/blob/main/sectorBottomswrMarketBottom.jpg">
