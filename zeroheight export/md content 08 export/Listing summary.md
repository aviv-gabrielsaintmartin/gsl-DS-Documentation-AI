# Listing summary · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

EXPERIENCES

# Listing summary

Ready

Listing summaries are concise versions of listings featured on any AVIV Group website. Designed for high flexibility, they adapt to a wide range of use cases. While they provide an overview of the listings, they may not always include actionable elements.

**Web:** Non-gemini component │ **iOS:** Ready ✅ │ **Android:** Ready ✅

![](/uploads/Iz67boRjTJzqScSvPj-H6g.png)

-   [
    
    Listing summary in Figma
    
    
    
    
    
    ](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Experiences?m=auto&node-id=2115-63352&t=Wjql7VOThGReKVmi-1 "https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Experiences?m=auto&node-id=2115-63352&t=Wjql7VOThGReKVmi-1")
-   [
    
    Listing summary in Storybook (non-Gemini)
    
    
    
    
    
    ](https://bff.balanced-werewolf-dev.aws.aviv.eu/storybook/app/index.html?path=/story/ui-ui-classified-info--default "https://bff.balanced-werewolf-dev.aws.aviv.eu/storybook/app/index.html?path=/story/ui-ui-classified-info--default")

## Usage

Listing summaries are concise versions of listings featured on any AVIV Group website. They are versatile and can be tailored to include as much or as little information as needed, ranging from a couple of details to a fuller overview.

The Listing summary component can function as a standalone short version of a listing, as part of larger patterns, or as an individual entity. It can be made interactive and can include various actions or additional components alongside it.

  

---

  

## Anatomy

While Listing Summaries provide a high degree of flexibility, enabling designers to customize and organize them according to specific needs, they come with a default set of elements.

![](/uploads/Gfc912zUuMwTYZGnGOI1Yg.png)

**Sub-component**

**Enable/Disable capability**

**Quantity**

**Sizes**

**Other**

Thumbnail

Yes

N/A

Width: 64, 72, 84, 96, 104, 112, 128, 256

-   Aspect ratio: 1:1, 4:3, 3:2
    
-   Alignment: Left, Top
    

Tags

Yes

1,2,3

N/A

  

Price tag

Yes

N/A

-   Headline 24 / €m2 14 (default)
    
-   Headline 20 / €m2 12
    

  

Title

Yes

N/A

16 (default), 14, Headline 24

  

Feature list

Yes

3, 4

12 (default), 14, 16

Icons enabled/disabled

-   12 Size (16px icon)
    
-   14 Size (16px icon)
    
-   16 Size (20px icon)
    

Location

Yes

N/A

12 (default), 14, 16

  

Helper text

Yes

N/A

12 (default), 14, 16

  

Action

Yes

1,2

Button size 40

  

---

  

## Variants

Listing Summaries come with two default variants that change the position of the thumbnail. However, using the Listing Summary component, you can create an infinite number of custom variants.

![Listing summary (Thumbnail on the left)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e18e9d1fa3f17249aa61da?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b884ad0bfe913b8d79043b646e1b22c353b17b516b240c61b8629ec230f63688)

Listing summary (Thumbnail on the left)

Add notes

![Listing summary (Thumbnail on top)](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9ac648216d31501e4549c0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=17c9c17136f685c3da4f4309db899dcfd99700dd4d1b139c24fc2feec293d582)

Listing summary (Thumbnail on top)

Add notes

---

  

## Guidelines

![](/uploads/evET_lMfcZpaoAvWXbzO6g.png)

Do

Add more elements next to the Listing Summary to make it part of a bigger pattern if needed

![](/uploads/kus2D5Kc0kSUiFP6QWg9cQ.png)

Do

Listing Summaries can be part of larger layouts like tables

![](/uploads/XWS1_FYIbaIEz8Qyh3sHMw.png)

Do

Listing Summaries can also trigger an action, like going to the detail page of a listing

![](/uploads/ZAAlFIlgGsQ7MKocqCQgeQ.png)

Do

Listing Summaries can be placed inside a Card component or any other container for your convenience

![](/uploads/YMMw6xvpC9emgqcEDUSdrg.png)

Don’t

Don't use the Listing Summary to mimic the layout and functions of the Listing Card. You can use the Listing Card component for that