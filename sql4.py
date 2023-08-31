SELECT City, COUNT(*) as NumSalespeople
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City;
