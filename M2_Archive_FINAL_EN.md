# The M2 Archive [Part 2.5]

---


## Chapter 1. The Definition Map: Where Does M2 End?

 

---

### For First-Time Readers: What Is M2, and Why Do the Numbers Wobble?

#### 0.1 "Money" Is Not One Thing

The 50,000-won note in your wallet is certainly money. The balance in your salary account also feels like money. What about a one-year time deposit? You can use it if you cancel before maturity, but you lose part of the interest. An ETF or a fund unit becomes cash when you sell it, but you don't know what price you will get when you sell.

All four are "assets," but they differ in **how quickly, and without loss, they can be spent**. The monetary aggregates are a ladder built from this difference.

#### 0.2 The Rungs of the Ladder: M0, M1, M2, M3

The names differ slightly from country to country, but the broad framework is the same.

- **Monetary base (M0).** Money printed directly by the central bank. It consists of cash and the reserves that banks deposit with the central bank.
- **M1 (narrow money).** Money that can be spent right away. Its core is cash and demand deposits (accounts from which you can withdraw at any time).
- **M2 (broad money).** M1 plus "somewhat less liquid savings." Short-term savings products such as time deposits and MMFs are included.
- **M3 and beyond (L, etc.).** Broader than M2, including institutional deposits and even bonds. Some countries do not use it at all.

The key point is that the **lines dividing these rungs are not drawn in nature**. In some countries a time deposit is in M2 if it is shorter than two years and outside it if it is two years or longer. Some countries draw the line between "small" and "large" at $100,000. Why that line in particular is usually explained as "that is how it has been done, and it has generally been useful."

#### 0.3 Why Look at M2?

M2 often appears in the news under the name "money released into the market." People ask whether, if this number grows quickly, pressure builds on prices, housing prices, or the exchange rate. Central banks also treat M2 as reference material.

But for this number to carry meaning, **what has been put into M2 must stay constant**. If the standard changes midway, a statement such as "it grew by X percent compared with last year" no longer compares like with like.

#### 0.4 The Standard Really Does Change

There have already been several major cases in recent years. The United States (2020), China (2025), and South Korea (2026) revised their definitions; here we look first at the earliest and the latest of these.

**United States, May 2020 (by observation month).** The Federal Reserve moved savings deposits from a component of M2 into M1. This was because the rule (Regulation D) that had limited banks to six transfers or withdrawals per month from savings accounts was removed on April 24, 2020, which effectively turned savings deposits into something like checking accounts. The official announcement came on December 17, 2020, and it was applied retroactively from the release in February 2021, back to the May 2020 observation. As a result M1 suddenly jumped sharply, but M2 as a whole stayed the same. Many people mistook this "M1 surge" for newly created money.

**South Korea, January 2026.** The Bank of Korea removed equity and bond funds (beneficiary certificates), including ETFs, from M2. The reason given was that their prices fluctuate widely, so their function of "storing money" is weak. As a result the M2 growth rate for October 2025 fell from 8.7% to 5.2%.

What these cases have in common is that **money was not newly created or destroyed; the way of counting changed**.

#### 0.5 The One Question This Essay Poses

> What does it mean to "count money"?

- Hyperinflation is defined as "price increases of 50% or more per month," and the story there was that this threshold is a convention.
- The decline in the U.S. money stock in 1929–33 produced very different numbers depending on whether one used M1, M2, or total deposits.

#### 0.6 A Plain-Language Glossary

- **M2.** A broad measure of the money stock: cash and account balances, plus short-term savings products. Its composition differs from country to country.
- **Liquidity.** The degree to which an asset can be used like cash, quickly and without loss of value.
- **Medium of exchange and store of value.** The function of being used immediately when buying things, and the function of being set aside for later. The Federal Reserve explains that it distinguishes M1 from M2 by these two functions.
- **Average balance and end-of-period balance.** The average balance over a month versus the balance on the last day of the month. The Bank of Korea's M2 is based on the average balance by default.
- **Seasonal adjustment.** A value from which the seasonal effects that recur each month have been removed. When comparing the same month, check whether the series is the unadjusted (original) series.
- **Redefinition.** Changing the range of items included in an indicator. In that case, past values are recalculated, or the old and new standards are published in parallel.
- **Unit discipline.** This essay's principle of stating, whenever a figure is cited, the reference month, average vs. end-of-period balance, unadjusted vs. seasonally adjusted series, and old vs. new standard.

---

### 1. The Definition Map

#### 1.1 The Federal Reserve's Principle of Division

On September 4, 2026, Federal Reserve staff (Payne and Styczynski) summarized the principle of monetary aggregation in a FEDS Note as follows. Money is a bundle of safe, value-stable assets used for payments or short-term investment, and the monetary aggregates divide assets by **liquidity and function** (medium of exchange versus store of value).

- Assets that are primarily a medium of exchange (usable immediately, used for payments, low interest) go in M1.
- Assets that are primarily a store of value (liquid, but converting them to cash requires some procedure; used for short-term saving; interest close to market rates) go in M2 minus M1 (non-M1 M2).

The document states of itself that it reflects the authors' personal views and is not a Federal Reserve policy discussion. Even so, this principle matters because Federal Reserve staff wrote down directly that **the boundary is set by an asset's "use."** When the use changes, the position changes. Savings deposits in 2020 were an example (a footnote in the Note cites this case), and the stablecoins discussed in Chapter 6 are the next candidate. The same Note also states that H.6 is the second most downloaded statistical release on FRED, which shows how widely this number is used.

#### 1.2 Four Currency Areas' "M2" Side by Side

The name is the same, but the items included differ. The table below **compares definitions only** and does not compare figures (units, bases, and seasonal adjustment differ, so figures are not placed side by side). Japan has a different structure and is described separately below the table.

| Item | United States | Euro area | Korea, new M2 (Jan. 2026–) | Korea, old M2 (–2025) |

| Cash, demand deposits | M1 | M1 | M1 | M1 |

| Savings deposits | M1 from May 2020 (before that, non-M1 M2) | Deposits redeemable at notice of up to 3 months are in M2 | At-call (freely deposited and withdrawn) deposits are in M1 | Same |

| Small time deposits | Under $100,000 is in M2 | Maturity of up to 2 years is in M2 (regardless of amount) | Time deposits and installment savings under 2 years are in M2 | Same |

| Large and institutional deposits | Excluded from M2 ($100,000 or more was formerly on the M3 side) | Not divided by size; distinguished only by maturity and notice | CDs are in M2 | Same |

| MMFs | Only retail MMFs are in M2 (institutional MMFs were formerly on the M3 side) | M3 | M2 | Same |

| Repos (RPs) | Excluded | M3 | M2 | Same |

| Short-term financial bonds | Excluded | M3 (debt securities issued by MFIs with maturity up to 2 years) | Financial debentures under 2 years are in M2 | Same |

| Beneficiary certificates (ETFs, equity and bond funds) | Excluded | No such item (only MMF shares are in M3) | Excluded (moved to Lf) | Included |

| Money in trust under 2 years | Excluded | No such item | Included | Included |

| Notes issued by mega investment banks (IBs), note-type CMAs | Not applicable | Not applicable | Newly included | None |


**U.S. deduction item.** U.S. M2 is calculated by subtracting individual retirement account (IRA) and Keogh account balances from the sum of small time deposits and retail MMFs. Beginning with the H.6 of July 28, 2026, the Federal Reserve stopped deducting these balances separately from the small time deposit and retail MMF components and switched to a separate item deducted directly from the total. This was applied retroactively to the beginning of the series. Seasonally adjusted M2 is constructed by summing the seasonally adjusted components and then deducting the IRA and Keogh balances, which are not seasonally adjusted.

**Japan.** The Bank of Japan has used four indicators, M1, M2, M3, and L, since June 2008. Investment trusts and money in trust are not in M3 but are components of L, the broadest indicator. According to the preliminary figures for August 2026 (average balance), M2 is ¥1,296.4 trillion (+2.0% year on year), M3 is ¥1,640.0 trillion (+1.2%), and L is ¥2,342.7 trillion (+4.4%); within L, money in trust is ¥491.1 trillion (+12.0%) and investment trusts are ¥127.6 trillion (+13.9%). In other words, funds and trusts are growing much faster outside Japan's M2 and M3, but since Japan never put them in M2 to begin with, they do not show up in the M2 growth rate. This is a line similar to the structure Korea arrived at in 2026.

**Sources.** The U.S. column follows the definitional wording of the Federal Reserve's H.6 and the FEDS Notes (November 2024, September 2026); the euro area column follows the definition table on the ECB statistics page; Japan follows Bank of Japan statistics; and the Korea columns follow the Bank of Korea's December 2025 announcement and subsequent monthly releases (confirmed through reports in multiple media outlets). The euro area's cells for large deposits, beneficiary certificates, and money in trust were filled in by checking whether the ECB definition table has such an item or not.

Reading item by item side by side shows the following. **Korea's M2 was broader than the U.S. or euro area M2 (it included MMFs, RPs, CDs, and even financial debentures).** The old standard was broader still, because it added beneficiary certificates. The euro area's M2 is narrow because it pushes MMFs and RPs out to M3. All of them are called "M2."

#### 1.3 The Design Principles Behind the Definition Table

The definition table shows only whether an item is present or absent, but the **principle** by which items are divided also differs from institution to institution.

- **Federal Reserve (U.S.): function.** If it is a medium of exchange it is M1; if it is a store of value it is non-M1 M2 (Section 1.1).
- **ECB (euro area): issuing sector and maturity.** The ECB derives its monetary aggregates from the liabilities of the monetary financial institutions (MFI) sector and explains that the aggregates differ from one another in their degree of "moneyness." M1 is cash and overnight deposits; M2 adds deposits with an agreed maturity of up to two years and deposits redeemable at notice of up to three months; M3 adds repos, MMF shares, and debt securities with maturity of up to two years. In addition, foreign-currency liquid assets that euro-area residents hold with euro-area MFIs are also included, and growth rates are calculated on a transactions basis rather than as a simple comparison of end-of-period balances. This means that even the same "M3 growth rate" can differ from a value calculated from balance differences (interpretation).
- **IMF manual: issuing and holding sectors and financial-instrument categories.** The IMF's Monetary and Financial Statistics Manual and Compilation Guide (MFSMCG) defines broad money in terms of the concepts of the money-issuing sector and the money-holding sector, and divides investment fund shares into MMF shares and other shares. The former are included in broad money and the latter are excluded (paragraphs 3.146 and 6.47). This is the direction Korea's 2026 overhaul moved toward, and the fact that the euro area's definition table has only MMF shares and no general fund shares can be understood within the same framework (interpretation).

The three principles do not so much conflict as answer different questions. The Federal Reserve asks, "What role does this asset play?" The ECB and the IMF ask, "Whose liability is it, and how quickly does it become cash?" Whichever is used, drawing the boundary is part of the definition, and this is why the identically named M2 holds different contents.

#### 1.4 Timeline of Redefinitions

The fact that boundaries are "a convention, but not fixed" becomes clear when viewed as a timeline.

- **Nov. 2005 / Mar. 2006.** The Federal Reserve announced on November 10, 2005 that it would discontinue publishing M3, and stopped publication after March 23, 2006. The judgment was that M3 provided no more information than M2 and was of no use in the policy process (FEDS Note, November 2024).
- **June 2008.** The Bank of Japan overhauled its monetary statistics. It reorganized them into the four indicators M1, M2, M3, and L, in response to the privatization of the postal system, which led to Japan Post Bank. A break with the old series arose. The new series was first published on June 9 together with the preliminary figure for May 2008, and retroactive data for April 2003–March 2008 was provided first. The old series was named M1, M2+CDs, M3+CDs, and Broadly-Defined Liquidity. On June 13, the Monetary Survey was also widened to cover all depository corporations including Japan Post Bank, which the Bank of Japan explained was bringing it closer to the IMF manual.
- **Mar. 2016 / Nov. 2017.** The IMF released the Monetary and Financial Statistics Manual and Compilation Guide (MFSMCG) first as a pre-publication draft (March 22, 2016) and officially published it in November 2017. It contains the distinction of including MMF shares in broad money and excluding investment fund shares other than MMFs.
- **Jan. 2019.** The Federal Reserve excluded non-bank-issued traveler's checks from M1 (because the amount was negligible).
- **Mar.–Apr. 2020.** The Federal Reserve lowered the reserve requirement ratio to 0% and deleted the rule limiting savings deposits to six transfers per month.
- **May 2020 (observation month at which retroactive application starts).** Savings deposits moved into M1, and a new item, "other liquid deposits," was created.
- **Dec. 17, 2020.** The Federal Reserve announced the overhaul of H.6. It stated that the entire balance of savings deposits (about $11.2 trillion) would be added to M1 and that M2 would not change.
- **Feb. 2021.** In the release of February 23, 2021, the overhaul was reflected in actual figures and revised retroactively back to the May 2020 observation.
- **Dec. 2, 2024 / Jan. 2025.** The People's Bank of China announced an overhaul of the definition of M1 (December 2, 2024) and published the new M1 from the January 2025 data. Personal demand deposits and the customer reserves of non-bank payment institutions came into M1, and each month-end value for 2024 was recalculated retroactively on a comparable basis.
- **Dec. 16, 2025.** The Bank of Korea announced a plan to exclude beneficiary certificates from M2. It was aligned with the IMF's Monetary and Financial Statistics Manual (revised edition), and the Bank of Korea explained that it had been preparing since 2019. Depending on the report, this manual is described as the 2017 or the 2018 one; the IMF's bibliographic information shows a pre-publication draft in March 2016 and an official publication in November 2017, so the difference in years among the reports appears to come down to which point in this publication history they refer to.
- **Dec. 30, 2025.** The Bank of Korea published the results of the overhaul.
- **From Jan. 2026.** The totals on the new and old standards are published in parallel for one year.
- **July 28, 2026.** The Federal Reserve's H.6 changed how IRA and Keogh balances are deducted from M2 (from deduction by component to a separate deduction from the total, applied retroactively to the beginning of the series).

Something stands out in the timeline. In 2020 the United States changed its definition **because a regulation changed** (the transfer limit on savings deposits disappeared). Korea changed it **because an international standard changed**. Japan changed it **because the financial structure (postal privatization) changed**. The reasons are all different, but in none of them did the definition change "because the essence of money changed." Boundaries are redrawn when institutions, technology, and standards change. This is the present-tense case of this essay's central proposition, namely the sentence "the boundary of money moves when institutions shake."

The fact that the Bank of Japan explained in June 2008 that it was bringing its monetary survey closer to the IMF manual resembles the reason for Korea's 2025 overhaul. That is, alignment with international standards appears repeatedly as a reason for overhauls. This essay relays that only as the explanation given at the time of the overhaul and does not weigh causation.

#### 1.5 Korea's Old M2 and New M2: Same Month, Different Numbers

Because this is the closest case, we check it directly with figures. The figures below are Bank of Korea announcements, confirmed by cross-checking multiple media reports and by summing arithmetic (secondary confirmation).

**October 2025 (unadjusted series, Bank of Korea overhaul results announcement)**

- Old M2 balance ₩4,466.3 trillion, growth rate 8.7%
- New M2 balance ₩4,056.8 trillion, growth rate 5.2%
- By calculation, the balance difference is ₩409.5 trillion, and the new M2 is 9.2% smaller than the old M2.
- The difference in growth rates is 3.5 percentage points.
- The broader indicators barely changed. Lf fell 0.2%, from ₩6,026.3 trillion to ₩6,011.4 trillion (growth rate from 7.8% to 7.1%), and L rose 0.7%, from ₩7,543.2 trillion to ₩7,597.1 trillion (growth rate from 7.1% to 6.9%). This is because beneficiary certificates left M2 and moved to Lf. Even if M2 shrinks by 9.2% when the definition changes, the funds remain intact in the broader aggregates.
- The fact that two M2 figures were reported for the same month is also a case showing why the basis (whether seasonally adjusted, average vs. end-of-period balance) must be stated. The average balance for October 2025 appears as ₩4,471.6 trillion in reports on the monthly release (+0.9% from the previous month, previous month ₩4,430.5 trillion), and as ₩4,466.3 trillion (+8.7% year on year, unadjusted series) in the overhaul results. The two figures differ by a little over ₩5 trillion because the series differ (seasonally adjusted vs. unadjusted), and this essay uses only unadjusted-series values for the overhaul comparison.

**Contribution of beneficiary certificates**

- The Bank of Korea explained that in October the contribution of beneficiary certificates to the old M2 growth rate was 3.3 percentage points (37.5% of total growth), the highest since the 2008 fund boom (7.1 percentage points, 44.7%). During October alone, beneficiary certificates grew by ₩31.5 trillion, and their month-on-month growth rate of 6.8% was the highest since November 2007 (8.5%).
- The breakdown of the ₩409.5 trillion decrease disclosed by the Bank of Korea is as follows. Exclusion of beneficiary certificates −₩497.1 trillion, addition of notes issued by mega IBs and note-type CMAs +₩44.7 trillion, and improvements to compilation methods and supplementation of underlying data +₩43.0 trillion (the sum is −₩409.4 trillion, and the ₩0.1 trillion is a rounding difference). The reason why the ₩497.1 trillion does not disappear in full is also explained. Of the beneficiary certificates, the ₩64.2 trillion of monetary instruments held by non-MMF funds is still counted in M2, because once beneficiary certificates leave M2 the classification changes from a money-issuing entity to a holding entity. The balance of beneficiary certificates grew by about 36.8% year on year.

**Growth rates published in parallel (year on year, unadjusted series)**

| Reference month | Old M2 | New M2 | Beneficiary certificate growth | Contribution of beneficiary certificates (old M2) |

| Oct. 2025 | 8.7% | 5.2% | +36.8% | 3.3 pp |

| Nov. 2025 | 8.4% | 4.8% | +38.4% | 3.4 pp |

| Dec. 2025 | 8.0% | 4.7% | +37.4% | 3.4 pp |

| Jan. 2026 | 8.4% | 4.7% | +43.1% | 3.9 pp |

| Feb. 2026 | 9.1% | 4.9% | – | – |

| May 2026 | 11.6% | 5.8% | +61.7% | 6.1 pp |


Looking at January 2026, 8.4% − 3.9% = 4.5%, which matches the report's "about 4.5% excluding beneficiary certificates." In August 2026, the new M2 was published at ₩4,266.8 trillion (seasonally adjusted average balance, +0.9% from the previous month; +5.6% year on year on the unadjusted series).

**The point of the comparison.** When the same economy is measured at the same time with different "M2s," the growth rates diverge by 3 to 6 percentage points. In terms of this essay's classification of conflicts (Chapter 6), this is **Type B** (the indicator and definition differ, so there is no independent standard). Which one is the "true money stock" is not settled. The Bank of Korea excluded beneficiary certificates on the grounds that their "store-of-value function is low," and that judgment is itself a renegotiation of convention.

