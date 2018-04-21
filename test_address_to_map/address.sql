DECLARE @ADDRESS TABLE (
       PT_FULL_ADDRESS VARCHAR(MAX)
)

INSERT INTO @ADDRESS

SELECT A.FULL_ADDRESS

FROM (
    select a.addr_line1 + ', ' + a.Pt_Addr_City + ', ' + a.Pt_Addr_State + ' ' + a.Pt_Addr_Zip AS [FULL_ADDRESS]

    from smsdss.c_patient_demos_v as a
	left outer join smsdss.BMH_PLM_PtAcct_V as b
    on a.pt_id = b.Pt_No
        and a.from_file_ind = b.from_file_ind

    WHERE a.Pt_Addr_City IS NOT NULL
    AND a.addr_line1 IS NOT NULL
    AND a.Pt_Addr_State IS NOT NULL
    AND a.Pt_Addr_Zip IS NOT NULL
    AND b.Plm_Pt_Acct_Type = 'I'
    AND b.tot_chg_amt > 0
    AND LEFT(B.PTNO_NUM, 1) != '2'
    AND LEFT(B.PTNO_NUM, 4) != '1999'
    AND DATEPART(YEAR, B.DSCH_DATE) = 2018
) A
;

SELECT * FROM @ADDRESS
;