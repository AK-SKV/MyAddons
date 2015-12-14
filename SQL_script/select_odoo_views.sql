SELECT 
  iuv.id, 
  iuv.arch, 
  iuv.name,
*
FROM 
  public.ir_ui_view iuv
where iuv.arch LIKE '%Odoo%'
order by id;