**Ratio to GDP.** The Bank of Korea explained that the ratio of new-standard M2 to nominal GDP was 154% at the end of Q3 2025, 3 percentage points below the long-term trend value (157%). This explanation came out together with the policy message that "liquidity is not excessive." The fact that the overhaul was announced at a time when claims were being made that "accommodative monetary policy is leaving excess liquidity unattended, pushing up the exchange rate and housing prices" is a case of "measurement and politics." This essay does not judge whether that timing was coincidence or intention. The Bank of Korea said it was work prepared since 2019, and the head of the financial statistics team explained that three years ago, when Statistics Korea drew up the Third Basic Plan for National Statistics Development, the Bank of Korea had applied to finish the monetary overhaul by 2025.

**Details of the overhaul**

- **Comparison with the long-term average.** The Bank of Korea explained that the new-standard M2 growth rate exceeded the long-term average (7.5%) during the COVID period but has been below the long-term average since January 2023. It also said the ratio of M2 to nominal GDP has been below the long-term trend value since Q1 2024.
- **Reclassification of economic-agent sectors.** The Foreign Exchange Stabilization Fund was moved from the central bank to central government, retirement-related trusts from other depository corporations to other financial institutions, and the civil service, military, and private school pensions from other financial institutions to central government. Work to subdivide investment funds and other financial institutions more finely was also carried out. No separate breakdown of the monetary impact of this reclassification has been disclosed.
- **Reason for parallel publication.** The Bank of Korea explained that, given the greatly increased interest in monetary indicators and the practical burden, it decided to run the new and old indicators in parallel for one year.
- **Stock-price sensitivity of the old M2.** In the October monthly statistics, published on the day of the overhaul announcement, the old M2 average balance rose ₩41.1 trillion (0.9%) from the previous month, with the stock-market rise cited as an influence. This shows that the old M2, in which beneficiary certificates have a large share, is sensitive to stock prices.

#### 1.6 The United States 2020: M1 Jumped, but M2 Stayed the Same

In the U.S. overhaul of May 2020, savings deposits were moved from non-M1 M2 to M1. Retroactive application extended back to May 2020. The overhaul was announced on December 17, 2020, and was reflected in actual figures from the release of February 2021.

- The M2 definition itself does not change in total, because both methods sum the same items. What changed is the **internal allocation** between M1 and non-M1 M2.
- According to Federal Reserve documents, the overhaul increased M1 by the entire balance of savings deposits (about $11.2 trillion as of May 2020), and M2 did not change. The Federal Reserve Bank of St. Louis's FRED Blog explains that M1 under the pre-overhaul definition would have been about $5 trillion in May 2020. By calculation, the new M1 jumped to the $16 trillion range. The share of other liquid deposits in M1 also changes from about 17% before the overhaul to about 70% after.

The Federal Reserve's H.6 release of July 28, 2026 shows a recent case with the same structure. On a seasonally adjusted basis, between October and December 2025, demand deposits within M1 rose by about $919 billion, from $5,708.1 billion to $6,627.3 billion, while other liquid deposits fell by about $823 billion, from $10,945.3 billion to $10,122.8 billion. Over the same two months, the M1 total rose only about $107 billion (0.6%), from $18.99 trillion to $19.09 trillion. The composition moved substantially within the total.

This case has the same structure as the reading of 1929–33 in Chapter 2. **Even when the aggregate (M2) is the same, if the composition (the allocation between M1 and non-M1 M2) changes, depending on which layer one looks at, it can become "the money stock surged" or "nothing changed."** In 1929–33 in the United States, the composition shifted as people converted deposits into cash (cash +30.5%, Anderson annual average), and in 2020 regulation moved the composition. The mechanisms of the two periods are completely different, but the point that "the aggregate and the composition are different questions" is the same (interpretation). The actual path of 1929–33 (liquidation of deposits, bank closures) is covered in Chapter 2.

#### 1.7 China 2025 and the Handling of Overhauls: Retroactive Revision, Parallel Publication, Break

China also revised its definition in 2025. The People's Bank of China announced an overhaul of the definition of M1 on December 2, 2024, and applied the new standard from the January 2025 data. According to the People's Bank's financial statistics report, the revised M1 consists of currency in circulation (M0), corporate demand deposits, personal demand deposits, and the customer reserves of non-bank payment institutions. The People's Bank recalculated each month-end M1 balance and growth rate for 2024 on a comparable basis and published them together. A commentary article (Caixin) reported that the overhaul would enlarge the M1 balance from about ¥63.3 trillion to ¥105.1 trillion, and the post-overhaul People's Bank report gives new-standard M1 as ¥109.44 trillion in February 2025 (+0.1% year on year) and ¥113.49 trillion in March (+1.6%). Although widening the definition changed the scale greatly, thanks to the retroactive recalculation the growth rates are compared on the same basis.

Here it becomes apparent that **how past values are handled** when an overhaul occurs differs from country to country.

- **Retroactive recalculation**: the United States (retroactively reflected back to the May 2020 observation) and China (2024 retroactively). The past is rewritten with the new definition to preserve the continuity of the time series.
- **Parallel publication**: Korea. The old M2 and new M2 are published together throughout 2026.
- **Separation and break between new and old**: Japan (June 2008). Retroactive data for the new series covering April 2003–March 2008 was provided, but the Bank of Japan itself stated that there is a discontinuity between the new and old series. The new M3 and the old "M3+CDs − money in trust" share the same scope of issuing institutions and financial assets, but differ because of the scope of holding sectors and estimation methods.

This classification is this essay's own summary. For series with retroactive recalculation, year-on-year comparisons continue on the same definition. During a parallel publication period, one must state whether a growth rate is the old or the new one. A series with a break is not read as continuous. The reasons for the definition change also differ by case: the United States is explained by regulation, Korea by international standards, Japan by financial structure (postal privatization), and China by changes in the means of payment (the rise of payment-app balances). Whatever the reason, the result is the same: an indicator of the same name counts a different object.

#### 1.8 Summary of This Chapter

- The U.S. H.6 definition of M2 and the May 2020 change; the 2006 discontinuation of M3.
- The ECB's definitions of M1, M2, and M3 and the differences from Korea (no items for beneficiary certificates and money in trust).
- The Bank of Japan's June 2008 overhaul of monetary statistics (the M1, M2, M3, L system, the break with the old series) and the position of L's components (investment trusts, money in trust).
- The functional classification principle in the Federal Reserve's FEDS Note (September 2026) and the discussion of stablecoins.
- The Bank of Korea's introduction of the new M2 and the parallel old-and-new figures (October 2025–August 2026).
- The IMF manual's distinction for investment fund shares (MMF shares included, other shares excluded).
- The People's Bank of China's January 2025 overhaul of M1 and the 2024 retroactive recalculation.

---

### The One Thing to Remember from This Chapter

> Even for an "M2" of the same name, the items it contains, the time at which the definition changed, and the treatment after the change (retroactive revision, parallel publication, break) differ. Before citing a number, first ask "which M2?"

---

### Sources (Chapter 1)

- Payne, K., & Styczynski, M.-F. (Sept. 4, 2026). "New Forms of Money and the U.S. Monetary Aggregates." FEDS Notes, Federal Reserve Board. https://www.federalreserve.gov/econres/notes/feds-notes/new-forms-of-money-and-the-u-s-monetary-aggregates-20260904.html
- Ford, H., & Styczynski, M.-F. (Nov. 12, 2024). "An Update to Measuring the U.S. Monetary Aggregates." FEDS Notes. https://www.federalreserve.gov/econres/notes/feds-notes/an-update-to-measuring-the-u-s-monetary-aggregates-20241112.html
- Federal Reserve Board. H.6 "Money Stock Measures" and the H.6 technical Q&A, overhaul notices (Dec. 17, 2020; Feb. 23, 2021), release of July 28, 2026 (change in method of deducting IRA and Keogh balances) https://www.federalreserve.gov/releases/h6/20260728/
- Federal Reserve Bank of St. Louis. FRED Blog, "Savings are now more liquid and part of 'M1 money'".
- European Central Bank. "Monetary aggregates." https://www.ecb.europa.eu/stats/money/aggregates/aggr/html/hist.en.html
- Bank of Japan. Money Stock preliminary figures (August 2026, published Sept. 9, 2026) https://www.boj.or.jp/statistics/money/ms/ms2608.pdf ; "Revision of the Monetary Survey" (May 16, 2008), "Release of the New Series Retroactive Data of the Money Stock Statistics" (June 3, 2008) https://www.boj.or.jp/en/statistics/outline/notice_2008/ntms25.htm
- International Monetary Fund. Monetary and Financial Statistics Manual and Compilation Guide (pre-publication draft Mar. 22, 2016; official publication Nov. 2017), Press Release 16/127. https://www.imf.org/external/np/sec/pr/2016/pr16127.htm
- People's Bank of China. Financial Statistics Report (January–May 2025 issues), note on the 2025 M1 revision. Caixin, "Commentary: China's Changes to M1 Money Supply Will Curb Volatility" (Dec. 4, 2024).
- Bank of Korea, "Results of the Overhaul of Money and Liquidity" (Dec. 30, 2025) and the monthly "Money and Liquidity" (Oct. 2025–Aug. 2026); confirmed through multiple reports: Herald Business (헤럴드경제) (Dec. 29, 2025), Financial News (파이낸셜뉴스) (Dec. 16, 2025; July 15, 2026), Newsis (뉴시스) (Dec. 16, 2025), The Fact (더팩트) (Dec. 16, 2025), Asia Economy (아시아경제) (Jan. 14, Feb. 13, Mar. 13, Apr. 15, July 15, 2026), Ajunews (아주경제) (June 16, 2026), SBS Biz (Oct. 15, 2026), Kyunghyang Shinmun (경향신문) (Dec. 16, 2025), Today Newspaper (투데이신문), Joseph Tax News (조세일보), and Economic Daily (이코노믹데일리) (Dec. 30, 2025, item-by-item changes in the overhaul results).

---

## Chapter 2. Monetary Collapse on the Deflation Side (United States, 1929–33)

 

---

### For First-Time Readers: How Do Bank Deposits Become "Money," and How Do They Disappear?

#### 0.1 A Deposit Is a "Promise," Not "Cash"

Just because 1 million won is printed in your passbook does not mean your 1 million won is sitting in the bank's vault as it is. A deposit is a promise the bank has written down: "we will convert it into cash for you whenever you want."

A bank keeps only part of the money it receives in its vault and lends out the rest to other people. The borrower puts that money into their own account or pays it to someone, and that money becomes a deposit at some bank again. In this way a single banknote comes to support the promises of several deposits. That is why the money stock including deposits (M1, M2) is larger than the number counting only cash (the monetary base).

#### 0.2 If Everyone Comes to Withdraw at Once

Ordinarily there is no problem. Not all depositors withdraw cash on the same day. But when a rumor spreads that "this bank is in danger," people rush to withdraw cash. This is a bank run.

The bank, short of cash in its vault, must hurriedly call in loans or sell assets at fire-sale prices. Then lending shrinks, and the deposits that had been created through lending shrink along with it. If a bank closes, that bank's deposits are simply frozen.

#### 0.3 So What Decreased and What Increased?

While bank runs spread, cash in people's hands increased and deposits in their accounts decreased. Cash rose, but the fall in deposits was far larger than the rise in cash. As a result, the money stock, "cash + deposits" combined, fell.

The question this essay deals with arises here. When a newspaper writes "the money stock fell by one third," it becomes a different story depending on whether it counted cash, counted deposits, or counted the two combined.

#### 0.4 A Plain-Language Glossary

- **Bank run.** A phenomenon in which depositors rush all at once to convert their deposits into cash.
- **Monetary base.** Money issued directly by the central bank. It is cash in circulation plus the reserves banks hold at the central bank.
- **Deposit money.** The portion of bank deposits that is included in the money stock.
- **Peak-to-trough.** The rate of change obtained by directly comparing the highest month with the lowest month. It captures a single extreme as it is.
- **Annual average.** The rate of change obtained by comparing average balances over a year. If the sharp decline was concentrated in a few months, the average dilutes that shock.

---

### 1. One Phenomenon, Several Numbers

#### 1.1 Listing the Figures One Line at a Time

The figures below follow the compilations of Friedman–Schwartz and Anderson, and the starting and ending values of monthly M1 were cross-checked again against the NBER Macrohistory Database (via FRED).

**Friedman–Schwartz (F–S, 1963) monthly table**

- M1: October 1929 28,264 → April 1933 19,039, **−32.6%**. However, October 1929 has a one-month spike mixed in, so using September (26,415) as the base gives **−27.9%**. The October value is 7.0% higher than September's.
- Currency + total deposits: August 1929 46,278 → March 1933 29,970, **−35.2%**.
- Total deposits of commercial banks: **−42.3%**.

**Anderson (2003) annual averages** (the F–S series table in Historical Statistics of the United States, annual average)

- M1 **−25.3%**, M2 **−30.9%**, total deposits **−36.5%**, currency **+30.5%**.
- Period: annual average 1929 versus 1933, with all peaks in 1929 and all troughs in 1933.
- Level values (in billions of dollars, 1929 → 1933): currency 3.90 → 5.09, demand deposits 22.74 → 14.82, M1 26.64 → 19.91, commercial bank total deposits 42.70 → 27.13, M2 46.60 → 32.22, M3 55.20 → 41.52, M4 60.99 → 48.09.
- From the same table, **M3 is −24.8%** and **M4 is −21.1%** (calculated). This −21.1% is the source of the "−21%" lower bound below.
- Note on definitions: F–S's M1 is currency held by the public plus commercial bank demand deposits, and **F–S's M2 is currency plus commercial bank total deposits**. M3 is M2 plus mutual savings bank and postal savings deposits, and M4 is M3 plus savings and loan association shares. **F–S's M2 is not the same as any currently published indicator, and what resembles the current Federal Reserve M2 is rather F–S's M4.** When this chapter writes "M2 −30.9%," it means F–S's M2, not a figure for today's M2.

**January–March 1933.** In two months, total deposits fell by 16%. This was the period when bank closures were concentrated.

**Bernanke (2004).** In a March 2004 speech, he said that the money stock (the sum of currency and bank deposits) fell by about one third in 1929–33, and that from December 1930 until the bank holiday of March 1933 about half of all banks were closed or merged into other banks. He also explained that the surviving banks, rather than expanding deposits and lending to fill the gap, shrank considerably.

**Greenwood (2017, Cato Journal).** He writes that the money growth rate was negative year on year from November 1929 to January–February 1934, and that the cumulative decline in 1929–33 was **M2 −38% and M1 −32%**. The source of his Figure 5 is shown as Friedman and Schwartz (1963). The author, John Greenwood, is chief economist at Invesco, and the whole paper is written from the position that "central banks should design policy on the basis of broad money growth." The figures are transcribed as they are, but the interpretation should be read as that position's.

