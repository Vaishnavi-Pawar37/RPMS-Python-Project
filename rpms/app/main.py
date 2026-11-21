from rpms.dao.candidate_dao import CandidateDAO
from rpms.dao.job_dao import JobDAO
from rpms.dao.application_dao import ApplicationDAO

from rpms.model.candidate import Candidate

from rpms.service.candidate_service import CandidateService
from rpms.service.eligibility_service import EligibilityService
from rpms.service.application_service import ApplicationService
from rpms.service.report_service import ReportService
from rpms.service.activity_log_service import ActivityLogService


def print_menu():
    print("\n==============================================")
    print("RPMS - CAMPUS RECRUITMENT & PLACEMENT PORTAL")
    print("==============================================")
    print("1. View All Registered Candidates")
    print("2. Register New Candidate")
    print("3. Browse Open Job Vacancies")
    print("4. Submit Job Application")
    print("5. View Technology-Wise Candidate Report")
    print("6. Search Candidates by Technology")
    print("7. Filter Candidates by Placement Status")
    print("8. Exit Application")


def main():
    candidate_dao = CandidateDAO()
    job_dao = JobDAO()
    application_dao = ApplicationDAO()

    candidate_service = CandidateService(candidate_dao)
    eligibility_service = EligibilityService()
    application_service = ApplicationService(
        candidate_dao,
        job_dao,
        application_dao,
        eligibility_service
    )

    report_service = ReportService()
    log_service = ActivityLogService()

    while True:
        print_menu()

        try:
            choice = int(input("Please select an option (1-8): "))

            if choice == 1:
                candidates = candidate_service.get_all_candidates()
                if not candidates:
                    print("No candidates found.")
                else:
                    for c in candidates:
                        print(c)
                    print(f"\nTotal Candidates Found: {len(candidates)}")

            elif choice == 2:
                candidate = Candidate(
                    candidate_code=input("Candidate Code: "),
                    full_name=input("Enter Candidate Full Name: "),
                    email=input("Email: "),
                    mobile=input("Mobile: "),
                    qualification=input("Qualification: "),
                    passing_year=int(input("Passing Year: ")),
                    percentage=float(input("Percentage: ")),
                    backlog_count=int(input("Backlog Count: ")),
                    primary_technology=input("Primary Technology: ")
                )

                candidate_id = candidate_service.add_candidate(candidate)
                print(f"Candidate created. ID = {candidate_id}")
                log_service.log(f"Candidate created: {candidate.candidate_code}")

            elif choice == 3:
                jobs = job_dao.find_open_jobs()
                if not jobs:
                    print("No open jobs available right now.")
                else:
                    for job in jobs:
                        print(job)
                    print(f"\nTotal Open Jobs Found: {len(jobs)}")

            elif choice == 4:
                candidate_id = int(input("Candidate ID: "))
                job_id = int(input("Job ID: "))
                application_id = application_service.apply_for_job(candidate_id, job_id)
                print(f"Application created. ID = {application_id}")
                log_service.log(
                    f"Application created: candidate={candidate_id}, job={job_id}"
                )

            elif choice == 5:
                for technology, total in report_service.candidate_count_by_technology():
                    print(f"{technology}: {total}")

            elif choice == 6:
                tech = input("Enter Technology to Search (e.g., Python, Java): ")
                results = candidate_service.search_by_technology(tech)
                if not results:
                    print(f"No candidates found for technology: {tech}")
                else:
                    for c in results:
                        print(c)
                    print(f"\nTotal Matching Candidates: {len(results)}")

            elif choice == 7:
                status = input("Enter Placement Status (PLACED / NOT_PLACED): ")
                results = candidate_service.get_candidates_by_placement_status(status)
                if not results:
                    print(f"No candidates found with status: {status}")
                else:
                    for c in results:
                        print(c)
                    print(f"\nTotal Candidates ({status.upper()}): {len(results)}")

            elif choice == 8:
                print("Thank you for using RPMS. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

        except Exception as exc:
            print("ERROR:", exc)


if __name__ == "__main__":
    main()