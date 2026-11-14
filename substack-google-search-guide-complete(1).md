# How to Get Your Substack Listed on Google Search

*As of November 2026. Substack and Google screens change, so use this as a map, not a script.*

## TL;DR

**You register your Substack in one place: Google Search Console.** To do that you have to prove the site is yours, and Substack doesn't let you edit your site's hidden code. So you prove ownership by entering a Google ID in your Substack settings. Google Tag Manager is the method I recommend first (slightly easier than Google Analytics in my experience), but only one method needs to succeed. After that, you submit your **feed** (the main thing you submit) and request indexing for each new post. A sitemap is an optional extra that only some publications have.

**Addresses.** Replace `seoulinside` with your own Substack name, and put `https://` in front when you type an address into a tool.

- Your Substack: `seoulinside.substack.com`
- Feed: `seoulinside.substack.com/feed`
- Sitemap (may not exist): `seoulinside.substack.com/sitemap.xml`

Paste the feed and sitemap addresses into your browser's address bar to check them. A normal feed shows a plain-text screen listing post titles, links, and dates. A normal sitemap shows a list of post addresses. If you use a custom domain, use the address people actually visit instead (for example, `www.mydomain.com`).

**Step 1. Pre-check.** You need at least one public (Everyone) post, and your publication must not be set to Private. Do the whole setup in a desktop browser; the screens in this guide are the desktop versions.

**Step 2. Add your site in Search Console.**

1. Log in at `search.google.com/search-console` with a Google account. Use this same account for every Google tool below.
2. Choose the **URL prefix** property type and enter your address with `https://` in front. A Domain property can only be verified through DNS, so the Tag Manager and Analytics options won't appear.
3. In the verification window, skip the big "HTML file" option (Substack has nowhere to upload a file). Expand **Other verification methods** and leave the window open.

**Step 3. Get a verification ID and put it in Substack (one method is enough).**

*Recommended first: Google Tag Manager.*

1. In a new tab, go to `tagmanager.google.com` (same Google account) and create an account (any name, your country).
2. Name the container after your Substack address and choose **Web**.
3. Accept the terms and close the "Install Tag Manager" window. You don't need to paste any code.
4. Copy the ID that starts with `GTM-` at the top of the workspace.
5. Ignore every card and banner. An empty container ("0 changes") is normal; you don't need to create any tags.
6. Click the blue Submit button once to publish the container.
7. In Substack, go to Dashboard → Settings → Analytics (older guides call it Advertising Analytics), paste the ID into the Google Tag Manager ID field (no spaces), and save.

*Other options:* Google Analytics (GA4) works too and is a good choice if you already use it (section 8). A Google Site Verification (HTML tag) field exists only on some accounts, and custom-domain users can use DNS (section 9).

**Step 4. Verify.** Back in Search Console, choose Google Tag Manager under "Other verification methods" and click **Verify**. If Search Console already shows an "automatically verified" notice, you're done. If it fails, wait. It can take a few minutes to 24–48 hours.

**Step 5. Submit your feed.** Go to Indexing → Sitemaps. In the "Add a new sitemap" area, the front part of the address is already filled in. Type only `feed` in the empty field and submit. The type shows as RSS, and a status of **Success** means Google has read your list. Success doesn't mean your posts are indexed. If you see "Couldn't fetch" right after submitting, that is common and often temporary. Check again after a few hours to two days.

Then open `yourname.substack.com/sitemap.xml` in your browser. If it shows a list of post addresses, submit `sitemap.xml` the same way (the type shows as Sitemap). If you see the message "This publication does not have a sitemap," an error, or a blank screen, that is normal, not a setup error. Skip it, or delete the row if it keeps failing.

The two serve different purposes. The feed covers roughly the 20 most recent posts, while a sitemap lists all posts, so the "Discovered pages" numbers differ.

**Step 6. For each new post.** Paste the post address (for example, `seoulinside.substack.com/p/post-slug` with `https://` in front) into the URL Inspection bar at the top of Search Console. If it says "URL is not on Google," click **Request indexing**. Once per URL is enough. The daily limit isn't published; people report about 10–12, so do your most important posts first.

**Step 7. Check results.** After 2–4 weeks, open Performance to see which searches bring people to you.

**Remember:**

- Use the same Google account from start to finish, and choose URL prefix (the only exception is a custom-domain user who verifies with DNS, which requires a Domain property; see section 9).
- Don't delete the ID from Substack after verification, because it may undo the verification.
- A feed and a sitemap are only hints that your posts exist. They don't guarantee indexing. A few days to a few weeks is normal.
- Google search may be only a small share of your readers (around 5% in some reports), so keep up with social media and Substack's own recommendations too.

---

## Full guide

### 1. Labels used in this guide