**The range from −21% to −42%.** The decline in the 1929–33 money stock diverges from −21% to −42%. The smallest value, −21.1%, is **F–S's M4** (the broadest aggregate, which includes even savings and loan association shares) on Anderson's annual average, and the largest value, −42.3%, is **commercial bank total deposits** on the monthly peak-to-trough. The two differ in both definition (M4 versus deposits) and window (annual average versus monthly peak-to-trough). Looking at monetary aggregates alone, it runs from −21% (F–S M4 annual average) to −38% (Greenwood's cumulative M2), and including bank deposits it is −42%.

#### 1.2 Three Reasons the Numbers Diverge

**First, which M is used.**

- Looking at cash alone, it rose (+30.5%); M1 is −25.3% to −32.6%; F–S M2 is −30.9% to −38% (Greenwood); and commercial bank total deposits are −36.5% to −42.3%.
- Widening the aggregate does not make the decline keep growing. M3 (−24.8%), which adds mutual savings bank and postal savings deposits to F–S's M2 (−30.9%) that includes only commercial bank deposits, and M4 (−21.1%), which further adds savings and loan association shares, actually fell less.
- Calculation: M3 − M2 goes from 8.60 → 9.30 (+8.1%), and M4 − M3 from 5.79 → 6.57 (+13.5%) (in billions of dollars, Anderson annual average). The balances of savings institutions outside commercial banks did not decline. Whether that increase was due to a shift toward savings institutions or to other factors cannot be determined from this table alone.

**Second, peak-to-trough or annual average.**

- F–S's monthly peak-to-trough captures a single month's extreme as it is. Anderson's annual average blends twelve months.
- The more briefly the sharp decline is concentrated, the larger the gap between the two methods. Since total deposits fell 16% in the two months of January–March 1933 alone, measuring such a period by average dilutes the shock.
- This essay interprets a substantial part of why even the same M1 diverges by 7.3 percentage points between F–S's −32.6% (peak-to-trough) and Anderson's −25.3% (annual average) as lying here. Since the periods of the two figures differ, no exact decomposition is made.

**Third, where the period is cut.**

- F–S M1 runs from October 1929 to April 1933, and the same M1 with a September base is −27.9%. A single starting month moves it by 4.7 percentage points.
- Currency + total deposits runs from August 1929 to March 1933. The starting and ending months differ from M1's.
- Greenwood's M1 −32% is almost the same as F–S's −32.6%, while his M2 −38% is larger than Anderson's −30.9%. Since there is no guarantee that the periods and aggregation methods are the same, this essay does not judge the reason for the difference.

Because these three overlap, "−21% to −42%" is not the width of a measurement error. In this essay's classification (Chapter 6), it is **Type A** (the object itself is not defined as a single value) overlapped with **Type B** (differences in indicator and definition).

---

### 2. What Cash +30.5% Says

#### 2.1 First, a Misreading

It is easy to read "cash +30.5%" as "the substance of the M2 collapse," but this is an over-interpretation.

- Cash is contained in both M1 and M2.
- So if $1 of deposits turns into $1 of cash, the totals of M1 and M2 do not change. One side falls and the other rises by the same amount.
- Therefore what reduced the total was not "deposits → cash movement" but **the portion by which deposits fell beyond the increase in cash**.

What cash +30.5% shows is not "the reason the total fell" but the fact that "while the total was falling, the composition tilted toward cash" (interpretation).

#### 2.2 Small in Size, Cash Could Not Protect the Total Even by Growing a Lot (Calculation)

Let us tie Anderson's three figures into a single equation. M2 is, by F–S's definition, currency + total deposits, and the three figures cover the same period (annual average 1929 versus 1933).

- Let s be the share of cash in initial M2; the share of deposits is then 1 − s.
- The rate of change of M2 = (1 − s) × (rate of change of deposits) + s × (rate of change of cash).
- Substituting values: −30.9 = (1 − s) × (−36.5) + s × (+30.5).
- Rearranging: −36.5 + s × 67 = −30.9, so s = 5.6 / 67 ≈ **0.084**.

That is, the calculation says cash was about 8% of initial M2. Even though cash grew 30.5%, it added only +2.6 percentage points to M2 (8.4 × 0.305), while the fall in deposits cut away 33.4 percentage points (91.6 × −0.365). Together this is −30.8 percentage points, consistent with −30.9% within rounding error.

**Checking directly with level values (in billions of dollars).**

- 1929 M2 = cash 3.90 + total deposits 42.70 = 46.60, and cash's share is 3.90 ÷ 46.60 = **8.4%**.
- 1933 M2 = cash 5.09 + total deposits 27.13 = 32.22, and cash's share is 5.09 ÷ 32.22 = **15.8%**.
- Decomposition of the change: cash +1.19 (5.09 − 3.90), total deposits −15.57 (27.13 − 42.70), for a total of −14.38. The fall in deposits was about 13 times the rise in cash (15.57 ÷ 1.19 ≈ 13.1).
- The back-calculated value of 8.4% above matches the directly computed 8.4%.
- Total deposits ÷ cash fell by about half, from 42.70 ÷ 3.90 ≈ **10.9** to 27.13 ÷ 5.09 ≈ **5.3**. This ratio is used in the multiplier discussion in Section 3.3.
- Commercial banks' time and savings deposits (total deposits − demand deposits: 19.96 → 12.31, −38.3%) fell more than demand deposits (−34.8%).

This calculation serves one purpose. **Cash is small, so even when it grows it cannot protect the total.** Put the other way around, the large mass of the money stock was deposits, and so one can argue that it is more accurate to call this event a "deposit collapse" than a "monetary collapse." This essay does not judge which name is correct.

#### 2.3 Why Did Deposits Fall?

There are several candidate mechanisms, and only the monetary-side channels are noted here.

- **Debt liquidation (Fisher, 1933).** In the process of paying off debts, deposit money contracts and prices fall. This is a claim Fisher himself wrote as "tentative," and the BIS regards empirical evidence for this channel as "scarce and anecdotal."
- **Collapse of credit intermediation (Bernanke, 1983).** The claim is that banks became unable to lend, which hit the real economy.
- **The debate over the causes of bank failures.** Calomiris–Mason (2003b) hold that failures are broadly explained by fundamentals, and that only the surge in bank failures in early 1933 is not explained by fundamentals. This is the claim that the effect of panics was limited.

Which of these channels was the main one is an open question, and this essay adds no judgment.

#### 2.4 Interpretation: The Road from Deposits to Cash Is the Road Down the "Ladder of Promises"

Let us add an analogy. Money-like things form layers according to **who made the promise**.

- Layer 1: cash and reserves issued by the central bank (the monetary base).
- Layer 2: commercial bank deposits. This is the promise by a bank that "we will convert it to cash if you ask."
- Layer 3: promises of the same kind made by financial firms outside the banks (mutual savings banks and postal savings, savings and loan association shares, today's MMFs, and so on).

In ordinary times, all layers are used as "nearly the same money." But when people stop trusting the party making the promise, they move down from the upper layers to the lower ones. The "deposits → cash" of 1929–33 was a descent from Layer 2 to Layer 1. This analogy resembles concepts in the literature such as outside money and inside money, but it is only an analogy and does not transcribe that literature's claims.

The calculation in Section 1.2 (M3 and M4 fell less) shows a possibility consistent with this analogy. It is that not everyone descended only from Layer 2 to Layer 1, but that part of Layer 3 (savings institutions outside commercial banks) may have held steady or grown. But this is only a possibility; the reason has not been confirmed.

---

### 3. The Monetary Base Rose, but M2 Fell

#### 3.1 Greenwood's Footnote

Greenwood (2017) writes that the U.S. monetary base rose in 1931–32, and explains the reason in footnote 6. The monetary base rose not because the Fed bought assets, but mainly **because the public converted deposits into cash**, and **because banks decided to build up more reserves**.

This sentence shows two things.

- The monetary base (M0) and M2 may not move in the same direction. In 1931–32, the monetary base rose and M2 fell.
- According to Greenwood's explanation, the reason the monetary base rose was itself "the shift from deposits to cash" and "banks' expansion of reserves."

This is the same phenomenon as the "change in composition" seen in 2.1, viewed from the monetary-base side. This pattern appears in reverse in Japan in Chapter 4. There is an argument that in Japan the monetary base rose greatly while M2 barely moved (Greenwood, same paper), and now the monetary base is falling while M2 is actually rising.

#### 3.2 The Claim Greenwood Draws from This Comparison

Greenwood builds his argument with this comparison. In 1929–33 the Fed did not respond to the monetary contraction, but in 2008–11 the Fed purchased securities **from the non-bank sector**, creating new deposits, and so avoided a monetary contraction. The figures he cites are as follows.

- From November 2008 to Q4 2011, U.S. commercial bank loans and leases fell by a cumulative 14%.
- Yet the M2 growth rate averaged 6.8% a year from January 2009 to October 2013.

These figures should be read together with the author's position (a broad-money focus, the view that QE purchasing from non-banks is the correct design). This essay does not judge whether this policy claim is right or wrong, and takes only the figure itself: "even when loans fell 14%, M2 could rise." This too is a fact connected with this essay's larger question: "the movement of M2 can be separate from the movement of loans."

#### 3.3 Why the Money Stock Can Fall Even as the Monetary Base Rises: Decomposing the Multiplier (Calculation)

The money stock M can be written as the monetary base H multiplied by a **multiplier m**. Let cash be C, deposits D, and bank reserves R, and set M = C + D and H = C + R. Then:

- m = M ÷ H = (C + D) ÷ (C + R) = **(c + 1) ÷ (c + r)**. Here c = C ÷ D (the cash-to-deposit ratio) and r = R ÷ D (the reserve-to-deposit ratio).

This equation is an **ex post identity** derived from the definitions. When the public converts deposits into cash, c rises, and when banks build up reserves out of anxiety, r rises, so even if H stays the same or increases, m can fall and M can decline. A hypothetical example (not measured values): if c = 0.10 and r = 0.10, m = 1.10 ÷ 0.20 = 5.5, and if c = 0.25 and r = 0.20, m = 1.25 ÷ 0.45 ≈ 2.8, nearly halved. If H is the same, M falls by the same proportion.

As measured evidence, there is the fall in the total deposits/cash ratio calculated in Section 2.2 (about 10.9 → 5.3, that is, c = 3.90 ÷ 42.70 ≈ 0.091 → 5.09 ÷ 27.13 ≈ 0.188). This means c roughly doubled.

Friedman and Schwartz (1965, *The Great Contraction, 1929–33*) applied this identity to actual data and calculated the effects of each factor from August 1929 to March 1933. They explain that if only the monetary base had changed, the money stock would have risen by about 17½%; the fall in the deposit/currency ratio alone would have produced −37%; the fall in the deposit/reserve ratio alone, −20%; and the interaction between the two ratios, +10%; and that these three turned the monetary base's +17½% into an actual −35% decline. Extended to the trough in April 1933, the same order gives +13, −35, −19, +9, and a total decline of −35.7%. Each number is the effect "if only that factor had changed," and since there is a separate interaction term, they do not simply add up to −35%. The same book states that the deposit/currency ratio fell from 11.5 in October 1930 to 4.1 in March 1933, and the deposit/reserve ratio from 12.9 to 8.4, and explains that as the two ratios returned to their levels of the early twentieth century and of 1912 respectively, both the expanded use of deposits and the economizing of reserves of the 1920s were wiped out. Converting to the inverse of the deposit/currency ratio, c rose from about 0.087 to about 0.244, which is in the same direction as the annual-average calculation of 0.091 → 0.188, with the monthly extreme values being larger (calculation).

How the multiplier actually operated is also in the same book. From August 1931 to January 1932, the cash held by the public increased by $720 million while the increase in the monetary base was $330 million, so the remaining $390 million had to come out of bank reserves. Because banks could not lower their ratio of deposits to reserves, the multiplier operated at about 14, and deposits fell by $5.73 billion (15% of the August level). In January–February 1933, the multiplier was not 14 but 29, and in a single month deposits fell by more than $2 billion (about 7½% of the already reduced total).

This multiplier should be read as an **accounting identity**, not a causal model. The causal claim that "if the monetary base is increased, the money stock grows by a factor of m" requires the textbook assumption that banks first gather reserves and then lend. The Bank of England directly refuted this assumption in "Money creation in the modern economy" in its Quarterly Bulletin of March 2014 (2014 Q1). The explanation is that today banks do not receive deposits and then lend; they create deposits as they make loans, and they do not create loans by multiplying central bank money. The two readings have different uses. The identity is useful for dissecting periods like the 1930s when c and r changed drastically, and one must be careful about using it as a causal proposition, as seen in Japan's QE (Chapter 4).

#### 3.4 How Many Banks Closed: Three Accounts

- Wicker (preface to *The Banking Panics of the Great Depression*): More than 9,000 banks closed between 1930 and 1933, which was about 30% of the number of banks at the end of 1929. The surges came in four episodes: November 1930–January 1931, April–August 1931, September–October 1931, and February–March 1933, and 60% of closures in 1930–32 occurred at times other than panics. After the bank holiday of March 1933, about 3,400 banks were not granted permission to reopen.
- Bernanke (2004): From December 1930 to March 1933, about half of all banks were closed or merged.
- A university lecture note: an account that the number of operating commercial banks fell by more than one third.

The three accounts differ in what is counted (suspensions versus closures and mergers versus net decrease), the period (1930–33 versus December 1930–March 1933), and the denominator (the number of banks at the end of 1929 versus the number of operating banks), so they cannot be asserted to contradict one another. This essay classifies this as Type A+B. When citing, the object counted and the period must be stated together. Wicker's account that about two-fifths of the closures occurred during panics is worth reading alongside Calomiris–Mason (a fundamentals-centered interpretation) in Section 2.3 (interpretation).

---

### 4. Other Periods That Raised the Same Question

#### 4.1 United States 1920–21

In this period prices fell by 13% (Balke–Gordon), 14.8% (Romer), or 18% (Department of Commerce), depending on the estimate, and wholesale prices fell −36.8%. Over the same period the money stock was M1 −9.4% and M2 −5.6% (annual average), a much smaller decline than prices.

- In 1920–21, prices moved more than the money stock.
- In 1929–33, the money stock fell by nearly one third, and consumer prices fell by about one quarter (BIS Box 1).
- Placing the two periods side by side, the simple picture that "money and prices move in the same proportion" does not fit. However, this essay does not judge causation.

#### 4.2 Summary

- Even for the same "monetary decline," 1920–21 was not accompanied by a collapse of deposits (the period is summarized as short and violent), whereas in 1929–33 about half of all banks closed.
- More than which M is used, **what shrank** within that M may be a clue that explains the difference between the two periods (interpretation).

#### 4.3 2008 and 2023: Runs That Began Near the Boundary

In the modern era too there have been events in which deposits or deposit-like things drained away, and they began near the boundary of M2.

- **2008 MMFs.** On September 16, 2008, the Reserve Primary Fund (about $65 billion in assets under management) cut its net asset value from $1 to $0.97 because of losses on Lehman commercial paper. According to the New York Fed, over the following two days about $200 billion (10% of assets) left prime MMFs, and more than 90% of the redemptions were by institutional investors. Yale's YPFS summarizes that about $300 billion was withdrawn within a week. The run stopped when the Treasury announced its MMF guarantee program on September 19 and the Fed opened its MMF liquidity facility the same day. But as seen in Chapter 1, Section 1.2, the only MMFs that go into U.S. M2 are retail MMFs, and institutional MMFs used to be on the M3 side. The heart of the crisis was outside M2, and this was after the Fed had stopped publishing M3 in 2006. This is a case showing that **the boundary of an aggregate may not coincide with the boundary of what is "used like money"** (interpretation). This essay does not claim that continuing to publish M3 would have signaled this episode in advance.
- **2023 SVB.** The Fed's Vice Chair for Supervision testified in the Senate that withdrawal requests of about $42 billion came in on March 9, 2023 alone, and that about $100 billion more was scheduled to go out the next morning (CNBC and AP reports). 93–94% of deposits exceeded the insurance limit, and on March 12 regulators announced that they would protect even uninsured deposits under a systemic risk exception and opened a separate lending program. A dollar of M2 in the aggregate is **a mix of deposits within the insurance limit and deposits above it**. Even for the same total, the likelihood of a run differs. The aggregate shows the average, and vulnerability hides in the composition (interpretation).

#### 4.4 How the 2022–23 Decline in M2 Differed from the 1930s

- U.S. M2 grew at a pace above 25% year on year in 2020–21 (peaking in early 2021, 26–27% depending on the compilation). After peaking at about $21.75 trillion in April 2022, it then fell about 4.9% through October 2023, and the −4.6% year on year in April 2023 was the largest decline since 1959, when the Fed began officially tracking M2. Many reports said that a decline of 2% or more a year was the first since the Great Depression.
- The peak month and the size of the decline vary with the data revision vintage. Reports in mid-2023 gave the peak as July 2022 (about $21.7 trillion) and the decline as about 4.7%, while the current vintage sees April 2022 as the peak. On the most recent vintage, M2 regained its old peak in April 2025 and is on a record run at about $23.2 trillion in June 2026. That is about 6.7% above the old peak (calculation).
- The point is that a "decline in M2" that looks similar in numbers had a different outcome. In 1929–33, deposits came down into cash and banks closed, so c roughly doubled (Section 3.3: 0.091 → 0.188). The decline of 2022–23 reversed part of the scale of the 2020–21 expansion and did not lead to a collapse of the same structure.
- Therefore the fact that "M2 fell" alone cannot speak of a crisis, and it is likely that **what went where** decided the outcome (interpretation).

---

### 5. Proof and Verification

From here on we re-confirm the preceding account with numbers. Even if you skip it unread, the earlier story continues.

#### 5.1 Recalculating the F–S Rates of Change

- M1: 19,039 ÷ 28,264 = 0.6736, that is, **−32.6%**.
- M1 on a September base: 19,039 ÷ 26,415 = 0.7208, that is, **−27.9%**. The October value of 28,264 is 7.0% higher than September's 26,415 (28,264 ÷ 26,415 = 1.070), consistent with the October value being a one-month spike.
- Currency + total deposits: 29,970 ÷ 46,278 = 0.6476, that is, **−35.2%**.

#### 5.2 The Width Created by Differences in Period

Compare the three M1 figures.

- Peak-to-trough (October base): −32.6%
- Peak-to-trough (September base): −27.9%
- Annual average: −25.3%

The choice of starting month alone moves it by 4.7 percentage points, and the method (peak-to-trough versus annual average) alone moves it by a further 2.6 percentage points. However, since the periods in the second comparison are not exactly the same, it is not asserted to be "the effect of the method alone."

#### 5.3 Where Greenwood's Figures Stand

- M1: Greenwood −32%, F–S −32.6%. A 0.6-percentage-point difference.
- M2: Greenwood −38%, Anderson −30.9%. A 7.1-percentage-point difference.
- The periods of the two M2 figures differ (Greenwood: the cumulative change over the whole interval in which the year-on-year growth rate was negative; Anderson: annual average), so they cannot be compared directly. This essay places the two figures only in parallel.

---

### 6. Summary of This Chapter

- Greenwood's (2017) M2 −38% and M1 −32%, the reason for the monetary base increase (footnote 6), and loans −14% and M2 6.8% a year in 2008–11.
- The arithmetic consistency of the F–S monthly M1 and Anderson annual-average figures (M1 −32.6%/−27.9%, currency + total deposits −35.2%, cash share 8.4% → 15.8%, M3 −24.8%, M4 −21.1%).
- Bernanke's (2004) money stock of about −1/3 and about half of banks closed or merged. Wicker's scale of bank closures.
- The multiplier identity and the measured change in the cash/deposit ratio c (0.091 → 0.188).
- The dates and scale of the 2008 MMF and 2023 SVB events, and the peak and trough of the 2022–23 decline in M2.

---

### The One Thing to Remember from This Chapter

> The sentence "the money stock fell by one third" must be accompanied by the definition (which M), the window (annual average or monthly peak-to-trough), and the caveat that F–S's "M2" is not today's M2. The range from −21% to −42% is the width created by these three things.

---

### Sources (Chapter 2)

- Greenwood, J. (2017). "The Japanese Experience with QE and QQE." Cato Journal, 37(1), 17–38. https://www.cato.org/cato-journal/winter-2017/japanese-experience-qe-qqe
- Bernanke, B. S. (Mar. 2, 2004). "Money, Gold, and the Great Depression." H. Parker Willis Lecture. https://www.federalreserve.gov/boardDocs/speeches/2004/200403022/default.htm
- Anderson, R. G. (2003). "Some Tables of Historical U.S. Currency and Monetary Aggregates Data." St. Louis Fed Working Paper 2003-006; Historical Statistics of the United States, Millennial Edition, Table Cj42–48.
- Friedman, M., & Schwartz, A. J. (1963). A Monetary History of the United States, 1867–1960. NBER Macrohistory DB monthly series (FRED: M1474AUSM027SNBR, M1475AUSM027SNBR).
- Friedman, M., & Schwartz, A. J. (1965). The Great Contraction, 1929–33, "Factors Accounting for Changes in the Stock of Money." Princeton University Press (NBER). https://www.nber.org/system/files/chapters/c9275/c9275.pdf
- McLeay, M., Radia, A., & Thomas, R. (2014). "Money creation in the modern economy." Bank of England Quarterly Bulletin 2014 Q1. https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy
- Cipriani, Holscher, Martin et al. (2012). "Money Market Funds and Systemic Risk." Liberty Street Economics, New York Fed. https://libertystreeteconomics.newyorkfed.org/2012/06/money-market-funds-and-systemic-risk/ ; Yale YPFS, "Temporary Guarantee Program for Money Market Funds" (2016).
- Fisher (1933), Bernanke (1983), BIS (2015), Calomiris & Mason (2003b), and other literature cited in the Deflation installment.
- Wicker, *The Banking Panics of the Great Depression*, preface (publisher's excerpt). CNBC and AP (SVB withdrawal reports).
- U.S. M2 in 2022–23: S&P Global Market Intelligence (May 2023), The Motley Fool/YCharts (2025), thetrading.tools (Aug. 2026, based on Fed H.6/FRED M2SL).

---

## Chapter 3. The Shift of the Monetary Boundary on the Hyperinflation Side (Hungary, Zimbabwe, Venezuela, Greece, Yugoslavia)

The facts of this chapter are based on the literature of Cagan (1956), Hanke–Krus, Hanke & Kwok (2009), IMF PIN 09/53, Petrović–Bogetić–Vujošević (1999), Nielsen (2004), Uvalić (2022), Makinen, Paal (2000), Rodríguez, and others, and the 2026 Venezuela figures were confirmed through multiple media reports of the central bank's announcement (secondary confirmation).

 

---

### Plain Explanation: When Money Is Dying, How Do You Measure the "Quantity of Money"?

Suppose a country's money loses half its value every day.

- When you receive your salary, it pays to spend it that very day, because if you let it sit a day, its value is cut in half.
- Shopkeepers change their price tags every day, and some shops say they will accept dollars or gold instead of the domestic banknotes.
- The government tries not to take taxes in banknotes as they are but to index them to prices. Hungary's adópengő was such a device.

Suppose a statistician now asks, "How much money is there in this country right now?" If you count only the amount of banknotes issued, an answer comes out. But what people actually use in transactions is not only banknotes. Indexed units, foreign currency, gold, and de facto local currencies are mixed in.

So the core sentence of this chapter is this.

- **The "quantity of money" is a number that changes depending on what is counted. Hyperinflation is the laboratory that shows that fact in its most extreme form.**

First, a summary of terms.

- **Cagan's M**: the monetary aggregate used in Cagan's (1956) analysis, namely paper money (banknotes) issued by banks. Deposits and substitute currencies are not included.
- **Notgeld / Goldanleihe**: emergency money issued by local governments, firms, and others during the German hyperinflation, and certificates in the nature of gold-linked bonds. They are left out of Cagan's M.
- **adópengő (tax pengő)**: a price-indexed unit that Hungary introduced on January 1, 1946.
- **OMIR (implied exchange rate)**: a method that Hanke & Kwok (2009) used for Zimbabwe, which derives an implied exchange rate from the ratio of the share prices of Old Mutual, dual-listed in London and Harare.
- **QFA (quasi-fiscal activities)**: activities in which the central bank performed fiscal roles on the government's behalf. They include methods other than money issuance.
- **Relative PPP**: a method that assumes the rate of change of the exchange rate follows the difference between the rates of price change in the two countries, and back-calculates the inflation rate from the change in the exchange rate.

When comparing figures with one another, first check that the units and periods are the same. Calculations and inferences are written out in the text in phrases such as "by calculation" and "this is an estimate."

---

### 1. What Did Cagan's M Count?

Cagan's M is banknotes.

- The Hyperinflation installment pointed out that paper money alone can underestimate total liquidity.
- In the case of Germany, Notgeld and Goldanleihe are left out of this aggregate.
- That Cagan's 50%-per-month criterion is "purely arbitrary" is also a fact confirmed in the Hyperinflation installment.

The lesson to be drawn here is simple.

- Even M, one of the key numbers in hyperinflation research, is already the result of **a choice about "what to count as money."**
- This does not mean the choice was wrong. Since the issuance of banknotes was the direct instrument of the inflation tax, counting banknotes is reasonable. However, the more substitute means are used, the further this number can drift from people's actual liquidity.

---

### 2. Hungary 1945–46: Two Units Circulated at the Same Time

#### 2.1 The Facts

- November 1945: monthly money growth rate 233%, inflation 434%. Real balances were about 3.4% of their 1938 level.
- January 1, 1946: the adópengő was introduced. At first 1 adópengő = 1 pengő, and the conversion ratio was announced every morning at 8 o'clock.
- In the six zones of the postal rate table in July 1946, the pengő/adópengő ratio ranged from 160×10¹³ to 500×10¹⁷ (HPSGB, Morgan 2003).
- August 1, 1946: the forint was introduced. 1 forint = 4×10²⁹ pengő = 2×10⁸ adópengő.
- The peak monthly inflation was 4.19×10¹⁶ % in July 1946, 207% daily, with prices doubling in about 15.0 hours (Hanke–Krus table).

#### 2.2 Verification

- Dividing 4×10²⁹ by 2×10⁸ gives 2×10²¹. That is, at the time of the forint, 1 adópengő corresponds to 2×10²¹ pengő. The two conversion values mesh with each other without contradiction (multiplied, they give 4×10²⁹).
- The 2×10²¹ at the forint conversion point is larger than the maximum ratio of 5×10¹⁹ in the July 1946 postal rate table. If the two values are ratios on different dates, this is a natural size relationship.
- 4×10²⁹ ÷ 3.81×10²⁷ ≈ 105 times. Cagan's 3.81×10²⁷ is the 12-month cumulative from August 1945 to July 1946 and 4×10²⁹ is a conversion ratio, so the earlier Hyperinflation installment estimates this gap to be a difference of basis. Because the base periods and values of cumulative rises differ across sources (one collectors' commentary gives August 1945–July 1946 as about 3×10²⁵), this essay does not put the ratio of 105 forward as a single fact and relays it only as an estimate.
- There is a figure on the money side too. Salemi (Econlib) summarizes that over the same period (August 1945–July 1946) the money stock grew about 1.19×10²⁵ times. Compared with prices of 3.81×10²⁷ times, the calculation says real money balances shrank to about 1/320, that is, to around 0.3% of the initial level (3.81×10²⁷ ÷ 1.19×10²⁵ ≈ 320). On the velocity side, in a calculation cited by an additional study of the Hungarian hyperinflation, the velocity growth rate, which was 24.05% in the month right after the adópengő's introduction in January 1946, accelerated to 266.67% in February and 523.13% in March. That velocity actually accelerated right after the indexed unit was introduced is consistent with the account of side effects in Section 2.3.

#### 2.3 What This Scene Means for the Monetary Boundary

- If you count only the pengő, one number comes out, and if you count the adópengő as well, a different number comes out. When the conversion ratio between the two units moves by tens of times a day, the operation of "summing" itself is not defined.
- The Hyperinflation installment also noted a side effect of the adópengő structure. When banks deposited adópengő deposits with the central bank in the same unit, the central bank's liabilities became in effect indexed, real interest rates soared, and this invited further issuance of pengő.
- That is, **creating a new monetary unit was both changing the boundary of the monetary aggregate and changing the inflation path itself.**

#### 2.4 Paal (2000) and Remeasurement

- The Hyperinflation installment summarizes that Paal (2000) remeasured an aggregate combining the pengő and the adópengő. Based on the abstract, the conclusion is that inflation is less extreme and seigniorage is positive throughout the period. The abstract does not say less extreme compared with what, so the size of the conclusion is not cited.
- Note on terminology: applying a modern "M2" to Hungary at that time would be anachronistic, so we will call it only a "monetary aggregate."

---

### 3. Zimbabwe 2007–09: The Statistics Stopped and Foreign Currency Came In

#### 3.1 How Was It Measured?

- Table 1 of Hanke & Kwok (2009) lists the monthly inflation published by the RBZ for March 2007–July 2008, and states that the authors calculated August 2008–November 14.
- The authors' calculation is relative PPP using the OMIR, and assumes ΔP_US = 0. It is an exchange-rate-based estimate, not a consumer price measure.
- Result: on November 14, 2008, 7.96×10¹⁰ % per month, 98.0% daily, and about 24.7 hours until prices doubled. Hanke also writes the 12-month-basis rate of increase at the same point as 89.7 sextillion % (about 9×10²² %), which is an annual figure reported separately from the monthly value. He also states that the last official figure was July 2008 (231 million percent a year).
- Verification: Hanke's "30 million times" is the monthly peak ÷ the last official monthly figure. 7.96×10¹⁰ ÷ 2,600.24 ≈ 3.06×10⁷ checks out.

#### 3.2 A Conflict in the Record of When Statistics Stopped

- Hanke & Kwok (2009): the RBZ reported March 2007–July 2008, the last available figure is July's, and it was released only in October.
- The arXiv paper: writes that the CSO stopped providing inflation data in October.
- The two accounts conflict. Reports at the time sometimes write the July 2008 figure (231 million percent a year) as announced by the Central Statistical Office (CSO) on October 8 and sometimes as issued by the central bank (RBZ). So the conflict appears to be a difference in attribution at the reporting stage, and this essay does not decide who actually made the announcement. That the last official figure is July's also agrees with Hanke's account.
- What stopped was **price statistics**, and there is no basis in this chapter that monetary aggregate statistics stopped.

#### 3.3 QFA: Money Creation Outside the Money Stock

- On the basis of IMF PIN 09/53, the RBZ's QFA is estimated at about $1.1 billion in 2008, 36% of GDP. It was 22.9% in 2007, 35.7% in 2008, and 0.0% in 2009. In 2008 it was about four times central government expenditure.
- The means of financing, besides money issuance, were forced purchase of export proceeds, foreign-exchange retention requirements, freezing of foreign-currency deposits, external borrowing, and purchases of foreign exchange in the parallel market.
- What this scene means for the monetary boundary: **looking at money issuance alone, a considerable part of the government's financing is invisible.** The freezing of foreign-currency deposits is a case of a boundary shift in which deposits functioning as money turn into assets that cannot be withdrawn (interpretation).

#### 3.4 The End: Dollarization

- After Gono's remarks on November 20, 2008, the stock market closed, and dollarization proceeded within a few weeks.
- Official monthly rates of change in January–May 2009 were −2.3, −3.1, −3.0, −1.1, and −1.0%.
- A determination of the end under Cagan's criterion is possible only after the fact.

#### 3.5 Limits of the Method

- PPP does not hold in the short run.
- The OMIR can be distorted by speculative premiums and restrictions on ZSE trading.
- There is also the point that the government's blocking of fungibility of dual-listed shares in 2020 can render use of this method in subsequent periods ineffective.
- A basket that includes asset prices differs in composition and so cannot be compared directly with the CPI.

#### 3.6 Different Numbers for the Same Event: The IMF and Hanke, and the Debate over Causes

Zimbabwe's peak diverges by ten or more orders of magnitude depending on the institution.

- The IMF Board report (PIN 09/53) estimates that the 12-month consumer price increase peaked at nearly 500 billion percent in September 2008.
- Hanke writes, together with the monthly 7.96×10¹⁰ % of November 14, 2008, the 12-month-basis rate of increase as 89.7 sextillion % (about 9×10²² %).
- The ratio of the two values is about 1.8×10¹¹ (calculation). The dates (September versus mid-November) and the indicators (consumer prices versus implied-exchange-rate-based PPP) differ, and the way the 12-month figure is produced also differs, so it is not a matter of which is right but of **measuring different things**.
- The IMF writes in the same document that from October–November the domestic currency effectively disappeared from circulation and dollarization accelerated. This matches the account in Section 3.4.

The explanations of the parties also diverged over the cause. In 2006 the IMF's External Relations Director said that the central bank's printing of money through quasi-fiscal activities was the main cause of inflation, and the then central bank governor Gono explained that the roughly 21 trillion Zimbabwe dollars newly printed to buy foreign currency to repay IMF arrears pushed prices up (VOA report). Both explanations see money issuance as part of the cause, but they differ in the **reason** for the issuance (quasi-fiscal activities versus external debt repayment). This essay does not judge which side is right. After dollarization in 2009, broad money (M3) growth and monthly inflation fell to about 30% and 2% respectively, according to a secondary source (Pindiriri 2017, cited).

---

---

### 4. Venezuela: A Competition of Indicators

#### 4.1 Hanke's Method

- It is a method that rolls relative PPP on a daily basis. It uses the black-market exchange rate (DolarToday) and the U.S. CPI-U.
- Reproducing the case of November 3, 2016: (1.00125) × (1 + (1682.12 − 1084.63)/1084.63) − 1 = 0.5528, that is, 55.3% per month.
- "More than 50% for 30 consecutive days" means that the one-month rate of change, rolled forward day by day, stayed above 50% for more than 30 days in a row. It differs from the BCV and National Assembly monthly CPI even in definition.

#### 4.2 Differences in the Start Date

- Hanke: first exceeded 50% on November 3, 2016; the 30-day condition was met on December 3.
- BCV: December 2017 (55.6% per month).
- National Assembly/OVF: November 2017 (56.7% per month).
- Ecoanalítica: November 2017.
- A substantial part of the difference is explained by the difference in definition: a daily exchange-rate basis versus a monthly CPI. However, without BCV monthly data it cannot be confirmed that it is explained entirely.

#### 4.3 Gaps and Competition in the Statistics

- The BCV is said not to have published price statistics from December 2014 to January 2016. The only basis is a single statement by Hanke.
- In May 2019 the BCV published figures again: 130,060% for 2018 as a whole, and 33.8% per month for April 2019. The National Assembly's figure for 2018 is 1.7 million percent.
- Hanke argues that "the only accurate method is observing the black-market exchange rate" and evaluates the figures of the IMF and others as mere conjecture. This is a statement by an interested party.
- The Hyperinflation installment treated this not as "who is right" but from the viewpoint that **the indicators differ**, and this essay takes the same position.

#### 4.4 The End

- By the BCV's measure, the last month above 50% was December 2020 (77.5%), and the point at which one can confirm that it did not exceed 50% for the following 12 months is the December 2021 data.
- In Cagan's definition, hyperinflation begins in the month when monthly inflation first exceeds 50% and ends in the month before the one after which it falls below 50% and stays there for at least a year (as summarized by Fischer, Sahay, and Végh 2002). The "12-month confirmation" above follows this definition of the end.
- Rodríguez: the explanation is that the reason for the end was that real balances collapsed because of dollarization, so no more inflation tax could be collected. This is consistent with Cagan's logic of the seigniorage peak.

#### 4.5 The Current Situation (as of October 2026)

- The monthly inflation rate for September announced by the BCV on October 3, 2026 was 8.4%, lower than 8.9% in August. The monthly path is 32.6% in January, 6.3% in May (the year's low), 13.8% in June, 19.9% in July (the year's high), 8.9% in August, and 8.4% in September; the cumulative figure for January–September is 225.3%, and the annualized rate (calculated by Reuters and Bloomberg) is 465.5%. The official exchange rate at the end of September was 859.06 bolívars per dollar, up 8.06% in September alone and 188.14% since the start of the year.
- The BCV explained that stabilization of the foreign exchange market influenced the September figure. A monthly 8% is far short of Cagan's criterion (50% per month) but is above 400% in annualized terms. Depending on whether it is read monthly or annualized, the same number can be read either as "stabilization" or as "extreme inflation" (interpretation).

#### 4.6 The Monetary Side of Venezuela: Prices and Money Growth Side by Side

The preceding sections dealt only with price indicators. ECLAC's (CEPAL's) annual economic studies report money growth rates for the same period, so they can be placed side by side (annual, year on year).

| Year | Consumer prices (BCV) | Money growth (CEPAL) |

| 2018 | 130,060.2% | M1 and M2 above 60,000%, monetary base about 43,950% |

| 2019 | 9,585.5% | M1 and M2 about 4,500–5,000%, monetary base about 9,000% |

| 2020 | 2,959.8% | Monetary base +1,232% (Dec. 2019–Dec. 2020) |

| 2021 | 686.4% | M2 average annualized rate 1,161% |

| 2022 | 234.0% | M2 average annualized rate 434% |

| 2023 | 189.8% | M2 +356% (June 2023, year on year) |


Several things can be read.

- In 2018–19 price increases outran M2 growth. By calculation, in 2018 M2 rose about 601-fold (a 60,000% increase) and prices about 1,301-fold, so real M2 fell to about 0.46 times, that is, roughly by half. In 2019 as well, it is 46-fold versus about 97-fold, or about 0.48 times. Since the growth rate is "above 60,000%," the 2018 figure is a rough estimate. The collapse of real money balances that the Cagan model describes shows up in this calculation (Chapter 3, Section 6).
- In 2021 the direction reverses. The M2 average annualized rate (1,161%) was higher than prices (686%), so real balances may have recovered. This comparison is an approximation mixing the average of monthly annualized rates over the year with year-end prices. The BCV announced the end of hyperinflation, stating that monthly inflation had been below 50% for 12 consecutive months through December 2021.
- That is, the end of hyperinflation is not the point at which money growth stopped. Even in 2021, M2 was growing at four-digit percentages.
- CEPAL points out that the main source of monetary base expansion in 2018–19 was net assets linked to the public sector, that is, fiscal support. The official peak of BCV monthly prices in the same period was 196.6% in January 2019 (EFE report).
- As stabilization measures in 2021, a reserve requirement ratio at the 85% level and foreign exchange market intervention of more than $1.5 billion were reported, and de facto dollarization ran in parallel. How much these factors contributed cannot be sorted out from these data.

---

### 5. Greece and Yugoslavia: The Same "Peak" Diverges by Thousands of Times

#### 5.1 Greece 1941–45

- The monthly 13,800% in the Hanke–Krus table is based on the drachma's exchange rate against the gold sovereign.
- The 8.55×10⁷ % in Cagan's Table 1 is based on the Athens food price index, and is a value obtained by converting the 10-day interval of October 31–November 10, 1944 into a 30-day ratio.
- By calculation, the two values differ by more than 6,000 times (8.55×10⁷ ÷ 13,800 ≈ 6,196). One is a difference in indicator and one is a difference in period.
- Makinen footnote: apart from gold quotations, there is no continuous price series covering the whole period.
- Cagan's M is an index of banknotes issued by Greek banks. The problem of including vault holdings is pointed out (Alexiou et al. 2008, as cited in the Hyperinflation installment).


#### 5.2 Yugoslavia 1992–94

- PBV (1999) Table 1: M1/GDP fell from 6.9% in 1991 to 2.8% in 1992 to 0.2% in 1993. Money in the narrow sense had almost disappeared relative to GDP.
- The official estimate is 3.13×10⁸ % per month (January 1994, 64.6% daily; Hanke–Krus table and Hanke's commentary). PBV itself admits in a footnote that the black-market depreciation rate of 5.8×10⁷ % is based on more reliable data and that the official figure may be overstated.
- The 24-month cumulative figure diverges: PBV 3.6×10²² versus Nielsen 1.6×10²¹. The Hyperinflation installment calculates that it differs by nearly a factor of 10⁹ depending on whether the last two months (December 1993 and January 1994) are included.
- The inflation tax share of 16 → 15 → 22% and seigniorage of 10.4 → 9.6 → 10% are also in the same table.
- What this scene means: if money had shrunk to 0.2% of GDP, people were transacting with something else. However, whether that substitute was foreign currency or goods in kind cannot be sorted out from the data of this chapter.

---

### 6. The Inflation Tax Perspective: When the Boundary Moves, the Tax Base Shrinks

Chapter 2 of the Hyperinflation installment summarizes the Cagan model this way. The seigniorage the government obtains by printing money is **inflation × real money balances**, and in the semi-log form in which money demand falls as inflation rises, seigniorage is maximized when inflation is 1/α. α is the semi-elasticity of money demand.

We look at seven cases using Cagan's Tables 3 and 9 as carried in the Hyperinflation installment. Revenue-maximizing inflation is 1/α (continuous compounding) converted to monthly compounded %, and actual inflation is the average monthly rate of increase over the episode.

| Case | α | Revenue-maximizing inflation | Actual average inflation |

| Austria | 8.55 | about 12%/month | 47%/month |

| Germany | 5.46 | about 20% | 322% |

| Greece | 4.09 | about 28% | 365% |

| Hungary I | 8.70 | about 12% | 46% |

| Hungary II | 3.63 | about 32% | 19,800% |

| Poland | 2.30 | about 54% | 81% |

| Russia | 3.06 | about 39% | 57% |


The Hyperinflation installment notes that the original table misprinted Hungary II's 1/α as .236 and that .2755 is correct. The monthly compounding conversion is e^(1/α) − 1, so Germany is e^0.183 − 1 ≈ 20.1% and Hungary II is e^0.2755 − 1 ≈ 31.7% (calculation).

The interpretation is as follows.

- The three-directional boundary shifts in the next section are all in a direction that **reduces the real balances of official money**. The more official money is replaced by foreign currency, indexed units, or gold, the more the inflation tax base (real balances) shrinks, and the government must print faster for the same revenue. Hungary's adópengő can be read as a device to protect this base, and Venezuela's dollarization is, conversely, a case in which the base collapsed so that no more inflation tax could be collected (Rodríguez's explanation in Section 4.4).
- By calculation, in six of the seven cases (Austria, Germany, Greece, Hungary I and II, Russia), revenue-maximizing inflation is 12–39%, lower than Cagan's hyperinflation criterion (50% per month), and only Poland, at 54%, is above the criterion. The 50% criterion, which was itself admitted to be arbitrary, thus hangs above most of the revenue-maximizing points. This observation does not change the arbitrariness of the threshold, and this essay gives it no theoretical significance.
- Limitation: this comparison relies on the table values of the Hyperinflation installment, and Benati's point that the revenue-maximizing point may be an artifact of the model form (semi-log) is also in the Hyperinflation installment. The comparison above is a statement "within the model."

---

### 7. How Does the End Come: Cessation of Money Growth, or a Change of Regime?

How hyperinflation ends is directly connected to what "the quantity of money" means. If it ends because money growth stops, the quantity of money is the core; if it ends for other reasons, the quantity of money may be a symptom.

- **Sargent (1982).** A paper on the hyperinflations of the 1920s in Austria, Hungary, Germany, and Poland. The thesis is that all four countries ran large fiscal deficits and expanded the money stock greatly, and that the end came not from ordinary monetary and fiscal tightening but from a change in the government's policy regime (a one-time comprehensive fiscal reform, and a central bank that does not finance fiscal deficits). The NBER foreword summarizes that the one-time fiscal reform was the key in all four cases.
- **Counterargument.** Steinbaum (2015) criticized that this story makes it read as if all that was needed was to make the central bank politically independent. He argues that the four cases should be viewed not separately but as a single large shock, the postwar collapse, and that after the fiscal regime change a monetary regime change that blocks the government's seigniorage financing was needed.
- **Comprehensive analysis.** Bernholz and Kugler analyzed 34 high inflations and summarize that the introduction of independent central banks and monetary reforms are connected with the end of inflation, but that under what conditions reforms succeed is unclear in some cases.

Reading the cases of the preceding sections through this framework gives the following (interpretation).

- Venezuela came below the hyperinflation criterion even though M2 grew 1,161% a year in 2021. This reads not as the cessation of money growth but as the result of regime changes such as exchange-rate stabilization, higher reserve requirements, and dollarization, overlapping with a recovery of real money demand.
- Zimbabwe's prices stabilized only after the central bank's quasi-fiscal activities stopped and dollarization was introduced (the policy recommendation of IMF PIN 09/53 and the secondary literature in Section 3.6).
- In both cases this connects to the prescription not of "lower the money growth rate" but of "change the fiscal arrangements and institutions that made money issuance necessary." This is the same as the inflation-tax logic seen in Section 6.

Therefore, in hyperinflation the quantity of money may be the **channel** of inflation, but the **cause** that opens that channel and the **condition** that closes it lie outside the monetary aggregates. This is a question that comes before the question of which M to count. This essay takes neither Sargent's side nor Steinbaum's side and leaves this judgment as only the difference between the two positions.

---

### 8. Interpretation: In Hyperinflation the Monetary Boundary Moves in Three Directions

This section is this essay's interpretation, not a consensus of the literature.

- **Direction 1. Domestic substitute units**: Germany's Notgeld, Hungary's adópengő. A de facto currency arises next to the official banknotes. If an aggregate counts only banknotes, it undercounts.
- **Direction 2. Foreign currency and gold**: dollarization in Zimbabwe and Venezuela, gold sovereigns in Greece. The functions of the domestic currency (medium of exchange, unit of account) are transferred outside. Even if the quantity of domestic currency remains in the statistics, its actual monetary function shrinks.
- **Direction 3. The measurement indicator changes**: if prices cannot be measured directly, they are back-calculated from exchange rates and gold prices. Then the number called the "inflation rate" already carries assumptions about the monetary boundary (PPP, which exchange rate).

Compared with the deflation of Chapter 2, it is as follows.

- Deflation (United States 1929–33): **bank deposits** inside the boundary vanished through default on promises, and so the figures fell within the same M2 definition.
- Hyperinflation: the **monetary unit itself** was replaced, and so the range measurable by the same definition shrank.
- Both show that the "quantity of money" is not a fixed, objective object, but the layers that move are different. The former is the layer of debt, the latter the layer of units.

There are also cautions.

- This essay does not judge which figure is "more accurate." For example, it draws no conclusion that a PPP-based estimate is better than the CPI.
- The interpretation above is limited to the price statistics and literature figures cited earlier, and is not the result of analyzing the national monetary aggregate (M) time series themselves.

---

### 9. Summary of This Chapter

- Cagan's M is banknotes, and Germany's Notgeld and Goldanleihe are left out.
- Hungary's conversion relationship (1 forint = 4×10²⁹ pengő = 2×10⁸ adópengő) is internally consistent.
- Zimbabwe's peak (7.96×10¹⁰ %) is an exchange-rate-based estimate, not a CPI.
- A substantial part of the difference in Venezuela's start date is a difference in indicator definition, and the September 2026 monthly figure of 8.4% (annualized about 465%) shows the difference in interpretation between monthly and annualized units.
- The "peaks" for Greece and Yugoslavia diverge greatly depending on indicator and period.
- Zimbabwe's peak diverges by about 10¹¹ times between the IMF (about 500 billion percent over 12 months) and Hanke (about 9×10²² % on a 12-month basis); in Venezuela, real M2 fell by roughly half in 2018–19, and then in 2021 the country left hyperinflation with M2 growth still at 1,161% a year.
- There is Sargent's interpretation that the end of hyperinflation is explained by a change in the fiscal and institutional regime rather than by the cessation of money growth, and a critical position (Steinbaum) coexists with it.

---

### The One Thing to Remember from This Chapter

> When paper money collapses, the boundary of money moves in three directions—domestic substitute units, foreign currency and gold, and measurement indicators—and in any direction it reduces the real balances of official money, that is, the tax base of the inflation tax.

---

### Sources (Chapter 3)

- Cagan (1956); Hanke & Krus; Hanke & Kwok (2009), "On the Measurement of Zimbabwe's Hyperinflation"; IMF PIN 09/53; Petrović, Bogetić & Vujošević (1999); Nielsen (2004); Uvalić (2022); Makinen; Paal (2000); Rodríguez.
- Hanke, S. H., & Krus, N. "World Hyperinflations" table (Cato Working Paper No. 8, 2012; revised 2013, corrected 2020) https://www.bcci.bg/resources/files/hanke-krus-hyperinflation-table.pdf ; Hanke commentary (Cato 2009, National Review 2020).
- CEPAL, *Estudio Económico de América Latina y el Caribe*, Venezuela chapters (2020, 2021, 2023) https://repositorio.cepal.org/bitstream/handle/11362/46070/1/EE2020_Venezuela_es.pdf ; BCV annual prices (2018–2023) reports: EFE (Jan. 10, 2022), AFP (Jan. 2024), El Ciudadano.
- IMF, Public Information Notice No. 09/53 (2009) https://www.imf.org/en/News/Articles/2015/09/28/04/53/pn0953 ; VOA (Feb. 24, 2006). Pindiriri (2017), cited in a Danubius University paper.
- Sargent, T. J. (1982). "The Ends of Four Big Inflations." NBER 1982 https://www.nber.org/chapters/c11452.pdf ; Steinbaum (2015), Equitable Growth ; Bernholz & Kugler, "Stopping High Inflations: An Empirical Analysis of 34 High Inflations."
- Cagan table reproduction: Minneapolis Fed WP 343 https://www.minneapolisfed.org/research/wp/wp343.pdf ; QuantEcon "Demand for Money during Hyperinflations" ; Salemi, M. "Hyperinflation," Econlib ; Fischer, S., Sahay, R., & Végh, C. (2002). "Modern Hyper- and High Inflations." Journal of Economic Literature 40(3).
- Reports on the Banco Central de Venezuela's September price announcement (Oct. 3, 2026): Reuters (Oct. 3, 2026), Bloomberg Línea, El Diario (Oct. 3, 2026). Reuters on the August announcement (Sept. 4, 2026).

---

## Chapter 4. Japan and Korea: The Monetary Base and M2, and the "Old M2 / New M2"

 

---

### Plain Explanation: Printing Money and Money Growing Are Different Things

- What the central bank directly creates is the **monetary base** (cash + the reserves banks deposit with the central bank).
- M2, which we call the "money stock," is not the monetary base but a **total that includes bank deposits and so on**.
- When banks make loans, deposits are created, and when loans shrink, deposits shrink as well. So even if the central bank increases the monetary base, if lending does not increase, M2 may not change much.
- The United States in 1931–32, which we saw in Chapter 2, was exactly such a case. The monetary base rose, but M2 fell.

And in Korea something different happened.

- Money flowed in large amounts into **funds and ETFs** rather than bank deposits.
- The old definition put these in M2, and the new definition removed them.
- The movement of money is the same, but the range that carries the label "M2" changed.

A summary of terms follows.

- **Monetary base**: money directly supplied by the central bank (cash + reserves).
- **QE / QQE**: quantitative easing / quantitative and qualitative monetary easing. The policy by which the Bank of Japan increased the monetary base through large-scale asset purchases.
- **Beneficiary certificates**: funds (collective investment securities), ETFs, and so on. Principal is not guaranteed and they are valued at market prices.
- **Lf / L**: liquidity indicators broader than M2. Under the new definition, beneficiary certificates moved to Lf.

---

### A. Japan

#### A.1 The 2008 Overhaul: Money Stock Statistics and Monetary Survey Changed Together

- The Bank of Japan overhauled its monetary statistics in June 2008, switching to the M1/M2/M3/L system, and a discontinuity arose in the time series with the old M2+CD. The trigger was the privatization of Japan Post Bank (Chapter 1, Section 1.4).
- The overhaul had two branches. The Money Stock statistics were published on the new basis starting with the June 9 release, which carried the preliminary figure for May 2008, and retroactive data for April 2003–March 2008 was provided together. The Monetary Survey widened its scope to all depository corporations including Japan Post Bank from the June 13 release, and the Bank of Japan explained that this was closer to the IMF Monetary and Financial Statistics Manual.
- Even though the names are similar, the old series' M1, M2+CD, and M3+CD and the new series' M1, M2, and M3 differ in the scope of issuing sectors (whether Japan Post Bank is included), the scope of holding sectors, and the estimation methods for some data.
- Therefore, when reading Japan's M2 time series across 2008, one must first check this discontinuity.

#### A.2 Greenwood's Reading

- Source: Greenwood (Cato Journal, 2017). The author is chief economist at Invesco and takes the position of defending a quantitative easing design that targets broad money.
- Japan's QE1 (2001–06): the monetary base +70%, and the M2 path is said to have remained almost as it was.
- QQE: the monetary base roughly tripled, but M2 is said to have barely changed.
- The same paper's account of the United States: bank loans −14% in 2008–11, yet M2 grew +6.8% on average per year from January 2009 to October 2013. The thesis is that to see the effect of policy one must look at broad money, not the monetary base.

#### A.3 Harada's Reading

- Source: Bank of Japan Board member Harada's speech in Gifu on June 1, 2017 (published by the BIS on June 12, 2017).
- The speech compares the four years before and after the introduction of QQE (April 2013). In annualized terms for March 2009–March 2013 versus April 2013–April 2017, the M2 growth rate is +2.8% → +3.7%, and the bank lending growth rate is −0.3% → +2.5%. He also cites a study (Shioji) finding that QQE had a (small) quantitative effect on money stock and loan growth rates.

#### A.4 The Monetary Base and M2 in Bank of Japan Statistics

- In April 2013, QQE changed the policy operating target from the call rate to the monetary base, and declared that the monetary base would be doubled within two years. The monetary base at the end of 2012 was ¥138 trillion, the target for the end of 2014 was ¥270 trillion, and the actual balance at the end of 2013 was ¥202 trillion.
- At the end of January 2016 it was ¥358.76 trillion (+28.8% year on year), and at the end of March ¥375.70 trillion (+27.0%). Compared with the end of 2012, that is about 2.6 times and 2.7 times (calculation).
- The M2 growth rate over the same period was in the 2–4% range per year. It was 2.5% in 2012, 2.9% in Q1 2013, 3.5% in Q2 (June's 3.8% was reported as the highest in ten years), and 3.6% in March 2015. That M2 grew by a few percent a year while the monetary base became 2.6 times as large is the same fact that Greenwood's "barely changed" and Harada's "increased" both point to. Which expression to choose is a matter of interpretation.

**After normalization: the same configuration, with the direction reversed.** The Bank of Japan ended QQE and yield curve control, among other things, in 2024. Placing the year-on-year growth rates of the monetary base and M2 side by side from Bank of Japan statistics (published September 2026) gives the following.

| Period | Monetary base (average balance, y/y) | M2 (average balance, y/y) |

| 2025 | −4.9% | +1.2% |

| Apr.–Jun. 2025 | −3.9% | +0.7% |

| Jul.–Sep. 2025 | −4.7% | +1.3% |

| Oct.–Dec. 2025 | −8.7% | +1.7% |

| Jan.–Mar. 2026 | −10.6% | +1.8% |

| Apr.–Jun. 2026 | −12.4% | +2.3% |

| Jul.–Sep. 2026 (M2 for Jul.–Aug.) | −14.9% | +2.1%, +2.0% |


The average balance of the monetary base in December 2025 was ¥594.19 trillion (−9.8% year on year), and December 2024 is about ¥659 trillion by back-calculation (calculation). In August 2026 it was ¥543.0 trillion (−15.7%), and in September ¥532.8 trillion (−15.2%), declining. Since M2 in the same August was ¥1,296.4 trillion (+2.0%), the ratio of M2 to the monetary base is about 2.4 (calculation).

This table shows two things. First, just as M2 did not respond much when the monetary base swelled several-fold under QQE, M2 did not fall even as the monetary base shrank by double digits with normalization. Second, according to a Reuters report (March 2026 money stock), against the background of interest rate hikes, shifts of funds into time deposits continued, quasi-money rose +5.2%, and M2 was +2.0%. In that the rise and fall of the monetary base and the rise and fall of M2 cannot be read straight through to each other, this is the same story as "the multiplier is an accounting identity, not a causal law" in Chapter 2, Section 3.3 (interpretation).

A flow in the same direction is also seen in the United States. According to the Federal Reserve's H.6 (published July 28, 2026; seasonally adjusted M2, monetary base as monthly averages), the monetary base fell about 5.0%, from $5,774.8 billion in March 2025 to $5,488.4 billion in June 2026, while over the same period M2 rose about 6.8%, from $21.68 trillion to $23.16 trillion (calculation). The monetary base was affected by the decline in reserves (from $3,408.3 billion in March 2025 to $3,018.8 billion in June 2026), and M2 rose irrespective of that. Both Japan and the United States show that the monetary base and M2 can move in different directions.

#### A.5 Interpretation

- What this scene shows is **which layer the sentence "the money stock increased" points to**. Depending on whether it is the monetary base, M2, or bank loans, the evaluation of the same policy differs.
- In Chapter 2 (United States 1929–33), the monetary base and M2 moved in opposite directions. Japan reads as a case in which one side **did not respond** during QQE, and as a case in which the reverse recurred during normalization (interpretation).
- Greenwood and Harada are both interested parties. One is an economist at an asset manager who defends a broad-money-centered policy, and the other is a central bank board member who carried out the policy at the time. Since the two look at different periods and comparison targets (Greenwood at M2's response relative to the monetary base, Harada at levels before and after the policy shift), they cannot be asserted to contradict each other. This essay does not disparage either side and places them only in parallel.
- By calculation, maintaining an annual rate of 2.8% for four years gives a cumulative 11.7% or so, and maintaining 3.7% for four years gives about 15.6% (16.0% if the interval is 4.1 years). The 0.9-percentage-point difference in growth rates can be seen as "almost unchanged" or as "a meaningful rise." That is a matter of judgment, not of calculation.

---

### B. Korea

#### B.1 The Course of the Overhaul

- Dec. 16, 2025: overhaul direction announced; Dec. 30, 2025: results announced; applied from January 2026. For one year the old M2 and new M2 are published in parallel.
- Beneficiary certificates (equity and bond funds, including ETFs) were excluded from M2 and moved to Lf, and notes issued by mega IBs and note-type CMAs were added to M2.
- The reasons given by the Bank of Korea are that it follows the revision guidance of the IMF's Monetary and Financial Statistics Manual (MFSM), and international comparability, since major countries such as the United States do not include beneficiary certificates in M2 (Kyunghyang Shinmun, Dec. 16, 2025).
- The manual's formal title is the Monetary and Financial Statistics Manual and Compilation Guide; a pre-publication draft came out in March 2016 and it was officially published in November 2017. This manual includes MMF shares in broad money and excludes investment fund shares other than MMFs (paragraphs 3.146 and 6.47). That reports give the year variously as 2017 or 2018 appears to be a difference in which point of this publication history one takes.
- According to the same report, beneficiary certificates accounted for 32.1% of the increase in M2 in September 2025.

#### B.2 The Figures Published in Parallel

- October 2025: old M2 ₩4,466.3 trillion, growth rate 8.7% / new M2 ₩4,056.8 trillion, 5.2%.
- September 2025 (Bank of Korea blog): old M2 growth rate 8.5%, in the mid-5% range on the overhauled basis, and the U.S. M2 growth rate in the same month was 4.5%.
- November 2025: old M2 +8.4% year on year, beneficiary certificates +38.4% (contribution 3.4 pp), new M2 +4.8% (old M2 about 5.0% excluding beneficiary certificates). The seasonally adjusted average balance of new M2 was ₩4,057.5 trillion, down ₩1.9 trillion from the previous month. December 2025: old M2 +8.0%, beneficiary certificates +37.4% (contribution 3.4 pp), new M2 +4.7% (seasonally adjusted ₩4,080.7 trillion).
- January 2026: old M2 8.4% / new M2 4.7%. Beneficiary certificates +43.1%, contribution 3.9 pp. On a seasonally adjusted average balance basis, new M2 was ₩4,108.9 trillion (+0.7% from the previous month) and old M2 was +1.2% from the previous month. M1 ₩1,356.4 trillion, Lf ₩6,097.8 trillion, L (end-of-period balance) ₩7,759.2 trillion. By product, other monetary instruments such as CMAs grew ₩21 trillion and at-call savings deposits grew ₩15.5 trillion.
- February 2026: new M2 ₩4,114.0 trillion (seasonally adjusted, +₩0.6 trillion from the previous month), unadjusted series +4.9% year on year. Old M2 +9.1%.
- April 2026: new M2 ₩4,153.9 trillion (+0.6%), old M2 ₩4,684.6 trillion (+1.3% from the previous month, +10.4% year on year), beneficiary certificates +51.4%.
- May 2026 (average balance): old M2 ₩4,766.5 trillion, +11.6% year on year / new M2 ₩4,183.2 trillion, +5.8% (unadjusted series). Beneficiary certificates +61.7%, contribution 6.1 pp. M1 ₩1,398.2 trillion (+10.0%), Lf ₩6,309 trillion, L ₩8,053.9 trillion. New M2 was +0.8% from the previous month and old M2 was +2.2%, and money in trust under 2 years turned from a ₩3.2 trillion decrease to a ₩3.8 trillion increase.
- August 2026 (average balance, published Oct. 15, 2026): new M2 ₩4,266.8 trillion, +0.9% from the previous month (₩39.1 trillion), +5.6% year on year. Time deposits and installment savings under 2 years +₩28.7 trillion, money in trust under 2 years +₩14.2 trillion (inflow of deposited funds from semiconductor companies), and MMFs +₩12.6 trillion; money holdings of non-financial corporations rose ₩33.9 trillion, driving the increase. M1 was ₩1,357.6 trillion (−1.1% from the previous month), Lf ₩6,386.4 trillion, L ₩8,094.3 trillion. The September data is scheduled for release in mid-November.

#### B.3 Verification

- Level difference (unadjusted average balance): October 2025 4,466.3 − 4,056.8 = ₩409.5 trillion. May 2026 4,766.5 − 4,183.2 = ₩583.3 trillion. In seven months the gap between old and new M2 widened by about ₩174 trillion. It was largest in June (₩621.2 trillion) and was ₩575.7 trillion in August.
- Growth-rate difference: January 2026 8.4 − 4.7 = 3.7 pp, May 11.6 − 5.8 = 5.8 pp. The gap grew.
- Check of the beneficiary certificate contribution: January 8.4 − 3.9 = 4.5, which is within 0.2 pp of new M2's 4.7%, while May 11.6 − 6.1 = 5.5 is off from new M2's 5.8% by 0.3 pp. Since the contribution is a value measured on the old M2 basis, this subtraction is an approximation that mixes different bases, and the media use the same subtraction (December 2025: 8.0 − 3.4 ≈ 4.6). The discrepancy may include the added notes and rounding, and this essay does not pin down a single cause.
- Back-calculation of beneficiary certificate share: since the contribution is the prior-year share multiplied by the growth rate (assuming the Bank of Korea's contribution has this definition), contribution ÷ growth rate is the share beneficiary certificates held in old M2 one year earlier. January is 3.9/43.1 ≈ 9.0%, May is 6.1/61.7 ≈ 9.9%. Let us also check October 2025. 497 trillion ÷ 1.368 ≈ 363 trillion, and old M2 4,466.3 trillion ÷ 1.087 ≈ 4,109 trillion; the increase of about ₩134 trillion is about 3.3% of the prior-year M2, which matches the Bank of Korea's contribution of 3.3 pp, and the share is about 8.8%. Therefore the share at the point one year earlier grew from about 8.8% in October 2024 to about 9.0% in January 2025 and about 9.9% in May 2025.
- The new M2 growth rate rose from 4.7% in January to 5.8% in May, rose to 6.0% in June, and then fell to 5.8% in July and 5.6% in August.
- The itemized breakdown of the difference between ₩497 trillion and ₩409.5 trillion is in Chapter 1, Section 1.5 (exclusion of beneficiary certificates −₩497.1 trillion, mega-IB notes and CMAs +₩44.7 trillion, compilation method improvements and so on +₩43.0 trillion).
- Looking back with the Bank of Korea's component data (unadjusted average balance; the new-standard series is available back to October 2003), the old M2 exceeded the new M2 by 6.7% in October 2003, 3.3% in December 2022, 7.2% in December 2024, 10.1% in October 2025, and 13.9% in May 2026. The gap has widened most steeply over the most recent two years.
- By component, the largest contributors to the new M2's year-on-year growth of 5.6% in August 2026 were foreign-currency deposits under 2 years (+27.5%, contribution 1.03 pp), money in trust under 2 years (+14.5%, 1.00 pp), time deposits and installment savings under 2 years (+2.1%, 0.94 pp), at-call savings deposits (+4.9%, 0.87 pp), and MMFs (+15.5%, 0.67 pp). Each contribution is the component's year-on-year change divided by the total a year earlier, and the twelve components sum to the 5.6%.

#### B.4 Background of the Policy Debate

- At the time of the overhaul, the issue was "is excess liquidity the cause of won weakness?" The Bank of Korea said it sees foreign exchange supply and demand as the larger factor in the exchange rate rise, and the low growth rate of the overhauled M2 was introduced in a context supporting that position (Kyunghyang Shinmun).
- The reasons the Bank of Korea gave for the overhaul are the IMF manual and international comparison. This essay does not judge whether the overhaul was aimed at a particular debate. This essay has no basis to prove or refute intent.
- On the same day as the overhaul announcement (December 16, 2025), the Bank of Korea posted "Understanding the Recent Liquidity Situation" on its blog, stating that explaining the rise in housing prices and the exchange rate by liquidity growth is an "over-interpretation," and wrote that it judges that the price and liquidity channels are not having a significant effect on the recent rise in the exchange rate (Chapter 5, Section 4). This is not so much a position on the overhaul itself as the Bank of Korea's position on the liquidity debate. This essay notes only that the two pieces came out on the same day and does not judge intent.

#### B.5 Connection to Monetary Policy

- Under Governor Shin Hyun-song (신현송), who took office in April 2026, the Bank of Korea held the base rate at 2.50% for the eighth consecutive time on May 28 (two members dissented in favor of a hike), then raised it in July and August in succession, bringing it to 3.00% on August 27. Cited as the background to the hikes were growth (the 2026 growth forecast was raised from 2.6% to 3.3%), inflation above the target, and concerns about financial imbalances such as housing prices in the capital region and household lending. That is, even while the new M2 growth rate looked stable in the 5% range, policy moved toward tightening.
- In reports on the August 2026 minutes, a majority of members cited "market liquidity is still growing rapidly" as one of the grounds for preemptive action. The reports do not say which indicator was meant. Listing the candidates: new M2 5.6–5.8%, old M2 11.6%, M1 10.0% (May). Since the meaning of "rapid" differs greatly depending on the candidate, when quoting this sentence one must note together that the indicator was not specified.
- In his inaugural address on April 21, 2026, Governor Shin said he would widen the scope of analysis to non-bank sector information, off-balance-sheet transactions, and non-traditional financial products. This can be read as a concern in the same direction as the structure in which beneficiary certificates left M2 and moved to Lf, but there is no basis connecting the two causally (interpretation).
- Korea's CPI does not include owner-occupied housing costs in the headline and publishes them only as a supplementary indicator. The ECB, too, put the inclusion of owner-occupied housing costs as a long-term task in its 2021 strategy statement. **The problem of "what to count" exists not only for money but also for prices.** This is the link to the next chapter, Chapter 5.

#### B.6 Interpretation

- For the same month of May, Korea has two growth rates: 5.8% and 11.6%.
- The two numbers answer different questions.
  - New M2 is closer to "how much have short-term assets that can serve as a medium of exchange without loss of nominal value grown?" (a summary of Financial News's definitional sentence).
  - Old M2 is broad liquidity that adds to that funds and ETFs, whose market value fluctuates.
- When stock prices rise, the balance of beneficiary certificates grows and the old M2 growth rate rises. Whether what grew is "money" or "asset prices" depends on the definition. If the definition is changed, the question itself changes.
- Therefore, "by what percent did Korea's money stock grow?" cannot be answered without stating the definition. A report that cites only one of the numbers creates a misunderstanding unless it states the definition.
- Compared with Japan, Japan placed funds and trusts outside M2 and M3 (in L) from the start (Chapter 1, Section 1.2). Korea approached the same line in 2026, and the fact that in August 2026 Japan's investment trusts (+13.9%) and money in trust (+12.0%) grew much faster than M2 (+2.0%) shows how large a difference this line makes to the interpretation of growth rates.

---

### Summary of This Chapter

- The Bank of Japan overhauled its statistical system in 2008, and the time series is discontinuous (Chapter 1).
- Greenwood's thesis is that monetary base expansion did not lead to M2 expansion, and the changes in M2 and loan growth rates that Harada presented are the figures above (confirmed against the original text of the Bank of Japan speech).
- According to Bank of Japan statistics, while the monetary base shrank by as much as −15% a year in 2025–26, M2 rose from +0.7% to +2.3%.
- The parallel published figures for Korea and the widening gap between old and new M2 are consistent across the reports above.

---

### The One Thing to Remember from This Chapter

> Even when the monetary base swelled several-fold, the M2 growth rate could stay in the 2–4% range a year (Japan), and when the definition was changed, the growth rate for the same month fell by nearly half (Korea). In both cases one must first ask which layer the number points to.

---

### Sources (Chapter 4)

- Greenwood, J. (2017). Cato Journal 37(1).
- Harada, Y. (June 1, 2017). "Economic Activity, Prices, and Monetary Policy in Japan." Bank of Japan https://www.boj.or.jp/en/about/press/koen_2017/ko170601a.htm ; BIS publication https://www.bis.org/review/r170612c.pdf
- Bank of Japan: Monetary Base (September 2026, published Oct. 2, 2026) https://www.boj.or.jp/statistics/boj/other/mb/base2609.pdf ; Money Stock preliminary figures (August 2026) https://www.boj.or.jp/statistics/money/ms/ms2608.pdf ; explanation of QQE and the Governor's speeches (July 2013, March 2014).
- Reports of historical Japanese M2 and monetary base figures: Mainichi, Central Banking, Reuters Japan edition, Nissay Basic Research Institute "Economic and Financial Flash" (2013–2019), MNI.
- Kyunghyang Shinmun, Dec. 16, 2025, report on the Bank of Korea's M2 overhaul https://www.khan.co.kr/article/202512161602001/
- Financial News, July 15, 2026 https://www.fnnews.com/news/202607150806501374 ; Asia Economy, Jan. 14, Feb. 13, Mar. 13, Apr. 15, July 15, 2026 ; Ajunews, June 16, 2026 ; SBS Biz, Oct. 15, 2026 https://biz.sbs.co.kr/amp/article/20000340139 ; Korea Times, Oct. 15, 2026.
- Reports on the Bank of Korea base rate decisions (May 28 and Aug. 27, 2026): Yonhap News, NoCut News, SBS Biz, Economist (이코노미스트). Bank of Korea economic outlook (Aug. 27, 2026) https://eiec.kdi.re.kr/policy/materialView.do?num=285904

- Bank of Korea, ECOS, table 1.1.3.1.2 "M2 composition by product (average balance, unadjusted series)," Oct. 2003–Aug. 2026 (the Aug. 2026 value is preliminary).
---

## Chapter 5. The Quantity Theory and Velocity: Before Asking "If M2 Grows, Do Prices Rise?"

 
---

### Plain Explanation: The Quantity of Money, the Number of Turns, Prices, and Transaction Volume

- If you add up the value of everything bought and sold in a country over one year, that is **nominal GDP**.
- Money is needed for those transactions, and if the same money changes hands many times, a large volume of transactions is possible with a small amount of money.
- The average number of times money turns over in a year is called **velocity (V)**.
- Written as an identity, `M × V = P × Y`. M is the money stock, P is the price level, and Y is real transaction volume (real GDP).

There is one important point here.

- This equation is an identity that comes from a definition, so **it always holds.** This is because V is defined as `P×Y ÷ M`.
- Therefore, the observation that "M grew but prices did not rise" does not mean the equation is wrong; it means **V fell or Y grew**.
- For the quantity theory to become a claim, it needs the **additional assumption** that "V is stable." Whether that assumption holds is the core of the debate.

A summary of terms follows.

- **Quantity theory of money**: a theoretical tradition holding that changes in the money stock lead to changes in prices in the long run. It takes several forms.
- **Velocity V**: nominal GDP divided by the money stock. This essay follows FRED's definition of M2V: quarterly nominal GDP ÷ quarterly average M2.
- **Average balance / end-of-period balance**: the monthly average balance / the month-end balance.

---

### 1. The Same Equation, a Different M: Definition Changes V

- Since V is `nominal GDP ÷ M`, if the range of M changes, V differs even for the same economy.
- In the Federal Reserve's May 2020 H.6 overhaul, savings deposits were moved from non-M1 M2 to M1. The M2 total stayed the same (Chapter 1, Section 1.6).
- Working it out, since the M2 total is the same, **M2V is not affected by this overhaul**, while M1V, which uses M1, falls mechanically because its denominator suddenly becomes larger. This sentence is an inference from the definitions.
- Korea has the same problem. On the new M2 basis, M2/GDP was 154% in Q3 2025, and the trend was 157%.
  - Converting the new M2 of ₩4,056.8 trillion (October 2025) and the old M2 of ₩4,466.3 trillion into a ratio, M2/GDP on the old M2 basis is about 169–170%. By calculation, 154% × 4,466.3 ÷ 4,056.8 ≈ 169.5%. This is an approximation mixing the month (October balance) and the quarter (the Q3 ratio).
  - Therefore Korea's V (= GDP/M2) is about 0.65 on the new M2 basis and about 0.59 on the old M2 basis. For the same economy, V diverges by about 10% depending on the definition.

---

### 2. Velocity of U.S. M2: 2008 and 2020

FRED M2V (quarterly, seasonally adjusted)

- Q1 2007: 1.992
- Q2 2008: 1.923
- Q4 2008: 1.810
- Q4 2009: 1.722
- Q4 2012: 1.582
- Q4 2019: 1.435
- Q1 2020: 1.390
- Q2 2020: **1.126** (the lowest value in the table)
- Q4 2020: 1.165
- Q2 2021: 1.152
- Q4 2021: 1.163
- Q2 2022: 1.192
- Q4 2022: 1.252
- Q4 2023: 1.371
- Q4 2024: 1.397
- Q2 2025: 1.402, Q3: 1.411, Q4: 1.411
- Q1 2026: 1.415, Q2: 1.418 (updated Sept. 30, 2026; next update Oct. 29)

When quarterly GDP is revised, past V changes too. The Q2 2020 trough was reported at around 1.10 in the previous vintage and is 1.126 (about 1.13) in the current vintage. The values above are from the September 30, 2026 vintage.

The calculation results are as follows.

- Q1 2007 → Q4 2019: 1.435 / 1.992 − 1 ≈ −28.0%. A gentle decline spanning 12 years.
- Q2 2008 → Q4 2009: 1.722 / 1.923 − 1 ≈ −10.5%. The decline in the crisis interval.
- Q4 2019 → Q2 2020: 1.126 / 1.435 − 1 ≈ −21.5%. A sharp drop in just two quarters.
- Q2 2020 → Q4 2023: 1.371 / 1.126 − 1 ≈ +21.8%. Recovery.
- Q4 2021 → Q4 2022: 1.252 / 1.163 − 1 ≈ +7.6%.

The interpretation is as follows.

- The decline of 2008 is long and gradual, and the decline of 2020 is short and steep. The shapes differ.
- Since V = nominal GDP ÷ M2, the sharp drop in 2020 is **the result of the numerator (economic activity) shrinking and the denominator (M2) growing**. How much each side contributed can be sorted out only by looking at quarterly M2 and GDP separately.
- Low interest rates and increased money demand are often cited as causes of the decline after 2008, but this essay does not judge the cause.

---

### 3. 2021–23: Why Judgment Is Withheld

#### 3.1 Confirmed Facts and the Reason for Withholding Judgment

**What was confirmed as fact**

- M2 growth rate: it exceeded 25% year on year in early 2021 (26–27% depending on the compilation), the fastest pace since 1959.
- U.S. M2 peaked at about $21.75 trillion in April 2022 and then fell about 4.9% through October 2023, and the −4.6% year-on-year in April 2023 was the largest decline since 1959, when the Federal Reserve began officially tracking M2 (see the revised-vintage explanation in Chapter 2, Section 4.4).
- U.S. CPI was 9.1% year on year in June 2022, which the BLS announced as the largest 12-month increase since the 12 months ending November 1981.
- M2V rose from 1.165 in Q4 2020 to 1.252 in Q4 2022 and 1.371 in Q4 2023.

**Reasons for withholding judgment**

- The M2 surge confirmed above was in 2020–21, and the CPI peak was in mid-2022. The lag is about 12–18 months. Whether this is evidence that "M2 led" or evidence that "a supply shock came separately" cannot be sorted out from the same numbers.
- According to the V calculation above, V was rising in 2022–23. Nominal GDP growth splits into the sum of M2 growth and V growth, and from this calculation alone, which does not decompose that contribution, one cannot say "how much did V's rebound contribute."
- There are several layers in the explanation of inflation: money, supply chains, energy, fiscal policy, expectations. Since this essay's subject is the definition of M2, it does not judge which explanation prevails.

#### 3.2 How the Studies Diverge

The causes of the 2021–22 inflation are still a matter on which research results diverge. We place the literature this essay confirmed side by side by method and gist of conclusion.

| Study | Method | Gist |

| Bordo, Duca & Jones (NBER WP 34017, July 2025) | Consumption velocity of Divisia M3 and a P-Star model | Estimates that aggregate demand factors (captured by Divisia money) accounted for a larger share than supply pressures in the 2021–22 inflation. However, the authors themselves oppose an "overly simplistic monetarist interpretation" and leave room for the share of fiscal policy and shifts in risk aversion |

| Hall, Tavlas & Wang (2023, cited by the paper above) | VAR | Identifies simple-sum M2 and increases in government spending as the main drivers of U.S. inflation |

| Bernanke & Blanchard (AEJ: Macroeconomics 17(3), 2025) | A dynamic model of prices, wages, and expected inflation | Estimates that most of the inflation surge came from shocks to prices rather than wages. These shocks include sharp rises in commodity prices reflecting strong aggregate demand, and sectoral price surges combining shifts in the composition of demand with sector-specific supply constraints. The overheated labor market was not the main driver but had a more persistent effect on wages and prices (confirmed against the original abstract) |

| Gagliardone & Gertler (NBER WP 31263, 2023) | A New Keynesian model and structural VAR | What mainly explained the surge since mid-2021 was the combination of oil price shocks and "loose" monetary policy shocks. The monetary policy shock here is a **policy rate shock** identified from interest-rate-futures movements around FOMC meetings, and is not an increase in the money stock (confirmed against the original abstract and NBER commentary) |

| Fed staff (FEDS 2025-070) | Comprehensive review | Summarizes that inflation rose as large supply and demand shifts coincided. The contribution of supply factors peaked at 3.2 pp in June 2022. Labor market tightening alone explains only part |

| Dallas Fed WP 2306 (2023) | Divisia money and nominal GDP | Judges that both money growth and the recovery of velocity are useful for tracking nominal GDP, and that supply disruptions also contributed, but that the acceleration of aggregate demand was large in Q4 2021–Q3 2022 |


What can be read from this table is as follows.

- Even studies that emphasize money specify **which money**. What Bordo, Duca & Jones used is not simple-sum M2 but Divisia M3. This indicator weights components by their liquidity cost and also includes institutional MMFs and RPs.
- The same literature does not deny supply factors. All the studies in the table merely distribute the shares of supply and demand differently.
- Which side is right depends on the choice of model.
- In the table, those that base themselves on the money **stock** are Bordo, Duca & Jones and Hall, Tavlas & Wang, whereas Gagliardone & Gertler's "accommodative monetary policy" is an interest rate path. The same phrase "monetary factor" points to different variables. The commodity price surge that Bernanke & Blanchard speak of also reflects strong aggregate demand, so it does not divide neatly into "supply versus demand."

One figure connects directly with this chapter's discussion of V. In Bordo, Duca & Jones's estimates, the consumption velocity of Divisia M3 took a shock of about −0.20 in log terms (about −18%) in Q2 2020 and rebounded by about +0.15 (about +16%) in Q3 (the coefficients on the quarterly dummies for 2020; calculation). In the same paper, the Divisia M3 growth rate exceeded 18% a year in Q2 2020–Q1 2021 and exceeded 9% in the following three quarters, then plunged in 2022 and turned negative in 2023. This path has the same direction as the M2V of Section 2 above (a sharp drop in Q2 2020, then a rebound). That the same shape emerges from two indicators with different definitions is a clue that this sharp drop is not merely a product of one particular M2 definition (interpretation).

#### 3.3 M2's Own Weakness: The Shift to Funds

The most concrete explanation for why M2 was unstable as an inflation indicator is **the shift to funds**.

- Bordo, Duca & Jones summarize that as the trading fees (loads) on equity mutual funds fell in the late 1980s and 1990s, households moved from M2 items such as small time deposits into funds, and that this produced a permanent decline in M2 demand and an upward shift in velocity (citing Duca 2000 and Becsi & Duca 1994). As a result, P-Star models using simple-sum M2 under-predicted inflation and lost credibility.
- This explanation has the same structure as the Korean case in Chapter 4. In Korea, beneficiary certificates were inside the old M2, so the shift to funds occurred within M2 and inflated the growth rate, whereas in the United States funds are outside M2, so the shift appeared as a decline in M2 demand. Either way, **when money flows in and out of M2, M2's number diverges from economic activity** (interpretation).
- The same paper also cites as a weakness that simple-sum indicators assume the components are perfect substitutes. Divisia indicators avoid this, but this is a solution in a different direction from the Bank of Korea's new M2. The new M2 reduces the components (excluding beneficiary certificates) and keeps the simple sum. This essay does not judge which solution carries more information.
- Korea is a case in point. The Bank of Korea publishes only simple-sum aggregates, but Divisia indices for Korea have been constructed in academic work: Hahm and Kim (2000) took up the volatility of M2 after financial innovation in the 1980s, and Barnett, Lee, and Mohiuddin (2024) built Divisia aggregates for Korea for 2009–2024 from the Bank of Korea's ECOS data. A Bank of Korea issue note (Park and Shim, 2018) and a Korea Institute of Finance brief (2016) are cited in that paper as having discussed Divisia M2. In that study, Korea's Divisia M2 is slightly higher than simple-sum M2, and Divisia Lf is consistently higher than Lf, so simple-sum aggregates understate the growth of monetary services in Korea; in Hong Kong the opposite holds. Three cautions apply. The study uses the old M2, which includes beneficiary certificates, so the result cannot be carried over to the new M2. The authors found no cointegration between nominal GDP and any Korean aggregate, simple-sum or Divisia, so the evidence of added explanatory power comes from Hong Kong and Taiwan, not Korea. And because the Bank of Korea does not publish interest rates matched to every component, proxy rates were used. The Bank of Korea reduced the components (the new M2), while the Divisia approach reweights them; the two answer different questions.
- The paper above reports that the consumption velocity of Divisia M3 has a stronger tendency to revert to its mean since the mid-1980s than simple-sum M2 or Divisia M2. This means that widening the definition sometimes stabilizes velocity, and it is a counter-clue to the premise of Chapter 1, Section 0.3 ("Why Look at M2?").

---

### 4. Korea: M2 and CPI in the Same Month

Monthly comparison for 2026 (new M2 average balance year on year vs. CPI year on year)

| Month | New M2 | CPI | Difference |

| June | 6.0% | 3.2% | 2.8 pp |

| July | 5.8% | 2.8% | 3.0 pp |

| August | 5.6% | 3.1% | 2.5 pp |

| September | Scheduled for release in mid-November | 2.9% | – |


**Supplement**

- Consumer price statistics are produced by the National Data Agency (국가데이터처; formerly Statistics Korea). September CPI was 2.9% (released Oct. 2), and core (excluding food and energy) was 2.8%.
- The August CPI of 3.1% included a base effect of about 0.6 pp from last August's telecommunications fee reductions, and in September that effect dropped out and it came down to 2.9%. Petroleum products were still +14.8% year on year in September, and the government estimated that without the oil maximum price system the September rate would have been 3.5%. There were also reports that petroleum products had a large share in the August CPI as well.
- In its August economic outlook, the Bank of Korea presented 2026 consumer prices of 2.7%, core 2.5%, and growth of 3.3%.
- Since "core" has two definitions (excluding food and energy; excluding agricultural and petroleum products), different core figures should not be compared directly.

Let us read it through the quantity equation (this essay's rough calculation).

- `ΔV ≈ inflation rate + real growth rate − M2 growth rate`.
- Let us put in the August values. Prices are 3.1%, the real growth rate is 3.3% for 2026 from the Bank of Korea's August outlook, and the new M2 growth rate is 5.6%, so ΔV ≈ 3.1 + 3.3 − 5.6 = **+0.8%**.
- This calculation used CPI in place of the GDP deflator and mixed an annual forecast with monthly data, so it is a rough estimate. The conclusion is only that "V has barely changed."
- Sensitivity example: if the old M2 growth rate of 11.6% (May) is put into the same equation, ΔV ≈ 3.1 + 3.3 − 11.6 = −5.2%. This is a hypothetical example mixing months and indicators and is not a measured value. What this example shows is that **depending on which M2 is used, the judgment of "is V stable?" changes**.

**The Bank of Korea's money–prices research: 1997 and 2025.** The Bank of Korea's own assessment of the relationship between money and prices in Korea has differed by period.

- **1997.** "An Analysis of the Relationship between Money and Inflation" (통화와 인플레이션의 관계분석) by the Bank of Korea's Research Coordination Office (Kim Hyeon-ui and Jeong Ik-jun [김현의·정익준], Nov. 1997) estimated that a 1-percentage-point rise in the M2 growth rate raises inflation by about 0.51 percentage points over two years. The effect of a 1-percentage-point rise in the growth rates of unit labor cost and energy prices was about 0.08 percentage points. The study concluded that the money stock is the most important variable determining inflation and that its effect appears with a lag of 2–3 years, so the money stock should be seen not as a short-term business-cycle adjustment tool but as an anchor for inflation. However, it also stated that for forecasting consumer prices, Phillips-curve-based models are more useful than the P* model. In the year after this study appeared (1998), the Bank of Korea switched from money-stock-centered operation to inflation targeting (Section 5).
- **December 2025.** The Bank of Korea's liquidity commentary ("Understanding the Recent Liquidity Situation") writes that it judges that the "price and liquidity channels are not having a significant effect" on the recent rise in the won/dollar exchange rate. The reasons are that there is no large difference in long-term inflation expectations between Korea and the United States and that the consumer price gap has actually widened. The same piece also writes that if the inflation gap with the United States widens because of domestic liquidity expansion, that could be a factor pushing the exchange rate up to that extent, and it presents, together, an M2 growth rate excluding products not included in U.S. M2.
- **The voices on the other side.** In the domestic press, there have been an editorial arguing that if the money stock grows faster than the size of the economy it stimulates prices and asset markets (Digital Times, after the report of M2 at ₩4,184 trillion in May 2026), and criticism that the Bank of Korea tolerated money stock growth even in a tightening period (The Scoop, 2025). Their M2 figures are on the old basis.

The 1997 study saw the money stock as an anchor, and the 2025 commentary sees a low impact of the liquidity channel in relation to the exchange rate. The two pieces differ in object (consumer prices versus the exchange rate), period, and method, so they cannot be seen as contradicting each other. This essay does not judge which side is right, and records only that even in Korea the relationship between money and prices has not been fixed to a single answer.

**Cautions**

- It is only a few months, a few data points. Too few to speak of correlation or causation.
- M2 is on an average-balance basis, and CPI is the year-on-year comparison of the monthly index. The bases differ.
- Since oil prices accounted for a large share of this year's price increase, it is unknown how much of the roughly 3% inflation can be explained by money.

---

### 5. The Change in M2's Status: From Steering Wheel to Dashboard

The preceding sections were about the **definition** of M2 shaking. M2's **status**, that is, what role it plays in policy, also shook. We list only what was confirmed, as a timeline.

- **1975.** Goodhart, presenting British monetary management experience at a Reserve Bank of Australia conference in Sydney, said to the effect that any statistical regularity tends to collapse once pressure is placed upon it for control purposes, and this later came to be called Goodhart's law.
- **1976.** Goldfeld published "The Case of the Missing Money" in the Brookings Papers on Economic Activity. In the mid-1970s the existing money demand function systematically over-predicted actual money demand, and Enzler, Johnson, and Paulus dealt with the same phenomenon in the same year. It was interpreted that financial innovation changed how money is held and the demand function shifted.
- **Oct. 6, 1979.** Volcker's Fed announced that, instead of targeting the federal funds rate, it would control non-borrowed reserves in order to hold down M1 growth. The federal funds rate rose from 11% in September 1979 to nearly 18% in March–April 1980.
- **Oct. 5, 1982.** The FOMC set aside the non-borrowed reserves target. There is a commentary that the Fed returned to a price (interest rate) focus rather than quantity, citing financial innovation and falling inflation.
- **1987.** The Fed took M1 off as a target indicator and turned its eyes to broad money such as M2.
- **July 1993.** Chairman Greenspan, in congressional testimony on July 20, said to the effect that M2 had lost its status as a reliable indicator of financial conditions, and effectively set aside monetary targets. The San Francisco Fed summarized this as a judgment that "the historical relationship among money, income, and prices had largely broken down," and a New York Fed study tried to explain M2's abnormal behavior in this period by capital constraints on banks and savings institutions.
- **1998.** The Bank of Korea introduced inflation targeting, and was reported to have explained that financial innovation and financial liberalization had made the relationship between intermediate targets such as the money stock and the final target unclear, so that the previous approach was no longer valid. The explanation that the Bank of Korea has since looked at Lf, financial conditions indices, the neutral rate, and so on, together with M2, in judging liquidity is in the reports quoted in Chapter 4.
- **1998–2003.** In December 1998 the ECB announced a reference value of 4.5% for M3 growth as a marker of the "prominent role of money." It was derived from the definition of price stability (an increase in the HICP of below 2%) together with the assumptions of trend potential output growth of 2–2.5% a year and a trend decline in M3 income velocity of 0.5–1% a year; by calculation, 2 + 2 + 0.5 gives roughly 4.5. That is, the reference value was a policy figure with the equation of exchange of this chapter's opening, and an assumption about V, built into it. The ECB also said from the beginning that deviations would not be corrected mechanically. In August–October 2001 the three-month average of M3 growth reached 6.8%, well above the reference value, and the ECB explained that investors had shifted their portfolios from shares and other longer-term assets into the liquid short-term assets included in M3, that this was temporary, and that it should not be read as an inflation signal. In its strategy review of May 8, 2003, the ECB discontinued the annual review of the reference value and moved monetary analysis down to a cross-check of economic analysis.
- **July 2000.** The Monetary Policy Report did not set ranges for money and debt growth for 2000–2001, and the expiry of the legal reporting requirement and uncertainty about velocity were explained as the reasons.
- **Nov. 2005 / Mar. 2006.** The Fed announced (Nov. 10, 2005) and then ended (Mar. 23, 2006) publication of M3 (Chapter 1, Section 1.4).
- **July 2021.** In its strategy review the ECB replaced the two pillars with an integrated assessment built on an economic analysis and a monetary and financial analysis, and recorded that, owing to a weakening of the link between monetary aggregates and inflation, the original focus of monetary analysis had become less important. An ECB paper describes a gap between the formal description of the strategy after 2003 and actual practice, in which monetary analysis had been redirected toward assessing the transmission of monetary policy. In August 2026 euro-area M3 grew 3.5% year on year (seasonally adjusted; M1 2.9%, marketable instruments 7.1%), below the 4.5% once set as the reference value, which the ECB has not used since 2003.

These markers all point in the direction that **making monetary aggregates the target of policy was difficult**, but the reasons are explained differently by each institution. The three below are this essay's interpretations and overlap one another.

- **Instability of demand.** The explanation is that financial innovation changed how money is held and shook the relationship between the money stock and income and prices. Goldfeld's "missing money" (1976) and Goodhart's law are often cited in this context. That the title of Duca's (2000) paper on M2's abnormal behavior in the 1990s is "Financial Technology Shocks and the Case of the Missing M2" reads as an expression that continues Goldfeld's title (interpretation), and its explanation is the shift to funds in Section 3.3.
- **Change in policy regime.** In a regime that uses the interest rate as the instrument, the money stock follows as an outcome.
- **Instability of definition.** This is what the earlier chapters of this essay showed. However, whether the instability of definition was the reason for abandoning targets cannot be confirmed from the above sources.

M2 has not disappeared. That the Bank of Korea refined the definition again in December 2025 and even published in parallel reads as the market and policy authorities still consulting M2, which has stepped down from the steering wheel of policy (interpretation). The San Francisco Fed also wrote in 1998 that there were signs M2 was regaining a "normal" relationship. Status, once lowered, does not end there; it rises and falls.

---

### 6. Long Run and Short Run, High Inflation and Low Inflation: Where Is the Correlation High?

For the quantity theory to read as a claim, the data must speak. McCandless and Weber (1995), using 30 years (1960–1990) of data from 110 countries, reported that the correlation between money growth and inflation is very high under all three definitions of money, and that there is no correlation between money growth and real output growth (only a weak positive correlation in the OECD subsample). The correlation coefficients are 0.925 for the monetary base, 0.958 for M1, and 0.95 for M2, while the correlation between money growth and real output growth is −0.03 to −0.14, and the correlation between inflation and output growth is about −0.10, essentially none. The facts the researchers summarized are three: a high correlation between money and prices, no correlation between money and output, and no correlation between prices and output.

Follow-up research summarizes that this relationship weakens when inflation is low. Olivo (2024), re-analyzing a panel of 133 countries for 1961–2022, reports that the effect of money growth on prices diminishes the lower the inflation rate is, while also summarizing that the effect of the most recent 30 years did not diminish noticeably compared with the preceding 30 years. That is, "weaker at low inflation" and "weaker over time" are different claims, and only the former is supported by these data.

- In the **long run, with high inflation, as an average across many countries**, money and prices move almost together. The hyperinflation cases seen earlier are the extreme.
- In the **low-inflation, short-run, single-country** setting, the relationship is weak and unstable. This connects with the abandonment of intermediate targets in Section 5.

Correlation is not causation. Whether the money stock created prices, or whether the expectation that prices will rise and fiscal circumstances brought about money issuance (the fiscal-centered reading), cannot be sorted out from this correlation alone (interpretation). This essay's principle of withholding judgment is maintained here too.

---

### 7. Summary

- The quantity theory is a relationship among four variables, M, V, P, and Y. This essay has shown only that M and V are **not fixed objects but values that depend on definitions**.
- When the definition changes, the same economy appears to have a different V (Korea about 0.59 versus 0.65). Even when the definition is the same, V moves greatly depending on the period (United States 2020, −21.5%).
- Therefore, a sentence such as "since M2 grew by x%, prices will rise by y%" must state at least three things together: which M2, which period, and how V is assumed.
- Studies that distribute the shares of money, supply, and fiscal policy differently in the 2021–23 inflation coexist, and even studies emphasizing money use Divisia indicators rather than simple-sum M2 (Section 3.2). M2 diverges from economic activity when funds flow to and from funds (Section 3.3).
- M2 has changed not only in definition but also in policy status (Section 5), and the correlation between money and prices is high at high inflation and in the long run (Section 6).

---

### The One Thing to Remember from This Chapter

> M2 is a value that depends on its definition, and its status in policy has also changed. The sentence "if M2 grows, prices rise" must first state which M2, which period and price range, and how V is assumed.

---

### Sources (Chapter 5)

- FRED, Velocity of M2 Money Stock (M2V). https://fred.stlouisfed.org/series/M2V (Sept. 30, 2026 update)
- Goldfeld, S. M. (1976). "The Case of the Missing Money." Brookings Papers on Economic Activity, 1976(3), 683–740. Enzler, Johnson & Paulus (1976). "Some Problems of Money Demand." BPEA 1976(1).
- Goodhart, C. (1975). "Problems of Monetary Management: The U.K. Experience." Reserve Bank of Australia, Papers in Monetary Economics. Central Banking, "Lifetime achievement: Charles Goodhart".
- Federal Reserve Bank of San Francisco (Mar. 1998). "Is It Time to Look at M2 Again?" Economic Letter. Federal Reserve Bank of New York (1999). "What Was Behind the M2 Breakdown?" Staff Report 83. Atlanta Fed, macroblog (Nov. 24, 2005). Christian Science Monitor (Aug. 6, 1993).
- McCandless, G. T., & Weber, W. E. (1995). "Some Monetary Facts." Minneapolis Fed Quarterly Review 19(3), 2–11. https://doi.org/10.21034/qr.1931 ; Olivo, V. (2024). "A Reexamination of the Relationship Between Money Growth and Inflation Around the World: 1961–2022." MPRA 122587 ; Duca, J. V. (2000). "Financial Technology Shocks and the Case of the Missing M2." Journal of Money, Credit and Banking 32(4). ECB press release and speech of May 8, 2003. St. Louis Fed and SF Fed commentary on the chronology of Fed monetary targets, Brookings commentary.
- Bordo, M. D., Duca, J. V., & Jones, B. E. (2025). "Broad Divisia Money, Supply Pressures, and U.S. Inflation Following the COVID-19 Recession." NBER WP 34017. https://www.nber.org/system/files/working_papers/w34017/w34017.pdf ; Dallas Fed WP 2306 (2023) https://www.dallasfed.org/-/media/documents/research/papers/2023/wp2306.pdf ; FEDS 2025-070 https://www.federalreserve.gov/econres/feds/files/2025070pap.pdf ; Bernanke, B., & Blanchard, O. (2025). "What Caused the US Pandemic-Era Inflation?" AEJ: Macroeconomics 17(3), 1–35, doi:10.1257/mac.20230195 (NBER WP 31417) ; Gagliardone, L., & Gertler, M. (2023). "Oil Prices, Monetary Policy and Inflation Surges." NBER WP 31263 (NBER Digest, July 2023) ; Bank of Korea economic analysis, "An Analysis of the Relationship between Money and Inflation" (Nov. 1997) https://www.bok.or.kr/portal/bbs/P0000556/view.do?menuNo=200440&nttId=123 ; Bank of Korea, "Understanding the Recent Liquidity Situation" (Dec. 2025) ; Digital Times (June 2026), The Scoop (2025).
- BLS Consumer Price Index news release (July 13, 2022). S&P Global Market Intelligence (May 2023), thetrading.tools (Aug. 2026).
- National Data Agency, "Consumer Price Trends, September 2026" (Oct. 2, 2026), reports: Kyunghyang Shinmun, SBS Biz, The Fact, Korea Daily. Reports on the Bank of Korea economic outlook (Aug. 2026).

- ECB, Press release of May 8, 2003, "The ECB's monetary policy strategy" https://www.ecb.europa.eu/press/pr/date/2003/html/pr030508_2.en.html ; "Review of the quantitative reference value for monetary growth" (Dec. 5, 2002) ; Introductory statement of Dec. 6, 2001 ; Monthly Bulletin, Dec. 2001. ECB account of the 2020–21 strategy review (Account of the Governing Council meeting, July 2021); ECB speech, "Modern monetary analysis" (June 26, 2024); ECB press release, "Monetary developments in the euro area: August 2026" (Sept. 25, 2026) https://www.ecb.europa.eu/press/stats/md/html/ecb.md2608~406f8d243d.en.html
- Barnett, W. A., Lee, J., & Mohiuddin, N. (2024). "Constructing Divisia Monetary Aggregates for the Asian Tigers." Journal of Risk and Financial Management 17(10), 435. https://doi.org/10.3390/jrfm17100435 ; Hahm, J. H., & Kim, J. T. (2000). "The Signals from Divisia Money in a Rapidly Growing Economy." In Divisia Monetary Aggregates (Palgrave Macmillan).
---

## Chapter 6. Overall Verification, Classification of Conflict Types, List of M-Number Confusions, Open Questions, and Conclusion

 
---

### 1. Recalculation of Key Figures

The arithmetic in this essay has all been recalculated and checked. The main items are as follows.

- Gap between Korea's new and old M2: 4,466.3 − 4,056.8 = ₩409.5 trillion; the new M2 is 9.2% smaller than the old M2.
- 1929–33 M1 −32.6% (October base) and −27.9% (September base); currency + total deposits −35.2%.
- Agreement of the back-calculated cash share of 8.4% with the 8.37% computed directly from level values, and the subsequent 15.8%.
- U.S. M2V −28.0% (2007–2019), −10.5% (2008–09), −21.5% (Q4 2019–Q2 2020), +21.8%, +7.6%.
- Japan's M2/monetary base 1,296.4 ÷ 543.0 ≈ 2.39; the monetary base from about ¥659 trillion in December 2024 to ¥532.8 trillion in September 2026, about −19%.
- U.S. M2 from about $21.75 trillion in April 2022 to about $23.2 trillion in June 2026, about +6.7%.

---

### 2. Classification of Conflict Types

| Conflict | Type | Explanation |

| 1929–33 monetary decline −21% to −42% | A+B | The definition of M (F–S M4 versus total deposits) and the window (annual average versus monthly peak-to-trough) both differ |

| F–S M1 −32.6% versus −27.9% | B | Choice of starting month (October versus September) |

| Bank closures one-third / about half / 9,000 (30%) | A+B | The object counted, the period, and the denominator differ |

| U.S. M2 peak April 2022 versus July, decline 4.7% versus 4.9% | C | Difference in data revision vintage |

| M2V Q2 2020 1.10 versus 1.126 | C | Quarterly GDP revision |

| Korea old M2 11.6% versus new M2 5.8% | B | Whether beneficiary certificates are included |

| Korea October 2025 M2 ₩4,471.6 trillion versus ₩4,466.3 trillion | B | Whether seasonally adjusted |


| Japan: Greenwood "almost unchanged" versus Harada "increased" | A+B | Different periods and comparison targets |

| Japan M2 time series around 2008 | B | Discontinuity from the statistical overhaul |

| Zimbabwe: which body stopped statistics (CSO versus RBZ) | C | Difference in attribution at the reporting stage |

| Venezuela: start date of exceeding 50% (Nov. 2016 versus Nov.–Dec. 2017) | B | Daily exchange-rate basis versus monthly CPI |

| Greece: monthly peak 13,800% versus 8.55×10⁷ % | B | Indicator (gold exchange rate versus food prices) and period (month versus 10-day conversion) |

| Yugoslavia: 24-month cumulative 10²² versus 10²¹ | B | The last two months included |


For the Friedman–Schwartz factor-by-factor effects (monetary base +17½%, deposit/currency ratio −37%, deposit/reserve ratio −20%, interaction +10%, total −35%), the simple sum does not match the total rate of change. This is because each term is the effect "when only that factor changed" and there is a separate interaction term (Chapter 2, Section 3.3). None of the conflicts in this essay is classified as a pure error.

---

### 3. List of M-Number Confusions

This collects cases in which the same symbol points to different objects.

1. **F–S's M2** is currency + commercial bank total deposits, and differs from today's U.S. M2. What is close to today's M2 is F–S's M4.
2. **U.S. M1** includes savings deposits after May 2020. It cannot be read continuously with M1 before that (a series that has been recalculated retroactively can be read continuously).
3. **U.S. M3** has not been published since March 2006. Institutional MMFs and large deposits used to be in it.
4. **Euro-area M2** does not include MMFs and RPs. These are in M3. Korea's M2, which has the same name, includes MMFs and RPs.
5. **Japan's M3** does not have investment trusts and money in trust, which are in L. Japan's M2 differs between the new series after June 2008 and the earlier "M2+CD" series.
6. **Korea's M2** differs between the old standard through December 2025 (including beneficiary certificates) and the new standard from January 2026 (excluding beneficiary certificates, including notes and note-type CMAs). In 2026 the two are published in parallel.
7. **China's M1** includes, from January 2025, personal demand deposits and the customer reserves of non-bank payment institutions. The balance grew from about ¥63 trillion to the ¥100 trillion range.
8. **Cagan's M** is banknotes (paper money) and does not include deposits.
9. **Monetary base (M0)** is cash and reserves. It is a different layer from M2.
10. **Multiplier m** is not a causal law but the identity M ÷ H.
11. **M2V** is FRED's definition (quarterly nominal GDP ÷ quarterly average M2), and is the same concept as Korea's GDP/M2 ratio, but the bases differ.
12. **"Core inflation"** has two definitions in Korea (excluding food and energy; excluding agricultural products and petroleum products).
13. **The IRA and Keogh deduction in U.S. M2** is, from the H.6 of July 28, 2026, a separate deduction from the total rather than a deduction by component. The amounts of the small time deposit and retail MMF components may differ from values published before that.
14. **Korean statistics publishers**: consumer prices are published by the National Data Agency (formerly Statistics Korea), and the money stock by the Bank of Korea.

---

### 4. New Forms of Money: Questions Still Open

The Federal Reserve staff's FEDS Note (Sept. 4, 2026) reviews how stablecoins, tokenized deposits, and tokenized MMFs enter the U.S. monetary aggregates. The key points are as follows.

- **Tokenized deposits**: banks report them on the same reporting forms as existing deposits, so they are already counted in M1 or M2 and are not separately distinguished. There is no risk of double counting.
- **Tokenized MMFs**: they enter existing MMF reporting, and depending on the reporting entity there is some risk of double counting.
- **Stablecoins**: there is currently no separate item in H.6. When reserves are held in bank deposits or MMFs, those assets are already counted, so adding stablecoins could result in double counting, and its extent depends on the issuer's reserve composition. The Note does not change definitions and stops at summarizing the review results.
- The Note states of itself that it reflects the authors' personal views and is not the Federal Reserve's policy position.

There is also an institutional clock. The U.S. GENIUS Act was signed on July 18, 2025, and its effective date is the earlier of January 18, 2027 or 120 days after the final regulations are issued. The rulemaking deadline in mid-2026 was not met, and the OCC was reported to be targeting a final rule in November 2026. In Europe, MiCA applied in stages on June 30, 2024 (the stablecoin-related title) and December 30, 2024 (the rest).

**Interpretation.** Following the principle of Chapter 1, Section 1.1 (the boundary is set by an asset's use), the more widely stablecoins are used as a means of payment, the greater the likelihood that they become candidates for M1 or M2. However, the double-counting problem and the composition of issuers' reserves must be sorted out first. This essay does not predict that the definition will change. What is confirmed as fact extends only to Federal Reserve staff having begun to review this question publicly.

Other questions this essay has left open are as follows.

- How much did each component of M2 move during the 2020–21 expansion and the 2022–23 contraction?
- How will the gap between Korea's new and old M2 be used in policy discussion after the end of parallel publication (scheduled for December 2026)?
- What is the composition (shifts to time deposits, investment trusts and money in trust, and so on) of the phenomenon in Japan in which the monetary base at −15% and M2 at +2% go together?

---

### 5. A Collection of Interpretations

This brings together in one place the interpretations of this essay that had been scattered about. All of them are this essay's readings, not a consensus of the literature.

1. The boundary of money is redrawn when institutions, technology, and standards change (Chapter 1).
2. The aggregate and the composition are different questions. Even if M2 is the same, the story differs if the allocation between M1 and non-M1 changes (U.S. 2020), and even when the total has fallen, where it fell may have decided the outcome (1929–33 and 2022–23, Chapter 2).
3. When paper money collapses, money moves in three directions—domestic substitute units, foreign currency and gold, and measurement indicators—and all of them reduce the tax base of the inflation tax (Chapter 3).
4. There is no law that the monetary base and M2 must move in the same direction. The United States in 1931–32 and Japan's QQE and normalization are cases (Chapters 2 and 4).
5. When the definition is changed, the question changes. Korea's new and old M2 answer different questions (Chapter 4).
6. M2 has stepped down from the steering wheel of policy to the dashboard, but has not disappeared (Chapter 5).

---

### 6. Confirmation Grades and Scope of the Materials

| Grade | Materials covered |

| Primary confirmation (authorities and original data) | The abstracts of Bernanke–Blanchard (2025) and Gagliardone–Gertler (2023), the Bank of Korea economic analysis (1997) and the December 2025 liquidity commentary, the Cagan table (Minneapolis Fed WP 343, QuantEcon reproduction), IMF PIN 09/53, the original text of Bordo–Duca–Jones (NBER WP 34017), the Fed's FEDS Notes and H.6, the ECB definition table, Bank of Japan statistics, the People's Bank of China report, the IMF manual press release, FRED M2V, the NBER monthly series, Friedman–Schwartz (1965), the speeches of Bernanke (2004) and Harada (2017), the Hanke–Krus table |

| Secondary confirmation (cross-checking across multiple reports and arithmetic verification) | The Bank of Korea's monthly and overhaul announcements, Monetary Policy Board decisions and economic outlook, National Data Agency CPI, announcements of the Banco Central de Venezuela and annual prices, CEPAL's money growth rates (excerpts from published reports), the Caixin commentary, U.S. M2 revised-vintage figures, the 2008 MMF and 2023 SVB events, the conclusions of Hall–Tavlas–Wang (2023) and Duca (2000) (on the basis of citations by Bordo et al.) |

| Literature confirmation (recalculation of cited figures) | The hyperinflation figures of Chapter 3 (Cagan, Hanke & Kwok, Petrović–Bogetić–Vujošević, Nielsen, and others) |


- **Korean figures.** The Bank of Korea's monthly and overhaul announcements were confirmed through cross-checking across multiple media reports and through summing arithmetic (exclusion of beneficiary certificates −₩497.1 trillion, mega-IB notes and CMAs +₩44.7 trillion, compilation improvements and so on +₩43.0 trillion closing to −₩409.5 trillion) (secondary confirmation).
- **Itemized breakdowns.** The large items of the Korean overhaul results (beneficiary certificates −₩497.1 trillion, mega-IB notes and CMAs +₩44.7 trillion, compilation improvements +₩43.0 trillion) were confirmed, but the detailed composition of each item and the balances of the component items of Japan's M2 and M3 can be broken down only if the original tables are available. The compositional decomposition of the 2022–23 decline in U.S. M2 and the numerator–denominator decomposition of the Q2 2020 plunge in M2V are not included for the same reason.
- **Historical materials.** The Anderson annual-average level values follow the compilation of the Friedman–Schwartz series; the monthly M1 peaks and troughs were checked against the NBER monthly series, and the factor-by-factor effects against the original text of Friedman–Schwartz (1965).
- **Hyperinflation cases.** The extreme values in Chapter 3 (Hungary 4.19×10¹⁶ % and 207% daily; Zimbabwe 7.96×10¹⁰ % and 98.0% daily; Yugoslavia 3.13×10⁸ % and 64.6% daily) were checked against the Hanke–Krus table and Hanke's commentary. The other figures are based on the literature concerned, and their internal consistency was recalculated. The September 2026 Venezuela figures were confirmed through multiple media reports of the BCV announcement (secondary confirmation). Not covered are the monetary aggregate (M) time series of each country, the size of Paal's (2000) remeasured aggregates, and the substitute means behind the fall in Yugoslavia's M1/GDP (whether foreign currency or goods in kind).
- **Interested parties' positions.** The statements of Greenwood (an asset manager's economist), Harada (a central bank board member), Hanke (an advocate of monetary reform), and the Bank of Korea (the party that changed the definition) were all noted with their positions and placed in parallel.
- **Vintage.** FRED and H.6 values change with revisions. The M2V in this essay is the September 30, 2026 vintage, and U.S. M2 is the reported vintage as of August–September 2026. The next M2V update is October 29, 2026, and Korea's September M2 is scheduled for release in mid-November.
- **What was not judged.** Which M is the true money stock, whether M2 explains prices, whether the new M2 is right, and whether the overhaul was aimed at a particular debate.

---

### 7. Conclusion

This essay began from a single question. Not "how much money is there?" but "what are we to count as money?"

- Even in normal times the boundary is a promise. The United States redrew an indicator of the same name because regulation changed (2020), Japan because its financial structure changed (2008), China because its means of payment changed (2025), and Korea in order to follow international standards (2026).
- In times of crisis the promise visibly moves. In 1929–33, bank deposits came down into cash and the total shrank, and in hyperinflation, substitute units and foreign currency took over the role of money from official banknotes.
- The monetary base, M2, bank lending, and velocity are different layers, so the movement of one layer does not guarantee the movement of another. Japan's QQE and normalization are cases in both directions.
- The last open question is stablecoins and tokenized assets. When use changes, the boundary may be redrawn again.

So the habit this essay recommends is simple. When citing a money stock figure, write next to the number **(1) which indicator (M1, M2, old/new), (2) which period and what window (average vs. end-of-period balance, annual average vs. peak-to-trough, unadjusted vs. seasonally adjusted), and (3) which data vintage (revised edition)**. A number with these three attached can be corrected when it is wrong, and a number without them cannot be compared even when it is right.

---

### Sources (Chapter 6)

- Payne & Styczynski (Sept. 4, 2026), FEDS Notes. The source lists of Chapters 1–5.
- State of GENIUS Act implementation: Chapman and Cutler GENIUS Act Rulemaking Tracker (June–Aug. 2026), Tazapay "The GENIUS Act One Year On" (2026), PYMNTS (2026). The application dates of Europe's MiCA follow the EU's official schedule.



---
## Table of Contents

- Chapter 1. The Definition Map: Where Does M2 End?
- Chapter 2. Monetary Collapse on the Deflation Side (United States 1929–33)
- Chapter 3. The Shift of the Monetary Boundary on the Hyperinflation Side (Hungary, Zimbabwe, Venezuela, Greece, Yugoslavia)
- Chapter 4. Japan and Korea: The Monetary Base and M2, and the "Old M2 / New M2"
- Chapter 5. The Quantity Theory and Velocity: Before Asking "If M2 Grows, Do Prices Rise?"
- Chapter 6. Overall Verification, Classification of Conflict Types, List of M-Number Confusions, Open Questions, and Conclusion

---

## Summary at a Glance

- **Chapter 1.** Even when the name "M2" is the same, the items it includes differ by country and by period. The United States (May 2020, and the July 2026 change in how IRA and Keogh balances are deducted), Japan (June 2008), China (January 2025), and Korea (January 2026) have all corrected their definitions or methods of aggregation, and the treatment after the correction split into retroactive recalculation, parallel publication, and a break between old and new.
- **Chapter 2.** The "monetary collapse" of the United States in 1929–33 diverges from −21% (F–S M4, annual average) to −42% (commercial bank total deposits, monthly peak-to-trough). Cash rose and the monetary base rose too, yet the money stock fell.
- **Chapter 3.** When paper money collapses, people use other things as money. Aggregates that count only banknotes shrink together with the inflation tax base. The interpretation that hyperinflation ended not because money growth stopped but because the fiscal and institutional regime changed is the leading one, but it is contested.
- **Chapter 4.** In Japan, while the monetary base swelled several-fold, the M2 growth rate stayed in the 2–4% range a year, and even now, when the monetary base is shrinking by double digits after normalization, M2 has actually risen from the 1% range to the 2% range. In Korea, when the definition was changed, the growth rate for the same month fell by nearly half.
- **Chapter 5.** Velocity is a computed remainder, and M2's policy status has stepped down from the steering wheel (intermediate target) to the dashboard (information variable). Research is divided over the shares of money, supply, and fiscal policy in the 2021–23 inflation, and M2 has the weakness of diverging from economic activity when funds flow to and from funds. The correlation between money and prices is reported to be high at high inflation and in the long run and weak at low inflation and in the short run.
- **Chapter 6.** Most conflicts are of Type A+B, so they do not converge to a single value. When citing, three things must be written together: the indicator, the period, and the basis.

---

## How to Read

- Figures always state together the **reference month, average vs. end-of-period balance, unadjusted vs. seasonally adjusted series, and old vs. new standard**. This essay calls this "unit discipline."
- Sources are identified in the text by institution and name of the literature, and are collected as a list at the end of each chapter. The confirmation grades are summarized in Chapter 6, Section 6. Those for which authorities and original data were read directly are primary confirmation, and those for which several independent media reported the same figure and the totals and arithmetic matched are secondary confirmation; both grades were used as confirmed figures. Most Korean figures are secondary confirmation, and most Japanese, U.S., euro-area, and Chinese figures are primary confirmation.
- Calculations are marked with "by calculation" and this essay's judgments with "interpretation."
- This essay does not pass judgment on "which M is the true money stock," "if M2 grows, do prices rise," or "is the new M2 right." Its role is to state first the definitions needed for such a judgment.
- The scope and limits of the materials are collected in Chapter 6, Section 6.
