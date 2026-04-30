# Exchange analysis documentation

This project is to do a deep analysis of Korean equity market microstructure in order to prepare for implementing execution algorithms for Korean equities.

Markets to cover: KOSPI Market, KOSDAQ Market.

## Areas of analysis documentation

 - Short selling rules (price, eligibility, etc)
 - price ranges
 - Market hours
 - regular Auctions
 - trading rules
 - Volatility Interruption rules
 - Circuit breakers
 - Rules for amendments (how to deal with price and quantity amends)
 - Supported order types
 - other areas present in official market documentation

## Entry points to seed the research

KOSPI Market official documentation entry point:
https://global.krx.co.kr/contents/GLB/06/0602/0602010201/GLB0602010201.jsp#826f2bceb71bdd795d4f782fda605cb1=1

KOSDAQ Market official documentation entry point:
https://global.krx.co.kr/contents/GLB/06/0602/0602020201/GLB0602020201.jsp

## Out of scope

  - Nextrade and ATS / PTS
  - Derivatives markets

## Documentation format

### Raw format for the documentation database

A collection of Markdown files and pictures stored in a directory plus the index for assembling the final doc from constituents.

### Visualisation

HTML based documentation (JS/CSS and frameworks are welcomed) generated based on the raw Markdown, pictures and the index file.

Color pallette : selectable between clean pastel white and pastel dark.