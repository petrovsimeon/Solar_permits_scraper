from requests import request
import json
import pandas as pd


# Func for making requests using different urls and special payloads
def request_data(url, payload):
	headers = {
		"Accept": "application/json, text/plain, */*",
		"Accept-Language": "en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7,de;q=0.6",
		"Connection": "keep-alive",
		"Content-Type": "application/json;charset=UTF-8",
		"Cookie": "_ga=GA1.2.558750836.1677866625; _gid=GA1.2.1820624808.1677866625; Tyler-Tenant-Culture=en-US",
		"DNT": "1",
		"Origin": "https://energovweb.pickenscountysc.us",
		"Referer": "https://energovweb.pickenscountysc.us/EnerGovProd/SelfService",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"Tyler-Tenant-Culture": "en-US",
		"Tyler-TenantUrl": "Home",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/101.0.4951.64 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/101.0.4951.64",
		"sec-ch-ua": "Chromium';v='110', 'Not A(Brand';v='24', 'Google Chrome';v='110'",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "macOS",
		"tenantId": "1",
		"tenantName": "EnerGovProd"
	}
	proxies = {
		"https": "CUSTOM_PROXY",
	}

	response = request("POST", url, json=payload, headers=headers, proxies=proxies)
	data = json.loads(response.text)

	return data


# List of permit types' ids, needed for the main search
permit_type_ids = [
	"ac078529-b927-4d4f-a2a8-59fcad025114_87f7ac29-a484-40c8-8d58-2b1f76ed6d70",
	"c078529-b927-4d4f-a2a8-59fcad025114_12db34b2-9285-4f72-aed7-2dc1279f9cb8",
	"3f569456-8821-433d-8abe-420327950470_87f7ac29-a484-40c8-8d58-2b1f76ed6d70",
	"3f569456-8821-433d-8abe-420327950470_12db34b2-9285-4f72-aed7-2dc1279f9cb8",
]

# List of end results
end_results = []


