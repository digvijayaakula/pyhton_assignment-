''' 5. create_account(name, role="User")

**Question:**
Create a function with default role.

**Test Case 1:**
Input:
create_account("Rahul")

Expected Output:
Account created for Rahul with role User

**Test Case 2:**
Input:
create_account("AdminUser", "Admin")

Expected Output:
Account created for AdminUser with role Admin
'''
def make_account(friend_name, friend_role="SuperUser"):
    print(f"Account created for {friend_name} with role {friend_role}")
make_account("Rahul")
make_account("AdminUser", "Admin")