- **[Google docs]** and **[Substack docs]**: stated in official documentation.
- **[Author-tested]**: what I saw on my own publication.
- **[Other authors' reports]**: reported by other writers or commenters, not confirmed by me.
- **[Unofficial]**: widely observed figures that the company has not published.

### 2. Four things to do, and which kind of Substack you have

Four things to do:

1. Prove to Google that your Substack is yours (ownership verification).
2. Tell Google your list of posts (submit your feed, and your sitemap if you have one).
3. Quickly notify Google each time you publish a new post (request indexing).
4. See which search queries bring people to you (Performance report).

Which kind of Substack do you have?

- **A. Default address (`yourname.substack.com`):** follow the sections in order.
- **B. Custom domain connected (`www.yourdomain.com`, etc.):** follow the sections in order, but read every `yourname.substack.com` in this guide as your own domain address, because visiting the Substack subdomain redirects to your custom domain. Also note:
  - Check `https://yourdomain.com/feed` and `/sitemap.xml` on your own domain (include `www` if your domain uses it).
  - When you submit them later: if you registered a URL prefix property, type just `feed` or `sitemap.xml`, because Search Console fills in the front part. If you registered a Domain property (DNS), type the full address instead.
  - Register your own domain address in Search Console, not the Substack subdomain. Google's FAQ suggests verifying both the `www` and non-`www` versions. **[Google docs]**
  - One more verification method opens up: DNS (section 9). Some writers also report seeing the Google Site Verification field after connecting a custom domain. **[Other authors' reports]**
  - When you connect a domain in Substack, enter it with `www` and enable the root-domain redirect so both forms load. **[Other authors' reports]**
  - A custom domain is a paid feature on Substack: a one-time $50 fee per publication, after which you can add or remove domains at no extra cost. **[Substack docs]** You also have to buy the domain itself from a registrar. Writers report that Substack redirects your old `substack.com` address to the new domain. **[Other authors' reports]** Check Substack's current terms before deciding.

### 3. Terms to know first

- **SEO (search engine optimization):** work that polishes your posts so they show up well in search results.
- **Indexing:** Google discovering your post and adding it to its searchable list. A post that isn't indexed can't be found in search. It's like a book arriving at a library but not being entered in the catalog, so patrons can't find it at the search desk.
- **Crawling:** Google's robot visiting and reading a web page. A page must be crawled before it can be indexed.
- **Google Search Console:** a free site-management tool from Google. You can check how your site appears on Google and submit your list of posts.
- **Ownership verification:** proving to Search Console that "this site is mine." You can't use Search Console until it's done.
- **Google Tag Manager (GTM):** a tool for attaching tracking code to a site. In this guide it serves as the channel for ownership verification.
- **Google Analytics (GA4):** a tool for seeing where visitors come from and what they read. It can also serve as a channel for ownership verification.
- **Sitemap:** a list of your site's post addresses. Think of it as a "map" you hand to Google.
- **Feed:** a subscription-style list collecting recent posts. Substack provides a feed for every publication, and Google accepts a feed just like a sitemap.

### 4. Step 0: Check where you stand

Before doing anything, check whether your Substack already appears on Google, and whether the feed and sitemap open. Replace `yourname` in the addresses with your own Substack name.

**Check 0. Are your posts public?** Surprisingly many people get stuck here.

- **Do you have at least one public (Everyone) post?** A new publication with no posts, or only a "Coming soon" page, may be marked noindex until you publish a post. If you only edit the "Coming soon" placeholder instead of writing a new post, the noindex mark may stay, so publish a new post and delete the placeholder. Verification may also go more smoothly, or may fail with an error, depending on whether Google has a few posts to read at that moment. **[Other authors' reports]**
- **Is your publication set to Private?** A private publication may have only its welcome page appear in search, and its posts are not indexed. Check the Privacy item in Settings. **[Substack docs]**
- **Is the audience for the post you want found set to Everyone?** Subscriber-only and paid posts are treated differently (see section 13).

**Check 1. Does it show up on Google?** Search `site:yourname.substack.com` in Google (no space after the colon). If a list of your post titles appears, Google already knows some of your posts. If nothing comes up, it hasn't been discovered yet. This is only a rough clue, not a precise tool for seeing your indexing status. (Custom domain: search `site:yourdomain.com`.)

**Check 2. Is there a sitemap?** Even if the answer is "no," don't worry. The feed works either way, and it is the first thing you will submit. Four ways to check, easiest first (the first two are the main tests; the last two are supporting clues):

1. **Look at the very bottom of your homepage.** If the bottom has four links (About, Archive, Recommendations, Sitemap), the account has a sitemap. If those links aren't there, the account probably has no sitemap. This rule held for the accounts I checked, and another author reports that these bottom links are missing on new publications. **[Author-tested; Other authors' reports]** It is only an indirect signal and can change if Substack changes its layout, so confirm with method 2. Clicking the Sitemap link opens `yourname.substack.com/sitemap`, a page for people to read with a year-by-year list of posts. The file you submit to Google is the XML in method 2, which is a different address.
2. **Open `https://yourname.substack.com/sitemap.xml` in your browser (the deciding test).** If it's normal, you won't see an ordinary web page but a text-style screen with post addresses listed one after another. Depending on the browser, a notice like "This XML file does not appear to have any style information" may appear with it, and that's normal. If you see the message "This publication does not have a sitemap," an error message, or a blank screen, this account doesn't have a sitemap yet. Submit just the feed.
3. **Open `https://yourname.substack.com/robots.txt` (a supplementary clue).** Substack provides this file in common to all publications, so you can't edit it. On accounts that have a sitemap, two lines are written at the bottom:

   ```
   SITEMAP: https://yourname.substack.com/sitemap.xml # sitemap
   SITEMAP: https://yourname.substack.com/news_sitemap.xml # news sitemap
   ```

   I haven't confirmed how these lines look on accounts without a sitemap, so use this only as a supplementary clue. I also haven't confirmed whether `news_sitemap.xml` needs to be submitted; this guide tells you to submit just `sitemap.xml`. In the same file you can see that `/feed` is not blocked (only private feeds like `/feed/private` are), so feed submission is safe. **[Author-tested]**
4. **Submit it in Search Console and look at the status.** After verification, submit as in section 11 and check that the status says "Success." This is the final check, because there are reports of addresses that open in a browser but that Google can't read.

**Check 3. Does the feed open?** Open `https://yourname.substack.com/feed`. If a text screen appears with the titles, links, and dates of recent posts, it's normal. The feed generally holds about 20 recent posts; mine held 21, and Search Console showed 21 discovered pages for it. **[Author-tested]** The exact number may differ by account, so feel free to count yourself.

For why some accounts have no sitemap, see section 11.

### 5. Add the property in Search Console

Choose **URL prefix** (the right-hand box when you first add a property; "Add property" in the top-left dropdown if you already have one). Enter your address with `https://` in front and click Continue. Copy the address from your browser to avoid typos.

- URL prefix treats `http` and `https`, and `www` and non-`www`, as different addresses. Use the address people actually visit.
- A Domain property can only be verified with a DNS record, so the Tag Manager, Analytics, and HTML tag options won't appear for it. **[Google docs]** (Choose Domain only if you are a custom-domain user who plans to verify with DNS; see section 9.)

### 6. Choose a verification method

Open your Substack Dashboard → Settings, scroll to the Analytics section (older guides call it "Advertising Analytics"), and see which fields you have. Substack's current help page for this section lists a Google Analytics Measurement ID field, a Google Tag Manager ID field, Meta (Facebook) and X (Twitter) pixel fields, a Parse.ly field, and a Facebook Site Verification field. **[Substack docs]** It does not list a Google Site Verification field, although some accounts still show one.

| Method | When to use it | Notes |
|---|---|---|
| **Google Tag Manager ID** | My first recommendation | In my experience slightly easier than GA4. **[Author-tested]** You need only the `GTM-` ID, and an empty container is enough. |
| **Google Analytics Measurement ID** | You already use GA4, or want visitor statistics | One step instead of two, so some writers prefer it. **[Other authors' reports]** |
| **Google Site Verification field (HTML tag)** | Your settings show this field | The simplest when it exists, but many accounts don't have it. Custom-domain users report seeing it more often. **[Other authors' reports]** |
| **DNS** | You use a custom domain | Register a Domain property and add a TXT record at your domain provider. |

Only one method needs to succeed. The Tag Manager, Analytics, and Site Verification fields are not separate registrations. They are just ways to prove ownership to the one Search Console property.

**Which comes first, GTM or GA4?** Opinions differ. A writer who recommends GA4 says GTM is a two-step job of making an empty box and then filling a tag inside it, so GA4 is simpler. On the other hand, if your only purpose is Search Console verification, an empty GTM container is enough, and I verified and even submitted a sitemap successfully with an empty container with no tags created. **[Author-tested]** If you already use GA4, use Method B; if not, Method A is a safe choice.

**Where reports conflict.** Early-2026 posts say Search Console can't be used on a `substack.com` subdomain at all and recommend a custom domain with DNS verification, and one commenter says Substack support told them only DNS verification is supported. Later 2026 guides report success on subdomains with Google Analytics or Tag Manager, and Substack's own help documents fields for both. A few writers say Google didn't recognize their Tag Manager ID, or that neither method worked for them. **[Other authors' reports]** My advice: start with Tag Manager on your current address. If verification still fails after 24–48 hours and the checks in section 15, try GA4, or the HTML tag field if you have it. Consider a custom domain with DNS only if nothing else works.

Don't enter the same GA4 ID in both the GA field and the GTM field, because it may double-count visitors. If your GA4 tag lives inside your GTM container, verify with the Tag Manager method rather than the Analytics method. **[Other authors' reports]**

### 7. Method A: Tag Manager, in detail

Do this after you've added your URL prefix property in Search Console (section 5), and keep that verification window open in another tab. Search Console comes first; Tag Manager is only the tool that proves ownership to it.

GTM works by creating an empty box called a "container" and telling Substack that box's number (an ID starting with `GTM-`). You don't need to create tags inside the box. To use a building analogy, you're just telling Search Console the number of a mailbox that has nothing in it yet.

1. Log in to `tagmanager.google.com` with the Google account you'll also use for Search Console. If you have several Google accounts, check which one you're logged in with by looking at the round profile icon at the top right.
2. If it's a first-time account, a welcome screen shows a "Create Account" button. If you already have an account, click the create-account button at the top right.
3. In the settings window, enter an "Account Name" (any name is fine, for example your Substack name) and choose your country.
4. In the "Container setup" area, enter an easy-to-recognize "Container name," such as your Substack address. Under "Target platform," choose **Web**.
5. Click "Create," then review and accept the terms of service.
6. A window called "Install Tag Manager" appears with two long blocks of code. You don't need to paste this code. Close the window. (Substack takes only the ID and plants the code for you. Google's check looks for that snippet on your homepage, so it only passes after you save the ID in Substack in step 10.)
7. In the workspace, at the top, in the tab row (Workspace, Versions, Admin), on the right, next to "Workspace Changes," you'll see an ID starting with `GTM-` in blue text (for example, `GTM-AB12CDE`). Copy only this short ID, without spaces.
8. The first screen shows cards such as "Measure purchases in Google Ads," "Create a new tag," and "Safely test tags," plus blue notice banners. Ignore them all. The empty state showing "Pending changes 0 / No changes" is normal.
9. Click the blue Submit button at the top right to publish the container once. Google requires Publish or Admin permission on the container, which you have if you created it. **[Google docs]** Google's page doesn't say a published version must exist, but another guide lists a published container as a common requirement, and it costs almost nothing, so do it. **[Other authors' reports]**
10. In Substack, go to Dashboard → Settings, scroll to the Analytics section, paste the ID into the "Google Tag Manager ID" field, and save. Don't include spaces before or after. Wait at least 3–5 minutes. Reports range from 30 minutes to 24–48 hours, and some writers note a lag between Substack and Search Console. One author saw a failure notice, came back 30 minutes later, and found verification had passed on its own. **[Other authors' reports]**

Substack describes Tag Manager as best suited to publishers who already use several tracking tools. **[Substack docs]** For ownership verification alone, an empty container is enough.

**Optional: send GA4 visitor data through your container.** Skip this if you only want Search Console. If you also want GA4 statistics and prefer to route them through Tag Manager, do the following inside the same container:

1. Create your GA4 property and copy the `G-` Measurement ID first (section 8, steps 1–5).
2. In Tag Manager, open your Workspace and click **New Tag**. Name it something recognizable, such as `GA4 - yourname`.
3. Click **Tag Configuration** and choose the Google Analytics tag type. Depending on your screen it may be labeled "Google tag" or "Google Analytics: GA4 Configuration."
4. Paste your `G-` Measurement ID.
5. Click **Triggering** and choose **All Pages**.
6. Save, then click **Submit** and publish again.
7. Leave Substack's "Google Analytics Measurement ID" field empty. The same ID in both Substack fields may double-count visitors (section 6).

This tag has nothing to do with verification; the empty container already did that job. **[Other authors' reports]**

### 8. Method B: Google Analytics (GA4), in detail

Add your URL prefix property in Search Console first (section 5). You can do that right away and come back to verify after the 24-hour wait below.

The GA4 method gets you verification and visitor statistics at once. When GA4 is connected, Substack sends page views, free signups, and paid subscriptions as events, and they begin to show up after about 24 hours, so you can see which posts produced subscriptions (Reports → Engagement → Events). **[Substack docs]**

1. Log in to `analytics.google.com` with the Google account you'll use for Search Console and create a new property. Be sure to create it as GA4. Old IDs starting with `UA-` can't be used. **[Substack docs]**
2. When asked about business objectives, choose "Other business objectives." Google's help says to use this item if you have no special objective, and it gives the widest default set of reports. Older posts mention "Get baseline reports," which may be an old screen's name, so just pick what's on your screen. Either way, the data collected doesn't change; only the default reports shown differ.
3. When asked for a platform, choose **Web**. If you click skip, you end up without an ID to paste.
4. On the data stream screen, enter your Substack address as the website URL and any name as the stream name. Leave "Enhanced measurement" on.
5. Once the stream is created, a long number appears in the list. This is the stream ID, not the value you need. Click the stream row to open the detail screen, where the **Measurement ID starting with `G-`** is at the top right. Copy it. Even if the setup window recommends installing code, close it all.
6. Paste the `G-` ID into Substack Dashboard → Settings → Analytics → "Google Analytics Measurement ID" and save. Leave the GTM field empty.
7. *(Optional check.)* Confirm the tag is actually on your page. While logged out (or in a private window), open your Substack homepage and press Ctrl+U on Windows or Command+Option+U on Mac to open the page source (the raw code behind the page). Use the browser's search (Ctrl+F or Command+F) to look for your `G-` ID. If you find it near the word `gtag.js` inside the `<head>` section (the hidden top part of the page code), it's working. You can skip this check if you'd rather just wait and verify. Another way to check: in GA4, open the detail screen of your data stream and click **Test**, if your screen shows that button. **[Other authors' reports]**
8. Wait about 24 hours before verifying in Search Console (some writers advise up to 48 hours if nothing shows up). Verifying right away tends to fail, and the failure looks like a setup error, so many people give up at the last step. **[Other authors' reports]**

Google's guidance says the GA4 method requires the tracking code on the homepage as seen while logged out, and the Google account you use for Search Console must have edit permission on that GA4 property. If you created the property yourself, you already have it. This verification only confirms ownership; it isn't for viewing Analytics data. GA4 verification is not guaranteed to work on every account, so if you get stuck, try another method.

### 9. Methods C and D (only if they apply to you)

**HTML tag.** If your Substack Analytics section has a Google Site Verification field, this is the simplest. After adding a URL prefix property in Search Console, open "Other verification methods" → "HTML tag," and a line of this form appears:

```
<meta name="google-site-verification" content="..." />
```

Copy this entire line, paste the whole tag into the Substack field, save, and click Verify in Search Console. One commenter quotes Substack's own field text as advising a URL prefix property and the HTML tag method. **[Other authors' reports]** This field varies by account. Substack's current Analytics help page doesn't list it, many writers say it isn't visible, and several report success after connecting a custom domain. Some comments describe the opposite experience, so it isn't uniform. If the field isn't there, use Tag Manager or GA4.

**DNS (custom domain).** If you use your own domain connected to Substack, register it in Search Console as a "Domain" property and add the TXT record Google gives you to the DNS settings of the company where you bought the domain (GoDaddy, Namecheap, Cloudflare, Squarespace Domains, and so on). If you use Cloudflare, the record pointing to Substack must be "DNS only" (gray cloud, proxy off), so you can't inject a meta tag there, but a TXT record works fine. **[Other authors' reports]** This method touches only DNS, so it doesn't conflict with Substack features. A domain property covers subdomains, `www` and non-`www`, and `http`/`https` variants all at once. When you later submit your feed on a Domain property, type the full address (for example, `https://www.yourdomain.com/feed`).

