# Legend · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

Charts

# Legend

In progress

## Usage

-   Legend is mandatory if you display two data categories or more
    
-   If you display only one data, the legend is not needed. You can use the chart title (e.g. Price evolution in Paris) associated with the labels (e.g. 100k €, 200k €...)
    
      
    

---

  

## Position

We recommend positioning the legend below or on the left of the graph.

We do not recommend placing the legend above the graph. This positioning may divert the user's attention to the graphic, leading them to overlook the legend that is situated between the header and the graphic.

Following our research, no perfect position seems to exist. If you collect data regarding the position during user testing, please share it with us.

---

  

## Interaction

You can filter the data using the legend when interactive.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/36ecce63d419255e8e9adf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7bc7872a7c394b1a207dd69e3e138c8242bb23865c5e36fdf40faae6a7dd876f)

Add notes

To show/hide data sets, some design systems (e.g. [Carbon](https://carbondesignsystem.com/data-visualization/legends/#:~:text=about%20geospatial%20legends.-,Interactions,-Hover%20to%20highlight)) and frameworks (e.g. [HighChart.js](https://www.highcharts.com/demo/highcharts/bar-chart) or [Chart.js](https://www.chartjs.org/docs/latest/samples/bar/horizontal.html)) use the legend as a clickable element, acting like a checkbox.

Usually, there is no clear indication the legend is clickable leading in our opinion to discoverability issues.

We can expect our users to learn how to show/hide data with a product they'll need to reuse recurrently like a dashboard on a B2B product.

On a B2C product, the need to show/hide data sets should occur less often but we can't expect our user to understand the features without any indications, that's why we added a checkbox.