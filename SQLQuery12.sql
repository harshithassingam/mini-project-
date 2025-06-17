SELECT * FROM InCD.dbo.insurancedataclaims;

-- claim approval rate --

/* Claim approval rate is the percentage of claims that are approved. Higher claim approval rate signifies accuracy,
   efficiency, good internal processes, and probably higher customer satisfaction. 
   
   It can be calculated by dividing the total number of approved claims with total claims(approved+rejected)
   and calculating its percentage by multiplying it with 100.

   We use CAST function to convert INT into float. If we don't convert INT into FLOAT, it will perform integer division 
   and if the total number of approved claims to closer to total_claims, we get the output as 0,

   We are writing a subsquery because we do not have an approved claims column in our table and we have to calculate it.
   
   */
SELECT 
    approved_claims,
    total_claims,
    CAST(approved_claims AS FLOAT) / total_claims * 100 AS claim_approval_rate
FROM
    (SELECT COUNT(*) AS approved_claims
     FROM InCD.dbo.insurancedataclaims
     WHERE claim_status = 0) AS approved,

    (SELECT COUNT(*) AS total_claims
     FROM InCD.dbo.insurancedataclaims) AS total;


-- claim rejection rate -- 

/* Claim rejected rate is the percentage of claims that are rejected. 
  
  It can be calculated by dividing the total number of rejected claims with total claims and calculating its 
  percentage.

  We use CAST function to convert INT into float. If we don't convert int into float, it will perform integer division 
  and we get the output as 0, if the total number of rejected claims to closer to total_claims.
  */
SELECT 
    rejected_claims,
    total_claims,
    CAST(rejected_claims AS FLOAT) / total_claims * 100 AS claim_rejection_rate
FROM
    (SELECT COUNT(*) AS rejected_claims
     FROM InCD.dbo.insurancedataclaims
     WHERE claim_status = 1) AS rejected,

    (SELECT COUNT(*) AS total_claims
     FROM InCD.dbo.insurancedataclaims) AS total_claim

-- Fraud detection count -- 

/* Fraud detection count gives us the number of fraud claims. WE use COUNT() function to count the total 
   number of frauds and using WHERE we filter out only the Fraud claims */

SELECT COUNT(*) AS fraud_detection_count
FROM InCD.dbo.insurancedataclaims
WHERE fraud_flag = 'Fraud';

-- AVG Processing Time --

/* Average processing time is the average number of days it takes to make a decision about a claim.
   DATEDIFF is used to calculate the difference between two dates. Day is the unit of time that we want to 
   measure the difference in. */

SELECT AVG(DATEDIFF(day, submision_date, decision_date)) AS avg_processing_days
FROM InCD.dbo.insurancedataclaims;

-- Aggregation of fraud detection and its approval timings

/*  Here, we are aggregating the fraud claims and how long it took to make a decision about it.
    DATEDIFF is used to calculate the difference between two dates. Day is the unit of time that we want to 
    measure the difference in. Using WHERE,we filter out the Fraud claims. GROUP BY groups the columns specified */-- 

SELECT fraud_flag,DATEDIFF(day,  submision_date, decision_date) AS detection_time
FROM InCD.dbo.insurancedataclaims
WHERE fraud_flag = 'Fraud'
GROUP BY fraud_flag,decision_date,submision_date