**Connecting a custom domain (reference, if you haven't yet).** Substack shows the exact values on screen, so treat this as a map of the order of work. **[Other authors' reports]**

1. Buy the domain from a registrar (GoDaddy, Namecheap, Cloudflare, Squarespace Domains, and so on).
2. In Substack, open Settings and find the custom domain option. Pay the one-time fee and enter your domain with `www` at the front.
3. Substack shows a DNS record to add. Add it (a CNAME record) in your registrar's DNS settings.
4. Wait. Setup can take up to about 36 hours. In Substack's domain settings, use the **Check status** button to see progress. If it stalls, check that the domain you entered begins with `www`.
5. Once it is live, add a new URL prefix property in Search Console for your new address (with `https://`, in the exact `www` or non-`www` form people visit). A property for your old `substack.com` address doesn't cover the new one. Verify it, then submit `feed` again. You can keep the old property if you want to see its history.

**Summary for custom-domain users:** pick whichever is easiest from the HTML tag (if you see the field), DNS, Tag Manager, or GA4. Whichever you use, register your own domain address, the one people actually visit, not the Substack subdomain.

### 10. Verify, then keep the ID

This step is the same whichever method you used. Check that the ID shown in the Search Console window matches the one in Substack, then click **Verify**. You'll see "Ownership verified" with a "Go to property" button on success. On failure, an error window gives the reason; go to section 15.