# Iterates over the list of permit types
for permit_type_id in permit_type_ids:
	url_main_search = "https://energovweb.pickenscountysc.us/EnerGovProd/SelfService/api/energov/search/search"
	payload_main_search = {
		"Keyword": "",
		"ExactMatch": True,
		"SearchModule": 2,
		"FilterModule": 1,
		"SearchMainAddress": False,
		"PlanCriteria": {
			"PlanNumber": None,
			"PlanTypeId": None,
			"PlanWorkclassId": None,
			"PlanStatusId": None,
			"ProjectName": None,
			"ApplyDateFrom": None,
			"ApplyDateTo": None,
			"ExpireDateFrom": None,
			"ExpireDateTo": None,
			"CompleteDateFrom": None,
			"CompleteDateTo": None,
			"Address": None,
			"Description": None,
			"SearchMainAddress": False,
			"ContactId": None,
			"ParcelNumber": None,
			"TypeId": None,
			"WorkClassIds": None,
			"ExcludeCases": None,
			"EnableDescriptionSearch": False,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"PermitCriteria": {
			"PermitNumber": None,
			"PermitTypeId": permit_type_id,
			"PermitWorkclassId": None,
			"PermitStatusId": "none",
			"ProjectName": None,
			"IssueDateFrom": "2022-12-31T22:00:00.000Z",
			"IssueDateTo": "2023-02-27T22:00:00.000Z",
			"Address": None,
			"Description": None,
			"ExpireDateFrom": None,
			"ExpireDateTo": None,
			"FinalDateFrom": None,
			"FinalDateTo": None,
			"ApplyDateFrom": None,
			"ApplyDateTo": None,
			"SearchMainAddress": False,
			"ContactId": None,
			"TypeId": None,
			"WorkClassIds": None,
			"ParcelNumber": None,
			"ExcludeCases": None,
			"EnableDescriptionSearch": False,
			"PageNumber": 1,
			"PageSize": 10,
			"SortBy": "relevance",
			"SortAscending": False
		},
		"InspectionCriteria": {
			"Keyword": None,
			"ExactMatch": False,
			"Complete": None,
			"InspectionNumber": None,
			"InspectionTypeId": None,
			"InspectionStatusId": None,
			"RequestDateFrom": None,
			"RequestDateTo": None,
			"ScheduleDateFrom": None,
			"ScheduleDateTo": None,
			"Address": None,
			"SearchMainAddress": False,
			"ContactId": None,
			"TypeId": [],
			"WorkClassIds": [],
			"ParcelNumber": None,
			"DisplayCodeInspections": False,
			"ExcludeCases": [],
			"ExcludeFilterModules": [],
			"HiddenInspectionTypeIDs": None,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"CodeCaseCriteria": {
			"CodeCaseNumber": None,
			"CodeCaseTypeId": None,
			"CodeCaseStatusId": None,
			"ProjectName": None,
			"OpenedDateFrom": None,
			"OpenedDateTo": None,
			"ClosedDateFrom": None,
			"ClosedDateTo": None,
			"Address": None,
			"ParcelNumber": None,
			"Description": None,
			"SearchMainAddress": False,
			"RequestId": None,
			"ExcludeCases": None,
			"ContactId": None,
			"EnableDescriptionSearch": False,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"RequestCriteria": {
			"RequestNumber": None,
			"RequestTypeId": None,
			"RequestStatusId": None,
			"ProjectName": None,
			"EnteredDateFrom": None,
			"EnteredDateTo": None,
			"DeadlineDateFrom": None,
			"DeadlineDateTo": None,
			"CompleteDateFrom": None,
			"CompleteDateTo": None,
			"Address": None,
			"ParcelNumber": None,
			"SearchMainAddress": False,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"BusinessLicenseCriteria": {
			"LicenseNumber": None,
			"LicenseTypeId": None,
			"LicenseClassId": None,
			"LicenseStatusId": None,
			"BusinessStatusId": None,
			"LicenseYear": None,
			"ApplicationDateFrom": None,
			"ApplicationDateTo": None,
			"IssueDateFrom": None,
			"IssueDateTo": None,
			"ExpirationDateFrom": None,
			"ExpirationDateTo": None,
			"SearchMainAddress": False,
			"CompanyTypeId": None,
			"CompanyName": None,
			"BusinessTypeId": None,
			"Description": None,
			"CompanyOpenedDateFrom": None,
			"CompanyOpenedDateTo": None,
			"CompanyClosedDateFrom": None,
			"CompanyClosedDateTo": None,
			"LastAuditDateFrom": None,
			"LastAuditDateTo": None,
			"ParcelNumber": None,
			"Address": None,
			"TaxID": None,
			"DBA": None,
			"ExcludeCases": None,
			"TypeId": None,
			"WorkClassIds": None,
			"ContactId": None,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"ProfessionalLicenseCriteria": {
			"LicenseNumber": None,
			"HolderFirstName": None,
			"HolderMiddleName": None,
			"HolderLastName": None,
			"HolderCompanyName": None,
			"LicenseTypeId": None,
			"LicenseClassId": None,
			"LicenseStatusId": None,
			"IssueDateFrom": None,
			"IssueDateTo": None,
			"ExpirationDateFrom": None,
			"ExpirationDateTo": None,
			"ApplicationDateFrom": None,
			"ApplicationDateTo": None,
			"Address": None,
			"MainParcel": None,
			"SearchMainAddress": False,
			"ExcludeCases": None,
			"TypeId": None,
			"WorkClassIds": None,
			"ContactId": None,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"LicenseCriteria": {
			"LicenseNumber": None,
			"LicenseTypeId": None,
			"LicenseClassId": None,
			"LicenseStatusId": None,
			"BusinessStatusId": None,
			"ApplicationDateFrom": None,
			"ApplicationDateTo": None,
			"IssueDateFrom": None,
			"IssueDateTo": None,
			"ExpirationDateFrom": None,
			"ExpirationDateTo": None,
			"SearchMainAddress": False,
			"CompanyTypeId": None,
			"CompanyName": None,
			"BusinessTypeId": None,
			"Description": None,
			"CompanyOpenedDateFrom": None,
			"CompanyOpenedDateTo": None,
			"CompanyClosedDateFrom": None,
			"CompanyClosedDateTo": None,
			"LastAuditDateFrom": None,
			"LastAuditDateTo": None,
			"ParcelNumber": None,
			"Address": None,
			"TaxID": None,
			"DBA": None,
			"ExcludeCases": None,
			"TypeId": None,
			"WorkClassIds": None,
			"ContactId": None,
			"HolderFirstName": None,
			"HolderMiddleName": None,
			"HolderLastName": None,
			"MainParcel": None,
			"EnableDescriptionSearchForBLicense": False,
			"EnableDescriptionSearchForPLicense": False,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"ProjectCriteria": {
			"ProjectNumber": None,
			"ProjectName": None,
			"Address": None,
			"ParcelNumber": None,
			"StartDateFrom": None,
			"StartDateTo": None,
			"ExpectedEndDateFrom": None,
			"ExpectedEndDateTo": None,
			"CompleteDateFrom": None,
			"CompleteDateTo": None,
			"Description": None,
			"SearchMainAddress": False,
			"ContactId": None,
			"TypeId": None,
			"ExcludeCases": None,
			"EnableDescriptionSearch": False,
			"PageNumber": 0,
			"PageSize": 0,
			"SortBy": None,
			"SortAscending": False
		},
		"PlanSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "PlanNumber.keyword",
				"Value": "Plan Number"
			},
			{
				"Key": "ProjectName.keyword",
				"Value": "Project"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			},
			{
				"Key": "ApplyDate",
				"Value": "Apply Date"
			}
		],
		"PermitSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "PermitNumber.keyword",
				"Value": "Permit Number"
			},
			{
				"Key": "ProjectName.keyword",
				"Value": "Project"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			},
			{
				"Key": "IssueDate",
				"Value": "Issued Date"
			},
			{
				"Key": "FinalDate",
				"Value": "Finalized Date"
			}
		],
		"InspectionSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "InspectionNumber.keyword",
				"Value": "Inspection Number"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			},
			{
				"Key": "ScheduledDate",
				"Value": "Schedule Date"
			},
			{
				"Key": "RequestDate",
				"Value": "Request Date"
			}
		],
		"CodeCaseSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "CaseNumber.keyword",
				"Value": "Code Case Number"
			},
			{
				"Key": "ProjectName.keyword",
				"Value": "Project"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			},
			{
				"Key": "OpenedDate",
				"Value": "Opened Date"
			},
			{
				"Key": "ClosedDate",
				"Value": "Closed Date"
			}
		],
		"RequestSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "RequestNumber.keyword",
				"Value": "Request Number"
			},
			{
				"Key": "ProjectName.keyword",
				"Value": "Project Name"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			},
			{
				"Key": "EnteredDate",
				"Value": "Date Entered"
			},
			{
				"Key": "CompleteDate",
				"Value": "Completion Date"
			}
		],
		"LicenseSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "LicenseNumber.keyword",
				"Value": "License Number"
			},
			{
				"Key": "CompanyName.keyword",
				"Value": "Company Name"
			},
			{
				"Key": "AppliedDate",
				"Value": "Applied Date"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			}
		],
		"ProjectSortList": [
			{
				"Key": "relevance",
				"Value": "Relevance"
			},
			{
				"Key": "ProjectNumber.keyword",
				"Value": "Project Number"
			},
			{
				"Key": "ProjectName.keyword",
				"Value": "Project Name"
			},
			{
				"Key": "StartDate",
				"Value": "Start Date"
			},
			{
				"Key": "CompleteDate",
				"Value": "Completed Date"
			},
			{
				"Key": "ExpectedEndDate",
				"Value": "Expected End Date"
			},
			{
				"Key": "MainAddress",
				"Value": "Address"
			}
		],
		"ExcludeCases": None,
		"SortOrderList": [
			{
				"Key": True,
				"Value": "Ascending"
			},
			{
				"Key": False,
				"Value": "Descending"
			}
		],
		"HiddenInspectionTypeIDs": None,
		"PageNumber": 0,
		"PageSize": 0,
		"SortBy": "relevance",
		"SortAscending": True
	}

	# Makes search requests for each permit type
	search_results = request_data(url_main_search, payload_main_search)["Result"]["EntityResults"]

	# Iterates over each search result
	for entry in search_results:
		case_id = entry["CaseId"]

		url_details = "https://energovweb.pickenscountysc.us/EnerGovProd/SelfService/api/energov/entity/contacts/search/search"
		payload_details = {
			"PageNumber": 1,
			"PageSize": 10,
			"SortField": "",
			"IsSortedInAscendingOrder": True,
			"ModuleId": 1,
			"EntityId": case_id,
		}

		# Going to the details page to get contacts data
		details_data = request_data(url_details, payload_details)["Result"]
		for contact in details_data:
			result = {
				"case_id": entry["CaseId"],
				"permit_number": entry["CaseNumber"],
				"permit_type": entry["CaseType"],
				"status": entry["CaseStatus"],
				"main_parcel": entry["MainParcel"],
				"project_name": entry["ProjectName"],
				"address": entry["AddressDisplay"],
				"applied_date": entry["ApplyDate"],
				"issued_date": entry["IssueDate"],
				"expiration_date": entry["ExpireDate"],
				"finalized_date": entry["FinalDate"],
				"locations": entry["AddressDisplay"],
				"description": entry["Description"],
				"contact_type": contact["ContactTypeName"],
				"contact_company": contact["GlobalEntityName"],
				"contact_first_name": contact["FirstName"],
				"contact_last_name": contact["LastName"],
				"contact_title": contact["Title"],
				"confirmation": contact["ContactStatus"],
				"billing": contact["IsBillingDisplayText"],
			}

			# Adds the result data to the end results list
			end_results.append(result)

# Saving data to CSV or other format
df = pd.DataFrame(end_results)

# Specifies the output format
df.to_csv("text.csv")