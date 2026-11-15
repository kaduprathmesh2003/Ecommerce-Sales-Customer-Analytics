# Deployment and final publishing checklist

## Streamlit Community Cloud
The app entry point is `streamlit_app.py`. Dependencies are listed in `requirements.txt`.

1. Sign in to Streamlit Community Cloud using the GitHub account that can access this repository.
2. Choose **Create app**.
3. Select repository `kaduprathmesh2003/Ecommerce-Sales-Customer-Analytics`, branch `main`, and main file `streamlit_app.py`.
4. Deploy and wait for the build to finish.
5. Open the public app URL and test every tab and filter.
6. Add the real deployed URL to the README. Do not add a guessed URL.

## Power BI Desktop deliverable
The repository includes DAX measures, a date-table expression, a theme JSON and a detailed build guide in `powerbi/`. A genuine `.pbix` file is a Power BI Desktop-authored binary report. It cannot be truthfully generated or validated by committing DAX text files alone. Open Power BI Desktop, follow `powerbi/BUILD_DASHBOARD.md`, save as `powerbi/Ecommerce_Sales_Customer_Analytics.pbix`, then upload that file and screenshots.

## Final verification
- Confirm the app builds without errors.
- Test date, category, city and payment filters.
- Check KPI values against the source CSV and Python outputs.
- Confirm the Power BI model relationship and measure formatting.
- Verify the public app URL and repository URL in a signed-out browser.
- Keep the synthetic-data disclaimer visible.
