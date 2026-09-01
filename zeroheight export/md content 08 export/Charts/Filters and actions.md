# Filters and actions · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

Charts

# Filters and actions

In progress

You can change the data displayed using filters or/and an interactive legend.

## Filters

### Type

If you use other components as filters and confirm it works with user testing, we kindly ask you to share your findings with us.

![Chip](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/5b800373949d91fa1fb6d5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dd3a9865d7cab1214a19615512f9f039ceb17cb53fa7db1bf3369206eac13537)

Chip

Add notes

Works better with 5 options or less

![Dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e9d984921e565e109fac48?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4f94d65d08a560dc3d16454d679d427a4476c7d7b0f54865a3c590e644882d8c)

Dropdown

Add notes

Use it if you have more than 5 options available

---

  

### Position

Filters should be displayed above the graph. Depending on the space available, they can be next or below the graph title.

If you encounter a use case where the filters position make more sense below and is proving working by user test, please share it with us.

  

![Right](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e1866ab134b4b2e0db8f5b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=906ec397abfa6e2c0ba4142c1db354097a3c745f24aff04ce1319a71c903bd29)

Right

Add notes

![Below](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/8da7320a136489287bd484?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=25748c3a0b1b0de89082703177869120ae2a94837982b17a2762652c6d1756f8)

Below

Add notes

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/6beedc1c11ebc4a322bd5e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132003Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a407c96a974f69afd65eba9501c8bae36a5b4f710d19c4705fda1159b81e6a12)

Do

For mobile devices or in situations with limited screen space, we recommend displaying the filters in a modal bottom sheet. These filters can be accessed by clicking on a designated filter button. Use the close icon on the top left to cancel and the primary button to validate the changes.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/e4b766635f53137d38858e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132003Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=43f3e24a2bc963cfe3d4ae9afd99c59775f353ab2932554c1f78a45b2cd24b08)

Don’t

When space is limited, it’s important not to conceal the filters, as this could diminish their visibility and ease of access.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/c79ae21f48a79c344f9979?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132003Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b346550476759054b4f054d3e960bf5c2a3aabfb45511a0f1b76bec20f6050a5)

Caution

Displaying filters stacked on top of each other on small screens can diminish usability and overwhelm users.

  

  

---

  

## Legend

You can filter the data using the legend when interactive.

![Legend ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/notfoundfile.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c38c29cc40223c5a6484d1fce8fb21c7325a8a8685e5a1b0f3103c619c26f7e2)

Legend

Add notes

To show/hide data sets, some design systems (e.g. [Carbon](https://carbondesignsystem.com/data-visualization/legends/#:~:text=about%20geospatial%20legends.-,Interactions,-Hover%20to%20highlight)) and frameworks (e.g. [HighChart.js](https://www.highcharts.com/demo/highcharts/bar-chart) or [Chart.js](https://www.chartjs.org/docs/latest/samples/bar/horizontal.html)) use the legend as a clickable element, acting like a checkbox.

Usually, there is no clear indication the legend is clickable leading in our opinion to discoverability issues.

We can expect our users to learn how to show/hide data with a product they'll need to reuse recurrently like a dashboard on a B2B product.

On a B2C product, the need to show/hide data sets should occur less often but we can't expect our user to understand the features without any indications, that's why we added a checkbox.

  

  

---

  

  

## Other actions

You can include all the complementary actions you need depending on your use case.

This action menu is mandatory and should at least include the color-blind mode (on the web) and the table format.

[Know more about accessibility](https://zeroheight.com/626199550/p/025089-accessibility)

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/cf7233283abd42aea22eb0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e22a8623c2003901faea3906b6d40a511cb861a4761b66e996d345916135d403)

Add notes