- **Which item to expand:** for Tag Manager, expand Google Tag Manager; for GA4, expand Google Analytics; for the HTML tag, expand HTML tag.
- **Automatic verification:** if the ID is already saved in Substack under the same Google account, Search Console may verify automatically the moment you enter the address and show a completion notice. If so, skip this step. Some writers report auto-verification fails; that is fine, just verify manually. **[Other authors' reports]**
- **Google's requirements for Tag Manager:** the same Google account in Search Console and Tag Manager, Publish or Admin permission on the container, and the Tag Manager code on the homepage. If you made the container yourself, the first two are no problem, and Substack plants the code once it receives the ID. **[Google docs]** Typical error messages are "insufficient permissions," "wrong tag" (you are logged in with a different account), and "no container" (you created none in this account). Several guides also say the container must have been published at least once, which is why section 7 asks you to click Submit. **[Other authors' reports]**
- **Keep the ID in Substack.** Google re-checks periodically, so deleting it may undo the verification.
- **A backup method:** Google recommends keeping more than one verification method in case one is cut off. You can see and add methods under Search Console → Settings → Ownership verification. If you can, also enter whichever of GTM and GA4 you weren't using into Substack, but still don't create the same GA4 tag inside the GTM container. If you're unsure, using just one is safer. **[Google docs]**

### 11. Feed and sitemap: what each does

**The feed is your main route.** It is a list of your most recent posts, and Substack provides one for every publication. Google accepts RSS 2.0 and Atom 1.0 feeds as sitemaps, and notes that a feed only provides information on recent URLs. **[Google docs]** `/feed` is the standard address; some writers also report success with `/feed.xml`, so try that if `/feed` fails. **[Other authors' reports]**

A normal feed opens as a plain text screen. It may start with the notice "This XML file does not appear to have any style information," followed by `<rss version="2.0">`. Each post is an `<item>` like this:

```
<item>
  <title>Post title</title>
  <description>Post subtitle</description>
  <link>seoulinside.substack.com/p/post-slug</link>
  <pubDate>Thu, 12 Nov 2026 10:45:41 GMT</pubDate>
  <content:encoded>The full text of the post, as HTML</content:encoded>
</item>
```

(`https://` is omitted from the link above for display only.)

In my publication the feed held 21 posts, with title, subtitle, and full text, and Search Console showed 21 discovered pages for it. **[Author-tested]** Other publications may differ, but expect about 20. When the feed has more posts than that, the oldest drop out.

**A sitemap is an optional extra.** It is a list of post addresses (no text). Some publications have `sitemap.xml` and some don't, and Substack hasn't published the conditions. **[Other authors' reports]** Older reports say it appeared after about five posts, newer reports say Substack no longer gives new publications one and that they must grow to qualify, and some people say theirs appeared days later or never appeared even after three months. Some service descriptions still say Substack automatically maintains a sitemap for every publication, so the information conflicts. Mine exists, and Search Console showed 337 discovered pages for it. **[Author-tested]** Mine is the exception, so don't use my numbers as your expectation.

**Which one do you need?** Google has long advised using both a sitemap (for coverage) and a feed (for freshness) when you have both. **[Google docs, as summarized by other SEO writers]**

1. **About 20 posts or fewer:** the feed already contains all of them. A sitemap adds little, so you don't need one.
2. **More than 20 posts, and `sitemap.xml` opens:** submit it too. It lists older posts that have dropped out of the feed.
3. **More than 20 posts, and no sitemap:** rely on links between your posts and on requesting indexing for important older posts (see section 12). Open `/sitemap.xml` again from time to time in case it appears.

**Don't confuse two pages.** The page `yourname.substack.com/sitemap` is a human-readable list of posts by year, and it is not what you submit. The file you submit is `/sitemap.xml`. Neither feed nor sitemap guarantees indexing. Google calls submitting a sitemap a hint, and says a sitemap does not guarantee indexing or raise your ranking. **[Google docs]**

**How to submit.** You need Owner permission on the property. **[Google docs]** In the left menu of Search Console, find the "Indexing" group and click Sitemaps. At the top, the "Add a new sitemap" area already shows your Substack address, followed by an empty field and a "Submit" button. Type only the word below, then submit. Submit the feed first, then the sitemap.

- **Feed:** type `feed`. The address actually submitted is `https://yourname.substack.com/feed`, and the type shown afterward is **RSS**.
- **Sitemap:** type `sitemap.xml`. The address actually submitted is `https://yourname.substack.com/sitemap.xml`, and the type shown afterward is **Sitemap**.

*Exception:* if you registered a Domain property (custom domain with DNS verification), the front part may not be filled in. In that case, type the full address, for example `https://www.yourdomain.com/feed`.

After you submit, a line appears in the "Submitted sitemaps" list lower on the same screen. The columns are Sitemap (address), Type, Submitted date, Last read date, Status, Discovered pages, and Discovered videos. The Status column shows Success, Couldn't fetch, or Has errors. In my publication I submitted both, and both rows showed Success, with 337 discovered pages for the sitemap and 21 for the feed. **[Author-tested]** If you submitted an address that doesn't exist, delete it and keep only the ones that exist.

- **"Couldn't fetch" right after submitting** is common and often temporary. Check that the address opens in your browser, then look again after a few hours to two days. Reports also say this message can appear even when a file is valid and public, so don't assume your setup is wrong. **[Other authors' reports; discussed by Google staff as reported by Search Engine Journal]**
- **Test the address the way Google does.** Google's Sitemaps help suggests running a live URL inspection on the address and checking that "Page fetch" says Successful. **[Google docs]**
- **If a sitemap row keeps failing or says "Sitemap is HTML,"** delete that row and keep the feed. "Sitemap is HTML" means the address responds as an ordinary web page instead of XML, so open it in your browser and check for a typo. A missing sitemap is not your mistake. One user reported that deleting a failing `sitemap.xml` and keeping only the feed got it processed. **[Other authors' reports]**
- **"Discovered pages"** is the number of addresses Google found in the list, not the number of posts indexed.
- **Resubmitting** the same address over and over isn't known to speed anything up. One author advises against it. **[Other authors' reports]**

The feed's limit: it can't tell Google about all your older posts, because it contains only recent addresses. That is why the sitemap is worth adding when it's available. For older posts on an account without a sitemap, either wait for Google to discover them by following links, or request them directly (section 12).

### 12. Request indexing for posts

A feed or sitemap is only a hint that "these posts exist." If you tell Google directly about important new posts, they may be discovered faster.

Paste the post's full address (`yourname.substack.com/p/post-slug` with `https://` in front) into the long search bar at the very top of Search Console and press Enter. This bar is the URL Inspection tool, which you can also open from "URL Inspection" in the left menu. After a few seconds of "Checking whether it is indexed," the result appears.

- **"URL is on Google" (green check mark):** it's already indexed, and there's nothing to do.
- **"URL is not on Google":** click **Request indexing** and wait a moment for the notice that the request was received.

Repeat each time you publish a new post. If you have several properties, first check in the top-left dropdown that your Substack property is selected.

- If the inspection says "Discovered – currently not indexed" or "Crawled – currently not indexed," the Request indexing button is still worth using for important posts; see section 14 for what those statuses mean.
- Optional: before requesting, you can click **Test live URL** to confirm Google can reach the page right now.
- Requesting the same URL again doesn't speed anything up. **[Google docs]**
- There is a daily limit on how many times you can click Request indexing. Google doesn't publish the number; trade sites report about 10–12 per day (reports differ on whether it is counted per property or per Google account), and some writers continue the next day after hitting the limit. Simply inspecting a URL, without clicking Request indexing, is not known to use that limit. **[Unofficial]**
- It requires Owner or Full user permission, and only for URLs you manage. **[Google docs]**
- Crawling takes a few days to a few weeks, and indexing isn't guaranteed. Google's FAQ says the most common reason a site isn't indexed is simply that it's too new. **[Google docs]**

**For older posts that aren't in your feed,** pick the important ones and request them over several days, a few per day, so you stay under the daily limit. Also link to older posts from newer ones, and from outside places such as social media bios, your own website, and other writers' posts. Substack's own SEO guide calls inbound links the best way to improve your search ranking. **[Substack docs]**

### 13. Make found posts look good

Registration makes Google find your posts. From here on, the job is to make found posts look good in search results.

In the post editor, open Settings (the gear icon, bottom right). The SEO options are near the bottom of that panel. They let you edit the SEO title, SEO description, post URL, and social preview image. By default Substack fills them in from your post title and content, and they affect only how search engines display your post, not how it looks in email or on your site. **[Substack docs]** I found no per-post option to hide a single post from search in Substack's guide.

- **SEO title:** the blue headline in search results. Keep it brief, because long titles may be cut with an ellipsis, lose words, or be rewritten. Substack recommends under 60 characters. Make it unique, avoid stuffing keywords, and consider putting your name or brand at the end. **[Substack docs]** Many writers also put the main keyword near the front. **[Other authors' reports]**
- **SEO description:** the small text under the title. It is filled in automatically by default (writers report it usually draws on the post subtitle). Don't repeat the title, and add new context that makes people want to click. **[Substack docs]** About 150–160 characters is a common rule of thumb, but Substack and Google don't give an official figure. Google doesn't always use your description as is, and it isn't a direct ranking factor, only text that invites clicks.
- **Post address (slug):** short, readable words joined with hyphens. Edit it before you publish, because changing it afterward breaks existing links. **[Substack docs]** Writers suggest about 3–5 lowercase words with the main keyword first, and no random strings or numbers. **[Other authors' reports]**
- **Subtitle:** Google can read it, and it often becomes the default description. Write a clear sentence about what the post covers instead of leaving a generic line. **[Other authors' reports]**
- **Social preview image:** Substack says posts with a preview image get about twice the signups and 40% more clicks than posts without one. The default is the first image in the post. **[Substack docs]**
- **Publication introduction** (Settings → Publication details): it serves as a clue for Google about your publication's topic. Include the key words about what the publication is about, ideally words people would actually type into a search bar. One author reports an indexing problem was resolved after filling an empty introduction. **[Other authors' reports]**
- **Paid posts:** Settings → Publication details has an option called "Allow Search Engines to Index Paywalled Content." When it is on, the full text of paywalled posts can match searches, non-subscribers may see an excerpt in the results, and they hit the paywall when they open the post. **[Other authors' reports, quoting the setting's text]** The setting's location and default may change, so open it and look. It is separate from the setting that controls AI crawler access. Keep the posts you most want found through search free and public.

**In the body:**

- Build the post's skeleton with subheadings (H2, H3). Both search engines and AI use the heading hierarchy as a clue.
- Write alt text for images. Don't force keywords in; describe what the picture is.
- Check that the links you've placed actually open.
- Naturally link to your other posts. Links are how Google understands how posts relate and finds even older posts.
- Write steps or options as numbered or bulleted lists.
- Title posts with words people would actually search for, not issue numbers like "Issue 42."

### 14. Check results

**Performance report.** Open Performance → Search results in the left menu. At the top, total clicks, total impressions, average click-through rate (CTR), and average position appear as cards, with a graph over time below. The tabs under the graph (Queries, Pages, Countries, Devices) let you slice the data, and the Queries tab shows the exact phrases people typed into Google. Data takes a few days to build, so check after the first 2–4 weeks. Start early, because it is unclear how much earlier data a newly verified property shows, so don't count on a backfill. **[Other authors' reports]**

How to use it: for average position, positions 1–10 are page 1 and 11–20 are page 2. A post at about position 8–15 is in the "just missed" range, and polishing its title and description may lift it to the top of page 1. If you discover you're showing up for queries you didn't intend, that can become your next post topic.

**Pages report.** Indexing → Pages lists the number of indexed and non-indexed posts and the reasons posts aren't indexed. Reasons commonly seen by Substack users:

- *Excluded by 'noindex' tag:* expected for a Private or empty publication, and for comment and admin pages. If your post is public, recheck section 4 and the paid-post setting.
- *Blocked by robots.txt:* normal for subscribe (`/subscribe`), comment, and embed pages. Don't worry if such addresses show in the excluded list.
- *Discovered – currently not indexed:* Google knows the address but hasn't visited yet or postponed the visit. More links to the post from other posts or from outside help, and for your most important posts, request indexing one by one.
- *Crawled – currently not indexed:* Google visited and chose not to list it. Check length, originality, and heading structure. A commenter reports this status can clear after a few days as you keep publishing. **[Other authors' reports]**

**In Substack.** Settings → Stats → Traffic shows your traffic sources, including Google, and lets you download the data as a CSV file. **[Other authors' reports]** If you connected GA4, you can also check signup events in GA4's reports (Reports → Engagement → Events).

### 15. Troubleshooting

**Most common causes of failed verification, in order:**

1. You used different Google accounts in Search Console and Tag Manager (or Analytics).
2. You chose a **Domain** property instead of **URL prefix** (unless you are verifying with DNS).
3. You didn't wait long enough. Try again after a few hours, and up to 24–48 hours.

**Then check:**

- The ID has no typos or spaces. For GA4, you entered the `G-` Measurement ID, not the stream ID.
- There is at least one public post, only a "Coming soon" page isn't left, and the publication isn't Private. With no posts, verification can fail; publish a post, wait a few hours to a day, and try again. **[Other authors' reports]**
- If you're stuck, publish the Tag Manager container once (Submit, then Publish) and try again. This isn't confirmed as a required condition, but it's worth trying.
- The error "Could not find the Google Tag Manager container ID on the homepage" often means Substack hasn't finished applying the change.
- Tag Manager still isn't recognized after 24–48 hours? Try GA4 (wait 24 hours before verifying) or the HTML tag field if you have it. If neither works, contact Substack support.
- No verification field at all? Use whichever of the GTM or GA fields you see. If you see neither, contact Substack support or connect a custom domain and use DNS.

**Other questions:**

- **I typed my sitemap address and it says "This publication does not have a sitemap."** That is normal. Some publications have a sitemap right away and others don't, and Substack hasn't published the conditions. Your feed is the part that matters: open `yourname.substack.com/feed`, and if it shows your recent posts, submit `feed` in Search Console. With only a few posts, the feed alone is enough, because it carries the title, subtitle, and content of your most recent posts (about 21), while a sitemap is just a list of links to all posts. As your archive grows, check `/sitemap.xml` again from time to time.
- **`sitemap.xml` won't open, or the sitemap row shows "Couldn't fetch."** It may be normal. Keep the feed row and delete the sitemap row (section 11). If that doesn't help, concentrate on individual indexing requests.
- **Will my posts show up on Google even without a sitemap?** In some cases, yes. One user reported that posts began appearing through a combination of submitting the feed, connecting GTM, and links from external websites to Substack posts. Links placed from outside help a lot. One author advises that your homepage and About page may not appear in search if no other page links to them, so try putting a link to your home inside a post that already appears. **[Other authors' reports]**
- **Requested indexing but still not searchable after several days?** Normal. Crawling can take from a few days to a few weeks, and whether to index is Google's decision. Check the reason in the Pages report, and place links from other posts or social media. Repeatedly requesting the same URL doesn't help.
- **Many posts suddenly became "Discovered – currently not indexed," or rankings dropped?** Google updates its algorithm periodically, and rankings fluctuate greatly at those times. It may not be your fault. Some writers also blame a Substack-side technical problem, but the cause hasn't been confirmed, so I don't treat it as fact. Watch the trend for a few weeks and request indexing for your most important posts.
- **Is the default substack.com address a disadvantage?** Opinions differ. Substack's guide says the default address borrows Substack's established search reputation. **[Substack docs]** Some writers report better exposure after switching to a custom domain, and a custom domain is also said to make Search Console connection and indexing requests easier. **[Other authors' reports]** It's hard to say definitively, so first do registration and post optimization on your current address, and check the current custom-domain terms before deciding.

### 16. Realistic expectations and extras

- SEO doesn't show results immediately. Think in units of weeks to months, not days.
- Google may be only a small share of your readers (around 5% in some reports), and social media and Substack's internal recommendation traffic can be larger. Alongside SEO, publish consistently and be active on social media.
- GA4 is a tool for seeing visitor behavior, and Search Console is a tool for seeing exposure in search. Their purposes differ, so don't confuse them.

**Bing (Microsoft search).** Bing Webmaster Tools can import verified sites and sitemaps from Search Console (per Bing's official guidance). On Substack, file upload and DNS verification are difficult, so after finishing Search Console verification, importing is the most realistic route. Bing periodically syncs with your Search Console account to verify ownership, so if you revoke the access you granted to Bing, you'll have to import again or verify another way. Some Substack authors have introduced this method. IndexNow, Bing's instant indexing notification feature, requires uploading a key file to your site, and I couldn't find a confirmed case of whether this is possible on Substack.

### 17. Seven easy-to-miss mistakes

1. You logged in to Search Console and Tag Manager (or Analytics) with different Google accounts.
2. You chose "Domain" as the property type. (It should be URL prefix, unless you are a custom-domain user verifying with DNS.)
3. You entered the GA4 stream ID (the long number) instead of the `G-` Measurement ID.
4. You entered the same GA4 ID in both the GA field and the GTM field.
5. You deleted the ID from Substack after verification was done.
6. You gave up after a few minutes without waiting for it to take effect. Try waiting about 24 hours.
7. You're hunting for an indexing problem when there are no public posts or the publication is Private.

### 18. Checklist at a glance

- ☐ At least one public post (not just the "Coming soon" placeholder), and the publication isn't Private
- ☐ Current status checked with `site:yourname.substack.com` (your own domain if custom)
- ☐ `/feed` opens, and whether `/sitemap.xml` opens is checked (including the four links at the bottom of the homepage: About, Archive, Recommendations, Sitemap)
- ☐ Fields on the Substack Settings → Analytics screen checked
- ☐ (Method A) Tag Manager web container created, `GTM-` ID copied, container published, ID pasted into Substack and saved
- ☐ (Method B) GA4 web stream created, `G-` Measurement ID pasted into Substack and saved, about 24 hours waited
- ☐ Search Console property added as URL prefix (or Domain if verifying with DNS), with the same Google account
- ☐ Method chosen under "Other verification methods," and ownership verified
- ☐ Verification ID kept in Substack; if possible, a second method added
- ☐ Feed submitted under Indexing → Sitemaps, status Success (add `sitemap.xml` only if it opens; if it fails, delete that row and keep the feed)
- ☐ (Custom domain only) New URL prefix property added for the new address and the feed submitted again
- ☐ Indexing requested for each new post, once per URL
- ☐ Publication introduction and paid-post setting checked
- ☐ SEO title, description, post address, and alt text checked
- ☐ (Optional) Site imported from Search Console into Bing Webmaster Tools
- ☐ After 2–4 weeks, Performance and Pages reports reviewed

### Sources and further reading

Links were accessed at the time of writing (November 2026). Authors' posts may have different screen layouts depending on when they were written, so read them alongside the official documentation.

**Google official documentation**

- Verify your site ownership (requirements by method, the DNS-only condition for domain properties, recommendation to keep multiple methods): https://support.google.com/webmasters/answer/9008080
- Build and submit a sitemap (RSS 2.0 and Atom 1.0 feeds can be submitted; feeds focus on recent URLs): https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Sitemaps report (Owner permission, live test, report types): https://support.google.com/webmasters/answer/7451001
- Ask Google to recrawl your URLs (quota, repeated requests are ineffective, time required): https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- Google Search crawling and indexing FAQ: https://developers.google.com/search/help/crawling-index-faq
- URL Inspection tool help: https://support.google.com/webmasters/answer/9012289
- GA4 business objective settings (choices when creating a property): https://support.google.com/analytics/answer/16109068

**Substack official materials**

- A guide to SEO on Substack (SEO title, description, URL settings): https://on.substack.com/p/substack-seo-guide
- The state of SEO on Substack (Substack's crawling improvements): https://on.substack.com/p/the-state-of-seo-on-substack-feb-23
- How do I use the Analytics section on Substack?: https://support.substack.com/hc/en-us/articles/52667879688980-How-do-I-use-the-Analytics-section-on-Substack
- Using Advertising Analytics on Substack (GA connection, signup and subscription events, takes effect after 24 hours): https://faq.substack.com/p/using-advertising-analytics-on-substack
- Private publication settings (when private, only the welcome page may be indexed): https://support.substack.com/hc/en-us/articles/360044389731-Can-I-make-a-private-Substack-publication
- Adding a custom domain: https://on.substack.com/p/new-add-a-custom-domain-to-your-substack

**Addresses you can check directly on Substack publications (examples)**

- robots.txt examples (SITEMAP lines at the bottom): https://outbreaknewstoday.substack.com/robots.txt , https://theweekinpolls.substack.com/robots.txt
- Human-readable sitemap page example (post list by year): https://oldoldoldoldnew.substack.com/sitemap

**Reports from Substack authors (real success and failure cases)**

- Aman Parmar, GA4 verification tutorial (waiting 24 hours, distinguishing Measurement ID from stream ID): https://shipwithailab.substack.com/p/google-search-console-cant-verify
- Paul Arino, GTM verification and feed submission: https://howtotipstricks.substack.com/p/substack-google-search-console
- Paul Arino, the problem of Search Console failing to fetch the Substack sitemap: https://howtotipstricks.substack.com/p/substack-sitemap-not-fetched-google
- Content Clarity, connecting to Search Console via GTM, sitemap presence and the feed alternative (many cases in the comments): https://contentclarity.substack.com/p/connect-your-substack-to-google-search-console
- Harshini, the problem of new publications having no sitemap and the feed solution, changes in the bottom link area: https://harshiniwrites.substack.com/p/substack-stopped-giving-this-feature
- Boodsy, the "Get your Substack on Google" series (noindex on the Coming soon page, keeping the verification ID): https://boodsy.substack.com/p/get-your-substack-on-google-search-console
- Mara Martins, three kinds of indexing problems and a case of strengthening the publication introduction: https://maramartins.substack.com/p/why-your-pages-arent-indexed-in-google
- Lisa Brown, discussion of connecting subdomains and custom domains to Search Console: https://bunlimited.substack.com/p/your-substack-disappeared-from-google
- Erica Drayton, Tag Manager verification and the need for posts: https://ericadrayton.substack.com/p/set-up-google-analytics-on-substack
- Colin Gardiner, comprehensive Substack SEO guide: https://www.gardinercolin.com/p/substack-seo
- Analytics Mania, why Search Console verification with Tag Manager fails (permissions, same account, snippet placement): https://www.analyticsmania.com/post/solved-cannot-verify-google-search-console-with-google-tag-manager/
- Sprout Social, Substack SEO guide (setting to allow paid-post indexing, custom domain and Search Console): https://sproutsocial.com/insights/substack-seo/

**Search Console behavior and quotas**

- Google staff on "Couldn't fetch" sitemap errors (Search Engine Journal): https://www.searchenginejournal.com/google-explains-couldnt-fetch-sitemap-errors/
- Request-indexing quota reports (Search Engine Land): https://searchengineland.com/google-search-console-url-inspection-tool-seo-use-cases-457462

**Bing**

- Bing Webmaster Tools, importing sites from Search Console: https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools

Reddit r/Substack threads about Substack and SEO strategy are useful for reference, but they are anecdotal experiences.
